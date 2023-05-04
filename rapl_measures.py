import pyRAPL as rapl
import matplotlib.pyplot as plt
import csv
import subprocess as sub
from threading import Thread
import time


class DataRAPL:
	"""The DataRAPL class stores the data collected during the execution of a program """
	def __init__(self):
		self.durations = []
		self.package = []
		self.dram = []
		self.mem = []

	def add_data(self, dur, pkg, dram, mem):
		self.durations.append(dur)
		self.package.append(pkg)
		self.dram.append(dram)
		self.mem.append(mem)

	def save_data(self,path,name, graph):
		"""Saves the duration, energy and dram consumption to a csv file and generates plots with the data"""
		with open(path + "/data_" + name + ".csv","w") as file:
			writer = csv.writer(file)
			writer.writerow(['duration','package','dram','peak_rss'])

			length = len(self.durations)
			for i in range(length):
				writer.writerow([self.durations[i],
								 self.package[i],
								 self.dram[i],
								 self.mem[i]])
		if graph == True:
			self.create_graphs(path,name)

	def create_graphs(self, path, name):
		"""Creates 2 plots, one for Package Energy Consumption and another for DRAM Energy Consumption"""
		plt.title("Package Energy Consumption graph")
		plt.xlabel("Time(μs)")
		plt.ylabel("Package Energy Consumption(μJ)")
		plt.plot(self.durations, self.package, color ="green")
		plt.savefig(path + "/pck_energy_plt_" + name + '.png')
		plt.clf()

		plt.title("Dram Energy Consumption graph")
		plt.xlabel("Time(μs)")
		plt.ylabel("Dram Energy Consumption(μJ)")
		plt.plot(self.durations, self.dram, color ="green")
		plt.savefig(path + "/dram_energy_plt_" + name + '.png')
		plt.clf()




class CollectorRAPL:
	"""The CollectorRAPL class is responsible for executing the programs and collecting data"""
	def __init__(self, cmd, path, name, freq = 0.0, multithreaded = False, iter = 10, energy = True, memory = True):
		"""
			cmd - Execution cmd
			path - Path to store collected data
			name - Name to store the files
			freq - Frequency of measurements (not used if multithreaded = False)
			multithreaded - If measurements are done during or at the start and end of the program exec
			iter - number of repetitions of the exec
		"""

		self.freq = float(freq)
		self.multithreaded = multithreaded
		if multithreaded == True and freq <= 0.0:
			raise Exception("Measurement Frequency cannot be below or equal to zero")

		self.iter = int(iter)
		self.cmd = cmd
		self.path = path
		self.name = name
		self.energy = energy
		self.memory = memory

		self.ret_codes = None

		# Initializes the RAPL API
		rapl.setup()
		self.meter = rapl.Measurement('Energy Consumption')
  
	def execute_command(self):
		if self.memory:
			process = sub.Popen(f"/usr/bin/time -f '%M' {self.cmd}", shell=True, stdout=sub.DEVNULL, stderr=sub.PIPE)
		else:
			process = sub.Popen(self.cmd, shell=True)
		
		process.wait()
		self.ret_codes = process

		return process


	def collect_multiple(self):
		"""Runs the program and collects data during the execution of the program"""
		for i in range(self.iter):
			sub_data = DataRAPL()
			self.meter.begin()
			exec = Thread(target=self.execute_command)
			exec.start()

			while exec.is_alive():
				#For small duration programs freq should be very low or it wont measure many time
				time.sleep(self.freq)
				self.meter.end()
				sub_data.add_data(self.meter.result.duration,self.meter.result.pkg[0],self.meter.result.dram[0],0)

			process = exec.join()
			if self.ret_codes.returncode != 0:
				raise Exception("[" + self.cmd +"] - Error when executing this command")
   
			if self.memory:
				# TODO: add logic to save peak_rss
				peak_rss = int(self.ret_codes.stderr.read().decode().strip())
				sub_data.add_data(self.meter.result.duration,self.meter.result.pkg[0],self.meter.result.dram[0],peak_rss)

				self.ret_codes = None
   
			sub_data.save_data(self.path,self.name + str(i),True)


	def collect_single(self):
		"""Runs the program and collects data only at the start and end of the execution of the program"""
		data = DataRAPL()

		for i in range(self.iter):
			print(self.cmd)
			self.meter.begin()
   
   
			process = self.execute_command()
			# Can't use stdout=sub.PIPE because it hangs for some reason
			# cmp = sub.Popen(self.cmd, shell=True)
			# ret = cmp.wait()

			self.meter.end()
   
			if process.returncode != 0:
				raise Exception("[" + self.cmd +"] - Error when executing this command")

			if self.memory:
				# TODO: add logic to save peak_rss
				peak_rss = int(process.stderr.read().decode().strip())
				data.add_data(self.meter.result.duration,self.meter.result.pkg[0],self.meter.result.dram[0],peak_rss)
			else:
				data.add_data(self.meter.result.duration,self.meter.result.pkg[0],self.meter.result.dram[0],0)

			

		data.save_data(self.path,self.name,False)


	def collect(self):
		if self.multithreaded:
			self.collect_multiple()
		else:
			self.collect_single()

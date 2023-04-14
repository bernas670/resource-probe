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

	def add_data(self, dur, pkg, dram):
		self.durations.append(dur)
		self.package.append(pkg)
		self.dram.append(dram)

	def save_data(self,path,name, graph):
		"""Saves the duration, energy and dram consumption to a csv file and generates plots with the data"""
		with open(path + "data_" + name + ".csv","w") as file:
			writer = csv.writer(file)
			writer.writerow(['duration','package','dram'])

			length = len(self.durations)
			for i in range(length):
				writer.writerow([self.durations[i],
								 self.package[i],
								 self.dram[i]])
		if graph == True:
			self.create_graphs(path,name)

	def create_graphs(self, path, name):
		"""Creates 2 plots, one for Package Energy Consumption and another for DRAM Energy Consumption"""
		plt.title("Package Energy Consumption graph")
		plt.xlabel("Time(μs)")
		plt.ylabel("Package Energy Consumption(μJ)")
		plt.plot(self.durations, self.package, color ="green")
		plt.savefig(path + "pck_energy_plt_" + name + '.png')
		plt.clf()

		plt.title("Dram Energy Consumption graph")
		plt.xlabel("Time(μs)")
		plt.ylabel("Dram Energy Consumption(μJ)")
		plt.plot(self.durations, self.dram, color ="green")
		plt.savefig(path + "dram_energy_plt_" + name + '.png')
		plt.clf()




class CollectorRAPL:
	"""The CollectorRAPL class is responsible for executing the programs and collecting data"""
	def __init__(self,cmd,path,name,freq = 0.0,meas_type = False,iter = 10):
		"""

			cmd - Execution cmd
			path - Path to store collected data
			name - Name to store the files
			freq - Frequency of measurements (not used if meas_type = False)
			meas_type - If measurements are done during or at the start and end of the program exec
			iter - number of repetitions of the exec
		"""

		self.freq = float(freq)
		self.meas_type = meas_type
		if meas_type == True and freq <= 0.0:
			raise Exception("Measurement Frequency cannot be below or equal to zero")

		self.iter = int(iter)
		self.cmd = cmd
		self.path = path
		self.name = name

		# Initializes the RAPL API
		rapl.setup()
		self.meter = rapl.Measurement('Energy Consumption')

	def execute_thread(self):
		# Can't use stdout=sub.PIPE because it hangs for some reason
		cmp = sub.Popen(self.cmd, shell=True)
		ret = cmp.wait()

		if ret != 0:
			raise Exception("[" + self.cmd +"] - Error when executing this command")


	def collect_multiple(self):
		"""Runs the program and collects data during the execution of the program"""
		for i in range(self.iter):
			sub_data = DataRAPL()
			self.meter.begin()
			exec = Thread(target=self.execute_thread)
			exec.start()

			while exec.is_alive():
				#For small duration programs freq should be very low or it wont measure many time
				time.sleep(self.freq)
				self.meter.end()
				sub_data.add_data(self.meter.result.duration,self.meter.result.pkg,self.meter.result.dram)

			exec.join()
			sub_data.save_data(self.path,self.name + str(i),True)




	def collect_single(self):
		"""Runs the program and collects data only at the start and end of the execution of the program"""
		data = DataRAPL()

		for i in range(self.iter):
			print(self.cmd)
			self.meter.begin()
			# Can't use stdout=sub.PIPE because it hangs for some reason
			cmp = sub.Popen(self.cmd, shell=True)
			ret = cmp.wait()

			self.meter.end()
			print(ret)
			if ret != 0:
			   raise Exception("[" + self.cmd +"] - Error when executing this command")

			data.add_data(self.meter.result.duration,self.meter.result.pkg,self.meter.result.dram)

		data.save_data(self.path,self.name,False)






def main():
	#col = CollectorRAPL("python3 test/test.py","test/","test",2.0,True)

	#col.collect_single()

	#col = CollectorRAPL("python3 test/test.py","test/","test2",0.1,True)

	#col.collect_multiple()
	pass
	 



if __name__ == '__main__':
	main()

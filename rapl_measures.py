import pyRAPL as rapl
import matplotlib.pyplot as plt
import csv
import subprocess as sub
from threading import Thread
import time


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

class DataRAPL:

	def __init__(self):
		self.durations = []
		self.package = []
		self.dram = []

	def add_data(self, dur, pkg, dram):
		self.durations.append(dur)
		self.package.append(pkg)
		self.dram.append(dram)

	def save_data(self,path,name, graph):
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
		
		plt.title("Package Energy Consumption graph")
		plt.xlabel("Time")
		plt.ylabel("Package Energy")
		plt.plot(self.durations, self.package, color ="green")
		plt.savefig(path + "pck_energy_plt_" + name + '.png')
		plt.clf()

		plt.title("Dram Energy Consumption graph")
		plt.xlabel("Time")
		plt.ylabel("Dram Energy")
		plt.plot(self.durations, self.dram, color ="green")
		plt.savefig(path + "dram_energy_plt_" + name + '.png')
		plt.clf()




class CollectorRAPL:

	def __init__(self,cmd,path,name,freq = 0.0,meas_type = False,iter = 10):
		self.freq = float(freq)
		self.meas_type = meas_type
		if meas_type == True and freq <= 0.0:
			raise Exception("Measurement Frequency cannot be below or equal to zero")

		self.iter = int(iter)
		self.cmd = cmd
		self.path = path
		self.name = name

		rapl.setup()

		self.meter = rapl.Measurement('Energy Consumption')

	def execute_thread(self):
		cmp = sub.Popen(self.cmd, shell=True)
		ret = cmp.wait()

		if ret != 0:
			raise Exception("[" + self.cmd +"] - Error when executing this command")


	def collect_multiple(self):

		for i in range(self.iter):
			sub_data = DataRAPL()
			self.meter.begin()
			exec = Thread(target=self.execute_thread)
			exec.start()

			while exec.is_alive():
				#time.sleep(self.freq)
				self.meter.end()
				sub_data.add_data(self.meter.result.duration,self.meter.result.pkg,self.meter.result.dram)

			exec.join()
			sub_data.save_data(self.path,self.name + str(i),True)




	def collect_single(self):
		data = DataRAPL()

		for i in range(self.iter):
			print(self.cmd)
			self.meter.begin()
			#res = sub.run(self.cmd.split(" "), shell=True, capture_output=True, text=True)

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
	 



if __name__ == '__main__':
	main()

#Result(label='bar', timestamp=1681220978.6671045, duration=2494.895, pkg=[57739.0], dram=[977.0])
#Result(label='bar', timestamp=1681220978.6671045, duration=5070.584, pkg=[105529.0], dram=[1526.0])
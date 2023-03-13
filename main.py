import subprocess
import psutil
import time
import os


# TODO: warm up the cpu


command = 'python test/fasta.py 7500'
interval = 1 / 1000

# TODO: make this dynamic, somehow...
cpu_sensor = 'k10temp'

# memory (B), cpu freq (Hz), cpu temp (C)
mem_samples, cpu_samples, tmp_samples = [], [], []

start_time = time.perf_counter()
process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

while process.poll() is None:
    # print('running')
    begin_sample_time = time.perf_counter()
    
    # mem_samples = [*mem_samples, psutil.Process(process.pid).memory_info().rss]
    cpu_samples = [*cpu_samples, psutil.cpu_freq().current]
    # tmp_samples = [*tmp_samples, psutil.sensors_temperatures()[cpu_sensor][0].current]
    
    print(f'Measurement time: {(time.perf_counter() - begin_sample_time) * 1000:.2f} ms')
    
    # time.sleep(interval - (time.perf_counter() - begin_sample_time))

execution_time = time.perf_counter() - start_time
return_code = process.returncode

print(f'Execution time: {execution_time * 1000:.2f} ms')

# print(f'Min. Mem.: {min(mem_samples) / 1e6:.2f}')
# print(f'Avg. Mem.: {(sum(mem_samples) / len(mem_samples)) / 1e6:.2f}')
# print(f'Max. Mem.: {max(mem_samples) / 1e6:.2f}')

print(f'Min. CPU.: {min(cpu_samples):.2f}')
print(f'Avg. CPU.: {(sum(cpu_samples) / len(cpu_samples)):.2f}')
print(f'Max. CPU.: {max(cpu_samples):.2f}')

# print(f'Min. Temp.: {min(tmp_samples):.2f}')
# print(f'Avg. Temp.: {(sum(tmp_samples) / len(tmp_samples)):.2f}')
# print(f'Max. Temp.: {max(tmp_samples):.2f}')

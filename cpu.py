import subprocess
import multiprocessing
import sys
import time
from pprint import pprint

def cpu_temp() -> int:
    return int(subprocess.check_output(
        "sensors | grep -oE 'Package id [0-9]: * \\+[0-9]+\\.[0-9]+' | grep -oE '\\+[0-9]+\\.[0-9]+'",
        shell=True
    ).decode('ascii'))
    
def cpu_temperature() -> float:
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
        cpu_temperature = float(file.read().strip()) / 1000
    return cpu_temperature


def round_robin():
    """Functions to heat CPU 

    Based on the implementation of https://gist.github.com/ishan1608/87cb762f31b7af70a867 
    but capable of terminating when the temperature reaches a threshold
    """
    while(True):
        number = 0
        if(number >= sys.maxsize):
            number = 0
        else:
            number = number + 1


def heat_up_cpu(temperature, interval=0.15):
    """Functions to heat CPU 
    
    Based on the implementation of https://gist.github.com/ishan1608/87cb762f31b7af70a867 
    but capable of terminating when the temperature reaches a threshold
    """
    process_cnt = 1
    processes = []
    
    q = multiprocessing.Queue()

    print("[CPU] - CPU temperature to get high enough")

    cpu_temp = cpu_temperature()
    prev_temp = cpu_temp

    while(cpu_temp < temperature) or (prev_temp < temperature):

        for process in processes:
            if not process.is_alive():
                process_cnt -= 1
                process.join(timeout=0.4)
                print("[CPU] - Terminated process sucessfully joined")

            
        while(process_cnt <= multiprocessing.cpu_count()):
            print("[CPU] - Spawning Process to to Heat up CPU")
            temp = multiprocessing.Process(target=round_robin)
            processes.append(temp)
            temp.start()
            process_cnt += 1

        time.sleep(interval)
        prev_temp = cpu_temp
        cpu_temp = cpu_temperature()


    for process in processes:
        print("[CPU] - Terminating process")
        process.kill()
        process.join()
        print("[CPU] - Terminated process sucessfully joined")



    print(f"[CPU] - Finished Heating up. Currently at {cpu_temp}ºC")
    q.close()

    return cpu_temp

def cool_down_cpu(temperature, interval = 0.15):
    print("[CPU] - Awaiting for cpu to cool down")
    
    temp = cpu_temperature()
    prev_temp = temp

    while temp > temperature or prev_temp > temperature:
        time.sleep(interval)
        prev_temp = temp
        temp = cpu_temperature()

    print(f"[CPU] - Finished cooling down. Currently at {temp}ºC")
    return temp

def set_temp(min_temp, max_temp, interval=0.15):
    cur_temp = cpu_temperature()
    print(f"[CPU] - Current initial temperature at {cur_temp}ºC")

    if cur_temp < min_temp:
        return heat_up_cpu(min_temp, interval)
    elif cur_temp > max_temp:
        return cool_down_cpu(max_temp, interval)
    else:
        return cur_temp

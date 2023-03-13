import subprocess

def cpu_temp() -> int:
    return int(subprocess.check_output(
        "sensors | grep -oE 'Package id [0-9]: * \\+[0-9]+\\.[0-9]+' | grep -oE '\\+[0-9]+\\.[0-9]+'",
        shell=True
    ).decode('ascii'))
    
def cpu_temperature() -> float:
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
        cpu_temperature = float(file.read().strip()) / 1000
    return cpu_temperature
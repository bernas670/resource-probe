import argparse
import cpu
from rapl_measures import CollectorRAPL


def main(command, folder, file,min_temp, max_temp, temp_int, energy, memory, multithreaded, interval, repetitions):
    

    # TODO: implement --no-energy
    
    collector = CollectorRAPL(command, folder, file,min_temp,max_temp,temp_int,interval, multithreaded, repetitions, energy, memory)
    collector.collect()
    
    return 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Measure a command's energy and memory consumption")
    parser.add_argument('cmd', type=str, help='The command to execute')
    parser.add_argument('path', type=str, help='The path where to save the csv and generated graphs')
    parser.add_argument('file', type=str, help='File naming convention')
    parser.add_argument('min_temp', type=int, help='The min temperature threshold')
    parser.add_argument('max_temp', type=int, help='The max temperature threshold')
    parser.add_argument('temp_int', type=float, help='Interval for temperature measures')
    parser.add_argument('-ne', '--no-energy', dest='energy', action='store_false',
                        help='Turn off energy metrics collection')
    parser.add_argument('-nm', '--no-memory', dest='memory', action='store_false',
                        help='Turn off memory metrics collection')
    parser.add_argument('-mt', '--multithreaded', dest='multithreaded', action='store_true',
                        help='Switch to multithreaded mode') 
    parser.add_argument('-i', '--interval', dest='interval', type=float,
                        help='Set the interval for collecting metrics in multithreaded method (in seconds)',
                        default=0.0)
    parser.add_argument('-r', '--repetitions', dest='repetitions', type=int,
                        help='Set the number of times to run the specified command',
                        default=1)

    args = parser.parse_args()

    main(args.cmd, args.path , args.file ,args.min_temp, args.max_temp, args.temp_int , args.energy, args.memory, args.multithreaded, args.interval, args.repetitions)
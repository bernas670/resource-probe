import argparse
from rapl_measures import CollectorRAPL

def main(command, temperature, energy, memory, multithreaded, interval, repetitions):
    
    # TODO: add temperature
    # TODO: implement --no-energy
    # TODO: save memory measurements
    
    collector = CollectorRAPL(command, "./test", "test", interval, multithreaded, repetitions, energy, memory)
    collector.collect()
    
    return 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Measure a command's energy and memory consumption")
    parser.add_argument('command', type=str, help='The command to execute')
    parser.add_argument('temperature', type=int, help='The baseline temperature')
    parser.add_argument('-ne', '--no-energy', dest='energy', action='store_false',
                        help='Turn off energy metrics collection')
    parser.add_argument('-nm', '--no-memory', dest='memory', action='store_false',
                        help='Turn off memory metrics collection')
    parser.add_argument('-mt', '--multithreaded', dest='multithreaded', action='store_true',
                        help='Switch to multithreaded mode') 
    parser.add_argument('-i', '--interval', dest='interval', type=float,
                        help='Set the interval for collecting metrics (in seconds)',
                        default=0.0)
    parser.add_argument('-r', '--repetitions', dest='repetitions', type=int,
                        help='Set the number of times to run the specified command',
                        default=1)

    args = parser.parse_args()

    main(args.command, args.temperature, args.energy, args.memory, args.multithreaded, args.interval, args.repetitions)
# resource-probe

Tools used:
https://pypi.org/project/memory-profiler/
https://pypi.org/project/pyRAPL/
https://phoenixnap.com/kb/linux-cpu-temp

## Running and Compiling

To compile the test programs run:

```bash=
$ make compile
```

To run the test programs run:

```bash=
$ make run
```

To measure energy consumption, duration and peak memory usage of the test programs run:

```bash=
$ make measure
```

To clean the folders run:

```bash=
$ make clean
```

To measure total memory usage run:

```bash=
$ make measure
```

## Adding more languages to test

See one of the already present languages, do not change the command names of the makefiles inside each of the benchmarks. Other than that replace it at your leisure. 

## Main program usage:

```bash=
usage: main.py [-h] [-ne] [-nm] [-mt] [-i INTERVAL] [-r REPETITIONS] cmd path file min_temp max_temp temp_int

Measure a command's energy and memory consumption

positional arguments:
  cmd                   The command to execute
  path                  The path where to save the csv and generated graphs
  file                  File naming convention
  min_temp              The min temperature threshold
  max_temp              The max temperature threshold
  temp_int              Interval for temperature measures

options:
  -h, --help            show this help message and exit
  -ne, --no-energy      Turn off energy metrics collection
  -nm, --no-memory      Turn off memory metrics collection
  -mt, --multithreaded  Switch to multithreaded mode
  -i INTERVAL, --interval INTERVAL
                        Set the interval for collecting metrics in multithreaded method (in seconds)
  -r REPETITIONS, --repetitions REPETITIONS
                        Set the number of times to run the specified command
```




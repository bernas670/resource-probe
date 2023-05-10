.PHONY: compile clean run measure make_dirs copy_filescd

compile: | make_dirs copy_files
	
clean:
	rm -r -f python2.6
	rm -r -f python2.7
	rm -r -f python3.0
	rm -r -f python3.4
	rm -r -f python3.5
	rm -r -f python3.6
	rm -r -f python3.7
	rm -r -f python3.8
	rm -r -f python3.9
	rm -r -f python3.10
	rm -r -f python3.11 

run:
#	python2.6 ./python2.6/pidigits-4.py 10000
#	python2.7 ./python2.7/pidigits-4.py 10000
	python3.0 ./python3.0/pidigits-4.py 10000
	python3.4 ./python3.4/pidigits-4.py 10000
	python3.5 ./python3.5/pidigits-4.py 10000
	python3.6 ./python3.6/pidigits-4.py 10000
	python3.7 ./python3.7/pidigits-4.py 10000
	python3.8 ./python3.8/pidigits-4.py 10000
	python3.9 ./python3.9/pidigits-4.py 10000
	python3.10 ./python3.10/pidigits-4.py 10000
	python3.11 ./python3.11/pidigits-4.py 10000
	

measure:
#	python3 ../../main.py "python2.6 ./python2.6/pidigits-4.py 10000" "./python2.6" "py-pidigits-2.6" 40 45 0.01 -r 10
#	python3 ../../main.py "python2.7 ./python2.7/pidigits-4.py 10000" "./python2.7" "py-pidigits-2.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.0 ./python3.0/pidigits-4.py 10000" "./python3.0" "py-pidigits-3.0" 40 45 0.01 -r 10
	python3 ../../main.py "python3.4 ./python3.4/pidigits-4.py 10000" "./python3.4" "py-pidigits-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "python3.5 ./python3.5/pidigits-4.py 10000" "./python3.5" "py-pidigits-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "python3.6 ./python3.6/pidigits-4.py 10000" "./python3.6" "py-pidigits-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "python3.7 ./python3.7/pidigits-4.py 10000" "./python3.7" "py-pidigits-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.8 ./python3.8/pidigits-4.py 10000" "./python3.8" "py-pidigits-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "python3.9 ./python3.9/pidigits-4.py 10000" "./python3.9" "py-pidigits-3.9" 40 45 0.01 -r 10
	python3 ../../main.py "python3.10 ./python3.10/pidigits-4.py 10000" "./python3.10" "py-pidigits-3.10" 40 45 0.01 -r 10
	python3 ../../main.py "python3.11 ./python3.11/pidigits-4.py 10000" "./python3.11" "py-pidigits-3.11" 40 45 0.01 -r 10



make_dirs:
	mkdir -p python2.6
	mkdir -p python2.7
	mkdir -p python3.0
	mkdir -p python3.4
	mkdir -p python3.5
	mkdir -p python3.6
	mkdir -p python3.7
	mkdir -p python3.8
	mkdir -p python3.9
	mkdir -p python3.10
	mkdir -p python3.11 

copy_files:
	sudo cp pidigits-4.py ./python2.6/pidigits-4.py
	sudo cp pidigits-4.py ./python2.7/pidigits-4.py
	sudo cp pidigits-4.py ./python3.0/pidigits-4.py
	sudo cp pidigits-4.py ./python3.4/pidigits-4.py
	sudo cp pidigits-4.py ./python3.5/pidigits-4.py
	sudo cp pidigits-4.py ./python3.6/pidigits-4.py
	sudo cp pidigits-4.py ./python3.7/pidigits-4.py
	sudo cp pidigits-4.py ./python3.8/pidigits-4.py
	sudo cp pidigits-4.py ./python3.9/pidigits-4.py
	sudo cp pidigits-4.py ./python3.10/pidigits-4.py
	sudo cp pidigits-4.py ./python3.11/pidigits-4.py 
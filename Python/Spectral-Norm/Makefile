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
#	python2.6 ./python2.6/spectralnorm-8.py 5500
#	python2.7 ./python2.7/spectralnorm-8.py 5500
#	python3.0 ./python3.0/spectralnorm-8.py 5500
	python3.4 ./python3.4/spectralnorm-8.py 5500
	python3.5 ./python3.5/spectralnorm-8.py 5500
	python3.6 ./python3.6/spectralnorm-8.py 5500
	python3.7 ./python3.7/spectralnorm-8.py 5500
	python3.8 ./python3.8/spectralnorm-8.py 5500
	python3.9 ./python3.9/spectralnorm-8.py 5500
	python3.10 ./python3.10/spectralnorm-8.py 5500
	python3.11 ./python3.11/spectralnorm-8.py 5500
	

measure:
#	python3 ../../main.py "python2.6 ./python2.6/spectralnorm-8.py 5500" "./python2.6" "py-spectralnorm-2.6" 40 45 0.01 -r 10
#	python3 ../../main.py "python2.7 ./python2.7/spectralnorm-8.py 5500" "./python2.7" "py-spectralnorm-2.7" 40 45 0.01 -r 10
#	python3 ../../main.py "python3.0 ./python3.0/spectralnorm-8.py 5500" "./python3.0" "py-spectralnorm-3.0" 40 45 0.01 -r 10
	python3 ../../main.py "python3.4 ./python3.4/spectralnorm-8.py 5500" "./python3.4" "py-spectralnorm-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "python3.5 ./python3.5/spectralnorm-8.py 5500" "./python3.5" "py-spectralnorm-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "python3.6 ./python3.6/spectralnorm-8.py 5500" "./python3.6" "py-spectralnorm-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "python3.7 ./python3.7/spectralnorm-8.py 5500" "./python3.7" "py-spectralnorm-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.8 ./python3.8/spectralnorm-8.py 5500" "./python3.8" "py-spectralnorm-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "python3.9 ./python3.9/spectralnorm-8.py 5500" "./python3.9" "py-spectralnorm-3.9" 40 45 0.01 -r 10
	python3 ../../main.py "python3.10 ./python3.10/spectralnorm-8.py 5500" "./python3.10" "py-spectralnorm-3.10" 40 45 0.01 -r 10
	python3 ../../main.py "python3.11 ./python3.11/spectralnorm-8.py 5500" "./python3.11" "py-spectralnorm-3.11" 40 45 0.01 -r 10


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
	sudo cp spectralnorm-8.py ./python2.6/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python2.7/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.0/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.4/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.5/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.6/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.7/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.8/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.9/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.10/spectralnorm-8.py
	sudo cp spectralnorm-8.py ./python3.11/spectralnorm-8.py 
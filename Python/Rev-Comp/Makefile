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
#	python2.6 ./python2.6/revcomp-4.py 0 < ../../revcomp-input25000000.txt
#	python2.7 ./python2.7/revcomp-4.py 0 < ../../revcomp-input25000000.txt
#	python3.0 ./python3.0/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.4 ./python3.4/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.5 ./python3.5/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.6 ./python3.6/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.7 ./python3.7/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.8 ./python3.8/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.9 ./python3.9/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.10 ./python3.10/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	python3.11 ./python3.11/revcomp-4.py 0 < ../../revcomp-input25000000.txt
	

measure:


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
	sudo cp revcomp-4.py ./python2.6/revcomp-4.py
	sudo cp revcomp-4.py ./python2.7/revcomp-4.py
	sudo cp revcomp-4.py ./python3.0/revcomp-4.py
	sudo cp revcomp-4.py ./python3.4/revcomp-4.py
	sudo cp revcomp-4.py ./python3.5/revcomp-4.py
	sudo cp revcomp-4.py ./python3.6/revcomp-4.py
	sudo cp revcomp-4.py ./python3.7/revcomp-4.py
	sudo cp revcomp-4.py ./python3.8/revcomp-4.py
	sudo cp revcomp-4.py ./python3.9/revcomp-4.py
	sudo cp revcomp-4.py ./python3.10/revcomp-4.py
	sudo cp revcomp-4.py ./python3.11/revcomp-4.py 
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
#	python2.6 ./python2.6/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
#	python2.7 ./python2.7/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.0 ./python3.0/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.4 ./python3.4/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.5 ./python3.5/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.6 ./python3.6/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.7 ./python3.7/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.8 ./python3.8/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.9 ./python3.9/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.10 ./python3.10/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	python3.11 ./python3.11/knucleotide-8.py 0 < ../../knucleotide-input25000000.txt
	

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
	sudo cp knucleotide-8.py ./python2.6/knucleotide-8.py
	sudo cp knucleotide-8.py ./python2.7/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.0/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.4/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.5/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.6/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.7/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.8/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.9/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.10/knucleotide-8.py
	sudo cp knucleotide-8.py ./python3.11/knucleotide-8.py 
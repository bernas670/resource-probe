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
	python2.6 ./python2.6/regexredux.py 0 < ../../regexredux-input5000000.txt
	python2.7 ./python2.7/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.0 ./python3.0/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.4 ./python3.4/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.5 ./python3.5/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.6 ./python3.6/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.7 ./python3.7/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.8 ./python3.8/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.9 ./python3.9/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.10 ./python3.10/regexredux.py 0 < ../../regexredux-input5000000.txt
	python3.11 ./python3.11/regexredux.py 0 < ../../regexredux-input5000000.txt
	

measure:
	python3 ../../main.py "python2.6 ./python2.6/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python2.6" "py-regexredux-2.6" 40 45 0.01 -r 10
	python3 ../../main.py "python2.7 ./python2.7/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python2.7" "py-regexredux-2.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.0 ./python3.0/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.0" "py-regexredux-3.0" 40 45 0.01 -r 10
	python3 ../../main.py "python3.4 ./python3.4/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.4" "py-regexredux-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "python3.5 ./python3.5/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.5" "py-regexredux-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "python3.6 ./python3.6/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.6" "py-regexredux-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "python3.7 ./python3.7/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.7" "py-regexredux-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.8 ./python3.8/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.8" "py-regexredux-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "python3.9 ./python3.9/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.9" "py-regexredux-3.9" 40 45 0.01 -r 10
	python3 ../../main.py "python3.10 ./python3.10/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.10" "py-regexredux-3.10" 40 45 0.01 -r 10
	python3 ../../main.py "python3.11 ./python3.11/regexredux.py 0 < ../../regexredux-input5000000.txt" "./python3.11" "py-regexredux-3.11" 40 45 0.01 -r 10

define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
	$(call measure_mem,python2.6 ./python2.6/regexredux.py 0 < ../../regexredux-input5000000.txt,./python2.6,mem_test)
	python3 ../../mem_parser.py "./python2.6/" "py-regexredux-2.6"
	$(call measure_mem,python2.7 ./python2.7/regexredux.py 0 < ../../regexredux-input5000000.txt,./python2.7,mem_test)
	python3 ../../mem_parser.py "./python2.7/" "py-regexredux-2.7"
	$(call measure_mem,python3.0 ./python3.0/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.0,mem_test)
	python3 ../../mem_parser.py "./python3.0/" "py-regexredux-3.0"
	$(call measure_mem,python3.4 ./python3.4/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.4,mem_test)
	python3 ../../mem_parser.py "./python3.4/" "py-regexredux-3.4"
	$(call measure_mem,python3.5 ./python3.5/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.5,mem_test)
	python3 ../../mem_parser.py "./python3.5/" "py-regexredux-3.5"
	$(call measure_mem,python3.6 ./python3.6/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.6,mem_test)
	python3 ../../mem_parser.py "./python3.6/" "py-regexredux-3.6"
	$(call measure_mem,python3.7 ./python3.7/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.7,mem_test)
	python3 ../../mem_parser.py "./python3.7/" "py-regexredux-3.7"
	$(call measure_mem,python3.8 ./python3.8/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.8,mem_test)
	python3 ../../mem_parser.py "./python3.8/" "py-regexredux-3.8"
	$(call measure_mem,python3.9 ./python3.9/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.9,mem_test)
	python3 ../../mem_parser.py "./python3.9/" "py-regexredux-3.9"
	$(call measure_mem,python3.10 ./python3.10/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.10,mem_test)
	python3 ../../mem_parser.py "./python3.10/" "py-regexredux-3.10"
	$(call measure_mem,python3.11 ./python3.11/regexredux.py 0 < ../../regexredux-input5000000.txt,./python3.11,mem_test)
	python3 ../../mem_parser.py "./python3.11/" "py-regexredux-3.11"

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
	sudo cp regexredux.py ./python2.6/regexredux.py
	sudo cp regexredux.py ./python2.7/regexredux.py
	sudo cp regexredux.py ./python3.0/regexredux.py
	sudo cp regexredux.py ./python3.4/regexredux.py
	sudo cp regexredux.py ./python3.5/regexredux.py
	sudo cp regexredux.py ./python3.6/regexredux.py
	sudo cp regexredux.py ./python3.7/regexredux.py
	sudo cp regexredux.py ./python3.8/regexredux.py
	sudo cp regexredux.py ./python3.9/regexredux.py
	sudo cp regexredux.py ./python3.10/regexredux.py
	sudo cp regexredux.py ./python3.11/regexredux.py 
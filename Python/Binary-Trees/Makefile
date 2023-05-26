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
#	python2.6 ./python2.6/binarytrees-5.py 21
#	python2.7 ./python2.7/binarytrees-5.py 21
#	python3.0 ./python3.0/binarytrees-5.py 21
#	python3.4 ./python3.4/binarytrees-5.py 21
#	python3.5 ./python3.5/binarytrees-5.py 21
	python3.6 ./python3.6/binarytrees-5.py 21
	python3.7 ./python3.7/binarytrees-5.py 21
	python3.8 ./python3.8/binarytrees-5.py 21
	python3.9 ./python3.9/binarytrees-5.py 21
	python3.10 ./python3.10/binarytrees-5.py 21
	python3.11 ./python3.11/binarytrees-5.py 21
	

measure:
#	python3 ../../main.py "python2.6 ./python2.6/binarytrees-5.py 21" "./python2.6" "py-bintrees-2.6" 40 45 0.01 -r 10
#	python3 ../../main.py "python2.7 ./python2.7/binarytrees-5.py 21" "./python2.7" "py-bintrees-2.7" 40 45 0.01 -r 10
#	python3 ../../main.py "python3.0 ./python3.0/binarytrees-5.py 21" "./python3.0" "py-bintrees-3.0" 40 45 0.01 -r 10
#	python3 ../../main.py "python3.4 ./python3.4/binarytrees-5.py 21" "./python3.4" "py-bintrees-3.4" 40 45 0.01 -r 10
#	python3 ../../main.py "python3.5 ./python3.5/binarytrees-5.py 21" "./python3.5" "py-bintrees-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "python3.6 ./python3.6/binarytrees-5.py 21" "./python3.6" "py-bintrees-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "python3.7 ./python3.7/binarytrees-5.py 21" "./python3.7" "py-bintrees-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "python3.8 ./python3.8/binarytrees-5.py 21" "./python3.8" "py-bintrees-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "python3.9 ./python3.9/binarytrees-5.py 21" "./python3.9" "py-bintrees-3.9" 40 45 0.01 -r 10
	python3 ../../main.py "python3.10 ./python3.10/binarytrees-5.py 21" "./python3.10" "py-bintrees-3.10" 40 45 0.01 -r 10
	python3 ../../main.py "python3.11 ./python3.11/binarytrees-5.py 21" "./python3.11" "py-bintrees-3.11" 40 45 0.01 -r 10
	

define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
#	$(call measure_mem,python2.6 ./python2.6/binarytrees-5.py 21,./python2.6,mem_test)
#	python3 ../../mem_parser.py "./python2.6/" "py-bintrees-2.6"
#	$(call measure_mem,python2.7 ./python2.7/binarytrees-5.py 21,./python2.7,mem_test)
#	python3 ../../mem_parser.py "./python2.7/" "py-bintrees-2.7"
#	$(call measure_mem,python3.0 ./python3.0/binarytrees-5.py 21,./python3.0,mem_test)
#	python3 ../../mem_parser.py "./python3.0/" "py-bintrees-3.0"
#	$(call measure_mem,python3.4 ./python3.4/binarytrees-5.py 21,./python3.4,mem_test)
#	python3 ../../mem_parser.py "./python3.4/" "py-bintrees-3.4"
#	$(call measure_mem,python3.5 ./python3.5/binarytrees-5.py 21,./python3.5,mem_test)
#	python3 ../../mem_parser.py "./python3.5/" "py-bintrees-3.5"
	$(call measure_mem,python3.6 ./python3.6/binarytrees-5.py 21,./python3.6,mem_test)
	python3 ../../mem_parser.py "./python3.6/" "py-bintrees-3.6"
	$(call measure_mem,python3.7 ./python3.7/binarytrees-5.py 21,./python3.7,mem_test)
	python3 ../../mem_parser.py "./python3.7/" "py-bintrees-3.7"
	$(call measure_mem,python3.8 ./python3.8/binarytrees-5.py 21,./python3.8,mem_test)
	python3 ../../mem_parser.py "./python3.8/" "py-bintrees-3.8"
	$(call measure_mem,python3.9 ./python3.9/binarytrees-5.py 21,./python3.9,mem_test)
	python3 ../../mem_parser.py "./python3.9/" "py-bintrees-3.9"
	$(call measure_mem,python3.10 ./python3.10/binarytrees-5.py 21,./python3.10,mem_test)
	python3 ../../mem_parser.py "./python3.10/" "py-bintrees-3.10"
	$(call measure_mem,python3.11 ./python3.11/binarytrees-5.py 21,./python3.11,mem_test)
	python3 ../../mem_parser.py "./python3.11/" "py-bintrees-3.11"

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
	sudo cp binarytrees-5.py ./python2.6/binarytrees-5.py
	sudo cp binarytrees-5.py ./python2.7/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.0/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.4/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.5/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.6/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.7/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.8/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.9/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.10/binarytrees-5.py
	sudo cp binarytrees-5.py ./python3.11/binarytrees-5.py 
.PHONY: compile clean run measure make_dirs copy_filescd

JAVA6 := $(DISS_JAVA)/jdk1.6.0_45/bin/
JAVA7 := $(DISS_JAVA)/jdk1.7.0_80/bin/
JAVA80 := $(DISS_JAVA)/jdk1.8.0_202/bin/
JAVA81 := $(DISS_JAVA)/jdk1.8.0_351/bin/
JAVA9 := $(DISS_JAVA)/jdk-9.0.4/bin/
JAVA10 := $(DISS_JAVA)/jdk-10.0.2/bin/
JAVA11 := $(DISS_JAVA)/jdk-11.0.17/bin/
JAVA12 := $(DISS_JAVA)/jdk-12.0.2/bin/
JAVA13 := $(DISS_JAVA)/jdk-13.0.2/bin/
JAVA14 := $(DISS_JAVA)/jdk-14.0.2/bin/
JAVA15 := $(DISS_JAVA)/jdk-15.0.2/bin/
JAVA16 := $(DISS_JAVA)/jdk-16.0.2/bin/
JAVA17 := $(DISS_JAVA)/jdk-17.0.6/bin/
JAVA18 := $(DISS_JAVA)/jdk-18.0.2.1/bin/
JAVA19 := $(DISS_JAVA)/jdk-19.0.2/bin/
JAVA20 := $(DISS_JAVA)/jdk-20.0.1/bin/


compile: | make_dirs copy_files
	
clean:
	rm -r -f java-6
	rm -r -f java-7
	rm -r -f java-8.0
	rm -r -f java-8.1
	rm -r -f java-9
	rm -r -f java-10
	rm -r -f java-11
	rm -r -f java-12
	rm -r -f java-13
	rm -r -f java-14
	rm -r -f java-15
	rm -r -f java-16
	rm -r -f java-17
	rm -r -f java-18
	rm -r -f java-19
	rm -r -f java-20

run:
#	(cd ./java-6 && $(JAVA6)java binarytrees7 21); cd ..
#	(cd ./java-7 && $(JAVA7)java binarytrees7 21); cd ..
	(cd ./java-8.0 && $(JAVA80)java binarytrees7 21); cd ..
	(cd ./java-8.1 && $(JAVA81)java binarytrees7 21); cd ..
	(cd ./java-9 && $(JAVA9)java binarytrees7 21); cd ..
	(cd ./java-10 && $(JAVA10)java binarytrees7 21); cd ..
	(cd ./java-11 && $(JAVA11)java binarytrees7 21); cd ..
	(cd ./java-12 && $(JAVA12)java binarytrees7 21); cd ..
	(cd ./java-13 && $(JAVA13)java binarytrees7 21); cd ..
	(cd ./java-14 && $(JAVA14)java binarytrees7 21); cd ..
	(cd ./java-15 && $(JAVA15)java binarytrees7 21); cd ..
	(cd ./java-16 && $(JAVA16)java binarytrees7 21); cd ..
	(cd ./java-17 && $(JAVA17)java binarytrees7 21); cd ..
	(cd ./java-18 && $(JAVA18)java binarytrees7 21); cd ..
	(cd ./java-19 && $(JAVA19)java binarytrees7 21); cd ..
	(cd ./java-20 && $(JAVA20)java binarytrees7 21); cd ..

	

measure:
#	(cd ./java-6 && python3 ../../../main.py "$(JAVA6)java binarytrees7 21" "." "java-bintrees-6" 40 45 0.01 -r 10); cd ..
#	(cd ./java-7 && python3 ../../../main.py "$(JAVA7)java binarytrees7 21" "." "java-bintrees-7" 40 45 0.01 -r 10); cd ..
	(cd ./java-8.0 && python3 ../../../main.py "$(JAVA80)java binarytrees7 21" "." "java-bintrees-8.0" 40 45 0.01 -r 10); cd ..
	(cd ./java-8.1 && python3 ../../../main.py "$(JAVA81)java binarytrees7 21" "." "java-bintrees-8.1" 40 45 0.01 -r 10); cd ..
	(cd ./java-9 && python3 ../../../main.py "$(JAVA9)java binarytrees7 21" "." "java-bintrees-9" 40 45 0.01 -r 10); cd ..
	(cd ./java-10 && python3 ../../../main.py "$(JAVA10)java binarytrees7 21" "." "java-bintrees-10" 40 45 0.01 -r 10); cd ..
	(cd ./java-11 && python3 ../../../main.py "$(JAVA11)java binarytrees7 21" "." "java-bintrees-11" 40 45 0.01 -r 10); cd ..
	(cd ./java-12 && python3 ../../../main.py "$(JAVA12)java binarytrees7 21" "." "java-bintrees-12" 40 45 0.01 -r 10); cd ..
	(cd ./java-13 && python3 ../../../main.py "$(JAVA13)java binarytrees7 21" "." "java-bintrees-13" 40 45 0.01 -r 10); cd ..
	(cd ./java-14 && python3 ../../../main.py "$(JAVA14)java binarytrees7 21" "." "java-bintrees-14" 40 45 0.01 -r 10); cd ..
	(cd ./java-15 && python3 ../../../main.py "$(JAVA15)java binarytrees7 21" "." "java-bintrees-15" 40 45 0.01 -r 10); cd ..
	(cd ./java-16 && python3 ../../../main.py "$(JAVA16)java binarytrees7 21" "." "java-bintrees-16" 40 45 0.01 -r 10); cd ..
	(cd ./java-17 && python3 ../../../main.py "$(JAVA17)java binarytrees7 21" "." "java-bintrees-17" 40 45 0.01 -r 10); cd ..
	(cd ./java-18 && python3 ../../../main.py "$(JAVA18)java binarytrees7 21" "." "java-bintrees-18" 40 45 0.01 -r 10); cd ..
	(cd ./java-19 && python3 ../../../main.py "$(JAVA19)java binarytrees7 21" "." "java-bintrees-19" 40 45 0.01 -r 10); cd ..
	(cd ./java-20 && python3 ../../../main.py "$(JAVA20)java binarytrees7 21" "." "java-bintrees-20" 40 45 0.01 -r 10); cd ..


define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
#	cd ./java-6 && $(call measure_mem,$(JAVA6)java binarytrees7 21,./,mem_test) ; cd ..
#	python3 ../../mem_parser.py "./java-6/" "java-bintrees-6"
#	cd ./java-7 && $(call measure_mem,$(JAVA7)java binarytrees7 21,./,mem_test) ; cd ..
#	python3 ../../mem_parser.py "./java-7/" "java-bintrees-7"
	cd ./java-8.0 && $(call measure_mem,$(JAVA80)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-8.0/" "java-bintrees-8.0"
	cd ./java-8.1 && $(call measure_mem,$(JAVA81)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-8.1/" "java-bintrees-8.1"
	cd ./java-9 && $(call measure_mem,$(JAVA9)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-9/" "java-bintrees-9"
	cd ./java-10 && $(call measure_mem,$(JAVA10)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-10/" "java-bintrees-10"
	cd ./java-11 && $(call measure_mem,$(JAVA11)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-11/" "java-bintrees-11"
	cd ./java-12 && $(call measure_mem,$(JAVA12)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-12/" "java-bintrees-12"
	cd ./java-13 && $(call measure_mem,$(JAVA13)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-13/" "java-bintrees-13"
	cd ./java-14 && $(call measure_mem,$(JAVA14)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-14/" "java-bintrees-14"
	cd ./java-15 && $(call measure_mem,$(JAVA15)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-15/" "java-bintrees-15"
	cd ./java-16 && $(call measure_mem,$(JAVA16)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-16/" "java-bintrees-16"
	cd ./java-17 && $(call measure_mem,$(JAVA17)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-17/" "java-bintrees-17"
	cd ./java-18 && $(call measure_mem,$(JAVA18)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-18/" "java-bintrees-18"
	cd ./java-19 && $(call measure_mem,$(JAVA19)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-19/" "java-bintrees-19"
	cd ./java-20 && $(call measure_mem,$(JAVA20)java binarytrees7 21,./,mem_test) ; cd ..
	python3 ../../mem_parser.py "./java-20/" "java-bintrees-20"

make_dirs:
	mkdir -p java-6
	mkdir -p java-7
	mkdir -p java-8.0
	mkdir -p java-8.1
	mkdir -p java-9
	mkdir -p java-10
	mkdir -p java-11
	mkdir -p java-12
	mkdir -p java-13
	mkdir -p java-14
	mkdir -p java-15
	mkdir -p java-16
	mkdir -p java-17
	mkdir -p java-18
	mkdir -p java-19
	mkdir -p java-20

copy_files:
#	sudo cp binarytrees7.java ./java-6/binarytrees7.java
#	$(JAVA6)javac ./java-6/binarytrees7.java
#	sudo cp binarytrees7.java ./java-7/binarytrees7.java
#	$(JAVA7)javac ./java-7/binarytrees7.java
	sudo cp binarytrees7.java ./java-8.0/binarytrees7.java
	$(JAVA80)javac ./java-8.0/binarytrees7.java
	sudo cp binarytrees7.java ./java-8.1/binarytrees7.java
	$(JAVA81)javac ./java-8.1/binarytrees7.java
	sudo cp binarytrees7.java ./java-9/binarytrees7.java
	$(JAVA9)javac ./java-9/binarytrees7.java
	sudo cp binarytrees7.java ./java-10/binarytrees7.java
	$(JAVA10)javac ./java-10/binarytrees7.java
	sudo cp binarytrees7.java ./java-11/binarytrees7.java
	$(JAVA11)javac ./java-11/binarytrees7.java
	sudo cp binarytrees7.java ./java-12/binarytrees7.java
	$(JAVA12)javac ./java-12/binarytrees7.java
	sudo cp binarytrees7.java ./java-13/binarytrees7.java
	$(JAVA13)javac ./java-13/binarytrees7.java
	sudo cp binarytrees7.java ./java-14/binarytrees7.java
	$(JAVA14)javac ./java-14/binarytrees7.java
	sudo cp binarytrees7.java ./java-15/binarytrees7.java
	$(JAVA15)javac ./java-15/binarytrees7.java
	sudo cp binarytrees7.java ./java-16/binarytrees7.java
	$(JAVA16)javac ./java-16/binarytrees7.java
	sudo cp binarytrees7.java ./java-17/binarytrees7.java 
	$(JAVA17)javac ./java-17/binarytrees7.java
	sudo cp binarytrees7.java ./java-18/binarytrees7.java
	$(JAVA18)javac ./java-18/binarytrees7.java 
	sudo cp binarytrees7.java ./java-19/binarytrees7.java
	$(JAVA19)javac ./java-19/binarytrees7.java
	sudo cp binarytrees7.java ./java-20/binarytrees7.java
	$(JAVA20)javac ./java-20/binarytrees7.java
	
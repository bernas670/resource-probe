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
	(cd ./java-6 && $(JAVA6)java pidigits 10000); cd ..
	(cd ./java-7 && $(JAVA7)java pidigits 10000); cd ..
	(cd ./java-8.0 && $(JAVA80)java pidigits 10000); cd ..
	(cd ./java-8.1 && $(JAVA81)java pidigits 10000); cd ..
	(cd ./java-9 && $(JAVA9)java pidigits 10000); cd ..
	(cd ./java-10 && $(JAVA10)java pidigits 10000); cd ..
	(cd ./java-11 && $(JAVA11)java pidigits 10000); cd ..
	(cd ./java-12 && $(JAVA12)java pidigits 10000); cd ..
	(cd ./java-13 && $(JAVA13)java pidigits 10000); cd ..
	(cd ./java-14 && $(JAVA14)java pidigits 10000); cd ..
	(cd ./java-15 && $(JAVA15)java pidigits 10000); cd ..
	(cd ./java-16 && $(JAVA16)java pidigits 10000); cd ..
	(cd ./java-17 && $(JAVA17)java pidigits 10000); cd ..
	(cd ./java-18 && $(JAVA18)java pidigits 10000); cd ..
	(cd ./java-19 && $(JAVA19)java pidigits 10000); cd ..
	(cd ./java-20 && $(JAVA20)java pidigits 10000); cd ..

	

measure:
	(cd ./java-6 && python3 ../../../main.py "$(JAVA6)java pidigits 10000" "." "java-pidigits-6" 40 45 0.01 -r 10); cd ..
	(cd ./java-7 && python3 ../../../main.py "$(JAVA7)java pidigits 10000" "." "java-pidigits-7" 40 45 0.01 -r 10); cd ..
	(cd ./java-8.0 && python3 ../../../main.py "$(JAVA80)java pidigits 10000" "." "java-pidigits-8.0" 40 45 0.01 -r 10); cd ..
	(cd ./java-8.1 && python3 ../../../main.py "$(JAVA81)java pidigits 10000" "." "java-pidigits-8.1" 40 45 0.01 -r 10); cd ..
	(cd ./java-9 && python3 ../../../main.py "$(JAVA9)java pidigits 10000" "." "java-pidigits-9" 40 45 0.01 -r 10); cd ..
	(cd ./java-10 && python3 ../../../main.py "$(JAVA10)java pidigits 10000" "." "java-pidigits-10" 40 45 0.01 -r 10); cd ..
	(cd ./java-11 && python3 ../../../main.py "$(JAVA11)java pidigits 10000" "." "java-pidigits-11" 40 45 0.01 -r 10); cd ..
	(cd ./java-12 && python3 ../../../main.py "$(JAVA12)java pidigits 10000" "." "java-pidigits-12" 40 45 0.01 -r 10); cd ..
	(cd ./java-13 && python3 ../../../main.py "$(JAVA13)java pidigits 10000" "." "java-pidigits-13" 40 45 0.01 -r 10); cd ..
	(cd ./java-14 && python3 ../../../main.py "$(JAVA14)java pidigits 10000" "." "java-pidigits-14" 40 45 0.01 -r 10); cd ..
	(cd ./java-15 && python3 ../../../main.py "$(JAVA15)java pidigits 10000" "." "java-pidigits-15" 40 45 0.01 -r 10); cd ..
	(cd ./java-16 && python3 ../../../main.py "$(JAVA16)java pidigits 10000" "." "java-pidigits-16" 40 45 0.01 -r 10); cd ..
	(cd ./java-17 && python3 ../../../main.py "$(JAVA17)java pidigits 10000" "." "java-pidigits-17" 40 45 0.01 -r 10); cd ..
	(cd ./java-18 && python3 ../../../main.py "$(JAVA18)java pidigits 10000" "." "java-pidigits-18" 40 45 0.01 -r 10); cd ..
	(cd ./java-19 && python3 ../../../main.py "$(JAVA19)java pidigits 10000" "." "java-pidigits-19" 40 45 0.01 -r 10); cd ..
	(cd ./java-20 && python3 ../../../main.py "$(JAVA20)java pidigits 10000" "." "java-pidigits-20" 40 45 0.01 -r 10); cd ..


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
	sudo cp pidigits.java ./java-6/pidigits.java
	$(JAVA6)javac ./java-6/pidigits.java
	sudo cp pidigits.java ./java-7/pidigits.java
	$(JAVA7)javac ./java-7/pidigits.java
	sudo cp pidigits.java ./java-8.0/pidigits.java
	$(JAVA80)javac ./java-8.0/pidigits.java
	sudo cp pidigits.java ./java-8.1/pidigits.java
	$(JAVA81)javac ./java-8.1/pidigits.java
	sudo cp pidigits.java ./java-9/pidigits.java
	$(JAVA9)javac ./java-9/pidigits.java
	sudo cp pidigits.java ./java-10/pidigits.java
	$(JAVA10)javac ./java-10/pidigits.java
	sudo cp pidigits.java ./java-11/pidigits.java
	$(JAVA11)javac ./java-11/pidigits.java
	sudo cp pidigits.java ./java-12/pidigits.java
	$(JAVA12)javac ./java-12/pidigits.java
	sudo cp pidigits.java ./java-13/pidigits.java
	$(JAVA13)javac ./java-13/pidigits.java
	sudo cp pidigits.java ./java-14/pidigits.java
	$(JAVA14)javac ./java-14/pidigits.java
	sudo cp pidigits.java ./java-15/pidigits.java
	$(JAVA15)javac ./java-15/pidigits.java
	sudo cp pidigits.java ./java-16/pidigits.java
	$(JAVA16)javac ./java-16/pidigits.java
	sudo cp pidigits.java ./java-17/pidigits.java 
	$(JAVA17)javac ./java-17/pidigits.java
	sudo cp pidigits.java ./java-18/pidigits.java
	$(JAVA18)javac ./java-18/pidigits.java 
	sudo cp pidigits.java ./java-19/pidigits.java
	$(JAVA19)javac ./java-19/pidigits.java
	sudo cp pidigits.java ./java-20/pidigits.java
	$(JAVA20)javac ./java-20/pidigits.java
	
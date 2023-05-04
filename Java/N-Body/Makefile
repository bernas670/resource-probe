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
	(cd ./java-6 && $(JAVA6)java nbody5); cd ..
	(cd ./java-7 && $(JAVA7)java nbody5); cd ..
	(cd ./java-8.0 && $(JAVA80)java nbody5); cd ..
	(cd ./java-8.1 && $(JAVA81)java nbody5); cd ..
	(cd ./java-9 && $(JAVA9)java nbody5); cd ..
	(cd ./java-10 && $(JAVA10)java nbody5); cd ..
	(cd ./java-11 && $(JAVA11)java nbody5); cd ..
	(cd ./java-12 && $(JAVA12)java nbody5); cd ..
	(cd ./java-13 && $(JAVA13)java nbody5); cd ..
	(cd ./java-14 && $(JAVA14)java nbody5); cd ..
	(cd ./java-15 && $(JAVA15)java nbody5); cd ..
	(cd ./java-16 && $(JAVA16)java nbody5); cd ..
	(cd ./java-17 && $(JAVA17)java nbody5); cd ..
	(cd ./java-18 && $(JAVA18)java nbody5); cd ..
	(cd ./java-19 && $(JAVA19)java nbody5); cd ..
	(cd ./java-20 && $(JAVA20)java nbody5); cd ..

	

measure:


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
	sudo cp nbody5.java ./java-6/nbody5.java
	-$(JAVA6)javac ./java-6/nbody5.java
	sudo cp nbody5.java ./java-7/nbody5.java
	-$(JAVA7)javac ./java-7/nbody5.java
	sudo cp nbody5.java ./java-8.0/nbody5.java
	-$(JAVA80)javac ./java-8.0/nbody5.java
	sudo cp nbody5.java ./java-8.1/nbody5.java
	-$(JAVA81)javac ./java-8.1/nbody5.java
	sudo cp nbody5.java ./java-9/nbody5.java
	-$(JAVA9)javac ./java-9/nbody5.java
	sudo cp nbody5.java ./java-10/nbody5.java
	-$(JAVA10)javac ./java-10/nbody5.java
	sudo cp nbody5.java ./java-11/nbody5.java
	-$(JAVA11)javac ./java-11/nbody5.java
	sudo cp nbody5.java ./java-12/nbody5.java
	-$(JAVA12)javac ./java-12/nbody5.java
	sudo cp nbody5.java ./java-13/nbody5.java
	-$(JAVA13)javac ./java-13/nbody5.java
	sudo cp nbody5.java ./java-14/nbody5.java
	-$(JAVA14)javac ./java-14/nbody5.java
	sudo cp nbody5.java ./java-15/nbody5.java
	-$(JAVA15)javac ./java-15/nbody5.java
	sudo cp nbody5.java ./java-16/nbody5.java
	-$(JAVA16)javac ./java-16/nbody5.java
	sudo cp nbody5.java ./java-17/nbody5.java 
	-$(JAVA17)javac ./java-17/nbody5.java
	sudo cp nbody5.java ./java-18/nbody5.java
	-$(JAVA18)javac ./java-18/nbody5.java 
	sudo cp nbody5.java ./java-19/nbody5.java
	-$(JAVA19)javac ./java-19/nbody5.java
	sudo cp nbody5.java ./java-20/nbody5.java
	-$(JAVA20)javac ./java-20/nbody5.java
	
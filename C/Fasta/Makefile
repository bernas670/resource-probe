.PHONY: compile clean run measure make_dirs copy_filescd

CLang34 := $(DISS_C)/clang-3.4.2/bin/
CLang35 := $(DISS_C)/clang-3.5.2/bin/
CLang36 := $(DISS_C)/clang-3.6.2/bin/
CLang37 := $(DISS_C)/clang-3.7.1/bin/
CLang38 := $(DISS_C)/clang-3.8.1/bin/
CLang4 := $(DISS_C)/clang-4.0.0/bin/
CLang5 := $(DISS_C)/clang-5.0.2/bin/
CLang6 := $(DISS_C)/clang-6.0.1/bin/
CLang7 := $(DISS_C)/clang-7.0.1/bin/
CLang8 := $(DISS_C)/clang-8.0.0/bin/
CLang9 := $(DISS_C)/clang-9.0.0/bin/
CLang10 := $(DISS_C)/clang-10.0.0/bin/
CLang11 := $(DISS_C)/clang-11.1.0/bin/
CLang12 := $(DISS_C)/clang-12.0.1/bin/
CLang13 := $(DISS_C)/clang-13.0.1/bin/
CLang14 := $(DISS_C)/clang-14.0.0/bin/
CLang15 := $(DISS_C)/clang-15.0.6/bin/

LibCLang34 := $(DISS_C)/clang-3.4.2/lib/
LibCLang35 := $(DISS_C)/clang-3.5.2/lib/
LibCLang36 := $(DISS_C)/clang-3.6.2/lib/
LibCLang37 := $(DISS_C)/clang-3.7.1/lib/
LibCLang38 := $(DISS_C)/clang-3.8.1/lib/
LibCLang4 := $(DISS_C)/clang-4.0.0/lib/
LibCLang5 := $(DISS_C)/clang-5.0.2/lib/
LibCLang6 := $(DISS_C)/clang-6.0.1/lib/
LibCLang7 := $(DISS_C)/clang-7.0.1/lib/
LibCLang8 := $(DISS_C)/clang-8.0.0/lib/
LibCLang9 := $(DISS_C)/clang-9.0.0/lib/
LibCLang10 := $(DISS_C)/clang-10.0.0/lib/
LibCLang11 := $(DISS_C)/clang-11.1.0/lib/
LibCLang12 := $(DISS_C)/clang-12.0.1/lib/
LibCLang13 := $(DISS_C)/clang-13.0.1/lib/
LibCLang14 := $(DISS_C)/clang-14.0.0/lib/
LibCLang15 := $(DISS_C)/clang-15.0.6/lib/


compile: | make_dirs copy_files
	
clean:
	rm -r -f clang-3.4
	rm -r -f clang-3.5
	rm -r -f clang-3.6
	rm -r -f clang-3.7
	rm -r -f clang-3.8
	rm -r -f clang-4.0
	rm -r -f clang-5.0
	rm -r -f clang-6.0
	rm -r -f clang-7.0
	rm -r -f clang-8.0
	rm -r -f clang-9.0
	rm -r -f clang-10.0
	rm -r -f clang-11.1
	rm -r -f clang-12.0
	rm -r -f clang-13.0
	rm -r -f clang-14.0
	rm -r -f clang-15.0

run:
	./clang-3.4/fasta-9 25000000
	./clang-3.5/fasta-9 25000000
	./clang-3.6/fasta-9 25000000
	./clang-3.7/fasta-9 25000000
	./clang-3.8/fasta-9 25000000
	./clang-4.0/fasta-9 25000000
	./clang-5.0/fasta-9 25000000
	./clang-6.0/fasta-9 25000000
	./clang-7.0/fasta-9 25000000
	./clang-8.0/fasta-9 25000000
#	./clang-9.0/fasta-9 25000000
	./clang-10.0/fasta-9 25000000
	./clang-11.1/fasta-9 25000000
	./clang-12.0/fasta-9 25000000
	./clang-13.0/fasta-9 25000000
	./clang-14.0/fasta-9 25000000
	./clang-15.0/fasta-9 25000000

	

measure:
	python3 ../../main.py "./clang-3.4/fasta-9 25000000" "./clang-3.4" "c-fasta-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.5/fasta-9 25000000" "./clang-3.5" "c-fasta-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.6/fasta-9 25000000" "./clang-3.6" "c-fasta-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.7/fasta-9 25000000" "./clang-3.7" "c-fasta-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.8/fasta-9 25000000" "./clang-3.8" "c-fasta-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-4.0/fasta-9 25000000" "./clang-4.0" "c-fasta-4.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-5.0/fasta-9 25000000" "./clang-5.0" "c-fasta-5.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-6.0/fasta-9 25000000" "./clang-6.0" "c-fasta-6.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-7.0/fasta-9 25000000" "./clang-7.0" "c-fasta-7.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-8.0/fasta-9 25000000" "./clang-8.0" "c-fasta-8.0" 40 45 0.01 -r 10
#	python3 ../../main.py "./clang-9.0/fasta-9 25000000" "./clang-9.0" "c-fasta-9.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-10.0/fasta-9 25000000" "./clang-10.0" "c-fasta-10.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-11.1/fasta-9 25000000" "./clang-11.1" "c-fasta-11.1" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-12.0/fasta-9 25000000" "./clang-12.0" "c-fasta-12.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-13.0/fasta-9 25000000" "./clang-13.0" "c-fasta-13.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-14.0/fasta-9 25000000" "./clang-14.0" "c-fasta-14.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-15.0/fasta-9 25000000" "./clang-15.0" "c-fasta-15.0" 40 45 0.01 -r 10

define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
	$(call measure_mem,./clang-3.4/fasta-9 25000000,./clang-3.4,mem_test)
	python3 ../../mem_parser.py "./clang-3.4/" "c-fasta-3.4"
	$(call measure_mem,./clang-3.5/fasta-9 25000000,./clang-3.5,mem_test)
	python3 ../../mem_parser.py "./clang-3.5/" "c-fasta-3.5"
	$(call measure_mem,./clang-3.6/fasta-9 25000000,./clang-3.6,mem_test)
	python3 ../../mem_parser.py "./clang-3.6/" "c-fasta-3.6"
	$(call measure_mem,./clang-3.7/fasta-9 25000000,./clang-3.7,mem_test)
	python3 ../../mem_parser.py "./clang-3.7/" "c-fasta-3.7"
	$(call measure_mem,./clang-3.8/fasta-9 25000000,./clang-3.8,mem_test)
	python3 ../../mem_parser.py "./clang-3.8/" "c-fasta-3.8"
	$(call measure_mem,./clang-4.0/fasta-9 25000000,./clang-4.0,mem_test)
	python3 ../../mem_parser.py "./clang-4.0/" "c-fasta-4.0"
	$(call measure_mem,./clang-5.0/fasta-9 25000000,./clang-5.0,mem_test)
	python3 ../../mem_parser.py "./clang-5.0/" "c-fasta-5.0"
	$(call measure_mem,./clang-6.0/fasta-9 25000000,./clang-6.0,mem_test)
	python3 ../../mem_parser.py "./clang-6.0/" "c-fasta-6.0"
	$(call measure_mem,./clang-7.0/fasta-9 25000000,./clang-7.0,mem_test)
	python3 ../../mem_parser.py "./clang-7.0/" "c-fasta-7.0"
	$(call measure_mem,./clang-8.0/fasta-9 25000000,./clang-8.0,mem_test)
	python3 ../../mem_parser.py "./clang-8.0/" "c-fasta-8.0"
#	$(call measure_mem,./clang-9.0/fasta-9 25000000,./clang-9.0,mem_test)
#	python3 ../../mem_parser.py "./clang-9.0/" "c-fasta-9.0"
	$(call measure_mem,./clang-10.0/fasta-9 25000000,./clang-10.0,mem_test)
	python3 ../../mem_parser.py "./clang-10.0/" "c-fasta-10.0"
	$(call measure_mem,./clang-11.1/fasta-9 25000000,./clang-11.1,mem_test)
	python3 ../../mem_parser.py "./clang-11.1/" "c-fasta-11.1"
	$(call measure_mem,./clang-12.0/fasta-9 25000000,./clang-12.0,mem_test)
	python3 ../../mem_parser.py "./clang-12.0/" "c-fasta-12.0"
	$(call measure_mem,./clang-13.0/fasta-9 25000000,./clang-13.0,mem_test)
	python3 ../../mem_parser.py "./clang-13.0/" "c-fasta-13.0"
	$(call measure_mem,./clang-14.0/fasta-9 25000000,./clang-14.0,mem_test)
	python3 ../../mem_parser.py "./clang-14.0/" "c-fasta-14.0"
	$(call measure_mem,./clang-15.0/fasta-9 25000000,./clang-15.0,mem_test)
	python3 ../../mem_parser.py "./clang-15.0/" "c-fasta-15.0"


make_dirs:
	mkdir -p clang-3.4
	mkdir -p clang-3.5
	mkdir -p clang-3.6
	mkdir -p clang-3.7
	mkdir -p clang-3.8
	mkdir -p clang-4.0
	mkdir -p clang-5.0
	mkdir -p clang-6.0
	mkdir -p clang-7.0
	mkdir -p clang-8.0
	mkdir -p clang-9.0
	mkdir -p clang-10.0
	mkdir -p clang-11.1
	mkdir -p clang-12.0
	mkdir -p clang-13.0
	mkdir -p clang-14.0
	mkdir -p clang-15.0

copy_files:
	$(CLang34)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang34)  fasta-9.c -o ./clang-3.4/fasta-9 
	$(CLang35)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang35)  fasta-9.c -o ./clang-3.5/fasta-9 
	$(CLang36)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang36)  fasta-9.c -o ./clang-3.6/fasta-9 
	$(CLang37)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang37)  fasta-9.c -o ./clang-3.7/fasta-9 
	$(CLang38)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang38)  fasta-9.c -o ./clang-3.8/fasta-9 
	$(CLang4)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang4) fasta-9.c -o ./clang-4.0/fasta-9 
	$(CLang5)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang5) fasta-9.c -o ./clang-5.0/fasta-9 
	$(CLang6)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang6) fasta-9.c -o ./clang-6.0/fasta-9 
	$(CLang7)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang7) fasta-9.c -o ./clang-7.0/fasta-9 
	$(CLang8)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang8) fasta-9.c -o ./clang-8.0/fasta-9 
#	$(CLang9)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native    -L$(LibCLang9) fasta-9.c -o ./clang-9.0/fasta-9 
	$(CLang10)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang10)  fasta-9.c -o ./clang-10.0/fasta-9 
	$(CLang11)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang11)  fasta-9.c -o ./clang-11.1/fasta-9 
	$(CLang12)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang12)  fasta-9.c -o ./clang-12.0/fasta-9 
	$(CLang13)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang13)  fasta-9.c -o ./clang-13.0/fasta-9 
	$(CLang14)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang14)  fasta-9.c -o ./clang-14.0/fasta-9 
	$(CLang15)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native   -L$(LibCLang15)  fasta-9.c -o ./clang-15.0/fasta-9 
	
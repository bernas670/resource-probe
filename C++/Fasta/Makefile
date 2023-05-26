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

IncCLang34 := $(DISS_C)/clang-3.4.2/include/c++/v1
IncCLang35 := $(DISS_C)/clang-3.5.2/include/c++/v1
IncCLang36 := $(DISS_C)/clang-3.6.2/include/c++/v1
IncCLang37 := $(DISS_C)/clang-3.7.1/include/c++/v1
IncCLang38 := $(DISS_C)/clang-3.8.1/include/c++/v1
IncCLang4 := $(DISS_C)/clang-4.0.0/include/c++/v1
IncCLang5 := $(DISS_C)/clang-5.0.2/include/c++/v1
IncCLang6 := $(DISS_C)/clang-6.0.1/include/c++/v1
IncCLang7 := $(DISS_C)/clang-7.0.1/include/c++/v1
IncCLang8 := $(DISS_C)/clang-8.0.0/include/c++/v1
IncCLang9 := $(DISS_C)/clang-9.0.0/include/c++/v1
IncCLang10 := $(DISS_C)/clang-10.0.0/include/c++/v1
IncCLang11 := $(DISS_C)/clang-11.1.0/include/c++/v1
IncCLang12 := $(DISS_C)/clang-12.0.1/include/c++/v1
IncCLang13 := $(DISS_C)/clang-13.0.1/include/c++/v1
IncCLang14 := $(DISS_C)/clang-14.0.0/include/c++/v1
IncCLang15 := $(DISS_C)/clang-15.0.6/include/c++/v1


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
#	./clang-3.4/fasta-6 25000000
	./clang-3.5/fasta-6 25000000
	./clang-3.6/fasta-6 25000000
	./clang-3.7/fasta-6 25000000
	./clang-3.8/fasta-6 25000000
	./clang-4.0/fasta-6 25000000
	./clang-5.0/fasta-6 25000000
	./clang-6.0/fasta-6 25000000
	./clang-7.0/fasta-6 25000000
	./clang-8.0/fasta-6 25000000
#	./clang-9.0/fasta-6 25000000
	./clang-10.0/fasta-6 25000000
	./clang-11.1/fasta-6 25000000
	./clang-12.0/fasta-6 25000000
	./clang-13.0/fasta-6 25000000
	./clang-14.0/fasta-6 25000000
	./clang-15.0/fasta-6 25000000

	

measure:
#	python3 ../../main.py "./clang-3.4/fasta-6 25000000" "./clang-3.4" "cpp-fasta-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.5/fasta-6 25000000" "./clang-3.5" "cpp-fasta-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.6/fasta-6 25000000" "./clang-3.6" "cpp-fasta-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.7/fasta-6 25000000" "./clang-3.7" "cpp-fasta-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.8/fasta-6 25000000" "./clang-3.8" "cpp-fasta-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-4.0/fasta-6 25000000" "./clang-4.0" "cpp-fasta-4.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-5.0/fasta-6 25000000" "./clang-5.0" "cpp-fasta-5.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-6.0/fasta-6 25000000" "./clang-6.0" "cpp-fasta-6.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-7.0/fasta-6 25000000" "./clang-7.0" "cpp-fasta-7.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-8.0/fasta-6 25000000" "./clang-8.0" "cpp-fasta-6.0" 40 45 0.01 -r 10
#	python3 ../../main.py "./clang-9.0/fasta-6 25000000" "./clang-9.0" "cpp-fasta-9.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-10.0/fasta-6 25000000" "./clang-10.0" "cpp-fasta-10.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-11.1/fasta-6 25000000" "./clang-11.1" "cpp-fasta-11.1" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-12.0/fasta-6 25000000" "./clang-12.0" "cpp-fasta-12.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-13.0/fasta-6 25000000" "./clang-13.0" "cpp-fasta-13.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-14.0/fasta-6 25000000" "./clang-14.0" "cpp-fasta-14.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-15.0/fasta-6 25000000" "./clang-15.0" "cpp-fasta-15.0" 40 45 0.01 -r 10


define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
#	$(call measure_mem,./clang-3.4/fasta-6 25000000,./clang-3.4,mem_test)
#	python3 ../../mem_parser.py "./clang-3.4/" "cpp-fasta-3.4"
	$(call measure_mem,./clang-3.5/fasta-6 25000000,./clang-3.5,mem_test)
	python3 ../../mem_parser.py "./clang-3.5/" "cpp-fasta-3.5"
	$(call measure_mem,./clang-3.6/fasta-6 25000000,./clang-3.6,mem_test)
	python3 ../../mem_parser.py "./clang-3.6/" "cpp-fasta-3.6"
	$(call measure_mem,./clang-3.7/fasta-6 25000000,./clang-3.7,mem_test)
	python3 ../../mem_parser.py "./clang-3.7/" "cpp-fasta-3.7"
	$(call measure_mem,./clang-3.8/fasta-6 25000000,./clang-3.8,mem_test)
	python3 ../../mem_parser.py "./clang-3.8/" "cpp-fasta-3.8"
	$(call measure_mem,./clang-4.0/fasta-6 25000000,./clang-4.0,mem_test)
	python3 ../../mem_parser.py "./clang-4.0/" "cpp-fasta-4.0"
	$(call measure_mem,./clang-5.0/fasta-6 25000000,./clang-5.0,mem_test)
	python3 ../../mem_parser.py "./clang-5.0/" "cpp-fasta-5.0"
	$(call measure_mem,./clang-6.0/fasta-6 25000000,./clang-6.0,mem_test)
	python3 ../../mem_parser.py "./clang-6.0/" "cpp-fasta-6.0"
	$(call measure_mem,./clang-7.0/fasta-6 25000000,./clang-7.0,mem_test)
	python3 ../../mem_parser.py "./clang-7.0/" "cpp-fasta-7.0"
	$(call measure_mem,./clang-8.0/fasta-6 25000000,./clang-8.0,mem_test)
	python3 ../../mem_parser.py "./clang-8.0/" "cpp-fasta-8.0"
#	$(call measure_mem,./clang-9.0/fasta-6 25000000,./clang-9.0,mem_test)
#	python3 ../../mem_parser.py "./clang-9.0/" "cpp-fasta-9.0"
	$(call measure_mem,./clang-10.0/fasta-6 25000000,./clang-10.0,mem_test)
	python3 ../../mem_parser.py "./clang-10.0/" "cpp-fasta-10.0"
	$(call measure_mem,./clang-11.1/fasta-6 25000000,./clang-11.1,mem_test)
	python3 ../../mem_parser.py "./clang-11.1/" "cpp-fasta-11.1"
	$(call measure_mem,./clang-12.0/fasta-6 25000000,./clang-12.0,mem_test)
	python3 ../../mem_parser.py "./clang-12.0/" "cpp-fasta-12.0"
	$(call measure_mem,./clang-13.0/fasta-6 25000000,./clang-13.0,mem_test)
	python3 ../../mem_parser.py "./clang-13.0/" "cpp-fasta-13.0"
	$(call measure_mem,./clang-14.0/fasta-6 25000000,./clang-14.0,mem_test)
	python3 ../../mem_parser.py "./clang-14.0/" "cpp-fasta-14.0"
	$(call measure_mem,./clang-15.0/fasta-6 25000000,./clang-15.0,mem_test)
	python3 ../../mem_parser.py "./clang-15.0/" "cpp-fasta-15.0"


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
#	$(CLang34)clang++ -pipe -O3 -std=c++11 -fomit-frame-pointer -march=native -fopenmp -I$(IncCLang34) fasta-6.cpp -o ./clang-3.4/fasta-6 -stdlib=libc++
	$(CLang35)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang35) fasta-6.cpp -o ./clang-3.5/fasta-6 -stdlib=libc++
	$(CLang36)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang36) fasta-6.cpp -o ./clang-3.6/fasta-6 -stdlib=libc++
	$(CLang37)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang37) fasta-6.cpp -o ./clang-3.7/fasta-6 -stdlib=libc++
	$(CLang38)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang38) fasta-6.cpp -o ./clang-3.8/fasta-6 -stdlib=libc++
	$(CLang4)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang4) fasta-6.cpp -o ./clang-4.0/fasta-6 -stdlib=libc++
	$(CLang5)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang5) fasta-6.cpp -o ./clang-5.0/fasta-6 -stdlib=libc++
	$(CLang6)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang6) fasta-6.cpp -o ./clang-6.0/fasta-6 -stdlib=libc++
	$(CLang7)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang7) fasta-6.cpp -o ./clang-7.0/fasta-6 -stdlib=libc++
	$(CLang8)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang8) fasta-6.cpp -o ./clang-8.0/fasta-6 -stdlib=libc++
#	$(CLang9)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang9) fasta-6.cpp -o ./clang-9.0/fasta-6 -stdlib=libc++
	$(CLang10)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang10) fasta-6.cpp -o ./clang-10.0/fasta-6 -stdlib=libc++
	$(CLang11)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang11) fasta-6.cpp -o ./clang-11.1/fasta-6 -stdlib=libc++
	$(CLang12)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang12) fasta-6.cpp -o ./clang-12.0/fasta-6 -stdlib=libc++
	$(CLang13)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang13) fasta-6.cpp -o ./clang-13.0/fasta-6 -stdlib=libc++
	$(CLang14)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang14) fasta-6.cpp -o ./clang-14.0/fasta-6 -stdlib=libc++
	$(CLang15)clang++ -pipe -O3 -O2 -std=c++11 -fomit-frame-pointer -march=native -I$(IncCLang15) fasta-6.cpp -o ./clang-15.0/fasta-6 -stdlib=libc++
	
	
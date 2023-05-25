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
	./clang-3.4/binarytree-5 21
	./clang-3.5/binarytree-5 21
	./clang-3.6/binarytree-5 21
	./clang-3.7/binarytree-5 21
	./clang-3.8/binarytree-5 21
	./clang-4.0/binarytree-5 21
	./clang-5.0/binarytree-5 21
	./clang-6.0/binarytree-5 21
	./clang-7.0/binarytree-5 21
	./clang-8.0/binarytree-5 21
#	./clang-9.0/binarytree-5 21
	./clang-10.0/binarytree-5 21
	./clang-11.1/binarytree-5 21
	./clang-12.0/binarytree-5 21
	./clang-13.0/binarytree-5 21
	./clang-14.0/binarytree-5 21
	./clang-15.0/binarytree-5 21

	

measure:
	python3 ../../main.py "./clang-3.4/binarytree-5 21" "./clang-3.4" "c-bintrees-3.4" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.5/binarytree-5 21" "./clang-3.5" "c-bintrees-3.5" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.6/binarytree-5 21" "./clang-3.6" "c-bintrees-3.6" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.7/binarytree-5 21" "./clang-3.7" "c-bintrees-3.7" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-3.8/binarytree-5 21" "./clang-3.8" "c-bintrees-3.8" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-4.0/binarytree-5 21" "./clang-4.0" "c-bintrees-4.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-5.0/binarytree-5 21" "./clang-5.0" "c-bintrees-5.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-6.0/binarytree-5 21" "./clang-6.0" "c-bintrees-6.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-7.0/binarytree-5 21" "./clang-7.0" "c-bintrees-7.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-8.0/binarytree-5 21" "./clang-8.0" "c-bintrees-8.0" 40 45 0.01 -r 10
#	python3 ../../main.py "./clang-9.0/binarytree-5 21" "./clang-9.0" "c-bintrees-9.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-10.0/binarytree-5 21" "./clang-10.0" "c-bintrees-10.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-11.1/binarytree-5 21" "./clang-11.1" "c-bintrees-11.1" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-12.0/binarytree-5 21" "./clang-12.0" "c-bintrees-12.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-13.0/binarytree-5 21" "./clang-13.0" "c-bintrees-13.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-14.0/binarytree-5 21" "./clang-14.0" "c-bintrees-14.0" 40 45 0.01 -r 10
	python3 ../../main.py "./clang-15.0/binarytree-5 21" "./clang-15.0" "c-bintrees-15.0" 40 45 0.01 -r 10


define measure_mem
	for number in 1 2 3 4 5 6 7 8 9 10; do \
		valgrind --tool=massif --stacks=yes --massif-out-file=$(2)/$(3)_$$number $(1) ; done
endef

memory:
	$(call measure_mem,./clang-3.4/binarytree-5 21,./clang-3.4,mem_test)
	python3 ../../mem_parser.py "./clang-3.4/" "c-bintrees-3.4"
	$(call measure_mem,./clang-3.5/binarytree-5 21,./clang-3.5,mem_test)
	python3 ../../mem_parser.py "./clang-3.5/" "c-bintrees-3.5"
	$(call measure_mem,./clang-3.6/binarytree-5 21,./clang-3.6,mem_test)
	python3 ../../mem_parser.py "./clang-3.6/" "c-bintrees-3.6"
	$(call measure_mem,./clang-3.7/binarytree-5 21,./clang-3.7,mem_test)
	python3 ../../mem_parser.py "./clang-3.7/" "c-bintrees-3.7"
	$(call measure_mem,./clang-3.8/binarytree-5 21,./clang-3.8,mem_test)
	python3 ../../mem_parser.py "./clang-3.8/" "c-bintrees-3.8"
	$(call measure_mem,./clang-4.0/binarytree-5 21,./clang-4.0,mem_test)
	python3 ../../mem_parser.py "./clang-4.0/" "c-bintrees-4.0"
	$(call measure_mem,./clang-5.0/binarytree-5 21,./clang-5.0,mem_test)
	python3 ../../mem_parser.py "./clang-5.0/" "c-bintrees-5.0"
	$(call measure_mem,./clang-6.0/binarytree-5 21,./clang-6.0,mem_test)
	python3 ../../mem_parser.py "./clang-6.0/" "c-bintrees-6.0"
	$(call measure_mem,./clang-7.0/binarytree-5 21,./clang-7.0,mem_test)
	python3 ../../mem_parser.py "./clang-7.0/" "c-bintrees-7.0"
	$(call measure_mem,./clang-8.0/binarytree-5 21,./clang-8.0,mem_test)
	python3 ../../mem_parser.py "./clang-8.0/" "c-bintrees-8.0"
#	$(call measure_mem,./clang-9.0/binarytree-5 21,./clang-9.0,mem_test)
#	python3 ../../mem_parser.py "./clang-9.0/" "c-bintrees-9.0"
	$(call measure_mem,./clang-10.0/binarytree-5 21,./clang-10.0,mem_test)
	python3 ../../mem_parser.py "./clang-10.0/" "c-bintrees-10.0"
	$(call measure_mem,./clang-11.1/binarytree-5 21,./clang-11.1,mem_test)
	python3 ../../mem_parser.py "./clang-11.1/" "c-bintrees-11.1"
	$(call measure_mem,./clang-12.0/binarytree-5 21,./clang-12.0,mem_test)
	python3 ../../mem_parser.py "./clang-12.0/" "c-bintrees-12.0"
	$(call measure_mem,./clang-13.0/binarytree-5 21,./clang-13.0,mem_test)
	python3 ../../mem_parser.py "./clang-13.0/" "c-bintrees-13.0"
	$(call measure_mem,./clang-14.0/binarytree-5 21,./clang-14.0,mem_test)
	python3 ../../mem_parser.py "./clang-14.0/" "c-bintrees-14.0"
	$(call measure_mem,./clang-15.0/binarytree-5 21,./clang-15.0,mem_test)
	python3 ../../mem_parser.py "./clang-15.0/" "c-bintrees-15.0"

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
	$(CLang34)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-3.4/binarytree-5
	$(CLang35)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-3.5/binarytree-5
	$(CLang36)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-3.6/binarytree-5
	$(CLang37)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-3.7/binarytree-5
	$(CLang38)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-3.8/binarytree-5
	$(CLang4)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-4.0/binarytree-5
	$(CLang5)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-5.0/binarytree-5
	$(CLang6)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-6.0/binarytree-5
	$(CLang7)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-7.0/binarytree-5
	$(CLang8)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-8.0/binarytree-5
#	$(CLang9)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-9.0/binarytree-5
	$(CLang10)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-10.0/binarytree-5
	$(CLang11)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-11.1/binarytree-5
	$(CLang12)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-12.0/binarytree-5
	$(CLang13)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-13.0/binarytree-5
	$(CLang14)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-14.0/binarytree-5
	$(CLang15)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -pthread binarytree-5.c -o ./clang-15.0/binarytree-5
	
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
#	./clang-3.4/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-3.5/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-3.6/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-3.7/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-3.8/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-4.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-5.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-6.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-7.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-8.0/revcomp-6 < ../../revcomp-input25000000.txt
#	./clang-9.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-10.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-11.1/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-12.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-13.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-14.0/revcomp-6 < ../../revcomp-input25000000.txt
	./clang-15.0/revcomp-6 < ../../revcomp-input25000000.txt

	

measure:


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
#	$(CLang34)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-3.4/revcomp-6 -stdlib=libc++ -pthread
	$(CLang35)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-3.5/revcomp-6 -stdlib=libc++ -pthread
	$(CLang36)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-3.6/revcomp-6 -stdlib=libc++ -pthread
	$(CLang37)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-3.7/revcomp-6 -stdlib=libc++ -pthread
	$(CLang38)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-3.8/revcomp-6 -stdlib=libc++ -pthread
	$(CLang4)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-4.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang5)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-5.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang6)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-6.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang7)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-7.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang8)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-8.0/revcomp-6 -stdlib=libc++ -pthread
#	$(CLang9)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-9.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang10)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-10.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang11)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-11.1/revcomp-6 -stdlib=libc++ -pthread
	$(CLang12)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-12.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang13)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-13.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang14)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-14.0/revcomp-6 -stdlib=libc++ -pthread
	$(CLang15)clang++ -pipe -O3 -fomit-frame-pointer -march=native -std=c++11 revcomp-6.cpp -o ./clang-15.0/revcomp-6 -stdlib=libc++ -pthread
	
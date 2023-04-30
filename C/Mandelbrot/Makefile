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
	./clang-3.4/mandelbrot-9 21
	./clang-3.5/mandelbrot-9 21
	./clang-3.6/mandelbrot-9 21
	./clang-3.7/mandelbrot-9 21
	./clang-3.8/mandelbrot-9 21
	./clang-4.0/mandelbrot-9 21
	./clang-5.0/mandelbrot-9 21
	./clang-6.0/mandelbrot-9 21
	./clang-7.0/mandelbrot-9 21
	./clang-8.0/mandelbrot-9 21
#	./clang-9.0/mandelbrot-9 21
	./clang-10.0/mandelbrot-9 21
	./clang-11.1/mandelbrot-9 21
	./clang-12.0/mandelbrot-9 21
	./clang-13.0/mandelbrot-9 21
	./clang-14.0/mandelbrot-9 21
	./clang-15.0/mandelbrot-9 21

	

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
	$(CLang34)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-3.4/mandelbrot-9
	$(CLang35)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-3.5/mandelbrot-9
	$(CLang36)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-3.6/mandelbrot-9
	$(CLang37)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-3.7/mandelbrot-9
	$(CLang38)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-3.8/mandelbrot-9
	$(CLang4)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-4.0/mandelbrot-9
	$(CLang5)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-5.0/mandelbrot-9
	$(CLang6)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-6.0/mandelbrot-9
	$(CLang7)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-7.0/mandelbrot-9
	$(CLang8)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-8.0/mandelbrot-9
#	$(CLang9)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-9.0/mandelbrot-9
	$(CLang10)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-10.0/mandelbrot-9
	$(CLang11)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-11.1/mandelbrot-9
	$(CLang12)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-12.0/mandelbrot-9
	$(CLang13)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-13.0/mandelbrot-9
	$(CLang14)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-14.0/mandelbrot-9
	$(CLang15)clang -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp  mandelbrot-9.c -o ./clang-15.0/mandelbrot-9
	
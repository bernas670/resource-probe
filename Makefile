
install:
	pip3 install -r requirements.txt

compile:
	python3 compile_all.py compile

run:
	python3 compile_all.py run

clean:
	python3 compile_all.py clean

measure:
	sudo chmod -R a+r /sys/class/powercap/intel-rapl
	python3 disable_services.py
	python3 compile_all.py measure
	python3 disable_services.py -r

	
missing:	
	sudo chmod -R a+r /sys/class/powercap/intel-rapl
	python3 disable_services.py
#	cd Python/Mandelbrot && make measure
	cd Python/Spectral-Norm && make measure
	python3 disable_services.py -r

# TODO: Add other options

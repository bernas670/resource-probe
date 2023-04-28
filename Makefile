
install:
	pip3 install -r requirements.txt

compile:
	python3 compile_all.py compile

run:
	python3 compile_all.py run

clean:
	python3 compile_all.py clean

measure:
	python3 compile_all.py measure

	

# TODO: Add other options
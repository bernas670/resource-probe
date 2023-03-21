import os
import subprocess as sub

def print_errors(errors):
	print("The makefiles of the following folders failed to compile")
	for error in errors:
		print("->" + error)

def compile_all():
	errors = []

	directory = "."
	for filename in os.scandir(directory):
		if filename.is_dir() and filename.name != "__pycache__" and filename.name != ".git":
			print("Compiling: "+ filename.path)
			cmp = sub.Popen("cd " + filename.path + " && make compile", shell=True, stdout=sub.PIPE,stderr=sub.STDOUT)
			ret = cmp.wait()

			if ret != 0:
			   errors.append(filename.path)

	if len(errors) != 0:
		print_errors(errors)
	else:
		print("All makefiles ran without errors")



def main():
	compile_all()


if __name__ == '__main__':
	main()
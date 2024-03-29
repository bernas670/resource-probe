import os
import sys
import subprocess as sub

def print_errors(errors, action):
	print("The makefiles of the following folders failed to " + action)
	for error in errors:
		print("->" + error)

def action_all(action) -> int:
	errors = []

	directory = "."

	exclude = set(['Compilers','__pycache__','.git'])

	for root,dirs,files in os.walk(directory):
		dirs[:] = [d for d in dirs if d not in exclude]

		for file in files:
				if file == "Makefile" and root != ".":
					print("Performing " + action +": "+ root + "/" + file)
					cmp = sub.Popen("cd " + root + " && make " + action, shell=True, stdout=sub.PIPE,stderr=sub.STDOUT)
					ret = cmp.wait()

					if ret != 0:
			   			errors.append(root + "/" + file)

	if len(errors) != 0:
		print_errors(errors, action)
		return -1
	else:
		print("All makefiles ran without errors")
		return 0




def main() -> int:
	if len(sys.argv) != 2 and sys.argv[1] not in ['compile','run', 'measure', 'clean', 'memory']:
		print("Usage: Python3 compile_all.py [compile | run | measure | clean | memory]")
		return -1
	else:
		return action_all(sys.argv[1])


if __name__ == '__main__':
	main()
import msparser
import os
import argparse
import csv

def calculate_total_memory(path_to_file):
    data = msparser.parse_file(path_to_file)

    heap = 0
    stack = 0

    for snapshot in data['snapshots']:
        heap += snapshot['mem_heap']
        heap += snapshot['mem_heap_extra']
        stack += snapshot['mem_stack']

    return heap, stack



def main(directory,file):

    with open(directory + "/data_mem_" + file + ".csv","w") as file:

        writer = csv.writer(file)
        writer.writerow(['heap','stack'])

        for root,dirs,files in os.walk(directory):
                for file in files:
                    if file.startswith("mem_"):
                        heap, stack = calculate_total_memory(root + "/" +file)
                        writer.writerow([heap,stack])

                     
                    



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parses total memory consumption from massif files")
    parser.add_argument('path', type=str, help='The path  of the files to parse')
    parser.add_argument('file', type=str, help='File naming convention')

    args = parser.parse_args()

    main(args.path,args.file)
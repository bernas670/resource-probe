import pandas as pd
import scipy.stats as stats
import math
import os
import csv
import argparse

def anderson(data) -> float:
    ad, _, _ = stats.anderson(data)

    ad = ad * (1 + (.75/50) + 2.25/(50**2))

    if ad >= .6:
        p = math.exp(1.2937 - 5.709*ad - .0186*(ad**2))
    elif ad >= .34:
        p = math.exp(.9177 - 4.279*ad - 1.38*(ad**2))
    elif ad > .2:
        p = 1 - math.exp(-8.318 + 42.796*ad - 59.938*(ad**2))
    else:
        p = 1 - math.exp(-13.436 + 101.14*ad - 223.73*(ad**2))

    return p


def get_test_data(path, file, sf):
    df = pd.read_csv(path + "/" + file)

    sf = path + "/" + sf
    
    sf_exists = False

    if os.path.exists(sf):
        print("File exists")
        sf_exists = True
    else:
        print("File does not exist")
        sf_exists = False
        
    with open(sf,"a") as file:
        writer = csv.writer(file)

        if not sf_exists:
            writer.writerow(['shapiro_duration',
                             'shapiro_package',
                             'shapiro_dram',
                             'shapiro_peak_rss',
                             'anderson_duration',
                             'anderson_package',
                             'anderson_dram',
                             'anderson_peak_rss'])
        
        _,dur_pvalue = stats.shapiro(df['duration'])
        _,package_pvalue = stats.shapiro(df['package'])
        _,dram_pvalue = stats.shapiro(df['dram'])
        _,peak_rss_pvalue = stats.shapiro(df['peak_rss'])

        writer.writerow([dur_pvalue,
                         package_pvalue,
                         dram_pvalue,
                         peak_rss_pvalue, 
                         anderson(df['duration']),
                         anderson(df['package']),
                         anderson(df['dram']),
                         anderson(df['peak_rss'])])    




def get_program_language(root):
    if "C++" in root:
        return "cpp_" 
    elif "Java" in root:
        return "java_"
    elif "Python" in root:
        return "py_"
    elif "/C/" in root:
        return "c_"
    else:
        return "error"
    

def get_program(root):
    if "Binary Trees" in root:
        return "bintrees" 
    elif "Fannkuch Redux" in root:
        return "fannkuchredux"
    elif "Fasta" in root:
        return "fasta"
    elif "K-Nucleotide" in root:
        return "knucleotide"
    elif "Mandelbrot" in root:
        return "mandelbrot"
    elif "N-Body" in root:
        return "nbody"
    elif "Pi Digits" in root:
        return "pidigits"
    elif "Regex Redux" in root:
        return "regexredux"
    elif "Rev Comp" in root:
        return "revcomp"
    elif "Spectral Norm" in root:
        return "spectralnorm"
    else:
        return "error"
    


def main(directory):

    for root,dirs,files in os.walk(directory):
                for file in files:
                    if file.endswith(".csv"):
                        sf = "sa_test_" + get_program_language(root) + get_program(root) + ".csv"
                        print(sf)
                        get_test_data(root,file,sf)
                        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parses total memory consumption from massif files")
    parser.add_argument('path', type=str, help='The path  of the files to parse')

    args = parser.parse_args()
    main(args.path)



#df = pd.read_csv('./Results/C/Binary Trees/data_c-bintrees-3.4.csv')
#df


#_, pvalue = stats.shapiro(df['package'])
#print(pvalue)
#pvalue = anderson(df['package'])
#print(pvalue)
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

def file_exists(path):

    if os.path.exists(path):
        print("File exists")
        return True
    else:
        print("File does not exist")
        return False


def normality_tests(df, sf_exists, sf_writer):

    if not sf_exists:
        sf_writer.writerow([
                            'shapiro_duration',
                            'anderson_duration',
                            'dagostino_duration',
                            'shapiro_package',
                            'anderson_package',
                            'dagostino_package',
                            'shapiro_dram',
                            'anderson_dram',
                            'dagostino_dram',
                            'shapiro_peak_rss',
                            'anderson_peak_rss',
                            'dagostino_peak_rss'])
        
    _,s_dur_pvalue = stats.shapiro(df['duration'])
    a_dur_pvalue = anderson(df['duration'])
    _, da_dur_pvalue = stats.normaltest(df['duration'])

    _,s_package_pvalue = stats.shapiro(df['package'])
    a_package_pvalue = anderson(df['package'])
    _, da_package_pvalue = stats.normaltest(df['package'])

    _,s_dram_pvalue = stats.shapiro(df['dram'])
    a_dram_pvalue = anderson(df['dram'])
    _, da_dram_pvalue = stats.normaltest(df['dram'])

    _,s_peak_rss_pvalue = stats.shapiro(df['peak_rss'])
    a_peak_rss_pvalue = anderson(df['peak_rss'])
    _, da_peak_rss_pvalue = stats.normaltest(df['peak_rss'])

    res = [
        s_dur_pvalue,
        a_dur_pvalue,
        da_dur_pvalue,
        s_package_pvalue,
        a_package_pvalue,
        da_package_pvalue,
        s_dram_pvalue,
        a_dram_pvalue,
        da_dram_pvalue,
        s_peak_rss_pvalue,
        a_peak_rss_pvalue,
        da_peak_rss_pvalue
    ]

    sf_writer.writerow(res)

    return res



def is_normal_dist(s1,a1,da1):
    n_normal = []
    normal = []

    if s1 <= 0.05:
        n_normal.append(s1)
    else:
        normal.append(s1)

    if a1 <= 0.05:
        n_normal.append(a1)
    else:
        normal.append(s1)

    if da1 <= 0.05:
        n_normal.append(da1)
    else:
        normal.append(s1)


    if len(n_normal) == 3:
        return False
    else:
        return True
        


def spearman_coef(df1,df2):
    _, p = stats.spearmanr(df1,df2)
    return p
        

def get_spearman_data(df,writer,cf_exists):

    if not cf_exists:
        writer.writerow([
                        'spearman_dur-pckg',
                        'spearman_dur-dram',
                        'spearman_dur-peak_rss',
                        'spearman_pckg-dram',
                        'spearman_pckg-peak_rss',
                        'spearman_dram-peak_rss',
                        ])
        
    dur_pckg = spearman_coef(df['duration'],df['package'])
    dur_dram = spearman_coef(df['duration'],df['dram'])
    dur_rss = spearman_coef(df['duration'],df['peak_rss'])
    pckg_dram = spearman_coef(df['package'],df['dram'])
    pckg_rss = spearman_coef(df['package'],df['peak_rss'])
    dram_rss = spearman_coef(df['dram'],df['peak_rss'])

    writer.writerow([
                    dur_pckg,
                    dur_dram,
                    dur_rss,
                    pckg_dram,
                    pckg_rss,
                    dram_rss
                    ])



def pearson_coef(df1,df2):
    _,_,pearson,p_val,lin_err =stats.linregress(df1, df2)

    return [pearson,p_val,lin_err]


def get_pearson_data(df,writer,pf_exists,normals):
    
    if not pf_exists:
         writer.writerow([
                             'hom_dur-pckg',
                             'lin_dur-pckg',
                             'pearson_dur-pckg',
                             'lin_error_dur-pckg',
                             'hom_dur-dram',
                             'lin_dur-dram',
                             'pearson_dur-dram',
                             'lin_error_dur-dram',
                             'hom_dur-peak_rss',
                             'lin_dur-peak_rss',
                             'pearson_dur-peak_rss',
                             'lin_error_dur-peak_rss',                            
                             'hom_pckg-dram',
                             'lin_pckg-dram',
                             'pearson_pckg-dram',
                             'lin_error_pckg-dram',                            
                             'hom_pckg-peak_rss',
                             'lin_pckg-peak_rss',
                             'pearson_pckg-peak_rss',
                             'lin_error_pckg-peak_rss',                            
                             'hom_dram-peak_rss',
                             'lin_dram-peak_rss',
                             'pearson_dram-peak_rss'
                             'lin_error_dram-peak_rss',
                             ])
         
    _,h_dur_pckg = stats.bartlett(df['duration'],df['package'])
    _,h_dur_dram = stats.bartlett(df['duration'],df['dram'])
    _,h_dur_rss = stats.bartlett(df['duration'],df['peak_rss'])
    _,h_pckg_dram = stats.bartlett(df['package'],df['dram'])
    _,h_pckg_rss = stats.bartlett(df['package'],df['peak_rss'])
    _,h_dram_rss = stats.bartlett(df['dram'],df['peak_rss'])

    dur_pckg=dur_dram=dur_rss=pckg_dram=pckg_rss=dram_rss = ["NOT VALID","NOT VALID","NOT VALID"]

    if(h_dur_pckg < 0.05 and normals[0] == normals[1]):
        dur_pckg = pearson_coef(df['duration'],df['package'])

    if(h_dur_dram < 0.05 and normals[0] == normals[2]):
        dur_dram = pearson_coef(df['duration'],df['dram'])

    if(h_dur_rss < 0.05 and normals[0] == normals[3]):
        dur_rss = pearson_coef(df['duration'],df['peak_rss'])

    if(h_pckg_dram < 0.05 and normals[1] == normals[2]):
        pckg_dram = pearson_coef(df['package'],df['dram'])

    if(h_pckg_rss < 0.05 and normals[1] == normals[3]):
        pckg_rss = pearson_coef(df['package'],df['peak_rss'])

    if(h_dram_rss < 0.05 and normals[2] == normals[3]):
        dram_rss = pearson_coef(df['dram'],df['peak_rss'])

    writer.writerow([
                        h_dur_pckg,
                        dur_pckg[0],
                        dur_pckg[1],
                        dur_pckg[2],
                        h_dur_dram,
                        dur_dram[0],
                        dur_dram[1],
                        dur_dram[2],
                        h_dur_rss,
                        dur_rss[0],
                        dur_rss[1],
                        dur_rss[2],
                        h_pckg_dram,
                        pckg_dram[0],
                        pckg_dram[1],
                        pckg_dram[2],
                        h_pckg_rss,
                        pckg_rss[0],
                        pckg_rss[1],
                        pckg_rss[2],
                        h_dram_rss,
                        dram_rss[0],
                        dram_rss[1],
                        dram_rss[2],
                    ])



    
    


def get_test_data(path, file, n_file, c_file, p_file):
    df = pd.read_csv(path + "/" + file)

    nf = path + "/" + n_file
    cf = path + "/" + c_file
    pf = path + "/" + p_file
    
    sf_exists = file_exists(nf)
    cf_exists = file_exists(cf)
    pf_exists = file_exists(pf)
        
    with open(nf,"a") as normal, open(cf,"a") as spear, open(pf,"a") as pear:

        writer1 = csv.writer(normal)
        writer2 = csv.writer(spear)
        writer3 = csv.writer(pear)

        normal = normality_tests(df,sf_exists,writer1)

        is_normal = []

        for i in range(4):
            is_normal.append(is_normal_dist(normal[i * 3], normal[i * 3 + 1], normal[i * 3 + 2]))

        get_spearman_data(df,writer2,cf_exists)

        get_pearson_data(df,writer3,pf_exists,is_normal)

        







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
                        sf = "normal_test_" + get_program_language(root) + get_program(root) + ".csv"
                        cf = "spear_test_" + get_program_language(root) + get_program(root) + ".csv"
                        pf = "pearson_test_" + get_program_language(root) + get_program(root) + ".csv"
                        get_test_data(root,file,sf,cf,pf)
                        


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
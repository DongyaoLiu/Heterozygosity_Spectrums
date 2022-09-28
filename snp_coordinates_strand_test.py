##This script is to test the coordinates and strand in the mummer out file, like .snps
import sys
from Bio import SeqIO


##data input
species1_fa = "/lustre1/g/sbs_cgz/wormbase/ftp.wormbase.org/pub/wormbase/releases/current-production-release/species/c_elegans/PRJNA275000/c_elegans.PRJNA275000.WS285.genomic.fa"
species2_fa = "/home/dongyao/genomics/wild_strain/GCA_016989125.1_XZ1516_Canu/GCA_016989125.1_XZ1516_Canu_genomic.fna"
snps_file = open("/lustre1/u/dongyao/mummer/XZ1516_2_N2.snps", "r")

##fa2dict
fa_dict1 = SeqIO.to_dict(SeqIO.parse(f"{species1_fa}", "fasta"))
fa_dict2 = SeqIO.to_dict(SeqIO.parse(f"{species2_fa}", "fasta"))


reverse = {"A" : "T", "T" : "A", "C":"G", "G":"C"}

##main loop
flag = 0
for line in snps_file.readlines():
    flag = flag + 1
    if flag not in [1, 2, 3, 4, 5]:
        line_elements = line.strip().split()
        line_elements = list(filter(lambda a:a != "|", line_elements))
        Location1 = int(line_elements[0])
        nuc1 = line_elements[1]
        Location2 = int(line_elements[3])
        nuc2 = line_elements[2]
        Scaff1 = line_elements[8]
        Scaff2 = line_elements[9]
        Strand1 = line_elements[6]
        Strand2 = line_elements[7]
        if Strand1 == "1":
            if str(fa_dict1[f"{Scaff1}"].seq)[(Location1 - 1)].upper() == nuc1.upper():
                pass
            elif nuc1 == ".":
                pass
            else:
                print("this file is not 1 based coordinates index")
                print("wrong")
                break
        else:
            if str(fa_dict1[f"{Scaff1}"].seq)[(Location1 - 1)].upper() == reverse[f"{nuc1.upper()}"]:
                pass
            elif nuc1 == ".":
                pass
            else:
                print("-1 not represent - strand")
                print(wrong)
                break

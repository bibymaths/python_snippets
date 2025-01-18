#!usr\bin\python

#User INPUT
DNAseq = "ATGCGCAGACGATCGATAGCGCTAGGACGAGG";
print("For this nucleotide sequence: "+(DNAseq));

#Lowecase function call
lowDNAseq = DNAseq.lower();
print("The DNA sequence in lowercase : "+(lowDNAseq));

#Trancription
mRNAseq = DNAseq.replace("T", "U");
print("The mRNA sequence is : "+(mRNAseq));

#"ATG" count
ATG = DNAseq.find("ATG");
print("The position of ATG is : "+str(ATG));

#'AA', 'AT', 'AG', 'AC' counts
AA = DNAseq.count("AA");
AT = DNAseq.count("AT");
AG = DNAseq.count("AG");
AC = DNAseq.count("AC");
print("The Dinucleotide Count for dimer 'AA'      :" +str(AA));
print("The Dinucleotide Count for dimer 'AT'      :" +str(AT));
print("The Dinucleotide Count for dimer 'AG'     :" +str(AG)); 
print("The Dinucleotide Count for dimer 'AC'      :" +str(AC));
 
exit();

#!\usr\bin\python -w

#USER INPUT
DNAseq = input("\nEnter the DNA sequence :")
#Converting lowecases to Uppercase
UDNAseq = DNAseq.upper()

#Frequency of nucleotides
A = UDNAseq.count("A")
G = UDNAseq.count("G")
T = UDNAseq.count("T")
C = UDNAseq.count("C")
#Length of nucletide sequence
length = len(UDNAseq)
#sum of number of nucleotides 
Total = A + G + C + T

#checking for validity of code i.e. length must be equal to Total 
if length == Total :
    print("\nAdenine is " +str(A))
    print("\nCystosine is" +str(C))
    print("\nGuanine is " +str(G))
    print("\nThymine is " +str(T))

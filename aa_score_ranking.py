ProtSeq = input("Protein sequence: ").upper()
#print (len(ProtSeq))
ProtDeg = {"A":4,"C":2,"D":2,"E":2,"F":2,"G":4,"H":2,"I":3,"K":2,"L":6,"M":1,"N":2,"P":4,"Q":2,"R":6,"S":6,"T":4,"V":4,"W":1,"Y":2}
SegsValues=[]; i=0
#while len(ProtSeq[i:i+15])==15:
while i<(len(ProtSeq )-7):
    #print ("inside")
    degen = 0
    for x in ProtSeq[i:i+15]:
        degen += ProtDeg.get(x,3.05)
        #print (degen)
    SegsValues.append(degen); i += 1
    #print (SegsValues)
   
print (ProtSeq [SegsValues.index (min (SegsValues)) : SegsValues.index (min (SegsValues))+15])

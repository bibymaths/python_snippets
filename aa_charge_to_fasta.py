fh = open("prot.fas")
fh.readline()
sequence = ""
for line in fh:
    sequence += line[:-1].upper()
    fh.close()
    charge = -0.002
    AACharge={"C":-.045,"D":-.999,"E":-.998,"H":.091,
              "K":1,"R":1,"Y":-0.001}
    for aa in sequence:
        charge += AACharge.get(aa,0)
        fhout = open("out.txt")
        fhout.write(str(charge))
        fhout.close()

height = float(input("Enter height\n>>: "))
width = float(input("Enter width\n>>: "))
length = float(input("Enter length\n>>: "))
void = float(input("Enter VOID area\n>>: "))
coat = int(input("Enter Num coats\n>>: "))
area = height*(length+width)*2
parea = area - void
lneed = parea*coat
print("\tINFO:\nHeight:\t"+str(height)+"\nWidth:\t"+str(width)+"\nLength:\t"+str(length)+"\nVoid Area:\t"+str(void)+"\nCoats:\t"+str(coat)+"\nArea:\t"+str(area)+"\nPaintable Area:\t"+str(parea)+"\nL Needed:\t"+str(lneed))
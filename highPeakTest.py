file1=open(r"C:\Users\91904\source\repos\highPeakTest\highPeakTest\sample_input.txt","r")
li=file1.readlines()
goodies=[]
empno=int(li[0][-2])
for i in range(4,len(li)):
    l=li[i].split(":")
    goodies.append([l[0],int(l[1])])
goodies=sorted(goodies,key=lambda x:x[1])
md=float('inf')
for i in range(0,len(goodies)-empno+1):
    dif=goodies[i+empno-1][1]-goodies[i][1]
    if dif<md:
        mi=i
        md=dif
file1.close()
file2=open(r"C:\Users\91904\source\repos\highPeakTest\highPeakTest\sample_output.txt","w")
file2.write("The goodies selected for distribution are: \n \n")
for i in range(mi,mi+empno):
    for x in goodies:
        if(x==goodies[i]):
            file2.write(str(x[0])+": "+str(x[1])+"\n")

            
file2.write("\n And the difference between the chosen goodie with highest price and the lowest price is "+str(md))

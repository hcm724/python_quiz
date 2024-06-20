i,j=9,1
while i>=1:
    while j<=9:
        print(i,"x",j,"=",i*j,end="\t")
        print(i-1,"x",j,"=",(i-1)*j,end="\t")
        print(i-2,"x",j,"=",(i-2)*j,end="\n")
        j+=1
    print()
    i-=3
    j=1
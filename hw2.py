layers=int(input("Enter the number of layers(2 to 5)="))
side_length=int(input("Enter the side length of the top layer="))
growth=int(input("Enter the growth of each layer="))
trunk_width=int(input("Enter the trunk width(odd number 3 to 9)="))
trunk_height=int(input("Enter the height(4 to 10)="))

current_layer=1
current_side=1

while current_layer<=layers:
    i=1
    if side_length<=2: #第一種

        while i<=side_length: #第一種第一層
            a ="#"*(current_side)
            print(a)
            current_side+=2
            i+=1

        k=side_length-1 #有幾個@
        u=0 #這一層跑幾行@
        h=0 #第幾層的係數

        while current_layer<=layers: #後面層數
            c="#"+"@"*(k)+"#"
            print(c)

            k+=2
            u+=1
            h+=1

            if u==growth:
                u=0
            current_layer+=1

            
        d="#"*(k+2) #第?層的底
        print(d)
            


    else:
        print("#")
        n=side_length
        while i<side_length:
            b="#"+"@"*(current_side)+"#"
            print(b)
            current_side+=growth
            i+=1

        k=side_length-1 #有幾個@
        u=0 #這一層跑幾行@
        h=0
        while current_layer<=layers: #第?層
            c="#"+"@"*(k)+"#"
            print(c)
            k+=2
            u+=1
            h+=1
            if u==growth*2*h:
                u=0
                d="#"*(k+2) #第?層的底
                print(d)
                k=side_length-1
                
            current_layer+=1




















height = int(input("Input the height of the 1st ball:"))
mass1 = int(input("Input the mass of the 1st ball:"))
mass2 = int(input("Input the mass of the 2nd ball:"))

g = 9.8
U1 = mass1*g*height
v_m1_af = (2*U1/mass1)**(1/2)
v_m2_af = v_m1_af*(mass1/mass2)**(1/2)

print(v_m1_af)
print(v_m2_af)
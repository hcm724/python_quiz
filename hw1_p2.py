#設定input的參數並由字串變為數字
force = int(input("Input the force:"))
mass_of_m1 = int(input("Input the mass of m1:"))
distance = int(input("Input the distance:"))

#公式運算
G = 6.67*(10**(-11))
mass_of_m2 = force*(distance**2) /G /mass_of_m1

C = 299792458
energy_of_m2 = mass_of_m2*(C**2)

print(mass_of_m2)
print(energy_of_m2)
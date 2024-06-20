velocity = float(input("Input the velocity:"))
C = 299792458
percentage = velocity/C 

p = (1-(velocity**2)/C**2)**(1/2)
r = 1/p 

td1 = 4.3
td2 = 6.0
td3 = 309
td4 = 2000000

tp1 = td1*p
tp2 = td2*p 
tp3 = td3*p 
tp4 = td4*p

print("Travel time to Alpha Centauri = ", tp1)
print("Travel time to Barnard's Star = ", tp2)
print("Travel time to Betelgeuse (in the Milky Way) = ", tp3)
print("Travel time to Andromeda Galaxy (closest galaxy) = ", tp4)

import random
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = random.randint(0,25)
answer = l[n]

i = ""
ad = 0
eh = 0
il = 0
mp = 0
qt = 0
ux = 0
yz = 0
t = 0

while True :

	#猜測字數+1
	t += 1
	alphabet = input("Guess the lowercase alphabet: ")

	#若答案正確 break
	if alphabet == answer:
		break
	#若不正確 則印出大於還是小於
	elif alphabet < answer :
		print("The alphabet you are looking for is alphabetically higher.")
	elif alphabet > answer :
		print("The alphabet you are looking for is alphabetically lower.")

	#計算字母出現區間次數
	if alphabet == 'a' or alphabet == 'b' or alphabet == 'c'or alphabet == 'd':
		ad += 1
	elif alphabet == 'e' or alphabet == 'f' or alphabet == 'g' or alphabet == 'h':
		eh += 1
	elif alphabet == 'i' or alphabet == 'j' or alphabet == 'k' or alphabet == 'l':
		il +=1
	elif alphabet == 'm' or alphabet == 'n' or alphabet == 'o' or alphabet == 'p':
		mp += 1
	elif alphabet == 'q' or alphabet == 'r' or alphabet == 's' or alphabet == 't':
		qt += 1
	elif alphabet == 'u' or alphabet == 'v' or alphabet == 'w' or alphabet == 'x':
		ux += 1
	elif alphabet == 'y' or alphabet == 'z':
		yz += 1

print("Congratulations! You guessed the alphabet\"", answer, "\" in ",t ,"tries.")
#draw histogram
print("Guess Histogram:")
print("a - d: ",ad*"*")
print("e - h: ",eh*"*")
print("i - l: ",il*"*")
print("m - p: ",mp*"*")
print("q - t: ",qt*"*")
print("u - x: ",ux*"*")
print("y - z: ",yz*"*")
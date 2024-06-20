#1
x = 5
y = 3
if x >= y:
	x = x - 2
print(x)

#2
tc = 100
tf = (9/5) * tc + 32
print(tf) 

#3
x = 0
while x < 5:
	x = x + 1
print(x) 

#4階
x = 1
i = 1
while x <= 5:
	x = x * i
	i = i+1
	print(x) 

#5奇數偶數
x = 0
while x < 6:
	if x % 2 == 0:
		print('even', x)
	else:
		print('odd', x)
	x = x + 1 

#6???
i = 0
while i < 6:
	j = 0
	while j < i:
		print("*")
		j = j + 1
	i = i + 1
	print()

#7
score = 40
while score > 1:
	score = score/2 - 1
print(score) 

#8
x = 2
y = 7
while x < y:
	x = 2 * x
print(x) 

#9???
a, b = 63, 105
while b:
	a, b = b, a % b
print(a) 

#10
n = 21
while n != 1:
	print(n, end=", ")
	if n % 2 == 0:
		n = n // 2
	else:
		n = n * 3 + 1
print(n, end=".\n") 


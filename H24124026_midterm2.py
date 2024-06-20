import random

#設定變數
r = int(input("Enter the number of the rows (N): "))
c = int(input("Enter the number of the columns (M): "))
o = int(input("Enter the number of the obstacles (0-%d) : " % (r*(c-2)) ))

#若o過大無法有可以從左上到右下的路徑 重新輸入
if o > r*(c-2):
	o = int(input("Re-enter again(0-",r*(c-2) ,"): "))

#建立matrix
matrix = [[" | " for s in range(r)] for k in range(c)]


#跑o個障礙物
for k in range(o):
	h = random.randint(0, r-1)		#for row
	w = random.randint(0, c-1)		#for col
	if h == 0 and w == 0:
		o += 1
		continue

	#將空格鍵改為X
	matrix[h][w]+"X"	

#將矩陣何在一起
for i in range(c):	
    a=" ".join(matrix[i])

#print matrix
for i in range(r):
	print("+---"*c)
	print(a)
print("+---"*c)



	#若左上角到右下角路徑通順，則繼續執行
	#for i in range(c):
	#	if c % 2 == 0:
	#		if matrix[i][i] == "|   ":
	#			#將空格鍵改為X
	#			matrix[h][w][2] == "X"

	#	elif c % 2 != 0:
	#		if matrix[i][i] == "|   " or matrix[c/2][c/2 + 1] == "|   ":
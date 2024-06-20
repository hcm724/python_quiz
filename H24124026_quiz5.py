#符合輸入的size of grid
enter = int(input("Enter the size of the grid: "))

#印出範圍
grid = []
for i in range(5):
	a="_ "*enter
	print(a)
	grid.append(a)


#得到輸入所要取代掉的位置和取代的項目
while cell !=done:

	cell = input("Enter the cell coordinates to edit: ")
	new = input("Enter the new value for the cell: ")

	#b為把cell變為數字要進行迴圈的list
	cell.split(',')
	b=int(cell)


	#在b[0] b[1]皆無大於grid時可進行迴圈
	while b[0] < enter and b[1] < enter:

	#印出前b[0]行 不包括b[0]
		for j in range(b[0]):
			print(a)
		
	#將b[1]前的_照樣列出來
		d = "_ "*b[1]
		print(d)

	#印出要取代的項目
		print(new," ")

	#印出剩下的_補齊大小
		e = "_ "*(enter-b[1]-1)
		print(e)
		print()

	#將不會更改到的行數印回去
		for k in range(b[0]+1,enter+1):
			print(a)
		





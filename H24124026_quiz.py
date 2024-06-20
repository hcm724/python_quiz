#amount 為金額總數

amount = int(input("Enter the shopping amount : "))
memberdship = input("Enter the membership level (Regular of Gold) :")

#若會員資格符合則進入下個迴圈
if memberdship == "Regular":
	#若金額大於三千 a為0.8*amount
	if amount >= 3000:
		a = 0.8*amount
	#若金額大於兩千 a為0.85*amount
	if 2000 >= amount > 3000:
		a = 0.85*amount
	#若金額大於1千 a為0.9*amount
	if 1000 >= amount > 2000:
		a = 0.9*amount
	print(memberdship,"$",a)

#同上
if memberdship == "Gold":
	if amount > 3000:
		a = 0.75*amount
	if 2000 >= amount > 3000:
		a = 0.8*amount
	if 1000 >= amount > 2000:
		a = 0.85*amount
	print(memberdship,"$",a)
else:
	print("Invalid member level")

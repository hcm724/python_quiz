#ij由9開始減少
i,j =9,9

#迴圈進行到最後一個數字等於1
while i>=1:
	#j 為前面的數字(9->1)
	while j>=1:
		a=0
		while a<=2:
			#列出所需
			print(j,"x",i-a,"=",(i-a)*j,end="\t")
			a+=1
		#打完換行
		print()
		j-=1
	#9行皆打完空一行換下一個
	print()
	i-=3
	j=9
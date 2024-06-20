#設定INPUT
Intergers=input("Enter a sequence of intergers separated by whitespace: ")

#設定變數
l=[]	#lics
j=0		#a中的第j項
b=1		#計算length
i=0		#設定範圍不超過a list
c=0		#將list a變為數字

#將input的值變為list
a=Intergers.split(" ")

#將input的值變為數字
while c < len(a):
	a[c]=int(a[c])
	c+=1


#試試看找出list a中符合需求的項
while i<len(a):

	#若a中的後一項大於前一項，則符合需求
	if a[j+1]>a[j]:
		b+=1			# Length + 1
		h=a[j]			#要加入 list l 的
		l.append(h)		#將 h 加入list l 中
	j+=1
	i+=1

#print出題目的需求
print("Length: ",b)
print("LICS: ",l)

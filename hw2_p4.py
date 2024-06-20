def tree(l,t,g,w,h):
	base=((l-1)*g+t)*2-1
	space=(base-1)//2
	print(" "*space,"#")
	i=2
	while i<t:
		if t<=2:
			print(" "*(space-(i-1))+"#"*(i*2-1))
		else:
			print(" "*(space-(i-1))+"#"+"@"*(i*2-1)+"#")
		i+=1
	print(' '*(space-(i-1)) + '#'*(2*i-1)) #第一層結束

	layer = 2
	while layer <= l:
		a = 2
		while a < t + (g*(layer-1)):
			print(' '*(space-(a-1)) + '#' + '@'*((a-1)*2-1) +'#')
			a += 1
		print(' '*(space-(a-1)) + '#'*(2*a-1))	
		layer += 1
	height = 1
	while height <= h:
		print(' '*(space-((w-1)//2)) + '|'*w)
		height += 1
	return ''

layer = int(input('Enter the number of layers (2 to 5) : '))
top_length = int(input('Enter the side length of the top layer :'))
growth = int(input('Enter the growth of each layer : '))
width = int(input('Enter the trunk width (odd number, 3 to 9) : '))
height = int(input('Enter the trunk height (4 to 10) : '))
print(tree(layer, top_length, growth, width, height))





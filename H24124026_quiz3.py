print("Welcome to the simple calculator program")

done=False
while not done:

	num1=float(input("Enter the first number:"))
	num2=float(input("Enter the second number:"))
	operator=input("Select an arithmetic operation(+,-,*,/):")

	if operator=="+":
		result=float(num1+num2)
		print ("result:%d" % result)

	elif operator=="-":
		result=float(num1-num2)
		print ("result:%3.1f" % result)

	elif operator=="*":
		result=float(num1*num2)
		print ("result:%3.1f" % result)

	elif operator=="/":
		if num2!=0.0:
			result=float(num1/num2)
			print ("result:%3.1f" % result)
			
		else:
			print("Division by zero!")
			break

	again=input("Do you want to perorm another calculation?(yes or no):")
	done = (again != "yes")

print("Good bye!")
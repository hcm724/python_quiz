n = int(input('Input the total number of students (n>0) :'))
students = list(range(1, n+1))  #所有學生
c_students = students[:]        #當前學生
r_students = []                 #移除學生

#判斷第一圈誰要移除
i = 1
while i < len(students):
    if i%3 == 0:
        r_students += [students[i]]
    i += 1

#移除在第一圈該移除的
i2 = 0
while i2 < len(r_students):
    c_students.remove(r_students[i2])
    i2 += 1




while len(c_students) > 1:  #剩下一個學生後停止
     students = students + c_students   #把剩下的學生加到原本學生後面
     while i < len(students):
        if i%3 == 0:
            r_students = r_students + [students[i]]
        i += 1
     while i2 < len(r_students):
        c_students.remove(r_students[i2])
        i2 += 1

print('The last ID is :', c_students[0])
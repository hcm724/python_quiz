year = int(input("Please input year:"))
month = int(input("Please input month:"))
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")

# 檢查是否為閏年，若是二月天數加1
if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month = 29
    else:
        days_in_month = 28
else:
    days_in_month = 30

# 計算當月第一天是星期幾
# 使用Zeller's Congruence公式
original_month = month
if original_month < 3:
    original_month += 12
    year -= 1

k = year % 100
j = year // 100

first_day=((1 + ((13 * (original_month + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j) % 7)-1


# 計算當月的第一天前有幾個空格
day_count = 1
while day_count < first_day+1:
    print("    ",end="    ")
    day_count += 1

day = 1
while day <= days_in_month:
    print(f"{day:02d}      ", end="") #數字之間距離
    first_day = (first_day + 1) % 7
    if first_day == 0:
        print()
    day += 1

# 如果最後一天不是星期六，則換行
if first_day != 0:
    print()

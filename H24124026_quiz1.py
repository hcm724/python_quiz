#輸入芮氏規模以及印出所回覆的芮氏規模
richter_scale = input("Please input a Richter scale value:")
print("Ridhter scale value:", richter_scale)
scale = float(richter_scale)

#將題目有的資訊輸入變成變數
energy = 10**((1.5*scale)+4.8)
tnt = 4.184*(10**9)
nutritious_constant = 2930200

#將能量分別轉換為tnt或營養午餐
tons_of_tnt = energy/tnt
nutritious = energy/nutritious_constant

#印出能量、炸彈、營養午餐分別為單位時的個數
print("Equivalence in Joules:", energy)
print("Equivalence in tons of TNT:", tons_of_tnt)
print("Equivalence in the number of nutritious lunches:", nutritious)
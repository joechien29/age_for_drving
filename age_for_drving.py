# 判斷是否達開車年齡

driving = input("請問你有沒有開過車?(請輸入有/沒有) ")
if driving != "有" and driving != "沒有":
    print("只能輸入有/沒有")
    raise SystemExit

age = input("請輸入你的年齡: ")
age = int(age)
if driving == "有":
    if age >= 18:
    	print("你通過測驗")
    else:
    	print("你應未取得駕照，不能開車哦")
elif driving == "沒有":
 	if age >= 18:
 		print("你已達考照年齡，可以去考駕照囉")
 	else:
 		print("很好，再過幾年就可以考駕照囉")

while True:
    number = input("請輸入一個整數: ")
    if number.isdigit():
        number = int(number)
        break
    else: 
        print("輸入錯誤")
n = []
for i in range(2, number):
    if number % i == 0:
        n.append(i)   
    else:
        continue

if len(n) == 0:
    print(f"{number} 為質數")
else:
    print(f"{number} 可被 {n} 整除")
print("一番上の*の数を入力 : ", end="")
num = int(input())

print()
if num % 2 == 0:
    print("入力値が偶数なので1足します")
    num += 1

print("一番上の*の数", num)

target = int((num + 1) / 2)
print(target, "段の図形を表示します")

arry = ["*" for i in range(num)]

print(" ".join(arry))

for i in range(target - 1):
    arry[i], arry[num - 1 - i] = " ", " "
    print(" ".join(arry))

import math
#入力受け取る
P = int(input())
# 硬貨の枚数をカウントする
count = 0
# 硬貨の金額が大きい順に支払いたいのでrangeを逆順に回す
for i in reversed(range(1,11)):
# for i in range(10,1,-1):とも書ける
# N!円硬貨の金額はfactorial関数を使って出す
    N = math.factorial(i)
# PからPに近い数字順に引いていく
# 0になるまで引いていく
    while P >= N:
        P -= N
        # 引くごとにcount +1をしていく
        count += 1
print(count)


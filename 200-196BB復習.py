# 200Bーーーーーーーーーー
N,K = map(int,input().split())
# 以下の操作をK回行う
for i in range(K):
    if N%200 == 0:
        N = N//200
    else:
# 後の操作の関係で、文字列として扱う
        N = str(N) +'200'
# for文の処理は数字としての操作から始まるのでintになおす
        N =int(N)
print(N)



# 199Bーーーーーーーーーー
# Nの入力を受け取る
N = int(input())
# A,Bはリストとして受け取る
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# xの初期値は0とする
x = 0
# N回処理を繰り返す
for i in range(1,1001):
    ok=True
    for j in range(N):
        if i < A[j] or i > B[j]:
            ok = False
    if ok :
        x+=1
print(x)



# 198Bーーーーーーーーーー
N = input()

# 回文にできるならYes
# 先頭に0をつけて、逆順にしても同じなら回文
for i in range(10):
    T = '0'*i + N
    if T == T[::-1]:
        print('Yes')
        exit()
print('No')

# 197Bーーーーーーーーーー
#入力受け取る
H,W,X,Y = map(int,input().split())

X -= 1
Y -= 1

ls =[]

ans=1

for _ in range(H):
    S = input()
    ls.append(S)

# Xを上方向に探索する
for i in reversed(range(X)):
    if ls[i][Y] == '#':
        break
    else :
        ans += 1

# Xを下方向に探索する
for i in range(X+1,H):
    if ls[i][Y] =='#':
        break
    else:
        ans += 1

# Yを左方向に探索する
for j in reversed(range(Y)):
    if ls[X][j]=='#':
        break
    else:
        ans += 1

# Yを右方向に探索する
for j in range(Y+1,W):
    if ls[X][j] == '#':
        break
    else:
        ans += 1

print(ans)



# 196Bーーーーーーーーーー
# 文字列で入力を受け取る
X = input()

# 文字列の中に','があれば、その手前まで出力
if '.' in X:
# findメソッドでインデックスを取得
    index = X.find('.')
# Xをインデックスの手前までにする。スライスで指定する。
    X = X[:index]

print(X)
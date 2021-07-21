N = int(input())
S = input()
# 先に1を引いた方が負け
# つまりリストから最初の1の位置を探す
# Sのinputは文字列だから、’1’を探す
wrong = S.index('1')
# 1のインデックスが0か偶数なら高橋くん負け、奇数なら青木くん負け
if wrong == 0:
    print('Takahashi')
elif wrong%2 == 0:
    print('Takahashi')
else:
    print('Aoki')

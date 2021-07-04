A,B = map(int,input().split())


if B <= 600:
    # 2回ふって１になることはない
    if A*1 > B:
        print('No')
    # 最大6が出るサイコロをA回振る。でた目の合計がBになりうるのはBがA＊6以下の時 
    elif A*6 >= B:
        print('Yes')
    # BがA＊6以上ならNo
    elif A*6 < B:
        print('No')
#Aが100回以下だから、Bが600より大きかったらNo
else:
    print('No')
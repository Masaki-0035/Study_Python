# すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 各マスには 0 か 1 が書かれており、マス i には siが書かれています。
# すぬけ君は 1 が書かれたマスにビー玉を置きます。 ビー玉が置かれるマスがいくつあるか求めてください。
# 入力を受け付けます。
num = int(input())

num_str = str(num)

A = [int(n) for n in num_str]
print(A.count(1))

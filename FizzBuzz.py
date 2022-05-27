for num in range(1, 101):
    string = ''

    # ここから記述
    # 対象の数値が3で割り切ることができる場合
    if num % 3 == 0:
        string += "Fizz"
    # 対象の数値が5で割り切ることができる場合
    if num % 5 == 0:
        string += "Buzz"
    # string変数に文字が追加されていない場合
    if string == "":
        print(num)
        # 以下の命令を実行せず、for文の先頭に戻る
        continue
    # ここまで記述

    print(string)
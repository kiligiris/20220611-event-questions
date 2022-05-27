def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 探索範囲の上限index
    high = len(sorted_array) - 1
    # 探索範囲の下限index
    low = 0

    while low <= high:
        # 探索範囲の中間index
        middle = (low + high) // 2
        # 探索範囲の中間の値
        item = sorted_array[middle]
        # 探索対象が見つかった場合、中間indexを返却
        if item == target_number:
            return middle
        # 中間の値より探索対象が大きかった場合、下限値を更新
        elif item < target_number:
            low = middle + 1
        # 中間の値より探索対象が小さかった場合、上限値を更新
        else:
            high = middle - 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
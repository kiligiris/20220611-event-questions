def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # 探索範囲の下限index
    low = 0
    # 探索範囲の上限index
    high = len(array) - 1
    
    # 先頭と末端がぶつかっていない場合処理を続ける
    while low < high:
        # 先頭から基準値以上の値を検索
        while array[low] < pivot and low < high:
            low += 1
        # 末端から基準値未満の値を検索
        while array[high] >= pivot and low < high:
            high -= 1
        # 上記二つの検索で入れ替えるべき値が見つかっていた場合
        if array[low] >= pivot and array[high] < pivot:
            # 二つの値を入れ替える
            temporary = array[low]
            array[low] = array[high]
            array[high] = temporary
            # 処理済みなのでindexを更新
            low += 1
            high -= 1
    # 要素が二つの場合はソートがこの時点で完了しているので返却する
    if len(array) == 2:
        return array
    # 基準値以上と基準値未満の境界線を見つける
    border = 0
    while array[border] < pivot:
        border += 1
    # 境界線が0だった場合は基準値未満のグループ存在しないため、基準値以上のグループだけを再帰処理にかけ、返却する
    if border == 0:
        return sort(array[border : len(array)])
    # 基準値未満のグループと基準値以上のグループで各自再帰処理にかけ、結合したのち返却する。
    return sort(array[0 : border]) + sort(array[border : len(array)])
    # ここまで記述

if __name__ == '__main__':
    main()
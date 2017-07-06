"""
Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6. Каждая из следующих n строк
задаёт стоимость 0≤ci≤2⋅10^6 и объём 0<wi≤2⋅1060<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём
при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000
"""


def continuous_backpack(size, stocks):
    sorted_stocks = sorted(
        [(stock[0] / stock[1], stock[0], stock[1]) for stock in stocks],
        key=lambda x: x[0],
        reverse=True
    )
    value = 0
    for stock in sorted_stocks:
        if size > 0:
            if stock[2] > size:
                ratio = size / stock[2]
                value += stock[1] * ratio
                size = 0
            else:
                size -= stock[2]
                value += stock[1]
    return round(value, 3)


def main():
    total, size = [int(i) for i in input().split()]
    stocks = []
    for i in range(total):
        stocks.append(tuple(map(int, input().split())))
    print(continuous_backpack(size, stocks))


if __name__ == '__main__':
    main()

"""
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9,
задающих начало и конец отрезка. Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек
несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6
"""


def segments_cover(segments):
    segments.sort(key=lambda x: x[1])
    pointer = segments[0][1]
    points = [pointer]
    for segment in segments[1:]:
        if segment[0] > pointer:
            pointer = segment[1]
            points.append(pointer)
    return points


def main():
    total = int(input())
    segments = []
    for i in range(total):
        segments.append([int(i) for i in input().split()])
    points = segments_cover(segments)
    print(len(points))
    print(*points)


if __name__ == '__main__':
    main()

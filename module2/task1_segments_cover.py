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

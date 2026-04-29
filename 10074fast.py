def largest_rectangle_histogram(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()
    return max_area


def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        arr = [list(map(int, input().split())) for _ in range(n)]

        heights = [0] * m
        ans = 0

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, largest_rectangle_histogram(heights))

        print(ans)


if __name__ == "__main__":
    main()

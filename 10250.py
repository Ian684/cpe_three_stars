def main():
    while True:
        try:
            x1 , y1 , x2 , y2 = map(float , input().split())
        except EOFError:break
        midx , midy = (x1+x2)/2 , (y1+y2)/2
        rx , ry = (x2 - x1)/2 , (y2 - y1)/2
        ax1 , ay1 = midx + ry , midy - rx
        ax2 , ay2 = midx - ry , midy + rx
        print(f"{ax1:.10f} {ay1:.10f} {ax2:.10f} {ay2:.10f}")

if __name__ == "__main__":
    main()

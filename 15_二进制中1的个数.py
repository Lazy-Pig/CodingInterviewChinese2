def count_one(x):
    count = 0
    while x:
        print("{0:b}".format(x))
        count += 1
        x = x & (x - 1)
    return count


if __name__ == "__main__":
    print(count_one(x=10))

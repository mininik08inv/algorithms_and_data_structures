def find_max_number(arr: list):
    if len(arr) == 1:
        return arr[0]
    else:
        max_num = find_max_number(arr[1:])
        return max_num if max_num > arr[0] else arr[0]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(find_max_number(arr))

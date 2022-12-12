arr, cnt = [], 0
while True:
    try:
        l = input()
        if l == '':
            arr.append(cnt)
            cnt = 0
        else:
            cnt += int(l)
    except EOFError:
        break

y = sum(sorted(arr)[-3:])
print(y)

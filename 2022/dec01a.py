most,cnt = 0, 0
while True:
    try:
        l = input()
        if l == '':
            most = max(cnt, most)
            cnt = 0
        else:
            cnt += int(l)
    except EOFError:
        break
print(most)

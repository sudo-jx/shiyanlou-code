a = 0
while a < 100:
    a += 1
    if a % 7 == 0 or '7' in str(a):
        continue
    else:
        print("a:", a)

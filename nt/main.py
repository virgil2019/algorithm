import sys

start = int(sys.argv[1])
result = [start]

while True:
    current = result[-1]
    found = False
    if current % 2 == 0:
        current /= 2
    else:
        current = 3 * current + 1

    for num in result:
        if num == current:
            print("over")
            found = True
            break

    if found:
        break
    else:
        result.append(current)

print("Result", result, len(result))
curRow = 1
curColumn = 1

size = int(input("지도 크기를 입력하세요:"))
commands = list(map(str, input("명령을 입력하세요").split()))

for item in commands:
    if (item == 'U'):
        if (curRow > 1):
            curRow -= 1
    if (item == 'D'):
        if (curRow < size):
            curRow += 1
    if (item == 'R'):
        if (curColumn < size):
            curColumn += 1
    if (item == 'L'):
        if (curColumn > 1):
            curColumn -= 1

print(curRow,curColumn)
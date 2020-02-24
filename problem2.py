l_n = eval(input())
l_n = list(map(str, l_n))
for i in range(0, len(l_n)):
    for j in range(0, len(l_n)-1):
        if len(l_n[j]) == len(l_n[j + 1]):
            l_n[j], l_n[j+1] = str(max(int(l_n[j]), int(l_n[j+1]))), str(min(int(l_n[j]), int(l_n[j+1])))
        elif len(l_n[j]) > len(l_n[j + 1]):
            for k in range(0, len(l_n[j + 1])):
                if int(l_n[j][k]) <= int(l_n[j + 1][k]):
                    l_n[j], l_n[j + 1] = l_n[j + 1], l_n[j]
                    break
        elif len(l_n[j]) < len(l_n[j + 1]):
            for k in range(0, len(l_n[j])):
                if int(l_n[j][k]) < int(l_n[j + 1][k]):
                    l_n[j], l_n[j + 1] = l_n[j + 1], l_n[j]
                    break

result = ''.join(l_n)
print(result)
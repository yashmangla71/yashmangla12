num = int(input())
bin_n = bin(num)[2:]
one_l = [i for i in bin_n.split("0") if i != '']
one_l.sort(key=len)
print(len(one_l[-1]))
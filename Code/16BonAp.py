k = raw_input()
n = raw_input()
bcharged = int(input())

s = map(int, k.split())
m = list(map(int,n.split()))

rest = s[1]

total = sum(m)
both = total-m[rest]
part = both/2
solution = bcharged-part

if part != bcharged:
    print solution
else:
    print "Bon Appetit"

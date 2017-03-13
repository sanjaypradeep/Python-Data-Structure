

# https://www.hackerrank.com/challenges/mini-max-sum




a,b,c,d,e = list(map(int, input().split()))
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

lst = sorted([a, b, c, d, e])
print (lst)

print(sum(lst[:-1]), sum(lst[1:]))
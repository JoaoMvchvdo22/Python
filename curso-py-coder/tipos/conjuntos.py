# print({1, 2, 3})
print(type({1, 2, 3}))

conjunto = {1, 2, 3, 3, 3, 3, 3}
print(conjunto)

# operações
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
print(c1)

c2 <= c1
c1 >= c2
{1, 2, 3} - {2}
c1 - c2
c1 -= c2
print(c1)

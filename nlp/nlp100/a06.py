import a05

x = set(a05.n_gram('paraparaparadise', 2))
y = set(a05.n_gram('paragraph', 2))

print(x)
print(y)

print(x | y)

print(x & y)

print(x - y)

print('se' in x)
print('se' in y)
print('a')

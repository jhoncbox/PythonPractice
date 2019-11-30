from collections import OrderedDict
# a normal dictionary wont, when iterated, it doesn't maintain a certain order
# e.g.
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
print(d)
# some times the order of the printed items is mixed up cause dictionaries are more like maps
# it doesn't maintain the order
for k,v in d.items():
    print(k,v)
print("\n")
# to prevent this we use OrderedDict()
# e.g.
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print(k,v)

# better example, pay attention to the order added
d1 = {}
d1['a'] = 1
d1['b'] = 2
d2 = {}
d2['b'] = 2
d2['a'] = 1
print (d1==d2) # true

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print (d1==d2) # false




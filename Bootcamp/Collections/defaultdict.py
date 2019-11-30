from collections import defaultdict
# defaultdict work by definin a default value to any new key added to a dictionary
#  e.g.
# this defaultdict "d" with the function lamba will always place a zero as the default value for any new key
d = defaultdict(lambda: 0)
d["one"]
d["two"]
d["three"] = 3
print(type(d))
print(d)
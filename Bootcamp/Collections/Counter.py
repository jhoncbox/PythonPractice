from collections import Counter

# counter work like counting the times every item of a list os repeated
testlist = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6]

print(Counter(testlist))
# Counter({1: 4, 3: 4, 2: 3, 4: 3, 5: 3, 6: 3})

# lest count the words in a sentence

testString = "how many times does each word show up in this sentence word word show up up" 

wordCount = testString.split()
print(Counter(wordCount))

c = Counter(wordCount)
# Common patterns when using the Counter() object

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts


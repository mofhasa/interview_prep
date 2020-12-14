import math


def getNotIntersect(s1, s2):
    deletions = 0
    for x in s1:
        if x not in s2:
            curr_len = len(s1)
            s1 = s1.replace(x, '')
            deletions += curr_len - len(s1)

    return (deletions, s1)


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a1, a2 = getNotIntersect(a, b)
    b1, b2 = getNotIntersect(b, a)
    print(sorted(a2))
    print(sorted(b2))
    return a1 + b1 + abs(len(a2) - len(b2))


print(makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))


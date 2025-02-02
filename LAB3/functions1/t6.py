def lsst(lst):
    words=lst.split()
    rev_words = words[::-1]
    return ' '.join(rev_words)
lst=input()
print(lsst(lst))
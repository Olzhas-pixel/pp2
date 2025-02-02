def permute(s, l=0, r=None):
    if r is None:
        r = len(s) - 1

    if l == r:
        print("".join(s))
    else:
        s = list(s)
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

s = input()
permute(s)

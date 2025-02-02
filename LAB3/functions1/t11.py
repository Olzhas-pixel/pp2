def poli(str):
    b=len(str)
    for i in range(b):
        if str[i] != str[b-i-1]:
            return False
    return True
d=input()
print(poli(d))
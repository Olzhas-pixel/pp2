import math

def volume(r):
    V = (4 * math.pi * r**3)/3
    return V
raadius = int(input())
print(f"{volume(raadius):.4f}")
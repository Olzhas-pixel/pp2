def solve(numheads, numlegs):
    rabbits=(numlegs/2)-numheads
    chicken=numheads-rabbits
    print(f"Rabbits: {rabbits}, Chikens: {chicken}")
legs=94
heads=35
solve(heads, legs)
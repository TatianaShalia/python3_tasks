def closest_mod_5(x):
    for y in range(x, x**2):
        if y % 5 == 0:
            return y
print(closest_mod_5(6))

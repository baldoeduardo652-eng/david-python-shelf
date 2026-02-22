x = 300

print ("find the closest number to ", x)

a = float (input("enter your first number:"))
b = float (input("enter your second number:"))
c = float (input("enter your third number:"))

diff_a = abs(x - a)
diff_b = abs(x - b)
diff_c = abs(x - c)

closest = min(a, b, c, key=lambda num: abs(x - num))
print(f"The closest number to {x} is {closest}")

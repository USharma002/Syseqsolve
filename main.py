from data.matdet import *

eq = "x  = 2, y = 3, z = 12"
print(read_eq(eq)[0])
print(solve(eq))
#Calculate area of a triangle
# s = (a+b+c)/2, Area = [s*(s-a)*(s-b)*(s-c)]**(1/2)
a, b, c = 10, 11, 12
s = (a+b+c)/2
Area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("a, b, c = ", end = '')
print(a, b, c)
print("Area = ", end = '')
print(Area)

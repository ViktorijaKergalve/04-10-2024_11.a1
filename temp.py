try:
    a = int(input("Enter a: "))
    b =int(input ("Enter b: "))
    c=int(input ("Enter c: "))

except ValueError:
    print('a or b or c = int')
    
D = b**2-4*a*c
x1= (-b + D ** 1/2) / (2 * a)
x2= (-b - D ** 1/2) / (2 * a)
print(x1)
print(x2)
print("1. Rectangle")
print("2. Rectangular")
print("3. Circle")
print("4. Triangel")
shape = int(input("select shape (1/2/3/4) : "))
if shape == 1:
    selected_shape = "Rectangle"
    formula = "Area = a*a"
    a = int(input("Input a : "))
    area = a*a
elif shape == 2:
    selected_shape = "Rectangular"
    w = int(input("Input w : "))
    l = int(input("Input l : "))
    area = w*l
elif shape == 3:
    selected_shape = "Circle"
    r = int(input("Input r : "))
    area = 3.14*r*r
elif shape == 4:
    selected_shape = "Triangle"
    b = int(input("Input b : "))
    h = int(input("Input h : "))
    area = (h*b)/2
else :
    print("Undefined shape!")
print("Selecting ",selected_shape, "shape.")
print("Area = ", area)



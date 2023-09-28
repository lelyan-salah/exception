def finput():
    try:
        width = float(input("Please enter the width: "))
        length = float(input("Please enter the length: "))

        if width <= 0 or length <= 0:
            print("should be positive")
        else:
            return width, length
    except Exception as e:
        print("the width and length should be postive")


def Calculaterectanglearea():
    width, length = finput()
    area = length * width
    print("Rectangle area = ", area)


def Calculaterectangleperimeter():
    width, length = finput()
    perimeter = 2 * (length + width)
    print(" Rectangle perimeter = ", perimeter)


try:
    Calculaterectanglearea()
    Calculaterectangleperimeter()
except Exception as e:
    print("invalid input")

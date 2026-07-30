class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

def ShapeFactory(shape):
    if shape.lower() == "circle":
        return Circle()
    elif shape.lower() == "square":
        return Square()
    else:
        return None

c = ShapeFactory("circle")
s = ShapeFactory("square")

print("Circle Area:", c.area())
print("Square Area:", s.area())

# Small novelty
print("Factory created both shapes successfully!")
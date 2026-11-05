def count_occurrences(target, values):
    if (len(values) == 0):
        return 0
    if values[0] == target:
        return count_occurrences(target, values[1:]) + 1
    else:
        return count_occurrences(target, values[1:])

def is_sorted(values):
    if len(values) <= 1:
        return True
    if values[0] <= values[1]:
        return is_sorted(values[1:])
    else:
        return False

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area
        
    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        super().__init__()
        return f'{self.width}x{self.height}'

class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        super().__init__(side, side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    print(is_sorted([1, 2, 3]))                    # True
    print(Rectangle(3, 4).area())                  # 12
    print(Square(5))                               # 5x5
    print(is_sorted([1, 3, 2]))
    print(Rectangle(3, 4).perimeter())
    print(Rectangle(3, 4))

if __name__ == "__main__":
    main()

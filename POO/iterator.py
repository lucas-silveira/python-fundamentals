class RGB:
    def __init__(self):
        self.colors = ['red', 'green',  'blue'][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.colors.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    colors = RGB()
    print(next(colors))  # red
    print(next(colors))  # green
    print(next(colors))  # blue
    print(next(colors, 'End'))  # End

    for color in RGB():
        print(color)

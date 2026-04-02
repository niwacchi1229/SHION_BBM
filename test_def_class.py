class TEST:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_test(self):
        print(f"{self.name}と{self.color}")

test1 = TEST("ああ", "いい")
test2 = TEST("a", "b")

test1.print_test()
test2.print_test()

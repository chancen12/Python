class ex9():
    def __init__(self):
        self.ex = ""

    def get_String(self):
        self.ex = input()

    def print_String(self):
        print(self.ex.upper())

ex = ex9()
ex.get_String()
ex.print_String()
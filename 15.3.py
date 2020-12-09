class StringVar:
    def __init__(self):
        self.str = ""
    def set(self, par):
        self.str = par
    def get(self):
        return self.str


str = StringVar()
str.set("Some string")
print(str.get())
str.set("String is changed")
print(str.get())
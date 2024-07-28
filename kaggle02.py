class A:
    def __init__(self, char):
        self.char = char
    
    def char(self):
        if self.char.isalpha():
            print(self.char.lower())
        else:
            print("Invalid")

class B(A):
    def __init__(self, char):
        super().__init__(char)
    
    def char(self):
        if self.char.isalpha():
            print(ord(self.char))
        else:
            print("Invalid")
    
    def char1(self):
        if self.char.isalpha():
            print(self.char.upper())
        else:
            print("Invalid")

# Driver code
a = A('A')
a.char()  # Output: a

b = B('A')
b.char()  # Output: 65
b.char1() # Output: A

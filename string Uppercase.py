class IOString():
    
    def __init__(self):
        self.str = " "
    
    def get_String(self):
        self.str = input("Enter a string : ")
    
    def print_String(self):
        print(f"Result is : {self.str.upper()}")

string1= IOString()
string1.get_String()
string1.print_String()

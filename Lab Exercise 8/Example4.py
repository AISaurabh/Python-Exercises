#Example No. 4
class string:
    def __init__(self):
        self.string1=" "
    def get_string(self):
        self.string1=input("Enter the string value :")
    def print_string(self):
        print(self.string1.upper())

string1=string()
string1.get_string()
string1.print_string()

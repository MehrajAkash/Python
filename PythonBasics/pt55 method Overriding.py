
class phone:
    def __init__(self):
        print("In phone class")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("In Samsung class")        

obj = samsung()
        
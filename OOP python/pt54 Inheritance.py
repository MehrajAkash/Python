
class phone:
    def call(self):
        print('Call in phone')

    def message(self):
        print("You can Message")

class samsung(phone):
    def photo(self):
        print('Photo in samsung')    


print(issubclass(samsung,phone))
s = samsung()
s.photo()
s.call()
s.message()   


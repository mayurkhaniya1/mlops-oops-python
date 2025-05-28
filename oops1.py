# class 
class Employee:
    # special functions constructer

    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = 'se'

    def travel(self, city):
        # print("functions call")   
        # return 0    
        print(f"{city} going to travel")

# create an obj and instance

mayur = Employee()

print(mayur.salary, mayur.id)
# print(mayur.travel())

# call funtions 
mayur.travel("keshod")

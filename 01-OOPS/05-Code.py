class Emp():
    # constructor
    def __init__(self):
        self.e_id = None
        self.e_name = None
        self.e_age = None
        self.e_sal = None
        self.emp_list = []

    def show(self):
        self.emp_list.append([self.e_id, self.e_name, self.e_age, self.e_sal])
        print(self.emp_list)
    # Destructuor
    def __del__(self):
        print("Object {} deleted".format(self.e_name))

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 45000
obj_1.e_age = 40
obj_1.show()

del obj_1

obj_2 = Emp()
obj_2.e_id = 102
obj_2.e_name = 'Raman'
obj_2.e_sal = 41000
obj_2.e_age = 30
obj_2.show()
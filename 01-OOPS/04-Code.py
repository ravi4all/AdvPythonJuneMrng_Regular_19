class Emp():
    e_id = None
    e_name = None
    e_age = None
    e_sal = None
    emp_list = []

    def show(self):
        self.emp_list.append([self.e_id, self.e_name, self.e_age, self.e_sal])
        print(self.emp_list)

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 45000
obj_1.e_age = 40
obj_1.show()

obj_2 = Emp()
obj_2.e_id = 102
obj_2.e_name = 'Raman'
obj_2.e_sal = 41000
obj_2.e_age = 30
obj_2.show()
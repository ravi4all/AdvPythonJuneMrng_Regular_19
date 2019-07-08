class Emp():
    """This is a emp class"""
    e_id = None
    e_name = None
    e_age = None
    e_sal = None

    def show(self):
        print(self.e_id, self.e_name, self.e_age, self.e_sal)

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 45000
obj_1.e_age = 40
obj_1.show()
print(obj_1.__dict__)
print(obj_1.__dir__())
print(obj_1.__class__)
# Doc String
print(obj_1.__doc__)
class Emp():
    e_id = None
    e_name = None
    e_age = None
    e_sal = None

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 45000
obj_1.e_age = 40
print(obj_1.__dict__)
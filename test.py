class MyFirstClass:
    id = 10
    def __init__(self, name, id):
        self.name=name
        MyFirstClass.id = id
    def getName(self):
        return self.name
    
#    def __doc__():
#        print("plants")

def my_func(x,y):
    return x*y

#a=list(map(my_func, [4,6]))
# def lamda():
 #   my_list = [5,3,2,1]
  #  result = (list(map(lambda x , y : x*y , my_list, [5,2,8,0])))
   # print(result)

def square_matrix_simple(matrix=[[]]):
    print(matrix)
    result = [list(map(lambda x: x*x , row)) for row in matrix]
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

first = MyFirstClass('Abeni', 50)
print(first.getName())
print(first.id)
print(first.name)
print(MyFirstClass.id)

for i in range(2, 10, 2):
    print(i, end=" ")
print("--------")
for i in range(10, 0, -1):
    print(i, end=" ")

class User:
    id = 1

u = User()
u.id = 89
print("", end="\n")
print(User.id)
print(u.id)
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

print(id(l1))
l1 = l1 + [5]
print(id(l1))
print(l1)

# Inheritance

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id = 89       

u = User()
print(u.id)
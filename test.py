class MyFirstClass:
    id = 10
    def __init__(self, name, id):
        self.name=name
        MyFirstClass.id = id
    def getName(self):
        return self.name

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
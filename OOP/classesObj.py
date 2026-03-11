class Person:
    #Contrucao de um objeto , seus atributos 
    def __init__(self,name,age,email):

        self.name = name
        self.age = age
        self.email = email


p1 = Person("Gomes", 27, "qqqq@gmail.com")

print(p1.name)
print(p1.age)
print(p1.email)
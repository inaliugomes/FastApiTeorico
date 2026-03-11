class Person:

    def __init__(self,name,age):
        self.name=name
        #Con __ estamos informando que el atributo es privado
        self.__age=age

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        if new_age>self.__age and new_age >0:
            self.__age=new_age



p1 = Person("James",25)


print(p1.name)

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname,self.lname)

#Cuando nao adicionamos nenhum init , a funcao irá usar init do seu "Pai" ou classe maior
class Student(Person):
 def __init__(self,fname,lname,year):
     super().__init__(fname,lname)
     self.graduationyear  = year
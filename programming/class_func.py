
'''class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score 
    def grade_get(self):
        if self.score >= 90:
            return 'A'  
        elif self.score >= 60:    # 记住score前面要加self，self指向创建实例的本身
            return 'B'
        else :
            return 'C'

lisa = Student("Lisa",90)
print (lisa.name,lisa.grade_get())
bobe = Student("Bobe",50)
print (bobe.name,bobe.grade_get())
'''
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score 
    def grade_get(self):
        if self.__score >= 90:
            return 'A'  
        elif self.__score >= 60:    # 记住score前面要加self，self指向创建实例的本身
            return 'B'
        else :
            return 'C'
    '''def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score'''
johnson = Student("Johnson",100)
#print (johnson.get_name())
#print (johnson.grade_get())
print (johnson._Student__name())

# dir()函数可以获得一个对象所有属性和方法
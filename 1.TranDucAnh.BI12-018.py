Stu =[]
Cou =[]
n = int (input("Enter number of students in the class "))
while n < 0 :
        n = int (input("Enter number of students in the class "))
def Stu_in4(): 
    for i in range(n):
        a = (input ("Student id " + str(i+1)+ ": "))  
        Stu.append(a)      
        b = (input ("Student Name "+ str(i+1)+ ": "))
        Stu.append(b)
        c = (input ("Student DoB  "+ str(i+1)+ ": "))
        Stu.append(c)

def Course_in4():
    k = int(input ("Enter number of courses "))
    for i in range (k):
        d = (input("Course Name "+str(i+1)))
        Cou.append(d)
        e = (input("Course id "+str(i+1)))
        Cou.append(e)

def list_stu():
     for i in range(0,len(Stu),3):
        print('Name     ' + Stu[i] + ' ID   ' + Stu[i+1] + 'DoB   ' + Stu[i+2])

def list_course():
    for i in range(0,len(Cou),2):
        print()
    


Stu_in4()
Course_in4()
list_stu()
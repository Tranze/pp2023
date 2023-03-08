Stu =[]
Cou =[]
n = int (input("Enter number of students in the class "))
while n < 0 :
        n = int (input("Enter number of students in the class "))
def Stu_in4(): 
    for i in range(n):
        a = (input ("Student "+ str(i+1) + "id: "))  
        Stu.append(a)      
        b = (input ("Student"+ str(i+1)  + "Name : "))
        Stu.append(b)
        c = (input ("Student "+ str(i+1)+ " DoB  : "))
        Stu.append(c)

def Course_in4():
    k = int(input ("Enter number of courses "))
    for i in range (k):
        d = (input("Course " +str(i+1) + ' Name: ' )) 
        Cou.append(d)
        e = (input("Course " +str(i+1) +" id: "))
        Cou.append(e)

def list_stu():
     for i in range(0,len(Stu),3):
        print('Student Name ' + Stu[i] + '    ID ' + Stu[i+1] + '      DoB' + Stu[i+2])

def list_course():
    for i in range(0,len(Cou),2):
        print('Courses Name ' + Cou[i] + '    ID ' + Cou[i+1])
    
def mark():
    

Stu_in4()
Course_in4()
list_stu()
list_course()
# code made by Miłosz Łyczywek

# student or teacher

def choose():
    global stu_or_teacher
    stu_or_teacher=str(input("Are you a student or a teacher: "))

# main school class

class school():

    number_of_stu=0

    def __init__(self, first, last, ):
        self.first=first
        self.last=last
        self.email=(first+"."+last+"@myschool.com").lower()
        
        school.number_of_stu+=1
    
    def add_student():
        global student
        student=school(input("Choose first name: "),input("Choose last name: "))
        print(student.first, student.last)
        print("Your school e-mail is: ",student.email)
        
    def add_teacher():
        global add_teacher
        add_teacher=school(input("Choose first name: "),input("Choose last name: "))
        print(add_teacher.first, add_teacher.last)
        print("Your school e-mail is: ",add_teacher.email)

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

# teacher and student classes

class teacher(school):
    def __init__(self,first,last, proffesion):
        super().__init__(first,last)
        self.proffesion=proffesion

class it_student(school):
    number_of_it_stu=0
    def __init__(self, first, last, prog_lan):
        super().__init__(first,last)
        self.prog_lan=prog_lan
        it_student.number_of_it_stu+=1

class arts_student(school):
    number_of_arts_stu=0
    def __init__(self, first, last, art_style):
        super().__init__(first,last)
        self.art_style=art_style
        arts_student.number_of_arts_stu+=1

class sports_student(school):
    number_of_sports_stu=0
    def __init__(self, first, last, fav_sport):
        super().__init__(first,last)
        self.fav_sport=fav_sport
        sports_student.number_of_sports_stu+=1

# classmates interests function

def know_class():
    if stu_or_teacher=='student':
        know=str(input("Do you want to know more about your class mates? Type yes or no: "))
        if know=='yes':
            if subj=='it':
                print("Choose a student - ",school.fullname(stu_it_1),",",school.fullname(stu_it_2),",",school.fullname(stu_it_3))
                choice=input("Type the name: ")
                if choice==school.fullname(stu_it_1) or choice==school.fullname(stu_it_1).lower():
                    print(school.fullname(stu_it_1),"'s favourite programming language is: ",stu_it_1.prog_lan)
                elif choice==school.fullname(stu_it_2) or choice==school.fullname(stu_it_2).lower(): #------------------------------------------
                    print(school.fullname(stu_it_2),"'s favourite programming language is: ",stu_it_2.prog_lan)
                elif choice==school.fullname(stu_it_3) or choice==school.fullname(stu_it_3).lower():
                    print(school.fullname(stu_it_3),"'s favourite programming language is: ",stu_it_3.prog_lan)
            elif subj=='arts':
                print("Choose a student - ",school.fullname(stu_arts_1),",",school.fullname(stu_arts_2),",",school.fullname(stu_arts_3))
                choice=input("Type the name: ")
                if choice==school.fullname(stu_arts_1) or choice==school.fullname(stu_arts_1).lower():
                    print(school.fullname(stu_arts_1),"'s favourite art style is: ",stu_arts_1.art_style)
                elif choice==school.fullname(stu_arts_2) or choice==school.fullname(stu_arts_2).lower(): #------------------------------------------
                    print(school.fullname(stu_arts_2),"'s favourite art style is: ",stu_arts_2.art_style)
                elif choice==school.fullname(stu_arts_3) or choice==school.fullname(stu_arts_3).lower():
                    print(school.fullname(stu_arts_3),"'s favourite art style is: ",stu_arts_3.art_style)
            elif subj=='sports':
                print("Choose a student - ",school.fullname(stu_sports_1),",",school.fullname(stu_sports_2),",",school.fullname(stu_sports_3))
                choice=input("Type the name: ")
                if choice==school.fullname(stu_sports_1) or choice==school.fullname(stu_sports_1).lower():
                    print(school.fullname(stu_sports_1),"'s favourite sport is: ",stu_sports_1.fav_sport)
                elif choice==school.fullname(stu_sports_2) or choice==school.fullname(stu_sports_2).lower(): #------------------------------------------
                    print(school.fullname(stu_sports_2),"'s favourite sport is: ",stu_sports_2.fav_sport)
                elif choice==school.fullname(stu_sports_3) or choice==school.fullname(stu_sports_3).lower():
                    print(school.fullname(stu_sports_3),"'s favourite sport is: ",stu_sports_3.fav_sport)
        else:
            quit()
    else:
        quit()
# sample students

stu_it_1=it_student("Steve","Jobs","C")
stu_it_2=it_student("Bill","Gates","Javascript")
stu_it_3=it_student("Mark","Zuckerberg","Python")

stu_arts_1=arts_student("Kurt","Cobain","Music")
stu_arts_2=arts_student("Salvador","Dali","Painting")
stu_arts_3=arts_student("Vincent","van Gogh","Painting")

stu_sports_1=sports_student("Micheal","Jordan","Basketball")
stu_sports_2=sports_student("Cristiano","Ronaldo","Football")
stu_sports_3=sports_student("Mariusz","Pudzianowski","Weightlifting")


# adding yourself to the system

choose()

# teacher choice
if stu_or_teacher=='teacher':
    school.add_teacher()
    print()
    prof=(input("Choose your proffesion from (it, arts, sports): "))
    if prof=='it':
        print("You are now the it class teacher")
        teacher(add_teacher.first, add_teacher.last,prof)
        print("Your number of students is: ",it_student.number_of_it_stu)
        print("Thank you for joining our school, see you at the lessons!")
    elif prof=='arts':
        print("You are now the arts class teacher")
        teacher(add_teacher.first, add_teacher.last,prof)
        print("Your number of students is: ",arts_student.number_of_arts_stu)
        print("Thank you for joining our school, see you at the lessons!")
    elif prof=='sports':
        print("You are now the sports class teacher")
        teacher(add_teacher.first, add_teacher.last,prof)
        print("Your number of students is: ",sports_student.number_of_sports_stu)
        print("Thank you for joining our school, see you at the lessons!")
        
    else:
        print("You typed in wrong proffesion...")
        quit()
# student choice
elif stu_or_teacher=='student':
    school.add_student()
    print()
    subj=(input("Choose your favourite subject from (it, arts, sports): "))
    if subj=='it':
        print("You joined IT class.")
        it_student(student.first,student.last,input("Choose your favourite programming language: "))
        print()
        print("Your classmates are: ",school.fullname(stu_it_1),",",school.fullname(stu_it_2),",",school.fullname(stu_it_3))
        print("Thank you for joining our school, see you at the lessons!")
        print()
    elif subj=='arts':
        print("You joined arts class.")
        arts_student(student.first,student.last,input("Choose your favourite art style: "))
        print()
        print("Your classmates are: ",school.fullname(stu_arts_1),",",school.fullname(stu_arts_2),",",school.fullname(stu_arts_3))
        print("Thank you for joining our school, see you at the lessons!")
        print()
    elif subj=='sports':
        print("You joined sports class.")
        sports_student(student.first,student.last,input("Choose your favourite sport: "))
        print()
        print("Your classmates are: ",school.fullname(stu_sports_1),",",school.fullname(stu_sports_2),",",school.fullname(stu_sports_3))
        print("Thank you for joining our school, see you at the lessons!")
        print()
    else:
        print("You typed in wrong subject...")
        quit()
else:
    print("You typed in something wrong...")
    quit()

know_class()


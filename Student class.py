class Student:
    def __init__(self, name, major, andrew_id, gpa):
        self.name = name
        self.major = major
        self.andrew_id = andrew_id
        self.gpa = gpa
    def update_info(self, major, gpa):
        self.major = major
        self.gpa = gpa
    def __repr__(self):
        return self.name + " " + self.major + " " +   self.andrew_id + " " + str(self.gpa)
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major 
    def get_andrew_id(self):
        return self.andrew_id
    def get_gpa(self):
        return self.gpa

f1 = open("students_names.txt", "r+")

Students_list = []
Student_names = []
Student_andrew_id = []
Student_gpa = []
Student_major = []

for line in f1:
    line_splitted = line.split("-")
    temp_students = Student( line_splitted [0], line_splitted[1], line_splitted[2], float(line_splitted[3].rstrip('\n')))
    Students_list.append(temp_students)


for a in Students_list:
    Student_names.append(a.get_name())
    Student_andrew_id.append(a.get_andrew_id())
    Student_gpa.append(a.get_gpa())
    Student_major.append(a.get_major())
    


command = input("What do you want? ")
while command != "exit":
    if command == "show":
        print(Students_list)
    elif command == "show student names":
        print(Student_names)
    elif command == "check student gpa":
        n = 0
        a1 = input("Which students GPA do you want to check ")
        while True:
            if Student_names[int(n)] == str(a1):
                break
            else:
                n += 1
        GPA = float(Student_gpa[int(n)])
        if GPA == 0.0:
            print("F")
        elif GPA > 0.0 and GPA <= 1.0:
            print("D")
        elif GPA>1.0 and GPA<=2.0:
            print("C")
        elif GPA >2.0 and GPA <= 3.0:
            print("B")
        elif GPA >3.0 and GPA <=4.0:
            print("A")
        
    elif command == "edit":
        n = 0
        a1 = input("Which students info do you want to change ")
        a2 = input("What would be his/her major? ")
        a3 = input("What would be his/her gpa?" )
        a4 = input("What would be his/her andrew_id ")
        while True:
            if Student_names[int(n)] == str(a1):
                break
            else:
                n += 1
        Students_list[int(n)].update_info(str(a2), float(a3))
        
    elif command == "represent":
        a1 = input("Which student info do you want to see? ")
        n = 0
        while True:
            if Student_names[int(n)] == str(a1):
                break
            else:
                n += 1
        print(Students_list[int(n)].__repr__())
    command = input("OK. What else?" )
print("Thank you for using this application")       

f1.close()
with open('students_names.txt', "w") as updatedFile:
    updatedFile.write(str(Students_list))

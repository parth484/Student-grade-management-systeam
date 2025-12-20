import os
import datetime
import openpyxl
from openpyxl import Workbook
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

STUDENT_FILE = "students3.txt"
GRADE_FILE = "grades3.txt"
#database

#student loading and student saving
def load_students():
    students=[]
    if not os.path.exists(STUDENT_FILE):
        open(STUDENT_FILE, "w").close()
        return students
    
    with open(STUDENT_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 8:
                student = {
                    "student_id": data[0],
                    "first_name": data[1],
                    "last_name": data[2],
                    "email": data[3],
                    "dob": data[4],
                    "program": data[5],
                    "enrollment_year": data[6],
                    "status": data[7]
                }
                students.append(student)
    return students

def saveStudents(students):
    with open(STUDENT_FILE, "w") as f:
        for s in students:
            line = "|".join([
                s["student_id"], s["first_name"], s["last_name"],
                s["email"], s["dob"], s["program"],
                str(s["enrollment_year"]), s["status"]
            ])
            f.write(line + "\n")

# grade loading and grade saving

def load_grades():
    grades = []
    if not os.path.exists(GRADE_FILE):
        open(GRADE_FILE, "w").close()
        return grades
    with open(GRADE_FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 7:
                grade = {
                    "student_id": data[0],
                    "subject": data[1],
                    "assessment_type": data[2],
                    "marks_obtained": float(data[3]),
                    "maximum_marks": float(data[4]),
                    "date": data[5],
                    "semester": data[6]
                }
                grades.append(grade)
    return grades

def save_grades(grades):
    with open(GRADE_FILE, "w") as f:
        for g in grades:
            line = "|".join([
                g["student_id"], g["subject"], g["assessment_type"],
                str(g["marks_obtained"]), str(g["maximum_marks"]),
                g["date"], g["semester"]
            ])
            f.write(line + "\n")


  


#-----------validations-----------------------------------------------------------------
def validate_student_id(new_stu_id):
    return  new_stu_id.startswith("STU") and  new_stu_id[3:].isdigit() and len(new_stu_id) == 6

def validate_gmail(new_stu_email):
    return "@" in new_stu_email

def validate_dob(date_string):        
    try:
            datetime.datetime.strptime(date_string, "%d/%m/%Y")
            return True
    except:
            return False
    
def validate_marks(marks,max_marks):
    try:
        marks = float(marks)
        max_marks = float(max_marks)
        return 0 <= marks <= max_marks
    except:
        return False
       

def validate_semester(semester):
    validsem=["1st","2nd","3rd","4th","5th","6th","7th","8th"]
    if semester in validsem:
        return True
    else:
        return False

def exam_type(assessment_type):
    exam=["quiz","class assesment","case study","report","project","presentation"]
    if assessment_type in exam:
        return True
    else:
        return False

#This code is for main screen
def main_screen():
    students = load_students()
    grades = load_grades()
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*80)
    print(f"{Fore.BLUE}Student grade management{Style.RESET_ALL}".center(80))
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*80)
    print("  1.Student Management")
    print("  2.Grade Management")
    print("  3.Export data in excel file")
    print("  4.Exit")
    var=int(input("Enter your choice : "))
    if var==1:

        student_management(students,grades)

    elif var==2:

        grade_management(students,grades)

    elif var==3:
        excel(grades)    

#This code is for adding students/management of it
def student_management(students,grades):
   while True: 
    print("="*80)
    print("Student management".center(80))
    print("="*80)
    print("  1.Add a new student")
    print("  2.Search student")
    print("  3.Update student")
    print("  4.Delete student")
    print("  5.View all students")
    print("  6.Back to main menu")

    inp_1=int(input("Enter your choice : "))
    if inp_1==1:
      
      addStudents(students)

    elif inp_1==2:

        search_student(students)

    elif inp_1==3:

        update_student(students)

    elif inp_1==4:

       delete_student(students)

    elif inp_1==5:

        print("view all student")
        view_allStu(students)

    elif inp_1==6:
        main_screen() 
    else:
        print(f"{Fore.RED}YOU typed something wrong!!{Style.RESET_ALL}")       

  

def grade_management(students,grades):
  while True:  
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*80)
    print(f"{Fore.BLUE}Grade management{Style.RESET_ALL}".center(80))
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*80)
    print("  1.Add a grade entry")
    print("  2.View student grades")
    print("  3.Update grade")
    print("  4.Calculate GPA")
    print("  5.Back to main menu")

    inp_2=int(input("Enter your choice : "))
    if inp_2==1:
        add_grades(grades,students)
       

    elif inp_2==2:
        print("Student Grades")
        view_grades(grades)
    elif inp_2==3:
        print("update student")
        update_grade(grades)
    
    elif inp_2==4:
        print("view all student")
        calculate_gpa(grades)
    elif inp_2==5:
        main_screen() 
    else:
        print("YOU typed something wrong!!")      


def addStudents(students):
     
        print(f"{Fore.YELLOW}-----------ADD NEW STUDENT----------{Style.RESET_ALL}")
        new_stu_id=input("Enter ur student id : ")
        if not validate_student_id(new_stu_id):
            print("INVALID FORMAT!!")
            return
        for i in students:
            if i["student_id"]==new_stu_id:
                print("User already exists!")
                return
        new_stu_first_name=input("Enter your first name : ")
        new_stu_last_name=input("enter your last name : ")
        new_stu_email=input("enter your email : ")
        if not validate_gmail(new_stu_email):
            print("Your email is invalid")
            return
        for i in students:###+++++
            if i["email"]==new_stu_email:
                print("email is already taken/Try another one")
        new_stu_dob=input("enter your date of birth : ")
        if not validate_dob(new_stu_dob):
            print("invalid format try( dd/mm/yyyy ) format")
            return
        new_stu_course=input("Enter ur course name : ")
        new_stu_enrollyr=int(input("enter your enrollment year : "))
        
        student = {
         #it defines as key and its value   
            "student_id": new_stu_id,
            "first_name": new_stu_first_name,
            "last_name": new_stu_last_name,
            "email": new_stu_email,
            "dob": new_stu_dob,
            "program": new_stu_course,
            "enrollment_year": new_stu_enrollyr,
            "status": "Active"
        }
        students.append(student)
        saveStudents(students) 

# def searchStudents(students):

#       new_stu_id=input("Enter ur student id : ")
#       for i in new_stu_id:
def search_student(students):
    new_stu_id = input("Enter Student ID: ")
    for s in students:
        if s["student_id"] == new_stu_id:
            print("\n--- Student Details ---")
            for k, v in s.items(): print(f"{k}: {v}")
            return s
    print("Not found!")
    return None
          
def update_student(students):
    s=search_student(students)
    if not s: return
    print("U can update only 1.Email, 2.programm, 3.status")
    choose=int(input("choose option"))
    if choose==1:
        newem=input("enter a new email")
        if validate_gmail(newem):
            s["email"]=newem
            
    elif choose==2:
        s["program"]=input("enter changed programm")
        print(f"{Fore.BLUE}Programm updated succesfully!!{Style.RESET_ALL}")
    elif choose==3:
        s["status"]=input("status : ACTIVE/INAVTIVE/GRADUATE")
    saveStudents(students) 
    print("updated")

def delete_student(students):
        s=search_student(students)
        if not s:return
        confirm=input("Did you want to really detete it(Y/N)")
        if confirm.lower() == "y":
            students.remove(s)
            saveStudents(students)
            print("deleted!!")
        else:
            s["status"] = "Inactive"
            saveStudents(students)
            print("Soft deleted!")

def view_allStu(students):
    print("-"*150)
    print("  Student ID | First name        | Last nmae       |  Email                        | Date of birth   |  Stream(Branch)     | Enroll year | Status ")
    print("-"*150)
    for i in students:
      print(f"  {i["student_id"]:<5}     | {i[ "first_name"]:<15}   | {i["last_name"]:<11}     | {i["email"]:<29} | {i["dob"]:<15} |  {i["program"]:<18} |  {i["enrollment_year"]:<10} |  {i["status"]:3}  ")  
    vap=input("press enter to continue...")   

def add_grades(grades,students):
    new_stu_id=input("enter a student id: ")
    if not any(s["student_id"] == new_stu_id for s in students):
        print(f"{Fore.RED}Student not found!{Style.RESET_ALL}")
        return
        
    subject=input("Enter subject : ")
    assesment_type=input("Assesment type : ")
    if not exam_type(assesment_type):
        print(f"{Fore.RED}invalid format!!!{Style.RESET_ALL}")
        return 
    marks=input("Enter obtained marks : ")
    max_marks=input("Maximum marks of exam : ")
    if not  validate_marks(marks,max_marks):
        print(f"{Fore.RED}someting went wrong!!!{Style.RESET_ALL}")
        return
    date=input("Date (DD/MM/YYYY) : ")
    if not validate_dob(date):
        print(f"{Fore.RED}Invalid format!!{Style.RESET_ALL}")
        return
    semester=input("enter semester : ")
    if not validate_semester(semester):
        print(f"{Fore.RED}Enter valid semester{Style.RESET_ALL}")
        return
    grade = {
        "student_id": new_stu_id,
        "subject": subject,
        "assessment_type": assesment_type,
        "marks_obtained": float(marks),
        "maximum_marks": float(max_marks),
        "date": date,
        "semester": semester
    }
    grades.append(grade)
    save_grades(grades)
    print(f"{Fore.GREEN}Grade added!{Style.RESET_ALL}")
    ivb=input(f"{Fore.YELLOW}press enter to continue{Style.RESET_ALL}")


def view_grades(grades):
    sid = input("Enter Student ID: ")
    found = [g for g in grades if g["student_id"] == sid]
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*138)
    print(f" {Fore.BLUE}Student Id   |   Subject            |    Assesment Type    |   Marks obtained   |   Maximum marks  |      Percentage       |    Semester{Style.RESET_ALL}")
    print(f"{Fore.BLUE}={Style.RESET_ALL}"*138)
    if not found:
        print("No grades found!")
        return
    for g in found:
          print(f" {g["student_id"]:<11}  | {g["subject"]:<20} | {g["assessment_type"]:<20} | {g["marks_obtained"]:<18} | {g["maximum_marks"]:<16} | {(g["marks_obtained"]/g["maximum_marks"])*100:<20}% |  {g["semester"]}")
    kk=input(f"{Fore.YELLOW}press enter to continue...{Style.RESET_ALL}")      

def update_grade(grades):
    sid=input("enter a id : ")
    for i in grades:
        if i["student_id"]==sid:
           var=input("did you want to really change the grades Y/N : ")
           if var.lower()=='y':
               new_marks=input("enter a updated marks :")
               new_maxx=input("enter maximum marks")
               if validate_marks(new_marks,new_maxx):
                   i["marks_obtained"]=new_marks
                   save_grades(grades)

def get_grade_point(p):
    p = float(p)
    if p >= 90: return 4.0
    if p >= 85: return 3.7
    if p >= 80: return 3.3
    if p >= 75: return 3.0
    if p >= 70: return 2.7
    if p >= 65: return 2.3
    if p >= 60: return 2.0
    return 0.0


def calculate_gpa(grades):
    sid=input("enter student id: ")
    if not validate_student_id(sid):
        print(f"{Fore.RED}enter valid student id!!{Style.RESET_ALL}")
        return
    semester=input("enter a semester: ")
    if not validate_semester(search_student):
        print(f"{Fore.RED}enter valid semester!! such as 1st,2nd,..,8th{Style.RESET_ALL}")
    sg = [g for g in grades if g["student_id"] == sid and g["semester"] == semester]
            
    points=[]
    for g in sg:
        percent = (g["marks_obtained"] / g["maximum_marks"]) * 100
        points.append(get_grade_point(percent))
    gpa = sum(points) / len(points)
    print(f"GPA = {gpa:.2f}")

            
#Excel
def excel(grades):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Student Marks"

    # Headings
    sheet.append(["Student Id", "Subject", "Assesment Type","Marks Obtained","Maximum Marks","Semester"])
    for i in grades:
        sheet.append([
             i["student_id"], 
             i["subject"], 
             i["assessment_type"],
             i["marks_obtained"],
             i["maximum_marks"],
             i["semester"]])
        
    # Save file
    wb.save("marks.xlsx")

    print(f"{Fore.GREEN}Excel file created successfully{Style.RESET_ALL}")


   

if __name__ == "__main__":
    main_screen()

                

    
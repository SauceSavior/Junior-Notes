#from FileName import Class
from Student import Student
from Courses import Course
import random  #built in module, no need for the from syntax

#create a course
cs = Course("Comp Sci 1")
lunch = Course("Diners Drive-in Dives")
history = Course("American History post 1776")
gym = Course("Retirement Sports")

#create a student


masterStudentList = []
masterCourseList = [cs,lunch,history,gym]

file1=open("studentDatabase.txt","r")
file=file1.readlines()

def loadStudent(firstName,lastName):
    newStudent=Student(firstName,lastName)
    masterStudentList.append(newStudent)
        
    for student in masterStudentList:
        listOfCourses=masterCourseList.copy()
        for i in range(4):
            coursesToAdd=listOfCourses.pop(random.randrange(0,len(listOfCourses)))
            student.addCourse(coursesToAdd)
 
     #print out each student and their courses
    for student in masterStudentList:
        print(student)
loadStudent()

for line in file:
    first,last=line.rstrip().split(",")
    loadStudent(first,last)
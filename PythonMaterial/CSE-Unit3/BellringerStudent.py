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

def loadStudent():
     
     while newStudent=="y":
          #create new student object
          firstName=input("first: ")
          lastName=input("last: ")
          newStudent=student(firstName,lastName)
          #add student to masterStudentList
          masterStudentList.append(newStudent)
          
          newStudent=input("another student?")
          
          input()
     
     #print out each student and their courses
     for student in masterStudentList:
          print(student)



#randomly add courses to students
for student in masterStudentList:
     listOfCourses=masterCourseList.copy()
     #loop 4 times because we have 4 class to add
     for i in range(4):       #never use the i
          courseToAdd = listOfCourses.pop(random.randrange(0,len(listOfCourses)))
          student.addCourse(courseToAdd)
          #watch out to not duplicate a course in the schedule
          
          loadStudent()
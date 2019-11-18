class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while(tmp.next != None):
                tmp = tmp.next

            tmp.next = node

    def find(self, data):
        tmp = self.head
        while(tmp != None):
            if(tmp.isEqual(data)):
                return tmp

            tmp = tmp.next

        return None

class BST:
    def __init__(self):
        self.root = None

    def append(self, node):
        if self.root == None:
            self.root = node
        else:
            self._addNode(node, self.root)

    def _addNode(self, node, currroot):
        if node.deadline < currroot.deadline:
            if currroot.left == None:
                currroot.left = node
            else:
                self._addNode(node, currroot.left)
        elif node.deadline > currroot.deadline:
            if currroot.right == None:
                currroot.right = node
            else:
                self._addNode(node, currroot.right)
        else:
            print("the value has ben skipped")
            pass

    def find(self, title, curroot):
        if title == curroot.title:
            return curroot
        else:
            if curroot.right != None:
               self.find(title, curroot.right)
            elif curroot.left != None:
                self.find(title, curroot.left)
            else:
                pass

    def _find(self, title):
        self.find(title, self.root)


class Assignment:
    def __init__(self, title, deadline, percent):
        self.title = title
        self.deadline = deadline
        self.percent = percent
        self.grade = 0
        self.right = None
        self.left = None

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.percent) + ": " + str(self.grade)

    def addGrade(self, grade):
        self.grade = grade

    def getActualGrade(self):
        return self.grade

    def getCalculatedGrade(self):
        return self.grade * self.percent/100

    def isEqual(self, title):
        return self.title == title

class Course:
    def __init__(self, ID):
        self.ID = ID
        self.assignments = BST()
        self.next = None

    def __str__(self):
        return self.ID

    def isEqual(self, ID):
        return self.ID == ID

    def addAssignment(self, title, deadline, percent):
        assignment = Assignment(title, deadline, percent)
        self.assignments.append(assignment)

    def getAssignment(self, title):
        return self.assignments._find(title)

    def addGrade(self, title, grade):
        assignment = self.getAssignment(title)
        if (assignment != None):
            assignment.addGrade(grade)
        else:
            print("The Assignment", title, "doesn't exist for the student")

    def getGrade(self):
        grade = 0
        tmpAssignment = self.assignments.root
        while tmpAssignment != None:
            grade = grade + tmpAssignment.getCalculatedGrade()

            tmpAssignment = tmpAssignment.next


        return grade

class Student:
    def __init__(self, fName, lName, ID):
        self.fName = fName
        self.lName = lName
        self.ID = ID
        self.courses = LinkedList()

    def __str__(self):
        return self.getFullName() + ": " + self.ID

    def getCourse(self, ID):
        return self.courses.find(ID)

    def getFullName(self):
        return self.fName + " " + self.lName

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.append(course)

    def addAssignment(self, cID, title, deadline, percent):
        course = self.getCourse(cID)
        if (course != None):
            course.addAssignment(title, deadline, percent)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self, cID, title, grade):
        course = self.getCourse(cID)
        if (course != None):
            course.addGrade(title, grade)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getCourseGrade(self, cID):
        course = self.getCourse(cID)
        return course.getGrade()

    def getAssignmentGrade(self, cname, title):
        pass

    def getAssignmentCalculatedGrade(self, cname, title):
        pass

    def getFullGrade(self):
        grade = 0
        tmpcourse = self.courses.head
        x = 0
        while tmpcourse != None:
            grade = grade + tmpcourse.getGrade()
            tmpcourse = tmpcourse.next
            x = x+1

        return grade/x





def main():
    my_student = Student("Arthur", "Sargsyan", "AUA234")
    # print(my_student)

    #Adding Ccourses
    my_student.addCourse("ENGS115")
    my_student.addCourse("ENGS113")
    my_student.addCourse("ENGS105")

    # print(my_student.getCourse("ENGS115"))
    # print(my_student.getCourse("ENGS103"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Stack", 5, 30)
    # print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Queue", 6, 40)
    # print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    #adding Grades
    my_student.addGrade("ENGS115", "Implement Browser History using Stack", 90)
    my_student.addGrade("ENGS115", "Implement Browser History using Queue", 50)
    # print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))
    # print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    # print(my_student.getCourseGrade("ENGS115"))
    # my_student.getAssignmentGrade("ENGS115", "Implement Browser History using Stack")
    # my_student.getAssignmentCalculatedGrade("ENGS115", "Implement Browser History using Stack")

    # print(my_student.getFullGrade())

main()
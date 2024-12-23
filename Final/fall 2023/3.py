#a 


#+------------------+        +------------------+
#|   Instructor     |        |     Course       |
#+------------------+        +------------------+
#| instructor_id    |<----+  | course_id        |
#| name             |     |  | name            |
#| department       |     +--| credits         |
#| email            |        | instructor_id   |
#+------------------+        +------------------+




#b 
#Instructor Model:

class Instructor:
    def __init__(self, instructor_id, name, department, email):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department
        self.email = email

    def get_courses(self):
        pass
#Course Model:

class Course:
    def __init__(self, course_id, course_name, credits, description, instructor_id):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.description = description
        self.instructor_id = instructor_id

    def get_instructor(self):
        pass
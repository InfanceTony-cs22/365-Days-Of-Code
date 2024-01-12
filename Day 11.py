class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    # Creating instances of the Student class
    stud1 = Student("Robin", "CSE")
    stud2 = Student("Rahul", "ECE")

    # Calling the printfunction for each instance
    stud1.printfunction()
    stud2.printfunction()

    return 0

if __name__ == '__main__':
    main()

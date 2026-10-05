school = "Shivaji"  # Global variable
def classroom():
    subject = "Maths"  # Enclosing variable
    def student():
        name = "Srujith"  # Local variable
        print(name)     # Local
        print(subject)  # Enclosing
        print(school)   # Global
        def marks():
            score = 95  # Local to marks()
            print(score)
            print(subject)  # Enclosing
            print(school)   # Global

        marks()
    student()
classroom()

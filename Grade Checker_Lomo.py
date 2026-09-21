# TITLE: GRADE CHECKER
# AUTHOR: Lomo, Jabez Victor A.
# GRADE & SECTION: 8-Camia

grade = int(input("Enter your grade: "))

if 0 <= grade <= 100:
    print("Valid Grade.")
else:
    print("Invalid Grade. Grade must be between 0 and 100.")
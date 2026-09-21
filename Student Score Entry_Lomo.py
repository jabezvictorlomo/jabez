# TITLE: STUDENT SCORE ENTRY
# AUTHOR: Jabez Victor A. Lomo
# GRADE & SECTION: 8-Camia

exam_score = input("Enter examination score: ")

try:
    score = float(exam_score)
    if 0 <= score <= 100:
        print("Valid score.")
    else:
        print("Invalid input. Score must be between 0 and 100.")

except ValueError:
    print("Invalid input")









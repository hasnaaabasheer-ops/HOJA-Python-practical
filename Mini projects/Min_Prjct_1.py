print("STUDENTS GRADE CALCULATOR")

def get_mark():
    english = int(input("Enter marks for English: "))
    maths = int(input("Enter marks for Maths: "))
    science = int(input("Enter marks for Science: "))
    social = int(input("Enter marks for Social: "))
    computer = int(input("Enter marks for Computer: "))
    return english, maths, science, social, computer

def get_total(english, maths, science, social, computer):
    total = english + maths + science + social + computer
    return total

def get_average(total):
    average = total / 5
    return average 

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def display_result(total,average,grade):
    print('total marks : ',total)
    print('average : ',average)
    print('grade : ',grade)
    if average >=50:
        result ="PASS"
    else:
        result ="FAIL"
    print('Result:',result)

english,maths,science,social,computer = get_mark()

Total =get_total(english,maths,science,social,computer)
Average =get_average(Total)
Grade =get_grade(Average)

display_result(Total,Average,Grade)
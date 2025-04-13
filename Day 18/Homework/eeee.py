
#algorithm არის ნაბიჯ ნაბიჯ ინსტრუქციების შესრულება აი მაგალითად ბლინების ინსტრუქციები როგორ უნდა გავაკეთოდ



score = int(input("pls put in ur test score"))

if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 40:
    grade = "C"
elif score >= 20:
    grade = "D"
if score < 20:
    grade = "F"

    print("your grade is " + grade)

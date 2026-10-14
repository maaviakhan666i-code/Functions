


# function parameters, & function arguments

def calculate_percentage(obtained, total):
    percentage = (obtained / total) * 100
    print("Percentage:", percentage, "%")


calculate_percentage(777, 1000)

          
# make function for bmi calulation
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("BMI:", bmi, "- Underweight")
    elif (bmi >= 18.5) and (bmi < 24.9):
        print("BMI:", bmi, "- Normal weight")
    elif (bmi >= 24.5) and (bmi < 29.9):
        print("BMI:", bmi, "- Overweight")
    else:(bmi >= 30 and bmi < 34.9)
       print(overweight)
    calculate_bmi(94, 1.74)  # Example usage       
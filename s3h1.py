# Nazanin Ebrahimi - Thursday 14-18
# BMI calculator
# weight in kg and height in m

def BMI_calculator(weight, height, patient_ID):
    BMI = weight / (height ** 2)
    if BMI >= 30:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI}\t Result: Obese')
    elif BMI >= 25 and BMI < 30:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI}\t Result: Overweight')
    elif BMI <= 18.5:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI}\t Result: Underweight')
    else:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI}\t Result: Normal')


BMI_calculator(100, 1.55, 1)

BMI_calculator(72, 1.62, 2)

BMI_calculator(50, 1.60, 3)

BMI_calculator(44, 1.58, 4)

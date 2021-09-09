# Nazanin Ebrahimi - Thursday 14-18
# BMI calculation and evaluation using return

def BMI_calculator(weight, height):
    BMI = weight / (height ** 2)
    return BMI


def BMI_evaluation(weight, height, patient_ID):
    BMI_result = BMI_calculator(weight, height)
    if BMI_result >= 30:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI_result}\t Weight Status:\
         Obese')
    elif BMI_result >= 25 and BMI_result < 30:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI_result}\t Weight Status:\
         Overweight')
    elif BMI_result <= 18.5:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI_result}\t Weight Status:\
         Underweight')
    else:
        print(f'patient_ID= {patient_ID} \t BMI = {BMI_result}\t Weight Status:\
         Normal')


BMI_evaluation(100, 1.55, 1)

BMI_evaluation(72, 1.62, 2)

BMI_evaluation(50, 1.60, 3)

BMI_evaluation(44, 1.58, 4)

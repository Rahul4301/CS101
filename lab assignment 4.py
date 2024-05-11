#1
print('#1')

#creates vairable and stores input of a credit score
credit_score = int(input("Enter your credit score: "))

#creates variable and stores input of a loan amount
loan_amount = int(input("Enter your loan amount: "))

#creates if condition where the range of the loan amt is 25000-50000 and credit score > 640
if 25000< loan_amount < 50000 and credit_score > 640:
    print("Loan approved")

#creates elif condition where the range of the loan amt is 50000-100000 and credit score > 680
elif 50000<loan_amount > 100000 and credit_score > 680:
    print("Loan approved")

#creates elif condition where the range of the loan amt is 100000-500000 and credit score > 720
elif 100000<loan_amount > 500000 and credit_score >= 720:
    print("Loan approved")

#creates elif condition where the range of the loan amt is above 500000 and credit score > 760
elif 500000<loan_amount  and credit_score >= 760:
    print("Loan approved")

#creates else condition where none of the above conditions apply 
else:
    print('\n')
    print("Loan is rejected")

#2
print('\n')
print('#2')

#creates variables that stores inputs for the test scores
test1 = float(input('enter test score 1: '))
test2 = float(input('enter test score 2: '))
test3 = float(input('enter test score 3: '))
testAverage = ((test1+test2+test3)/3)


#creates if condition where the renge of the test average is 60-70
if 60 <= testAverage <70:
    print('\n')
    print(f'Your test average is {testAverage}')
    print('Your Grade: C')

#creates elif condition where the renge of the test average is 70-80
elif 70<= testAverage <80:
    print('\n')
    print(f'Your test average is {testAverage}')
    print('Your Grade: B')

#creates elif condition where the renge of the test average is 80-90
elif 80<= testAverage <90:
    print('\n')
    print(f'Your test average is {testAverage}')
    print('Your Grade: B+')

#creates elif condition where the renge of the test average is 90-95
elif 90<= testAverage <=95:
    print('\n')
    print(f'Your test average is {testAverage}')
    print('Yor grade: A')

#creates elif condition where the renge of the test average is above 95
elif 95 < testAverage:
    print('\n')
    print(f'Your test average is {testAverage}')
    print("Your Grade: A+")

#creates else condition where none of the above conditions apply
else:
    print('\n')
    print(f'Your test average is {testAverage}')
    print('Your Grade: F')

"""
# PROGRAM TO FIND THE LARGEST OF 3 NUMBERS
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third numberS: "))
 
if num1>num2 and num1>num3:
    print("num1 is the greatest")
    
if num2>num1 and num2>num3:
    print("num2 is the greatest")
if num3>num1 and num3>num2:
    print("num3 is the greatest")
    
    
# PROGRAM TO DECIDE BONUS TO GIVE TO EMPLOYEES
period=int(input("Enter your time period of service: "))
salary=int(input("Enter your salary: "))

if period>10:
    bonus=0.1*salary
    print("net_bonus: ",bonus+salary)
    
elif period>=6 and period<=10:
    bonus=0.08*salary  
    print("net_bonus: ",bonus+salary)
    
else:
    bonus=0.05*salary 
    print("net_bonus: ",bonus+salary)   """
    
    #PROGRAM TO ASSIGNING A GRADING SYSTEM
sub1=int(input("Enter marks for subject1: "))
sub2=int(input("Enter marks for subject2: "))
sub3=int(input("Enter marks for subject3: "))
sum=sub1+sub2+sub3
avg=sum/3
if (avg>=70 and avg<=100):
    print("Grade A")
elif (avg>=60 and avg<=69):
    print("Grade B")
elif (avg>=50 and avg<=59):
    print("Grade C")
elif  (avg>=40 and avg<=49):
    print("Grade D")
elif(avg>=0 and avg<=39):
    print("Grade E")    
else:
    print("invalid")        
        


    
           
    
 
   
            
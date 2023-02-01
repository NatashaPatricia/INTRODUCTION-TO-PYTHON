
#operators in python
a=20
b=6
print(a/b)
print(a//b)



#program to test divisibility by 5
n=int(input("Enter a number :"))

if (n%5==0):
   print("the number is divisible by 5")
else:
   print("the number is not divisible by 5")   
  



# program to check whether a number is even
n=int(input("Enter a number :"))

if (n%2==0):
   print("the number is even")
else:
   print("the number is not even ")  
   
   
   
   
   # program to assign discount of 5% if amount of purchase exceeds sh1000
amount=int(input("Enter amount spent"))
if(amount>1000):
    discount=float(amount*0.05)
    pay=(amount-discount)
    print("Discount= ",discount)
    print( "pay= ",pay)
else:
    print("No discount")
    
    
    #program to check if a person is eligible to vote
age=int(input("Enter your age :"))
nationality=str(input("Enter your national :")).lower()
if(age>= 18 and nationality=="kenyan"):
        print("Eligible to vote")
        
else:
        print(" Not Eligible to vote")
        
        
        #program to offer loan
age=int(input("Enter your age :"))
salary=int(input("Enter your salary :"))
if (salary>=21000 and age>=21):
    print("Congratulations, you are qualified for a loan")
else:
    print("Unfortunately, we are unable to offer you a loan at this time.")  
    
    #loan 2 crb
age=int(input("Enter your age :"))
salary=int(input("Enter your salary :"))
crb=(input("Enter your crb state:"))
if (salary>=21000 and age>=21 and crb<0):
    print("Congratulations, you are qualified for a loan")
else:
    print("Unfortunately, we are unable to offer you a loan at this time.") 
    
    
    # program to vote in eastafrica
b1=["kenya", "uganda","tanzania"]
b=input("Please Enter your country: ").lower()
age=int(input("Enter your age: "))
if age>=18 and b in b1:
    print("You can vote")
else:
    print("You are not allowed to vote")    
    
    
              
        



   

#DAY1
print("Hello"+" " + input(" Enter your name"))
#DAY1 Project
print("Hi! welcome to Band name generator")
city=input("May i know in which city you had growned up?\n")
pet=input("Great! May i know your favorite pet's name?\n")
print("Here we go!\n")
print("You could keep your band name as "+ " "+city+" "+pet)
#DAY2

#DAY2.1adding two number
two_digit_number = input("Type a two digit number: ")
first=two_digit_number[0]
two=two_digit_number[1]
conv1=int(first)
conv2=int(two)
print(conv1+conv2)

#Day2.2 BMI in Metre
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi=(float(weight)/float(height)**2)
print(int(bmi))

#Day2.3 remaining Life from 90
#COmplex_version
age = input("What is your current age?")
weeks90=1_59_120
days90=32_850
months90=1_080
weeks=52
days=365
months=12

whole_age=int(age)

conv_weeks=round(weeks90-(whole_age*weeks))
conv_days=round(days90-(whole_age*days))
conv_months=round(months90-(whole_age*months))

#print(conv_weeks,conv_days,conv_months)

print(f"You have {conv_days} days, {conv_weeks} weeks, and {conv_months} months left.")

#Simple_Version
age = input("What is your current age? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#DAY2 Project
print("Welcome to the tip calculator!")

total=input("Enter your total bill? $")

percentage= input("What percentage tip would like to give? 10,12, or 15? ")

split= input("How many people to split the bill? ")

Tip_per=((int(percentage)/100)*float(total))

#print(Tip_per)
sub_total=((float(total)+Tip_per)/int(split))

final=round(sub_total,2)

print(f"Each person should pay: ${final}")


#DAY3
#DAY3.1 ODD Or Even
number = int(input("Which number do you want to check? "))

if(number%2==0):
  print("This is an Even number.")
else:
  print("This is an Odd number. ")  

#DAY3.2 BMI2.0 in Metre
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


#DAY3.3 Leap year
year = int(input("Which year do you want to check? "))

if(year%4==0):
  if(year%100==0):
    if(year%400==0):
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")  


#DAY3.4 PYHTON_PIZZA
#MY_VERSION
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill=0

if(size=="S"):
  bill=15
  #print(f"your current bill {bill}")
elif(size=="M"):
  bill=20
  #print(f"your current bill {bill}")
elif(size=="L"):
  bill=25
  #print(f"your current bill {bill}")  
  
if(add_pepperoni=="Y"):
  if(size=="S"):
    bill+=2
    #print(f"your current bill {bill}")  
  if(size=="M"):
    bill+=3
    #print(f"your current bill {bill}")
  if(size=="L"):
    bill+=3
    #print(f"your current bill {bill}")
    
if(extra_cheese=="Y"):
  bill+=1
  #print(f"your current bill {bill}")
  print(f"Your final bill is: ${bill}.")
else:
  print(f"Your final bill is: ${bill}.")

#Simple_Version

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

#DAY3.5 LOVE CALCULATOR

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



low1=name1.lower()
low2=name2.lower()
combined=low1+low2

t=combined.count('t')
r=combined.count('r')
u=combined.count('u')
e=combined.count('e')

first_name=t+r+u+e

l=combined.count('l')
o=combined.count('o')
v=combined.count('v')
e=combined.count('e')

second_name=l+o+v+e

score= int(str(first_name)+str(second_name))


if(score<10 or score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")
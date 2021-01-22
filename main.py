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

  #DAY3 PROJECT
  
  print('''


                            /  \
                           |    |
             _             |    |
           /' |            | _  |
          |   |            |    |
          | _ |            |    |
          |   |            |    |
          |   |        __  | _  |
          | _ |  __   /  \ |    |
          |   | /  \ |    ||    |
          |   ||    ||    ||    |       _---.
          |   ||    ||    |. __ |     ./     |
          | _. | -- || -- |    `|    /      //
          |'   |    ||    |     |   /`     (/
          |    |    ||    |     | ./       /
          |    |.--.||.--.|  __ |/       .|
          |  __|    ||    |-'            /
          |-'   \__/  \__/             .|
          |       _.-'                 /
          |   _.-'      /             |
          |            /             /
          |           |             /
          `           |            /
           \          |          /'
            |          `        /
             \                .'
             |                |
             |                |
             |                |
             |                |
''')
print("Welcome to crush memory.")
print("This is to find the treasure in you.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

Bridge_scene=input("You are driving a car alone early morning and you are seeing a woman fellling into the river. What will you do? Will you save her or not?\n").lower()

if(Bridge_scene=="save"):
  print("Mmm!This shows your humanity, Next\n")
  saving_scene=input("Now you had rushed down to the bridge to save her. You had jumped into it and looked for her and saved her. Now you came to know that, She was your most favourite Crush in the college. Now will you be happy to see her or not happy?\n").lower()
  if(saving_scene=="happy"):
    print("Well! This tells that you still didn't forget her.\n") 
    Guilty_scene=input("Now you saved her, Hospitalised her and felt happy too. She felt guilt by seeing you, Because she rejected your proposal while you are in the college. Since you are not job ready and she doesn't believe in you. But now she realised her mistake and tries to speak with you for joining with you again. Will you speak with her or not speak?\n").lower()
    if(Guilty_scene=="speak"):
      print("haha! You are good to accept her \n") 
      joining_scene=input("She had regreted you before in college. Now Will you accept her proposal to join and marry her. Now you are well settled than she expected. Will you accept her or not? \n").lower()
      if(joining_scene=="not accept"):
        print("This shows your guts and manliness for rejecting her, Because she is not worth for you.\n")
   
else:
  print("sorry, You are not up to the mark as expected!")


#DAY 4
#DAY 4.1 COIN FLIP


import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

number= random.randint(0,1)

if(number==1):
  print("Heads")
else:
  print("Tails")


#DAY 4.2 BANK ROULETTE

#COMPLEX version
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

length=len(names)
random_gen=random.randint(0,length-1)
variable=names[random_gen]
print(f"{variable} is going to buy the meal today!")

#Simple_version using choice on list

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
#using choice 👇
random_gen=random.choice(names)
print(f"{random_gen} is going to buy the meal today!")

#DAY 4.3 Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

a=int(position[0])
b=int(position[1])
a=a-1
b=b-1
map[a][b]='X'


print(f"{row1}\n{row2}\n{row3}")



#DAY4 Project ROCK PAPER SCISSOR
#My version and Complex version, The normal one! 
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice= int(input(" What do you choose? Type 0 for Rock, Type 1 for Paper or 2 for Scissors.\n"))




if(choice==0):
  print(rock)

if(choice==1):
  print(paper)

if(choice==2):
  print(scissors)

computer=random.randint(0,2)
print("computer choose:")
if(computer==0):
  print(rock)

if(computer==1):
  print(paper)

if(computer==2):
  print(scissors) 

#result

if(choice>2 or choice<0):
  print("You entered invalid number!")

elif(choice==0 and computer==1):
  print("You loose")
  
elif(choice==1 and computer==2):
   print("You loose")

elif(choice==2 and computer==0):
     print("You loose")

elif(choice==computer):
  print("You draw")

else:
      print("You win")
      
#Tutor and simple version using list

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
 


#DAY 5

#DAY5.1 sum and avg height of persons in a list using loop
#My version

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#
counter = 0
for a in student_heights:
  counter+=1

sum=0
for b in range(0,counter):
  sum+=student_heights[b]
  avg=sum/counter
print(round(avg))

#Lecture version

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

#5.2 Finding Highet_score in list using loop.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high=0
for i in student_scores:
  if(i>high):
    high=i
print(f"The highest score in the class is: {high}")    







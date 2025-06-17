from random import randint

# We don't want this to do nothing
# Comment 

# Simple print with a fixed values

print("Hello IPI ! ")


# Simple variables and calculating profit

month = "Mai"
sales = 5000
expenses = 2000
profit = sales - expenses
print("The profit in May was :" + str(profit))


# User input (sales, expenses, and mouth)

month = input("what is the mouth ? ")
sales = int(input("Whats the sales value ? "))
expenses = int(input("Whats the expenses values ? "))
profit = sales - expenses
print(f"The result in {month} was {profit}")


# if / elif / else to check if the result is positive, negative or neutral

if profit > 0:
    print("You are doping good! PROFIT")
elif profit < 0:
    print("You are doping not as great! BAD RESULT")
else:
    print("Results are neutral.")


# Creating a list and using list methods (append, insert, remove, pop)

services = ["Websites", "Consulting"]
services.append("Training")
services.insert(0, "Classes")
services.pop()
services.remove("Websites")
print(services)



# For loop to iterate the list and print each product

for product in services:
    print(product)


# Defining and calling a function using an f-string

def print_name(name):
    print(f'Helllo {name}')

print_name(input("What's your name ? "))


# magic ball exercice

print("Welcome to the Magic 8 Ball!")
question = input("Ask your question: ")

number = randint(1, 10)

if number == 1:
    print("Magic answer: Yes, definitely.")
elif number == 2:
    print("Magic answer: It is certain.")
elif number == 3:
    print("Magic answer: Without a doubt.")
elif number == 4:
    print("Magic answer: Reply hazy, try again.")
elif number == 5:
    print("Magic answer: Ask again later.")
elif number == 6:
    print("Magic answer: Better not tell you now.")
elif number == 7:
    print("Magic answer: My sources say no.")
elif number == 8:
    print("Magic answer: Outlook not so good.")
elif number == 9:
    print("Magic answer: Very doubtful.")
else:
    print("Magic answer: Signs point to yes.")

# new version of the last exercice

print("Welcome to the Magic 8 Ball!")
question = input("Ask your question: ")

answers = ["Yes, definitely.", "It is certain.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Magic answer: probably, yes.", "Magic answer: Very doubtful.", "Magic answer: Signs point to yes."]

reponse=answers[randint(0, 9)]
print(reponse)
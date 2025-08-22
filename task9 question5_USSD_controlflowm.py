#    Simulated USSD Menu Interaction
    #You are to design a mock USSD interface for a mobile services.
    #   Requirements:
            # 1. when the user runs the program, display a welcome screen with
            # a Nigerian context greeting.
            # 2. ask the user to "dial" a USSD code (e.g., *123#) and store it in 
            # a variable.
            #3. print a menu with at least 3 options (e.g., "Check Balance", 
            # "Buy Airtime", "Buy Data") using newline escape squences (\n) for
            # formatting.
            # 4. ask the user to choose an option (1, 2, or 3) and store their 
            # choice in a variable.
            # 5. use f-strings and/or concatenation to display a confirmation
            # message showing the selected option.
            # 6. ask for an amount (if applicable) and store it as a 
            # number using type casting.
            #7. display a final message summarizing the transaction.

print ("Welcome to Olu.Oludayo Enterprises USSD Service")
confirm = input("Do you wish to continue ?(yes/no):").strip().lower()
if confirm =="yes":

    code = input("Input option of your choice please..!!! press enter-key ")
    print ("Please choose an option:\n1. Buy Airtime \n2. Buy Data \n3. Check Data \n4. select from option 1-3")
    option = int(input("Enter choice 1-4: "))
    print (f"You selected option {option}")
    print("<>"*20)
    amount = float(input("Enter amount: "))
    print(" Your Transcation successful")
    print("<>"*20)
confirm= input(" Do you want to print receipt? (yes/no):").strip().lower()
if confirm =="yes":
    print(amount)
    print(f"\nYou dialled {code} for service {option} and the amount N{amount}")
    
else:
    exit()
print ("Thank you for using our service.")



# Output:
#     Welcome to Olu.Oludayo Enterprises USSD Service
# Do you wish to continue ?(yes/no):yes
# Input option of your choice please..!!! press enter-key
# Please choose an option:
# 1. Buy Airtime
# 2. Buy Data
# 3. Check Data
# 4. select from option 1-3
# Enter choice 1-4: 1
# You selected option 1
# <><><><><><><><><><><><><><><><><><><><>
# Enter amount: 500
#  Your Transcation successful
# <><><><><><><><><><><><><><><><><><><><>
#  Do you want to print receipt? (yes/no):yes
# amount

# You dialled  for service 1 and the amount N500.0
# Thank you for using our service.
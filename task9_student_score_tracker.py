# Student Score Tracker**
# Ask the user for 3 student names.
# For each student, ask for their score.
# Store the results in two lists (one for names, one for scores).
# Print a formatted output showing Name — Score, aligned neatly.
#  Tips: You are to start by creating two empty lists.

name = []
score = []
nam = input("Enter first Name: ")
nam_1 = input("Enter second: ")
nam_2 = input("Enter third Name: ")
scr = input("Enter score: ")
scr_1 = input("Enter score: ")
scr_2 = input("Enter score: ")
confirm = input("Are done entering your details:?(yes/no): ").strip().lower()
if confirm == "yes":
      name.append(nam)
      name.append(nam_1)
      name.append(nam_2)
      score.append(scr)
      score.append(scr_1)
      score.append(scr_2)
else:   # if not "yes", program ends politely
      print("Goodbye! You chose not to continue.")
      exit()      
print("Name\t| Score")
print("="*20)
print(f"{name[0]} \t | {score[0]}")
print(f"{name[1]} \t | {score[1]}")
print(f"{name[2]} \t | {score[2]}")
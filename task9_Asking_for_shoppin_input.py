items = []
itm_1 = input("Enter  first item of your choice: ")
itm_2 = input("Enter item of your choice: ")
itm_3 = input("Enter item of your choice: ")
item_4 = input("Enter the item of your choice :")
 # Confirmation
confirm = input("Are done entering your items of your choice:?(yes/no): ")
if confirm.lower() == "yes":

      items.append(itm_1)
      items.append(itm_2)
      items.append(itm_3)
      items.append(item_4)
      res = (",".join(items))
      print(str(res))
      print(" Thank you")
else:   # if not "yes", program ends politely
      print("Goodbye! You chose not to continue.")
      exit()
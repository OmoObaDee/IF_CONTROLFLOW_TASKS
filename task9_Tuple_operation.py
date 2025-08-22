# Using if control flow 
state =[]
state_1 = input( " Enter first state :")
state_2 = input( " Enter first state :")
state_3 = input( " Enter first state :")
state_4 = input( " Enter first state :")
state_5 = input( " Enter first state :")
state = ( state_1, state_2, state_3, state_4, state_5)
if len(state) >= 5:
    print(state)
    print(f"First state is {state[0]}, and the last state is {state[4]}")
    print("THANK YOU!!!")

else:
    exit()
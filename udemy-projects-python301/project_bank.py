# create a class hold customers information

# class Bank:
    
#     def __init__(self,balance=0.00):
#         self.balance=balance

#     # write the title to the customer.txt
#     def add_title(s):
#         with open('customer.txt','a') as file:
#             file.write(s)


# bank=Bank(20.00)

# prompt the user to input the name of the account
user=input("type the names of your account: ")
# prompt user to enter the content like to add to account file
# content=input("type the name you enter:  ")
# capitalize the initial letters 
# content.upper()

# operation on the file
# with open(user,'a') as file:
#     file.write(content)

# prompt user to select if like to open the file
file_opt=input("do you like to open the file now?(y/n)   ")

if file_opt in ['y','n']:
    if file_opt == 'y':
        with open(user,'r') as file:
            names=file.readlines()
            print(type(names)) 
            print(names)
            print("---------")
for n in names:
    print(n)


    
    





    


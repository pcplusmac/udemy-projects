# create a class hold customers information

class Bank:
    
    def __init__(self,balance=0.00):
        self.balance=balance

    # write the title to the customer.txt
    def log_transaction(self,data):
        with open("transaction_records.txt","a") as file:
            # file.write("The new balance is:" + str(data)+ ".\n ")
            # above code can be written in f-format string as below:
            file.write(f"The new balance is:\t\t\t{data} dollars.\n")
    # use the decorator to decorate the withdraw method, so we can comment out line 26.
    @log_transaction
    def withdraw(self,amount):
        # this is good practice to ensure that the amount is not string via float() the value, if it not able to float, means it is string
        try: 
            amount = float(amount)
        except ValueError:
            # if the amount is float, but it is string, we will set the value of the amoutn to be zero
            amount=0
        
        if amount <= self.balance: 
            self.balance = self.balance - amount
            # self.log_transaction(self.balance)
        else:
            print("balance is not enough.")
    def deposit(self,amount):
        # ensure the amount is not string
        try:
            amount = float(amount)
        except ValueError:
            amount=0
        # because this is deposit, no need to check the balance, so just do 'if amount:'
        if amount:
            self.balance= self.balance + amount
            self.log_transaction(self.balance)
        
customer_acc=Bank(20)
# prompt the user to input the name of the account in a iterative circumstances
while True:
    action=input(" choose deposit / withdraw: ")
    if action in ['deposit','withdraw']:
        if action=='deposit':
            amt=input("how much do you want to put it? ")
            customer_acc.deposit(amt)
            print (customer_acc.balance)
        else:
            amt=input("how much do you want to take out? ")
            customer_acc.withdraw(amt)
            print(customer_acc.balance)




# prompt user to enter the content like to add to account file
# content=input("type the name you enter:  ")
# capitalize the initial letters 
# content.upper()

# operation on the file
# with open(user,'a') as file:
#     file.write(content)

# prompt user to select if like to open the file
# file_opt=input("do you like to open the file now?(y/n)   ")

# if file_opt in ['y','n']:
#     if file_opt == 'y':
#         with open(user,'r') as file:
#             names=file.readlines()
#             print(type(names)) 
#             print(names)
#             print("---------")
# for n in names:
#     print(n)


    
    





    


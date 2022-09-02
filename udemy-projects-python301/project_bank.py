# create a class hold customers information

class Bank:
    
    def __init__(self,balance=0.00):
        self.balance=balance
    
    # # the normal log_transaction method
    # def log_transaction(self,data):
    #     with open("transaction_records.txt","a") as file:
    #         # file.write("The new balance is:" + str(data)+ ".\n ")
    #         # above code can be written in f-format string as below:
    #         file.write(f"The new balance is:\t\t\t{data} dollars.\n")
    
    # define a decorator
    def decorator(func):
        # write the title to the customer.txt
        def log_transaction(self,amount):
            func(self,amount)
            with open("transaction_records.txt","a") as file:
            # file.write("The new balance is:" + str(data)+ ".\n ")
            # above code can be written in f-format string as below:
                file.write(f"The new balance is:\t\t\t{self.balance} dollars.\n")
        return log_transaction
    # use the decorator to decorate the withdraw method, so we can comment out line 26.
    @decorator
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

# there are 2 machenism of this app for updating each transaction, one is via decorator, the other is 
# via the normal method. both are doing for the same output. 




    
    





    


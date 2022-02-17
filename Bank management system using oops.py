import random
class Banking():
    name=''
    acno=''
    deposit=0
    actype=''

    def welcome(self):
        print("************************************** WELCOME TO BANK **************************************")

    def createaccount(self):
        self.name=input("Enter your name : ")
        print("For saving account minimum deposit 500Rs and For current account minimum deposit 1000Rs")
        self.actype=input("Enter your account type SAVING or CURRENT : ")
        if self.actype in['SAVING','CURRENT','saving','current']:
            for self.acno in range(9):
                self.acno = random.randrange(1, 999999999999999, 9)

        else:
            exit()
        self.deposit = int(input("Enter your deposit amount : "))
        if self.deposit>=500 and self.actype in['SAVING','saving']:
            print('********************************************************************************************************')
            print('Congratulations {},Your {} account no. {} is created succesfully. '
                        'And {} credited to your account. '.format(self.name,self.actype,self.acno,self.deposit))
            print('********************************************************************************************************')
            b.userchoice()
        if self.deposit>=1000 and self.actype in['CURRENT','current']:
            print('Congratulations {},Your {} account no. {} is created succesfully. '
                        'And {} credited to your account. '.format(self.name,self.actype,self.acno,self.deposit))
            b.userchoice()

    def deposite(self):
        deposit = int(input('Enter your deposit amount and press any key to exit : '))
        if deposit>=0:
         self.deposit=self.deposit+deposit
         print("Your {}Rs is successfully deposited to your account and now your balance is {}".format(deposit,self.deposit))
         b.userchoice()

    def withdraw(self):
        withdraw = int(input('Enter your withdraw amount and press any key to exit : '))
        if withdraw<=self.deposit:
            self.deposit=self.deposit-withdraw
            print("Your {}Rs is successfully withdraw to your account and now your balance is {}".format(withdraw,self.deposit))
        else:
            print("You have not sufficient balance to withdraw and your current balance is {}".format(self.deposit))
        b.userchoice()

    def balanceenquiry(self):
        print('********************************************************************************************************')
        print("In your A/C No. : '{}' Avialable Balance is - '{}' ".format(self.acno,self.deposit))
        print('********************************************************************************************************')
        b.userchoice()

    def listofaccount(self):
        print("In this bank list of a/c : {}".format(self.acno))
        b.userchoice()
    def userchoice(self):
        print("You want continue with following options or enter any key to exit :")
        print("2.deposit ")
        print("3.withdraw ")
        print("4.Balance enquiry ")
        print("6.Entered to exit ")

        user = int(input("Enter here ---->>  "))
        if user in [1]:
            b.createaccount()
        if user in [2]:
            b.deposite()
        if user in [3]:
            b.withdraw()
        if user in [4]:
            b.balanceenquiry()
        if user in [5]:
            b.listofaccount()
        if user in[6]:
            exit()
while True:
    b = Banking()
    user=input("You want to continue Bank operations 'Y' or entered any key to exit : ")
    if user in['Y','y']:
        b.welcome()
        print("Which type of opeartion you want to do select following options :")
        print("1.Open account")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")
        user=int(input("Enter option here ---->  "))
        if user in[1,2,3]:
            if user==1:
                b.createaccount()
                print("Which type of opeartion you want to do select following options :")
                print("1.Open account")
                print("2.deposit")
                print("3.withdraw")
                print("4.Exit")

                user = int(input("Enter option here ----> "))
                user = int(input())
                while user in[2,3]:
                 if user==2:
                     b.deposite()
                     continue
                 if user==3:
                     b.withdraw()
                     continue
                 elif withdraw<self.deposit:
                     print('You have not sufficient balance.....')
                 else:
                     exit()
        elif user==4:
            exit()
        else:
            print("You Entered wrong input.......")
    else:
        exit()
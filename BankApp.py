
from itertools import count
from datetime import date as dt


class BankApp():
    def __init__(s):
        s.bankAccounts = []
        s.data = []
        s.History = []
        s.deleteHistory = []
        s.unity = []
        s.id = 0
        s.currentDate = dt.today().strftime("%d/%m/%y")
        s.balance = None
        s.Hid = 0


    def menu(s):
        pick = input("""
        1. create an account
        2. deposit
        3. withdraw
        4. display account
        5. delete account
        6. check account balance
        7. History
        8. exit
        
        choose an option from the menu: """ )
        if pick == '1':
            print('creating account...\n')
            s.createAccount()
        elif pick == '2':
            print('Deposit\n')
            s.search_depositor()
        elif pick == '3':
            print('withdrawal...\n')
            s.search_withdrawer()
        elif pick == '4':
            print('displaying account...\n')
            s.displayAccount()
        elif pick == '5':
            print('deleting account\n')
            s.delete()
        elif pick == '6':
            print('checking account balance...\n')
            s.trial()
        elif pick == '7':
            s.checkHistory()
        elif pick == '8':
            print('logged out\n')
            exit()
        else:
            print('invalid option')
            s.menu()

    def floatCheck(s,entry):
        try:
            float(entry)
            return True
        except:
            return False

    def strCheck(s,entry):
        try:
            if entry.isdigit() or entry == '':
                return True
        except:
            return False

    def intcheck(s,entry):
        try:
            int(entry)
            return True
        except:
            return False

    def clear(s):
        s.data = []

    def fileTransfer(s, id, data, account):
        data.append(id)
        account.append(data)
        s.data = []

    def fileTransfer1(s, Hid, data, account):
        data.append('Transaction ID: ' + str(Hid))
        account.append(data)
        s.data = []

    def createAccount(s):
        #global userIdn
        for i in count():
            prompt = input('create an account (y/n): ').lower()
            if prompt == 'n':
                print('Thanks for creating an account\n')
                s.menu()
            elif prompt == 'y':
                userName = input('please enter full name: ')
                if s.strCheck(userName):
                    print('please enter a valid name')
                    s.createAccount()
                else:
                    password = input('please create a password (Not less than 8 characters): ')
                    if len(password) < 8 or password in s.bankAccounts:
                        print('please enter a password with 8 characters')
                        s.createAccount()
                    else:
                        s.balance = input('please deposit an amount to activate account: ')
                        if s.floatCheck(s.balance) is False:
                            print('please enter a valid amount')
                        else:
                            s.data.append('Name: ')
                            s.data.append(userName)
                            s.data.append('|')
                            s.data.append(' password: ')
                            s.data.append(password)
                            s.data.append(' |')
                            s.data.append( ' Account Balance: ')
                            s.data.append(s.balance)
                            s.data.append('|')
                            s.data.append(' Date created: ')
                            s.data.append(s.currentDate)
                            s.data.append('|')
                            s.data.append(' user ID: ')
                            #s.data.append(s.id)
                            s.fileTransfer(s.id, s.data, s.bankAccounts)
                            print('account successfully created')
                            print(s.bankAccounts)
                            s.id += 1
            else:
                print('invalid input')
                s.createAccount()
    def search(s, id, folder,redirect):
        k = 0
        while k < len(folder):
            if int(id) in folder[k]:
                s.balance = folder[k][7]
                print('account details ==>', *folder[k])
                redirect()
            k+=1
    
    def error(s):
        if userIdn.isdigit() is False:
            print('invalid ID')
            s.search_depositor()

    
    def displayAccount(s):
        userIdn = input('enter id: ')
        if s.intcheck(userIdn) is False:
            print('please enter a valid ID')
            s.displayAccount()
        else:
            s.search1(userIdn, s.bankAccounts,s.menu)
            print('account not yet Created / invalid ID')
            s.createAccount()


    def search_depositor(s):
        global userIdn
        userIdn= input('enter ID: ')
        s.error()
        #if s.intcheck(userIdn) is False:
         #   print('invalid input')
           # s.search_depositor()
        s.search(userIdn ,s.bankAccounts, s.deposit)
        print("Acct not yet created or invalid ID!")
        s.createAccount() 


    def deposit(s):
        depositedAmount = input('enter amount to deposit: ')
        if s.floatCheck(depositedAmount) is False or s.floatCheck(depositedAmount) <= 0:
            print('please enter a valid amount')
            s.deposit()
        else:
            s.bankAccounts[int(userIdn)][7] = float(s.bankAccounts[int(userIdn)][7]) + float(depositedAmount)
            print('New Balance: ', s.bankAccounts[int(userIdn)][7])
            s.data.append(int(userIdn))
            s.data.append('deposited: '+ str(depositedAmount) + ' on ' + str(s.currentDate))
            s.fileTransfer1(s.Hid, s.data, s.History)
            print(s.History)
            s.Hid +=1
            s.search(userIdn,s.bankAccounts,s.menu)
            #s.data.append('user ID number ==>')
            #s.data.append(s.id)
            

    def search_withdrawer(s):
        global userIdn
        userIdn = input('enter ID: ')
        s.error()
        s.search(userIdn ,s.bankAccounts, s.withdrawal)
        print("Acct not yet created or invalid ID!")
        s.createAccount() 


    def withdrawal(s):
        withdrawnAmount = input('enter amount to withdraw: ')
        if s.floatCheck(withdrawnAmount) is False or s.floatCheck(withdrawnAmount) <= 0:
            print('please enter a valid amount')
            s.withdrawal()
        elif s.floatCheck(withdrawnAmount) > float(s.bankAccounts[int(userIdn)][7]):
            print('insufficient funds')
            s.withdrawal()
        else:
            s.bankAccounts[int(userIdn)][7] = float(s.bankAccounts[int(userIdn)][7]) - float(withdrawnAmount)
            print('New Balance: ', s.bankAccounts[int(userIdn)][7])
            s.data.append(int(userIdn))
            s.data.append('withdrawn: '+ str(withdrawnAmount) + ' on ' + str(s.currentDate))
            s.fileTransfer1(s.Hid, s.data, s.History)
            print(s.History)
            s.Hid += 1
            s.search(userIdn,s.bankAccounts,s.menu)
            
        
    def delete(s):
        prompt = input('Are you sure you want to terminate account (y/n): ').lower()
        if prompt == "n":
            s.menu()
        elif prompt == "y":
            userIdn = input('please enter your ID: ')
            if userIdn.isdigit() is False:
                print('invalid ID')
                s.delete()
            else:
                s.deleteHistory.append(s.bankAccounts[int(userIdn)])
                s.bankAccounts.remove(s.bankAccounts[int(userIdn)])
                s.bankAccounts.insert(int(userIdn), ["This account is no longer available", int(userIdn)])
                print(s.deleteHistory)
                s.search1(userIdn,s.bankAccounts,s.menu)
                print('account not registered')
                s.menu()
        else:
            print('Invalid')
            s.delete()

    def checkDelete(s):
        global userIdn
        k = 0
        while k < len(s.deleteHistory):
            if int(userIdn) in s.deleteHistory[k]:
                print('This account has been deleted')
                s.menu()
            k+=1

    def trial(s):
        global userIdn
        userIdn = input('enter userID: ')
        s.error()
        s.checkDelete()
        s.search(userIdn ,s.bankAccounts, s.Balance)
        print("Acct not yet created or invalid ID!")
        s.createAccount() 
        #print('account not created')
        

    def Balance(s):
        print('account balance: ', s.bankAccounts[int(userIdn)][7])
        s.menu()

    def search1(s, id, folder, redirect):
        j = 0
        while j < len(folder):
            if int(id) in folder[j]:
                print('account details ==>', *folder[j])
                redirect()
            j+=1


    def searchHistory(s, id, folder, redirect):
      
        j = 0
        while j < len(folder):
            if int(id) in folder[j]:
                s.unity.append(folder[j])
            j+=1
        if  s.unity == [ ]:
            print("invalid or not yet registered!")
            s.createAccount()
        else:
            redirect()
                
    def display(s):
             i = 0
             while i < len(s.unity):
                 print(*s.unity[i])
                 
                 i +=1
             s.unity = []
             s.menu()
        
        
    def historyError(s):
        if userIdn.isdigit() is False:
            print('invalid ID')
            s.checkHistory()

    def checkHistory(s):
        global userIdn
        userIdn = input('enter ID: ')
        s.historyError()
        s.searchHistory(userIdn, s.History, s.display)
        print("Acct not yet created or invalid IDN!")
        s.createAccount()

    
BankApp().menu()

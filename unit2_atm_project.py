


user = {
    "harsh": {"password": "1234", "balance": 0, "transactions": []},
    "john": {"password": "5678", "balance": 0, "transactions": []},
    "rukmani": {"password": "9012", "balance": 0, "transactions": []}
}

print("Enter user name: ")
username:str = input()
if username in user:
    n:int = 0
    while(n<3):
        print("Enter password: ")
        password:str = input()
        if password == user[username]["password"]:
            break
        else:
            n=n+1
    
    if n>=3:
        print("You have exceed your trail")
    else:
        print(username+" Dashboard:")
        while(True):
            print("1.Check Balance \n2.Deposit Money \n3.Withdraw Money \n4.Logout \n5.View Transaction History")
            option = input()
            if option=="1":
                print(user[username]['balance'])
            elif option == "2":
                print("Enter amount:")
                amount:int = int(input())
                print(username+" Deposited:{amount}")
                user[username]['balance'] += amount 
                user[username]["transactions"].append("Deposited:{amount}")
            elif option=="3":
                print("Enter amount:")
                amount:int = int(input())
                print(username+f" Withdraw:{amount}")
                user[username]['balance'] =  user[username]["balance"] - amount
                user[username]["transactions"].append("Withdraw:{amount}" )
            elif option=="5":
                for items in user[username]["transactions"]:
                    print(items)  
            elif option=="4":
                break         
            elif option!="1" or "2" or "3" or"4" or"5":
                pass             
else:
    print("username is wrong")    
 
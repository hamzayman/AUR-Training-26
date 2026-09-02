data={}

def print_stock ( data ):
        i=1
        for key,value in data.items() :
            print(f"{i} {key} : {value}\n")
            i+=1
    
with open("stock.txt","a+") as f :
    f.seek(0)
    for line in f :
        line =line.strip()
        if line :
            name,value=line.split(",")
            data[name]=int(value)
while True :
    print("enter 1 to add stock \n enter 2 to remove stock\nenter 3 to show stock’s content\nsenter 4 to exit the program\n")
    choice=input()
    if choice not in ("1" , "2" , "3" , "4") :
        print ("Non valid input\n")
        break
    
    else: 
        print(f"you chose {choice}\n")


    if(choice == "1"):
        print_stock(data)
        stock_key = input ("enter the stock name : \n")
        stock_key = stock_key.lower()
        if  not stock_key.isalpha() :
            print ("Non valid input")
            break
        stock_val=input("enter number of stock \n")
        if  not stock_val.isdigit():
            print ("Non valid input")
            break

        if stock_key in data:
            data[stock_key] += int(stock_val)
        else:
            data[stock_key] = int (stock_val)    


    elif choice == "2" :
        print_stock(data)
        stock_key = input ("enter the stock name : \n")
        stock_key = stock_key.lower()
        if  ( not stock_key.isalpha() ) or ( stock_key not in data.keys()  )  :
                print ("Non valid input \n")
                break
        stock_val=input("enter number of stock : \n")
        if  ( not stock_val.isdigit() ) or (data[stock_key]- int (stock_val) < 0):
            print ("Non valid input \n ")
            break

    elif choice == "3" :
        print_stock(data)
    elif choice == "4":
        with open("stock.txt", "w") as f:
            for key, value in data.items():
                f.write(f"{key},{value}\n")
        break
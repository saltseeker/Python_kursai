import pickle, os

balansas = []
message = None
balance_FILE = "balansas.pkl"



def load_balance():
    global message
    try:
        with open(balance_FILE, 'rb') as pkl:
            balansas = pickle.load(pkl)
            suma = 0
            for skaicius, irasas in enumerate(balansas):
                suma += irasas
                print(skaicius + 1, irasas)
                print("balansas", suma)
    except:
        message = "failed to load"
        return[]
    else:
        print(f"{balansas} succesfully loaded ")
        return balansas
 


def print_message():
    #clear()
    global message
    if message:
        print('-'*(len(message)+4))
        print(f"| {message} |\n")    
    message = None     


def clear(): 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')


def save_balance():
    global message
    try:
        with open(balance_FILE, 'wb') as pkl:
            pickle.dump(balansas, pkl)
    except Exception as error:
        message = "failed to save!"
    else:
        message = "successfully saved"    


def balance_entry():
    global balansas
    global message
    pokytis = float(input("iveskite balanso pokiti: "))
    balansas = load_balance()
    balansas.append(pokytis)
    save_balance()
    
    
    return balansas
      


def print_menu():
    print('===[ MENU ]===')
    print('1. new balance entry')
    print('x or 0 to exit')
  





while True:
    #clear()
    print_message()
    print_menu() 
    choice = input('make a choice: ')  
    #clear()   #isvalo ekrana
    if choice.lower() ==  "x" or choice == "0" or choice =="":
        break
    if choice == "1":
        balance_entry()
        
    




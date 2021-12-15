#Elliot Eriksson
#TEINF-20
#14/12-2021
#Wishlist & Naughtylist

import sys,time,random

def print_slow(str):
    """
    Prints the text slowly letter by letter
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def wishlist():
    """
    This function creates wishlists for the user and writes their wishes, aswell as writes it out for them.
    """

    answer = input('\nSkriv "1" om du vill skapa en ny önskelista.\nSkriv "2" om du vill läsa upp en önskelista. \nSKriv "3" om du vill lägg till nytt på en gammal önskelista. \n')

    if answer == "1":
        file_name = input("Vad vill du kalla önskelistan?\n")
        file_name = file_name + ".txt"
        with open(file_name, "w", encoding="UTF-8") as x:
            child = input("Vad heter barnet: ")
            x.write(f"Barnets namn: {child}\n\n")
            x.write("---ÖNSKELISTA---\n")
            print("Skriv in det du önskar dig, skriv # när du vill avsluta.\n")
            while True:
                wish = input("Önskemål: ")
                if wish == "#":
                    break
                else:
                    x.write(f"{wish}\n")
            time.sleep(0.5)
            print_slow("\nSkapar din önskelista...\n\n") 

    elif answer == "2":
        file_name = input("Vilken önskelista vill du öppna?\n")
        file_name = file_name + ".txt"
        time.sleep(0.5)
        print_slow("\nLoading...\n\n") 
        with open(file_name, "r", encoding="UTF-8") as x:
            readline=x.read().splitlines()
            print(readline)

    elif answer == "3":
        file_name = input("Vilken önskelista vill du öppna?\n")
        file_name = file_name + ".txt"
        time.sleep(0.5)
        print_slow("\nLoading...\n\n") 
        with open(file_name, "r", encoding="UTF-8") as x:
            readline=x.read().splitlines()
            print(readline)
        
        with open("kolbarn.txt", "a", encoding="UTF-8") as x:  
            print("Skriv in det som ska läggas till, skriv # när du vill avsluta.\n")
            while True:
                wish = input("Önskemål: ")
                if wish == "#":
                    break
                else:
                    x.write(f"{wish}\n")  
        print_slow("Uppdaterar din önskelist...")

def naughtylist():
    """
    This function allows the user to read the naught list or add new children to the naughty list
    """
    answer = input('\nSkriv "1" om du vill läsa upp listan av kolbarn.\nSkriv "2" om du vill lägga till flera barn på listan av kolbarn.\n')

    if answer == "1":
        with open("kolbarn.txt", "r", encoding="UTF-8") as x:
            time.sleep(0.5)
            print_slow("Loading...")
            readline=x.read().splitlines()
            print(readline)
            
    elif answer == "2":
        with open("kolbarn.txt", "r", encoding="UTF-8") as x:
            readline=x.read().splitlines()
            print(readline)
        with open("kolbarn.txt", "a", encoding="UTF-8") as x:  
            print("Skriv in det barn som ska läggas till, skriv # när du vill avsluta.\n")
            while True:
                name = input("Namn: ")
                if name == "#":
                    break
                else:
                    x.write(f"{name}\n")     
            time.sleep(0.5)
            print_slow("Uppdaterar kolbarnslista...")

answer = input('Vad vill du göra? \nSkriv "1" om du vill göra ny, läsa upp eller skriva på en gammal önskelista. \nSkriv "2" om du vill läsa upp eller lägga till barn på kolbarnslistan\n')

if answer == "1":
    wishlist()
elif answer == "2":
    naughtylist()
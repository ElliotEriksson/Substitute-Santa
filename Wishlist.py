#Elliot Eriksson
#14/12-2021
#Wishlist

import sys,time,random

def wishlist():
    """
    This function creates wishlists for the user and writes their wishes, aswell as writes it out for them.
    """
    answer = input('Skriv "1" om du vill skapa en ny önskelista.\nSkriv "2" om du vill läsa upp en önskelista.\n')

    if answer == "1":

        file_name = input("Vad vill du kalla önskelistan?\n")
        file_name = file_name + ".txt"
        with open(file_name, "w", encoding="UTF-8") as y:

            child = input("Vad heter barnet: ")
            y.write(f"Barnets namn: {child}\n")

            y.write("---ÖNSKELISTA---\n")

            
            print("Skriv in det du önskar dig, skriv # när du vill avsluta.\n")
            while True:
                wish = input("Önskemål: ")
                if wish == "#":
                    break
                else:
                    y.write(f"{wish}\n")
                    
            time.sleep(1)

            def print_slow(str):
                for letter in str:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.1)

            print_slow("\nSkapar din önskelista...") 

    elif answer == "2":

        file_name = input("Vilken önskelista vill du öppna?\n")
        file_name = file_name + ".txt"

        time.sleep(1)

        def print_slow(str):
            for letter in str:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.1)

        print_slow("\nLoading...") 
        
        with open(file_name, "r", encoding="UTF-8") as x:
            for line in x:
                print(line)

wishlist()
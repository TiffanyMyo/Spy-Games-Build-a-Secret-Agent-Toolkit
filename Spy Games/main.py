import time
from password import gen
from message import decode
from lockpicking import Lockpick
from spy import Spy
from securenotes import SecureVault
from unscramble import unscrambled


print("You are on a secret spy mission trying to break into a rich person's house after hearing there is 1 million dollars hidden somewhere.")
time.sleep(1)
print("As you approach the house, you go behind to try and enter their backdoor but you realize there is a lock in the way.")
time.sleep(1)
print("As you realize this, you take out your lockpick and try your best to enter the house.")
time.sleep(1)
lp = Lockpick(length=5, amount=5)
lp.picking(4)


time.sleep(1)
print("As you enter the house, you have to get past the living room without making any noise.")
time.sleep(1)
us = Spy(10)
us.sneak()
time.sleep(1)
print("You passed through the living room and were presented with three options.\nWhere would you like to go first?")
time.sleep(1)


library_visited = False
library_solved = False
kitchen_visited = False
val3 = 0
result = ""
answer5 = gen()


def main():
   global library_visited, library_solved, kitchen_visited, val3, result, answer5
   while True:
       print("\n1. Bedroom")
       print("2. Library")
       print("3. Kitchen")
       print("4. Or would you like to access your toolkit")
       choice = input("Enter your choice (1-4): \n")


       if choice == '1':
           print("You found a chest! Though it has a lock that requires 4 letters.")
           while True:
               answer = input("What is the password? ")
               if answer.title() == "Echo":
                   print("You opened the chest!\nThough it seems the chest also requires a lock that requires a 5 character password.")
                   for i in range(1, 5):
                       answer1 = input("What is it? (Exit to leave this section) ")
                       if answer1 == answer5:
                           print("You opened the chest!")
                           answer2 = input("There also seems to be an extra chest nearby... Would you like to try opening it? Y/N ")
                           if answer2.upper() == "N":
                               print("Congrats! You left with 1 million dollars")
                               exit()
                           if answer2.upper() == "Y":
                               print("There is a three letter lock...")
                               for i in range(1, 4):
                                   answer3 = input("What's the password? (Hint use the riddle in your Secure Notes Vault)")
                                   if answer3.lower() == "man":
                                       print("Congrats! You left with 2 million dollars!")
                                       exit()
                                   else:
                                       print("Try again...")
                       elif answer1.lower() == "exit":
                           break
                       else:
                           if val3 <= 0:
                               print("That doesn't seem right...")
                           elif val3 == 4:
                               print("You used up all your tries and a alarm system broke out. You left with nothing.")
                               exit()
               else:
                   if answer.lower() == "exit":
                       break
                   else:
                      print("That doesn't seem right... You can try again or exit!")


       elif choice == '2':
           if library_visited == False:
               print("As you enter the library you see a book on the table containing a riddle, but it is encrypted.")
               with open("riddle.txt", "r") as file:
                   riddle = file.read()
                   time.sleep(1)
                   print(riddle)


               time.sleep(1)
               print("You think you might be able to solve this using a toolkit... but first, you need to solve the riddle!")
               library_visited = True
               toolkit()
               while True:
                   answer = input("What is the answer to this? ")
                   if answer.title() == "Echo":
                       print("Correct!")
                       library_solved = True
                       break
                   else:
                       print("That doesn't seem right... Try again!")


               print("There is another note but you don't have enough time so you store this note into your secure notes.")
           else:
               print("Nothing is left here to investigate.")


       elif choice == '3':
           if kitchen_visited == False:
               print("You found a note!")
               while True:
                   question = input("What has many keys but can't open a single lock? ")
                   if question.lower() == "piano":
                       print(f"Fantastic! You found a note containing a password: {answer5}")
                       result += f"\nPassword: {answer5}"
                       kitchen_visited = True
                       break
                   else:
                       print("Incorrect answer. Try again!")
           elif kitchen_visited == True:
               print("Nothing more to investigate.")
       elif choice == "4":
           toolkit()


       elif choice.lower() == "stop":
           break


       else:
           print("Invalid choice. Please enter a number between 1 and 4.")
val1 = False
val2 = False
val4 = False
result1 = ""
def toolkit():
   global library_solved, library_visited, val1, val2, result, kitchen_visited, val4,result1
   while True:
       print("\n1. Caesar Cipher Tool")
       print("2. Secure Note Vault")
       print("3. Message Decoder")
       choice = input("Enter your choice (1-3 or Exit): \n")


       if choice == "1":
           if not library_visited:
               print("Nothing can be done yet.")
           else:
               with open("riddle.txt", "r") as file:
                   riddle = file.read()
                   print("Decoded message:")
                   print(decode(riddle))
               break


       elif choice == "2":
           if kitchen_visited == True:
               print(result)
           elif kitchen_visited == False:
               pass
           if not library_solved:
               if kitchen_visited == False:
                   print("Nothing is in here yet.")
               elif kitchen_visited == True:
                   pass
           else:
               if val2 == False:
                   notes = SecureVault()
                   print(notes)
                   print("This seems to be scrambled!\nMaybe another toolkit option can help decipher it.")
                   val4 = True
               if val2 ==  True:
                   print("Riddle:"+result1+"\n"+"Answer:","Echo")


       elif choice == "3":
           if val4 == False:
               print("Nothing can be done here yet.")
           elif val4 == True:
               if len(result1) <= 0:
                   decoded = unscrambled()
                   print("\nUnscrambled message:")
                   print(decoded)
                   val2 = True
                   result1 += unscrambled()
                   break
               elif len(result1) > 0:
                   print("Nothing else to be done here")
       elif choice.lower() == "exit":
           break


       else:
           print("Invalid choice. Please enter a number between 1 and 3.")


# ---------------------------------------------------------------------------------------------


if __name__ == "__main__":
   main()

import random, time


class Lockpick:
   def __init__(self, length, amount, durability=10):
       self.length = length
       self.amount = amount
       self.durability = durability


   def picking(self, luck):
       if self.amount <= 0:
           print("No lockpicks left!")
           return False
       if self.durability <= 0:
           print("The lockpick is broken.")
           return False


       luck = max(0, min(10, luck))
       base_chance = 0.3
       max_bonus = 0.6


       while self.amount > 0 and self.durability > 0:
           capped_luck = min(luck, 10)
           success_chance = base_chance + (capped_luck / 10) * max_bonus
           print(f"Trying to pick the lock with {success_chance*100:.0f}% chance...")


           if random.random() < success_chance:
               print("Success! You picked the lock.\n")
               self.durability -= 1
               self.amount = 0
               return True
           else:
               print("Failed to pick the lock.")
               self.durability -= 1
               self.amount -= 1
               luck += 1
               time.sleep(1)


       print("All lockpicks are used up or broken.")
       exit()
       return False

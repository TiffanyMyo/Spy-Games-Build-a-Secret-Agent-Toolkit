import random


class Spy:
   def __init__(self, sound): #speed
       self.sound = max(0, min(10, sound))
       # self.speed = max(0, min(10, speed))


   # def attempt_lockpick(self, lockpick):
   #     print(f"{self.name} is attempting to pick a lock...")
   #     return lockpick.picking(self.luck)


   def sneak(self):
       base_detection_chance = 0.5
       reduction = (10 - self.sound) / 10 * 0.5
       detection_chance = base_detection_chance - reduction
       print(f"Chance of being detected: {detection_chance * 100:.0f}%")
       # for i in range(1,4):
       if base_detection_chance > detection_chance:
           print("Oops! You were heard.\nBetter luck next time!")
           exit()
       else:
           print("You progressed")
       print("And you made it through!")

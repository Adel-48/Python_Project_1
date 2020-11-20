# def final_boss_sequence(): Last function !!important!!

# Imports
import random
import time
from time import sleep

# Global Variables
hero_health = 100
boss_health = 300
boss_deffence = 15

# hero_attack = random.randint(1,9)
# boss_attack = random.randint(7,23)

# Game Funcation (do not edit without saving and leaving comments)
def final_boss_text(): 
    print("")
    time.sleep(2.0)
    print("Dungeon Keeper: Who dares wake me from my eternal slumber?")
    print("")
    time.sleep(2.3)
    print("Dungeon Keeper: You enter my domain and think you can just waltz out...!?")
    print("")
    time.sleep(2.4)
    print("Dungeon Keeper: You may have made it this far weakling, but you go no further!")
    print("")
    time.sleep(2.3)
    print("Dungeon Keeper: Prepare yourself...")
    print("")
    time.sleep(2.0)
    print("Dungeon Keeper: You...Die...Here!")
    print("")
    time.sleep(2.0)
    print("Dungeon Keeper: HA HA HA HA!!")
    print("")
    time.sleep(2.0)
    print("The Dungeon Keeper lunges at you clenching his 'Great Axe', you dodge and get ready to fight.")
    time.sleep(2.0)

def attack_animation():
          time.sleep(1.0)
          print(f"(╯°□°)> ┻━         ")
          time.sleep(1.0)
          print(f"(╯°□°）>   ┻━ ")

def attack_animation_boss():
     time.sleep(1.0)
     print("                          8=('-'Q)")
     time.sleep(1.0)
     print("                         8==('-'Q)")
     time.sleep(1.0)

def h_attack():
     global boss_health
     hero_damage_counter = 0
     print("")
     battle_Message1 = "You attack the Dungeon Keeper:"
     print(battle_Message1)
     print("")
     print(f"player HP: {hero_health}/100")
     for _ in range(3):
        attack_animation()
        dice_roll = random.randint(14,27)
        hero_damage_counter += dice_roll
        boss_health -= dice_roll
     print("")
     print(f"You did {hero_damage_counter} damage.")
     if boss_health <0:
          boss_health = 0

def h_health():
     global hero_health
     health_potion = random.randint(5,20)
     hero_health = hero_health + health_potion
     if hero_health in range (1,99):
          print("")
          print(f"You drank a Health Potion: +{health_potion}hp {hero_health}/100.")
          print("")
     elif hero_health >= 100:
          print("")
          print("You are already at full health...")
          print("")
     if hero_health > 100:
          hero_health = 100
     
def b_attack():
     global hero_health
     boss_damage_counter = 0
     print("")
     time.sleep(1.0)
     battle_Message2 = ("The Dungeon Keeper attacks you:")
     print(battle_Message2)
     print("")
     print(f"                                 Dungeon Keeper HP: {boss_health}/300")
     for _ in range(3):
        attack_animation_boss()
        dice_roll = random.randint(9,16)
        boss_damage_counter += dice_roll
        hero_health -= dice_roll
     print("")
     print(f"You took {boss_damage_counter} damage.")
     if   hero_health in range (50,90):
          print("")
          print("You took a hard hit!")
          time.sleep(0.7)
     elif hero_health in range(50,100):
          print("")
          print("You took Major damage!")
     elif hero_health in range(1,29):
          print("")
          print("You should heal up")
     
def b_deffence():
     global boss_deffence
     boss_deffence = boss_health + boss_deffence
     print(boss_deffence)

def attack_start():
     global hero_health
     global boss_health
     if hero_health < 1:
          hero_health = 100
     print("")
     attack = int(input("Press '1' to Attack:\nPress '2' to Heal: "))
     if attack == 1:
          h_attack()
          b_attack()
     elif attack == 2:
          h_health()
     else:
          ("Miss")

def game_start():
     # I moved global variables and if boss and heros statements to attackstart
     print("")
     start = input("                                                  Begin Battle?: ")
     if start == 'yes' or start == 'y' or start == "yeah":
          attack_start()
     else: 
          print("You ran away like a coward.")
          game_start()
          #add in return to start of game function call

def winning_screen(): 
    print("Dungeon Keeper: Ugghhh... how are you so strong!")
    time.sleep(2.0)
    print(" ")
    print("You stand over the Dungeon Keeper ready to deliver the final blow.")
    time.sleep(2.8)
    print(" ")
    print("Dungeon Keeper: Hurry up and get it over with. I have been on duty 3000 years too long. ")
    time.sleep(2.8)
    print("")
    print("You raise you sword and strike the Dungeon Keeper without hesitation.")
    time.sleep(2.8)
    print(" ")
    print("Dungeon Keeper: GUUURRRAAAAHHH!!!!!")
    time.sleep(2.8)
    print("")
    print("You watch as the Dungeon Keeper fades away while writhing in pain.")
    time.sleep(2.8)
    print("")
    print("You are faced with a giant door that opens slowly and lets in fresh air and light from the outside.")
    time.sleep(3)
    print("")
    print("Enjoy your freedom brave warrior.")

def credits():

    time.sleep(1.8)
    print("")
    print("                                  Created by: ")
    time.sleep(1.8)
    print(" ")
    print("                             **********Adel**********")
    time.sleep(1.8)
    print(" ")
    print("                              Speacial Thanks To: ")
    time.sleep(1.8)
    print(" ")
    print("                              Leon, Imran and Jay ")
    time.sleep(1.8)
    print(" ")
    print("                             Thank you for playing! ")
    time.sleep(1.8)
    print(" ")
    print("                           (╯°□°)> ┻━        8==('-'Q) ")

def game_over():
     global boss_health
     print("")
     print("                                                       You Died...")
     print("                                        You could not 'Escape The Dungeon Keeper'")
     print("")
     game_over = int(input("                                              Press '1' to play again: "))
     if game_over == 1:
          if boss_health < 300:
               boss_health = 300
          game_start()
     else:
          if boss_health < 300:
               boss_health = 0  
          print("")
          print("                                               Thank you for playing.")
                 

final_boss_text()    
game_start()
while boss_health > 0:
     attack_start()
     if boss_health <= 0:
          print("")
          print("")
          print("You have defeated the Dungeon Keeper!")
          print("")
          print("")
          print("")
          winning_screen()
          credits()
     elif hero_health <= 0:
          game_over()
   


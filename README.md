# Python_Project_1
This was my first python Project. I was tasked with creating a text RPG with two other team members. We each focused on a section of the game (start, middle and end) I created the last battle of a text RPG. I created the battle mechanics with Python 3.9 and got inspiration from the 'Chao Adventure' mini games form the Sega Dreamcast title Sonic Adventure.

I wanted to do something something with unicode emojis and adapted the ‘table flip emoji’ to make it look like it was holding a sword:

* (╯°□°）╯︵  ┻━┻ (original)

*  ( ╯°□°) > ┻━    (game version)

Planning:
I then had to think about the game mechanics and how to incorporate this into a small fun experience.
I then thought back to one of the most addictive mini games I have ever played “Chao Adventure” (see image). This was a small mini game that could be played on the Dreamcast VMU (virtual memory unit) that was a mix between a Tamagotchi and Rock Paper Scissors. One Chao would take a turn and either attack or miss. I went for a 3 stage process while planning the boss fight which also shows on the flowchart:

                     
 Boss introduction > Main Battle / Death/Restart > Win screen > Credits

Implementation:
I coded the final boss battle to be a similar experience with an option to attack or heal per turn. The attack is a ‘for loop’ that returns 3x random integers with a range between (7-24),  after each attack the boss will return the attack with the same mechanic but would be a higher range forcing the player to heal to win. 

The heal option is another random integer that will add a range of 5-20 to the players health points. This could be applied as many times as the player would like during a turn. The reason for this is pacing, due to the potential length of the battle forcing a player to use up a whole turn would end up making the fight boring. 

I imported the sleep library and used the ‘time.sleep()’ function to pace the strings to add a little character. I also used empty print statements ‘print(“”)’ as padding to space out the strings due to me not knowing how to pad strings yet. 

The battle will end if you die, giving you the option to either restart or quit, it will also end if you win by killing the ‘Dungeon Keeper’. By killing the boss you will trigger the last batch of strings that will give you the ending and will roll the credits. 

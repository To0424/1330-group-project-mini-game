# 1330-group-project-mini-game
1330 mindmap
Game Type：
Text_based action adventure game

Way to run the game: the game come in a python file. Simply download it and open the game file and play it. 

name: Zombie asylum

Story background:
You were wounded by a zombie, but fortunitaly you have a lot of food and you took shelter in a asylum. Yet, the asylum is not safe and you have to leave the asylum from the rooftop with at least a dose zombie serum to save yourself.
However, the asylum locked some of the doors to defend itself from the zombie horde. You have find clues in different rooms and floors to solve puzzles in order to excape. 


aim:
1. find the zombie serum 
2. find the password of the rooftop lock

character setting:
1. You have a health bar with a hundred hp, When you have 0 or less hp, You will die and the game is over. You cannot overheal either. 
2. You also have a pressure bar. When you have a hundred or more pressure point in your pressure bar. You will be forced to sleep and pass the day. 

Map:
1. The asylum consist of 4 floors. Each floor have 4 rooms and the last room will be locked. 
2. When you enter a room, you can choose to look left or right to trigger different events.
In short, each room have 2 or more events.

lock setting:
1. Every clues for the locked room on each floor can only be found on that specific floor(clue for F/1 locked room can only be found in F/1)
2. The lock in the rooftop is a 3 digits password lock, the clues for the password in scattered in the locked room in every floors.
3. F/1 locked room: 3, F/2 locked room: 4, F/3 locked room: the number order, the F/4 locked room: 2. the password is 423
4. everytime you enter the wrong password, you increase 20 point of pressure.
5. if the lock is unlocked but you still don't have a serum on you, the game continues.

general setting:
1. you can only explore the next level after you finish exploring the current floor(you have to completly explored floor 1 to unlock floor 2)
2. you can voluntarily end the day to reset your health(100) and pressure(0)
3. everytime you enter a room increase your pressure by 5.


floor 1:

Room 1 ：look left:
        you found a dose of sedative(reset pressure)  
        look right:
        random event: you found a locked chest.(need the key from room 3 to open it)
                           The chest have a clue about the lock in room 4(The clue is 4%^4%^1%^1)

Room 2 ：look left:
        1st exploration: You found a corpse. It has some bite marks on its neck, you realize there are zombies in here.(pressure+50) You found a broken knife in the corpse's hand.(block 1 attack).
             2nd exploration: You found a dose of sedative.
             3rd exploration: You found nothing.
               look right
         You wake up a inactive zombie and it attacks you. If you have the broken club, you can block the attack and leave the room with no injury. If not, you take 50 damage.
         There is a serum behind a zombie, but you have to kill the zombie to take it.(Acutally the player will not know there is a serum)(You can find a weapon in room 4 on floor 4)(serum+1)(Achievement: hidden serum)

Room 3 :  look left:     
        You found the key for the locked chest.
              look right:
        you found a medkit

Room 4（locked）look left               
                1.NPC: Michael
                        -->Mission: find his daughter

                      look right
                  You find a shard of the clue for the rooftop lock
                  you find the way to go to the second floor, and you feel scared of the second floor. (pressure+20)

floor 2

Room 1 ：look left:
        You find torch(active effect: avoid a attack)
        look right:
        You find a dose of sedative behind a corpse. (sedative+1, pressure+10)

Room 2 :  look left:
         You find an inactive zombie, since you don't want to disturb it. You left the room quietly.(pressure+10)(Serum+1 if you kill it)  
                look right:
         You found 1 iron shard and 1 contaminated bandages.(used for crafting but not on yourself)

Room 3 ：look left
        You find a crafting machine but it need power to activate.(You can use the torch batteries for power, but you will lose the torch)(it can craft a lockpicker)
         craft lockpicker by hand: you got hurt by the iron shard(hp-30)
                    look right:
                     You find a painkiller (hp+30, you immediately use it)

Room 4（unlocked by lockpicker)：look left:
                     		   You find a letter: The clue provided by the last room on each floor is the key to opening the roof door.
                    		   look right:
                                         There is a bloody "3" on the wall. You feel scared(pressure+20)


floor 3

As soon as you walk up the third floor, you hear the howling of a zombie horde.(pressure+10, you will only feel pressured if you come here for the first time)

Room 1 ：look left:
        You find a note about the storage of the zombie serum on a doctor's desk.
        look right:
        You read about the zombie behaviour pattern(attack people with a high heart rate due to pressure and stress) from a security's manuscript. 

Room 2 ：look left:
        You find a sleeping zombie(it will attack you if you have over 80 pressure point)
        look right:
        You find a sleeping zombie(it will attack you if you have over 80 pressure point)

Room 3 ：look left:
        You found a zombie tied up on a bed(it can be saved by injecting serum, achievement: Good guy)
        look right:
        You found nothing, but you saw a zombie running toward 4th floor.(pressure+20)

Room 4（Hideout)：look left:
                   You find michael's daughter, she is holding a piece of paper.      choice 1.use sedative(sedative-1, clue+1)
                                                                                     choice 2.leave her alone(achievement: cold blooded)
                                                                                              
                  look right:
                   You  get a medkit 
                                    

floor 4

Room 1（sugery room）：look left: 
                                     You get a medical kit
                          look right：
                                     zombie attack

Room 2 ： look left:
         you found some neurotoxin on a guard's corpse(neurotoxin+3)
         look right：
               you found a speacial key on another body

Room 3 ：look left：You found a  neurotoxin(neurotoxin+1)
        look right：
              You find a inactive zombie(it will attack you if you have over 80 pressure point)

Room 4（locked）：look left:
                                       You finally find 2 serums , You feel so relaxed (reset pressure = 0)
                                       
                                       look right :
                                       You got a sedative (sedative +1)
                                       You receive a script and you see that is a huge number '2' on it


floor 5: rooftop(enter password) (if you did not save Michael's daughter, you get an achievement: wandering in the dark)

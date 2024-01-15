import time
import random
playerhealth = 100
weapondmg = 5
allouttime = 0
healthposion = 10
playername = "null"
lastletter = "null"
attackdmg = random.randint(1,weapondmg)
shielddmg = random.randint(1,4)
ma = True
monsterhp = 100
def gamesetup():
    global playername
    print("Hello! Welcome to QuillStrike")
    print("You are in Quilland. A taribale monstor has attacked your vialge\nThe elder said that the mostonr is looking for the power gem\nand that he will do everything to find it. You are destend to destroy the mosntor\n")
    print("Type your name in:")
    playername = input("")
def monsterattack():
    global lastletter
    global playerhealth
    global ma
    global monsterdmg
    global attackdmg
    global shielddmg
    global monsterhp
    if ma == True:
        if playerhealth <= 0:
            print("You are dead. The land of Quillstike is destroed")
            ma = False
        else:
            print("It is time for the mostor to attack")
            monsterdmgrand = random.randint(1,100)
            monsterdmg = 5
            if lastletter == "D" or lastletter == "d":
                monsterdmg = monsterdmg - shielddmg
            if lastletter == "b" or lastletter == "B":
                monsterdmg = monsterdmg - 4
            if lastletter == "a" or lastletter == "A":
                monsterdmg = monsterdmg * 2
                print("It does", monsterdmg)
                playerhealth = playerhealth - monsterdmg
            elif monsterdmgrand <= 10:
                monsterdmg = monsterdmg * 1.5
                print("It does", monsterdmg)
                playerhealth = playerhealth - monsterdmg
            elif monsterdmgrand <= 50 and monsterdmgrand >= 55:
                monsterhp = monsterhp + 10
                print("The monster has a health posion and uses it. He has",  monsterhp)
            elif monsterdmgrand >= 90 and monsterdmgrand <=100 :
                monsterdmg = 0
                print("He missed!")
            else:
                playerhealth = playerhealth - monsterdmg
                print("It does", monsterdmg)

def monsterBattle(monsterName, dmg):
    quit = False
    global weapondmg
    global playerhealth
    global allouttime
    global healthposion
    global lastletter
    global ma
    global monsterhp
    global shielddmg
    attackdmgr = 0
    monsterdmg = random.randint(1,dmg)
    while ma == True:
        if monsterhp <= 0:
            ma = False
        attackdmg = random.randint(1,weapondmg)
        shielddmg = random.randint(1,4)
        print("Hello", playername)
        print("Your helth is ", playerhealth)
        print(allouttime, "more rounds before cou can use all out attack")
        print(healthposion, "more rounds until you can use the health posion")
        print("You are in battle with",monsterName,". The monster has", monsterhp," health. Will you...")
        print("[B]lock with shield(if attacker attacks, may lessen an amount of damage from the attacker)")
        print("[A]ll out attack(will do massive damage but leaves you exhausted. Being exhasted means if attacker attacks, they do 1.5 times more damage.)")
        print("[R]egular attack")
        print("[D]efence and counter(will do significantly less damage but enemy damage is also reduced.)")
        print("[U]se health potion")
        print("[E]xit the game")
        battle_do = input()
        if battle_do == "A" or battle_do == "a":
            if allouttime <= 0:
                print("You go on an all out attack")
                time.sleep(0.5)
                miss = random.randint(1,10)
                monsterdmg = monsterdmg * 2
                allouttime = 15
                if miss == 5:
                    print("You race after ",monsterName," and slice, cut, and go all fury at you but you missed!")
                else:
                    attackdmgr = (attackdmg * 3)
                    monsterhp = monsterhp - attackdmgr
                    print("You cut, slice, and turn into a tornado of death. You do ",attackdmgr, " at the monster." )
            else:
                print("Sorry, you canot do more allout attacks until", allouttime ,"rounds")
        elif battle_do == "B" or battle_do == "b":
            print("Ok, you rase your sheild to block 4 damage")
        elif battle_do == "D" or battle_do == "d":
            miss = random.randint(1,10)
            if miss <= 4:
                attackdmgr = attackdmg * 0.5
            print("Ok, you do", attackdmg, "at the", monsterName, "and you block", shielddmg)
        elif battle_do == "R" or battle_do =="r":
            miss = random.randint(1,1000)
            if miss <= 100:
                print("You do a regualr attack")
                print("But You miss")
            else:
                attackdmgr = attackdmg * 1.5
                print("You do a regualr attack")
                print("You use your sowrd to slice him, and do ", attackdmgr, "damage")
                monsterhp = monsterhp - attackdmgr
        elif battle_do == "U" or battle_do == "u":
            if healthposion == 0:
                playerhealth  = playerhealth + 20
                print("you drink the health poision and gain 20 health")
                healthposion = 11
            else:
                print("sorry, wait ", healthposion, "more rounds to have the health posion")
        elif battle_do == "E" or battle_do == "e":
            quit = True
            ma = False

#        elif battle_do == ""
        if ma == True:
            if allouttime > 0:
                allouttime = allouttime - 1
            if healthposion > 0:
                healthposion = healthposion - 1
            time.sleep(1)
            monsterattack()

        if quit == True:
            print("Ok, thanks for playing")
            ma = False
        if playerhealth <= 0:
            print("You are dead, and Quilland is deatroyed, thanks to you.")
            ma = False
        elif monsterhp <= 0 and playerhealth >= 0:
            print("Congratulations! You win, and here is one bitcoin. Get one from here: Q2k7jL4uY9eT8ZfV6n3m5H1aW0c")
            ma = False
gamesetup()
monsterBattle("goblin", 10)
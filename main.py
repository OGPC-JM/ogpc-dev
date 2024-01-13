import time
import random
import os
playerhealth = 100
weapondmg = 5
allouttime = 15

healthposion = 10
def monsterBattle(monsterName, dmg, monsterhp):
    global weapondmg
    global allouttime
    global healthposion
    ma = True
    while ma == True:
        if monsterhp <= 0:
            ma = False
        attackdmg = random.randint(1,weapondmg)
        monsterdmg = random.randint(1,dmg)
        shielddmg = random.randint(1,4)
        print("You are in battle with",monsterName,". The monster has", monsterhp," health. Will you...")
        print("[B]lock with shield(if attacker attacks, may lessen an amount of damage from the attacker)")
        print("[A]ll out attack(will do massive damage but leaves you exhausted. Being exhasted means if attacker attacks, they do 1.5 times more damage.)")
        print("[R]egular attack")
        print("[D]efence and counter(will do significantly less damage but enemy damage is also reduced.)")
        print("[U]se health potion")
        battle_do = input()
        if battle_do == "A" or battle_do == "a":
            if allouttime <= 0:
                print("You go on an all out attack")
                time.sleep(0.5)
                miss = random.randint(1,10)
                monsterdmg = monsterdmg * 1.5
                if miss <= 5:
                    print("You race after ",monsterName," and slice, cut, and go all fury at you but you missed!")
            else:
                attackdmgr = (attackdmg * 1.2)
                monsterhp = monsterhp - attackdmgr
                print("You cut, slice, and turn into a tornado of death. You do ",attackdmgr, " at the monster." )
        elif battle_do == "R" or battle_do =="r":
            miss = random.randint(1,1000)
            if miss <= 200:
                print("You do a regualr attack")
                print("But You miss")
            else:
                weapondmg = weapondmg * 0.5
                print("You do a regualr attack")
                print("You use your sowrd to slice him, and do ", weapondmg)
        elif battle_do == "U" or battle_do == "u":
            if healthposion == 0:
                print("you drink the health poision and gain 5 health")
                healthposion = 11
            else:
                print("sorry, wait ", healthposion, "more rounds to have the health posion")
        
        if allouttime <= 0:
            allouttime = allouttime - 1
        if healthposion <= 0:
            healthposion - 1
        time.sleep(1)
#hello!
monsterBattle("goblin", 3, 50)
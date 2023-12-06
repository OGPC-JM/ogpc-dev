import time
import random
playerhealth = 100
weapondmg = 5
def monsterBattle(monsterName, dmg, monsterhp):
    ma = True
    while ma == True:
        if monsterhp <= "0":
            ma = False
        attackdmg = random.randint(1,weapondmg)
        monsterdmg = random.randint(1,dmg)
        shielddmg = random.randint(1,4)
        print("You are in battle with",monsterName,". The monster has", monsterhp," health. Will you...")
        print("[B]lock with shield(if attacker attacks, may minus an amount of damage from the attacker)")
        print("[A]ll out attack(will do massive damage but leaves you exhausted. Being exhasted means if attacker attacks, they do 1.5 times more damage.)")
        print("[R]egular attack")
        print("[D]efence and counter(will do significantly less damage but enemy damage is also reduced.)")
        print("[U]se health potion")
        battle_do = input()
        if battle_do == "A" or battle_do == "a":
            print("You go on an all out attack")
            time.sleep(0.5)
            miss = random.randint(1,10)
            if miss == "1":
                print("You race after ",monsterName," and slice, cut, and go all fury at you but you missed!")
            else:
                attackdmgr = (attackdmg * 1.2)
                monsterhp = monsterhp - attackdmgr
                print("You cut, slice, and turn into a tornado of death. You do ",attackdmgr, " at the monster." )
        time.sleep(1)

monsterBattle("goblin", 3, 50)


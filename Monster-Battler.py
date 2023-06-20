# This is the start of the monster battler game. 
import random

def monsterBattler():
    playerHealth = input("How much health should the player have?\n")
    monsterHealth = input("How much health should the monster have?\n")
    moveSet = input("Choose your moves! Type in four values, with | representing the gap between them.")
    gameOver = False
    heroVictory = False
    effective = "not very effective"
    random.seed()
    try:
        playerHealth = int(playerHealth)
        monsterHealth = int(monsterHealth)
        placeholder= moveSet.split("|")
        trueMoveSet = []
        for i in range(4):
            trueMoveSet.append(placeholder[i][0:15])
    except:
        print("Do a better job at following instructions, next time.")
        gameOver= True

    #Formatting the moves. 
    

    # combat loop
    while not gameOver: 
        print("Choose your move!".center(33,'*')+ "\n" + "*".center(33,'*'))
        moveUsed = input("Pick from 1-4")
        playerDamage = hash(trueMoveSet[moveUsed-1]) % 100;
        if playerDamage <33:
            effective = "not very effective."
        elif playerDamage <66:
            effective = "somewhat effective."
        else:
            effective = "very effective. Wow!"
        monsterHealth = monsterHealth - playerDamage
        print("You used {}, it was {}".format(trueMoveSet[moveUsed-1],effective))
        print("You dealt {} damage. The monster has {} health left.".format(str(playerDamage), str(monsterHealth)))
        if monsterHealth <= 0:
            gameOver = True;
            heroVictory = True; 
            break;
        print("Now, the monster attacks!")
        monsterDamage = random.randrange(20,40)
        print("It bites you for {} damage!".format(str(monsterDamage)))
        playerHealth = playerHealth - monsterDamage
        if playerHealth <=0:
            gameOver = True
            heroVictory = False
            break
    if heroVictory:
        print("Through grave danger, you have triumphed, and rid the world of the horrible monster!")
    if not heroVictory:
        print("Unfortunately, the monster has won! Try again next time!")
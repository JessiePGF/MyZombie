import zombiedice
import random
import copy

class MyZombie:  # stop when 2 shotgun appears
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResult = zombiedice.roll()
        shotguns = 0
        while diceRollResult is not None:
            shotguns += diceRollResult['shotgun']

            if shotguns < 2 :
                diceRollResult = zombiedice.roll()
            else:
                break


class MyZombieq:  # monte zombie
    def  __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceColors = ['green']*6 + ['yellow']*4 + ['red']*3
        diceProb = {'green': 1/6, 'yellow': 2/6, 'red': 3/6}
        shotgunq = 0
        while True:
            diceRollResultq = zombiedice.roll()
            if diceRollResultq is None:
                break
            shotgunq += diceRollResultq['shotgun']

            if shotgunq == 2:  # Stop when 2 shotguns appear
                return
            
            elif shotgunq == 1:  # If there's only 1 shotgun, simulate 100 times. If the probability of getting more than 2 shotguns >= 0.25, stop.
                dicerolled = diceRollResultq['rolls']
                diceLeft = copy.deepcopy(diceColors)
                for d in dicerolled:
                    if d in diceLeft:
                        diceLeft.remove(d)

                if len(diceLeft) < 3:
                    continue

                simuShotgun1000 = 0
                for q in range(1000):
                    randomList = []
                    simuShotgun = 0
                    for r in range(3):
                        w = random.choice(diceLeft)
                        randomList.append(w)
                        if random.random() < diceProb[randomList[r]]:
                            simuShotgun += 1
                    simuShotgun1000 += simuShotgun       

                if (simuShotgun1000/1000) >= 0.45:
                    return

            else:  # If there's no shotgun, just keep rolling.
                continue


zombies = (MyZombie(name = 'Shotgun Zombie'),
           MyZombieq(name = 'Monte Zombie'))

zombiedice.runWebGui(zombies=zombies, numGames=1000)

from Zombie import Zombie
from Ogre import Ogre
from Enemy import Enemy

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)



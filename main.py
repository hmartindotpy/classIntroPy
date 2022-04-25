import random
class Move:

    distance = 0
    def walk(self):
        self.distance+=1

    def run(self):
        self.distance+=5
    
    def sprint(self):
        self.distance+=10

    def status(self):
        print(self.distance)

class EnemyEncounter:
    def halfdistance(self):
        r = random.randrange(2)
        if r ==0:
            return True
        else:
            return False
#access the move class
m = Move()
encounter = EnemyEncounter()
done = False
while True:
    action = input("1. Walk\n2. Run\n3. Sprint\n4. Status Check\n5. Quit\nchoice: ")
    chance = random.randrange(1,101)
    
    if action=="4":
        m.status()
        print("Distance: " + m.distance)
    if action=="5":
        break

    if encounter.halfdistance()==True:
        m.distance/=2
        print("you got attacked by vultures and your distance is now half")
    else:
        if action =="1":
            m.walk()
        elif action=="2":
            m.run()
        elif action=="3":
            m.sprint()
#create second class called enemyencounter,
#you have a 50% of an enemy attack which reduces your distance by half
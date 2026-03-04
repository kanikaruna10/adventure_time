
name = input("What is your name? ")
print("Welcome, ", name)

class Character:
    def __init__(self, name, health):
            self.name = name
            self.health = health
            self.inventory = []
    def show_status(self):
            print(f"{self.name}")
            print(f"Health: {self.health}%")
            print(f"Inventory: {self.inventory}") 
    def add_items(self, item):
            self.inventory.append(item)   
            print(f"**{item} wasadded to inventory**")
    def attack(self, other):
            damage = 20
            other.health -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage!")


def combat(player, dragon):
      while player.health > 0 and dragon.health > 0: 
            action = input("Do you Attack or ruunn?").lower().strip()    

            if action == "attack":
                player.attack(dragon)
            elif action == "run":
                  print("You Got away")
                  start()
            else:
                  print("Dont just stand there, do something!")
                  combat()          
                


                              
def intro():
    player = Character(name, 100)
    dragon = Character("Dragon", 75)
    print(f"Welcome to the Awesome Adventure Game!, {player.name}") 
    print("You wake up in a cold and dark room")
    print(f"You feel rested and your health is {player.health}%")
    print(f"You check your pockets and inventory is empty {player.inventory}")
    print(f"You look around and see your sword sheild")
    player.add_items("Sword")
    player.add_items("Shield")
    print("There is a door on your LEFT and RIGHT")
    

intro()

def start():

    choice = input("Which direction do you go?(Left/right)").lower().strip()

    # rooms to explore
    # Treasure room
    def treasure_room():
            print("You found the treasure! You win!")
    # Monster room
    def monster_room():
                print("A wild dragon appears")
                print("Rawwwwr!")
                print("It looks angry")
                action = input("Are you going to FIGHT or RUN?").lower().strip()

                if action == "fight":
                      combat()
                      print("The dragon burnt your butt - you lose!")
                elif action == "run":
                      print("You escaped safely")
                      print("You are back in the main room")
                      start()
                else:
                      print("You just got it, You lose")            

    if choice == "left":
        treasure_room()
        print("You went left")
    elif choice == "right":
        monster_room()
        print("You went right")   
    else:
        print("You stand still and ponder what to do next")
        start()
        
while True:
      
      start()
      again = input("Do you want to play again? (yes/no)").lower().strip()
      intro()
      if again != "yes":
            print("Thanks for playing! yall come back now ya hear!")
            break


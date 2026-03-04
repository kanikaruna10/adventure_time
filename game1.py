name = input("What is your name? ")

class Character:
    def __init__(self, name, health):
          self.name = name
          self.health = health
          self.inventory = []

    def show_stats(self):
         print(f"{self.name}")
         print(f"Health:", {self.health})
         print(f"inventory:", {self.inventory})

    def add_item(self, item):
         self.inventory.append(item)
         print(f"**{item} was added to your inventory**")

    def attack(self, other):
         damage = 20
         other.health -= damage
         print(f"{self.name} attacks {other.name} for {damage} damage!")


player = Character(name, 100)
dragon = Character("Dragon", 75)

def intro():
    print(f"Welcome to the Awesome Adventure Game, {player.name}")
    print("You wake up in a cold and dark room")
    print(f"You feel rested and your health is at {player.health}%")
    print(f"You check your pockets and your inventory is empty! {player.inventory}")
    print(f"You look around and see your sword and shield")
    player.add_item("Sword")
    player.add_item("Shield")
    print("There is a door on your LEFT and RIGHT")

    # player.show_stats()
    # dragon.show_stats()

    

intro()

def start():
    def combat(player, dragon):
     while player.health > 0 and dragon.health > 0:
        action = input("Do you ATTACK or RUN? ").strip().lower()

        if action == "attack":
            player.attack(dragon)
            # what happens after attack
            if dragon.health > 0:
                 print(f"Dragon's health is {dragon.health}")
                 dragon.attack(player)
                 print(f"Your health is {player.health}")
        elif action == "run":
            print("You got away!")
            start()
        else: 
            print("Dont just stand there, do something!")
            combat()
    
    choice = input("Which direction do you go? (Left/Right)").lower().strip()

    # rooms to explore
    # Treasure Room
    def treasure_room():
            print("You found the treaure! You Win!")
    # Monster Room
    def monster_room():
            print("A wild dragon appears")
            print("RAWWWWWR!")
            print("It looks angry...")
            action = input("Are you going to FIGHT or RUN?").lower().strip()

            if action == "fight":
                 combat(player, dragon)
            elif action == "run":
                 print("You escaped safely!")
                 print("You are back in the main room")
                 start()
            else:
                 print("You just got ate! You lose!")

    if choice == "left":
        treasure_room()
    elif choice == "right":
        monster_room()
    else:
        print("You stand still and ponder what to do next")
        start()

while True:
    start()
    again = input("Play again? (yes/no): ").lower().strip()
    intro()
    if again != "yes":
         print("Thanks for playing! Yall come back now ya hear?")
         break
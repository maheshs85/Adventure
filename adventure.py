import sys
import json

class GameEngine:
    def __init__(self, map_file):
        self.load_map(map_file)
        self.player_position = 0
        self.inventory = []

    def load_map(self, map_file):
        with open(map_file, 'r') as f:
            self.game_map = json.loads(f.read())

    def get_current_room(self):
        return self.game_map[self.player_position]

    def print_current_room(self):
        room = self.get_current_room()
        print(f"> {room['name']}\n")
        print(f"{room['desc']}\n")
        if 'items' in room:
            print("Items: ", " ".join(room['items']), "\n")
        print("Exits:", " ".join(room['exits']))
        
    def print_inventory(self):
        print("Inventory:")
        print(" ".join(self.inventory))

    def handle_input(self, user_input):
        user_input = user_input.lower()
        if user_input == 'quit':
            print("Goodbye!")
            return False
        elif user_input == 'look':
            self.print_current_room()
        elif user_input == 'inventory':
            self.print_inventory()
        elif user_input == 'go' or user_input.startswith('go '):
            try:
                direction = user_input.split(' ', 1)[1]
                self.go(direction)
            except IndexError:
                print("Sorry, you need to 'go' somewhere.")
        elif user_input == 'get' or user_input.startswith('get '):
            try: 
                item = user_input.split(' ', 1)[1]
                self.get(item)
            except IndexError:
                print("Sorry, you need to 'get' something.")
        return True       

    def go(self, direction):
        room = self.get_current_room()
        if direction in room['exits']:
            next_room_id = room['exits'][direction]
            self.player_position = next_room_id
            print(f"You go {direction}.\n")
            self.print_current_room()
        else:
            print(f"There's no way to go {direction}.")
        return True

    def get(self, item):
        room = self.get_current_room()
        if 'items' in room and item in room['items']:
            room['items'].remove(item)
            self.inventory.append(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} anywhere.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    map_filename = sys.argv[1]
    engine = GameEngine(map_filename)
    engine.print_current_room()
    
    while True:
        try:
            user_input = input("What would you like to do? ")
            if not engine.handle_input(user_input):
                break
        except EOFError:
            print("\nUse 'quit' to exit.")
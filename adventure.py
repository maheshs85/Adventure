import sys
import json

class GameEngine:
    def __init__(self, map_file):
        self._load_map(map_file)
        self.player_position = 0
        self.inv = []

    def _load_map(self, map_file):
        with open(map_file, 'r') as f:
            self.game_map = json.loads(f.read())

    def _get_current_room(self):
        return self.game_map[self.player_position]

    def look(self):
        room = self._get_current_room()
        print(f"> {room['name']}\n")
        print(f"{room['desc']}\n")
        if 'items' in room and room['items'] != []:
            str = "Items: " + ", ".join(room['items']).strip() + "\n"
            print(str)
        
        str = "Exits: " + " ".join(room['exits']).strip() + "\n"
        print(str)
        
    def inventory(self):
        if self.inv == []:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in self.inv:
                print(f'  {item}')

    def _handle_input(self, user_input):
        user_input = user_input.strip().lower()

        if user_input == 'quit':
            print("Goodbye!")
            return False
        elif user_input == 'help':
            self.help()
        elif user_input == 'look':
            self.look()
        elif user_input == 'inventory':
            self.inventory()
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
        elif user_input == 'drop' or user_input.startswith('drop '):
            try: 
                item = user_input.split(' ', 1)[1]
                self.drop(item)
            except IndexError:
                print("Sorry, you need to 'drop' something.")
        else:
            print("Invalid command.")
        return True       

    def go(self, direction):
        room = self._get_current_room()
        if direction in room['exits']:
            next_room_id = room['exits'][direction]
            if not self._is_door_locked(next_room_id):
                self.player_position = next_room_id
                print(f"You go {direction}.\n")
                self.look()
            else:
                print("The door is locked. You need a key to unlock it.")
        else:
            print(f"There's no way to go {direction}.")
        return True

    def get(self, item):
        room = self._get_current_room()
        if 'items' in room and item in room['items']:
            room['items'].remove(item)
            self.inv.append(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} anywhere.")

    def _is_door_locked(self, room_id):
        return 'locked' in self.game_map[room_id] and 'key' not in self.inv

    def drop(self, item):
        room = self._get_current_room()
        if item in self.inv:
            if 'items' not in room:
                room['items'] = []
            room['items'].append(item)
            self.inv.remove(item)
            print(f"You drop the {item}.")
        else:
            print(f"There's no {item} in your inventory.")

    def help(self):
        print("\nYou can run the following commands:")
        for method in dir(self):
            if callable(getattr(self, method)) and not method.startswith("_"):
                print(f"  {method} {'...' if getattr(self, method).__code__.co_argcount > 1 else ''}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    map_filename = sys.argv[1]
    engine = GameEngine(map_filename)
    engine.look()
    
    while True:
        try:
            user_input = input("What would you like to do? ")
            if not engine._handle_input(user_input):
                break
        except EOFError:
            print("\nUse 'quit' to exit.")
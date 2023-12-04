# Adventure Game Project

## Group Members
- Mahesh Swaminathan (mswamina@stevens.edu)

## GitHub Repository
[Link to GitHub Repository](https://github.com/maheshs85/Adventure)

## Project Hours Estimate
I estimate that I spent approximately 15 hours on this project.

## Testing
I tested my code using mainly manual testing. I played through different scenarios to ensure the game responds correctly to user input. I used the examples given in Canvas to test the base functionality as well as extensions.

## Bugs or Issues
All of the bugs / issues that I could find were resolved through manual testing.

## Difficult Issue
One issue I faced was implementing help and ensuring that the functions were being read dynamically instead of through a list and printing them. I used the dir function to go through all the functions and prefixed helper functions with a '_'. Then, it was simple to filter only verb functions which could be displayed in the help text.

## Extensions Implemented

### Locked Doors
Rooms in the map have a "locked" attribute, and the player needs to pick up a key item to unlock doors. The player only needs to have the key in the inventory.

### Help Verb
I added a dynamic help verb that displays the available commands based on the defined verbs in the game. The player can type "help" to see a list of valid commands.

Example:
- What would you like to do? help
- You can run the following commands:
  - go ...
  - get ...
  - look
  - inventory
  - quit
  - help
  - use ...

## Drop Verb
Drop lets you drop items in any room. It is implemented exactly as given in Canvas.

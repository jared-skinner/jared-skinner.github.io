import sys

#####################################
# START OF MAIN LOGIC... DO NOT ALTER
#####################################

def link(room_1, room_2):
    """
    Link to rooms together.  This gives us an easy way to connect rooms in our maze
    """
    room_1.add_direction(room_2)
    room_2.add_direction(room_1)

def message(text):
    """
    A nice way of displaying messages
    """
    print("")
    print(text)
    print("")

class Room:
    """
    The Room class gives us a template for creating rooms.  Each room has a name, a description,
    and an optional long_description.  Directions are added using the link function above.

    The main loop is in charge of using this information to run the dungeon
    """
    def __init__(self, name, description, long_description = "", final = False):
        self.name = name
        self.description = description
        self.long_description = long_description
        self.directions = {}
        self.final = final

    def add_direction(self, room):
        self.directions[room.name] = room

def main_loop(entrance):
    """
    This function is in charge of asking the player what they want to do next.  It uses a
    "while True" block to check what the player wanted to do last and then to prompt for the next
    action.
    """

    # these are the things a player can do
    actions = ["go", "look", "options", "directions", "help", "exit"]

    current_room = entrance

    action = None
    while True:
        if action == None:
            message(current_room.description)
        elif action == "":
            # do nothing
            pass
        elif action == "look":
            if current_room.long_description == "":
                message(current_room.description)
            else:
                message(current_room.long_description)
        elif action in ("options", "help"):
            message("the options are:")
            for option in actions:
                message(f"   * {option}")
        elif action == "exit":
            sys.exit()
        elif action == "directions":
            directions_message = "the directions are..."
            for direction in current_room.directions:
                directions_message += f"\n    * {direction}"

            message(directions_message)
        elif action.startswith("go "):
            location = action[3:]
            if location not in current_room.directions:
                message("you can't go there!")
            else:
                current_room = current_room.directions[location]
                message(current_room.description)

                if current_room.final:
                    sys.exit()
        else:
            message("THAT is not an option!")

        # get next action
        action = input("> ")

###################################
# END OF MAIN LOGIC... DO NOT ALTER
###################################


def example_dungeon():
    """
    This is a little example to give you an idea of how all the pieces are suppose to go together.
    """
    # create all the rooms
    entrance = Room(
        name = "entrance",
        description = "Welcome weary traveler to the cave of DOOM!!!",
        long_description = """
There's moss growing on the walls and crumbly stones everywhere.  The ground feels pretty solid,
but it looks like you are the first to come here in a very long time.  Step carefully...
        """
    )

    large_cavern = Room(
        name = "large cavern",
        description = "You find yourself in a large cavern",
        long_description = """
This room is so big there isn't even a echo.  It looks like it was man-made, but man... who made 
this place.  You notice that the floor is made of marbel tiles.  There are no columns in sight.
What's holding this place up!?
        """
    )

    small_cavern = Room(
        name = "small cavern",
        description = "You find yourself in a small cavern",
        long_description = """
Is this a cavern for ants?!  It needs to be at least... three times bigger.  Seriously though, this 
place is tiny!  Oddly it still feels cavernous.
        """
    )

    windy_passage = Room(
        name = "windy passage",
        description = "This looks to be the start of a windy passage",
        long_description = """
The walls are made of some smooth stone that you are not familiar with.  The passage goes on for a
long ways, twisting and turning.  Oddly this is the only passage which doesn't seem to be touched
by time.
        """
    )

    long_tunnel = Room(
        name = "long tunnel",
        description = "The entrance narrows to a tunnel that seems to stretch on forever",
        long_description = """
This tunnel descents deep into the earth.  The walls are cut rough of a green, blue stone.
        """
    )

    gift_shop = Room(
        name = "gift shop",
        description = "A gift shop in the cave of doom?!  Who woulda figured",
        long_description = """
It seems like everything in here is a nike product...

nike shoes, nike rope, nike bags of sand.  They tought of everything.  

The beach supplies are on discount!  Time to pick up a spare towel!
        """
    )

    treasure_room = Room(
        name = "treasure room",
        description = "You did it, you found the treasure room!  Congratulations, the quest was a success",
        long_description = """

        """, 
        final = True
    )

    # link the rooms together
    link(entrance, large_cavern)
    link(entrance, long_tunnel)

    link(long_tunnel, gift_shop)
    link(gift_shop, small_cavern)
    link(gift_shop, windy_passage)

    link(small_cavern, large_cavern)
    link(windy_passage, treasure_room)

    # run the dungeon!
    main_loop(entrance)

def my_dungeon():
    """
    This is where your code goes.

    The example dungeon is in a classic setting.  That doesn't mean yours has to be!  You could
    chose a haunted mansion, or St. Max, or the woods.  Let your imagination run wild!
    """
    # This is where your code goes.
    pass

# When you feel good about your dungeon, feel free to uncomment the second line of code
example_dungeon()
# my_dungeon()

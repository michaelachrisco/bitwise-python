# The Bear Game
print("Welcome!")
action = input("What would you like to do? ")
action_hash = dict()
action_hash = {"look": ("you see a bear. Its angry", 0),
               "looking": ("you see a bear. Its angry", 0),
               "stay": ("YOU GET EATEN! DEAD!!", -1),
               "run": ("You run forward", 1),
               "left": ("You go left", 0),
               "right": ("You go right", 0),
               "up": ("You go up", 0),
               "down": ("You cant go down", 0)
               }


def act(action):
    if action in action_hash:
        action_description, act_int = action_hash[action]
        print(action_description)
        if act_int == -1:
            return False
        if act_int == 1:
            return True
        if act_int == 0:
            action = input("What would you like to do? (try looking!) ")
            return act(action)
    else:
        print("You cannot do that. (try looking!).")
        action = input("What would you like to do? (try looking!) ")
        act(action)


game_bool = act(action)

if game_bool:
    print("You win!!")
else:
    print("You lose! Try again!")

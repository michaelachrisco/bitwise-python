# The Bear Game
print("Welcome!")
action_hash = dict()
action_state = 0
tries = 3
result_bool = False
action_hash = dict(look=("you see a bear. Its angry", 0), looking=("you see a bear. Its angry", 0),
                   stay=("YOU GET EATEN! DEAD!!", -1), run=("You run forward", 1), left=("You go left", 0),
                   right=("You go right", 0), up=("You go up", 0), down=("You cant go down", 0))
print("Welcome!")
action = input("What would you like to do? ")
while not result_bool and tries > 0:
    if action in action_hash:
        tries -= 1
        action_description, act_int = action_hash[action]
        print(action_description)

        if act_int != 0:
            result_bool = True
            action_state = act_int
    else:
        print("You cannot do that. (try looking!).")
        action = input("What would you like to do? (try looking!) ")

if action_state == 1:
    print("You win!!")
else:
    print("You lose! Try again!")
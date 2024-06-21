import turtle
import pandas as pd


    
    
state_df = pd.read_csv("50_states.csv")
state_raw_dict = state_df.to_dict()

# Sets are faster than lists when doing contains.
states_set = set(state_df["state"])
state_cor_dict = {}
# We want something like:
# my_dict = {
#     "Alabama": {"x": -37, "y": 256},
#     "New Mexico": {"x": -227, "y": 36},
# }
for i in range(50):
    state_val = state_raw_dict['state'][i]
    x_val = state_raw_dict['x'][i]
    y_val = state_raw_dict['y'][i]
    state_cor_dict[state_val] = {"x": x_val, "y": y_val}

ydoodle = turtle.Turtle()
ydoodle.up()
ydoodle.hideturtle()


def write_state(state_name):
    # Have the yankee doodle go to the coordinates.
    ydoodle.goto(state_cor_dict[state_name]["x"], state_cor_dict[state_name]["y"])
    # Have him write the state's name.
    ydoodle.write(state_name, align="center", font=("Arial", 12, "normal")) 

        # self.write(f"Game Over",align="center", font=("Arial", 40, "normal")) 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# Move the map down so you can see it under the text input box.
turtle.shape(image)

given_state = screen.textinput(title="Guess a state.", prompt="What is the name of a state?")
print(given_state)
correct_answers = []
# Check for cancel button with None.
while len(correct_answers) < 50 and given_state != None: 
    # Make it Title case before evaluating.
    given_state = given_state.title()
    if given_state in states_set and given_state not in correct_answers:
        # Write the state.
        write_state(given_state)
        # Add to correct answers.
        correct_answers.append(given_state)
    given_state = screen.textinput(title=f"{len(correct_answers)}/50 Guess a state. ", prompt="What is the name of a state?")

# If they left the game early, give a csv of states they did not guess to learn.csv.
if given_state == None:
    # Hooray, we're using list comprehension syntax cause it's awesome.
    to_learn = sorted([i for i in states_set if i not in correct_answers])
    learn_df = pd.DataFrame(data=to_learn, columns=["States"])
    learn_df.to_csv("learn.csv")
    
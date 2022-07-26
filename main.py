import pandas
from turtle import *

t = Turtle()
screen = Screen()
map_image = "map.gif"

screen.title("Guess the States Game - India")
screen.addshape(map_image)
t.shape(map_image)

# Finding coordinates of the states
# def get_mouse_click_cor(x,y):
#     print(x,y)

# screen.onscreenclick(get_mouse_click_cor)

def write_name_on_map(useranswer, xcor,ycor):
    '''Takes in user answer and writes in its xcor and ycor '''
    pen = Turtle()  #Writing turtle
    pen.color('green')
    pen.penup()
    pen.hideturtle()
    pen.goto(int(xcor),int(ycor))
    pen.write(useranswer)


data = pandas.read_csv("data.csv")
state_names = data['State'].to_list()

guessed_states = []
while len(guessed_states) < 29:
    user_answers =  screen.textinput(title=f'Guess The States {len(guessed_states)}/29 ', prompt="Enter the name of a state").title()
    new_row = data[data['State'] == user_answers]
    new_x = new_row.x #x and y cor of the user answer
    new_y = new_row.y
   
    if user_answers == 'Exit':
        break
    elif user_answers in guessed_states:
        print("already Guessed")
    elif user_answers in state_names:
        guessed_states.append(user_answers)
        write_name_on_map(useranswer= user_answers, xcor= new_x, ycor= new_y)
        

#Create dataframe csv for non guessed states
not_guessed_states = []
for state in state_names:
    if state not in guessed_states:
        not_guessed_states.append(state)

df = pandas.DataFrame(not_guessed_states)
df.to_csv('notguessed.csv')





screen.mainloop()

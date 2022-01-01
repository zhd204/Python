import turtle

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.register_shape(image)
screen.setup(width=725, height=491)
turtle.shape(image)
screen.title("U.S. States Game")


# Refer to https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
# Coordinates are pre-determined and loaded in the csv file.
def get_mouse_click_coords(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coords)

turtle.mainloop()

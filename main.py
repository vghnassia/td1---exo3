def on_button_pressed_a():
    global nb
    nb += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

nb = 1
while True:
    basic.show_number(nb)
    if nb > 10:
        nb = 10

def on_forever():
    pass
basic.forever(on_forever)

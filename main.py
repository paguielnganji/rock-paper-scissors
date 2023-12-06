Hand = 0

def on_gesture_shake():
    global Hand
    Hand = randint(1, 3)
    if Hand == 1:
        basic.show_icon(IconNames.HEART)
    elif Hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

let Hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Hand = randint(1, 3)
    if (Hand == 1) {
        basic.showIcon(IconNames.Heart)
    } else if (Hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    
})

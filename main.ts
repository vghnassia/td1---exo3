input.onButtonPressed(Button.A, function () {
    nb += 1
})
let nb = 1
while (true) {
    basic.showNumber(nb)
    if (nb > 10) {
        nb = 10
    }
}
basic.forever(function () {
	
})

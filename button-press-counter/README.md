## Button Press Counter
Output how many times the button has been pressed (it won't increment perfectly - [learn why below](#button-bouncing)!)

## Supplies
- Microcontroller
- Push Button

## Wiring Diagram
![push_button_sketch](https://github.com/modern-maker/starter-kit/assets/8736328/fd3ea7ea-c436-4ca7-9885-303af5350c63)

### Instructions
1. Make sure your microcontroller is connected to your computer and selected in Thonny (per the [getting started guide](https://github.com/modern-maker))
2. In Thonny create a new file
3. Copy/paste the contents of [`main.py`](main.py) into the new file
4. Press the run icon in Thonny

### Run Script Automatically
Blink the LED whenever the microcontroller is powered on
1. In Thonny, with the file containing your script selected, click the save icon
2. Select "MicroPython device" in the pop-up screen
3. In the "File name" field enter `main.py` and click "OK"

## Next Project
- [Button Press Debounce](https://github.com/modern-maker/starter-kit/tree/intermediate/button-press-debounce)

### Button Bouncing
Button bouncing occurs when a button (or switch) is transitioning between the open and closed state. During this transition electrons are able to jump the gap because the connection is so close which, to a computer, translates to multiple button presses.
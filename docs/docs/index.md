# EasyTkinter
EasyTkinter is a simple and easy to use wrapper for the tkinter gui module.
It is in its early stages, but already it vastly simplifies basic programs.

Use it like so:
```python
import gui
window = gui.Window("Hello")
btn = window.add_button("Click Me")
gui.on("btnPress", btn, lambda: print("Button Pressed."))
#If you don't know what lambda is, it just returns an anonymous, single expression function.
window.start()
```

And you're done!

## Installation
Simple run ```pip install easytkinter``` to install the module.

## Documentation
Here it is:

#### Class `gui.Window(title, layout="pack", master=None)`
Set title to the title of your window.
Set layout to grid to use a grid layout method(placer isn't supported yet.)
If you want to be complicated, use master.

This creates a new window instance, which is like the app and the frame in tkinter(if you care).

##### `Window.add_button(label, layout={}, ...)`
This adds a new button to the window, with the set label.
It returns the tkinter button instance, which you can fiddle with.

Any placing rules you want to add(like row and column) should be put in the layout dict(`{row=4,col=2}`) and any extra args for the button can be given straight to the function(`fg='blue'`).

##### `Window.add_textbox(layout={}, ...)`
This adds a new textbox to the window(something the user can type in.)
It returns the tkinter entry instance.

As always, placing rules in layout, and arguments about the box straight into the function(`text="Prefilled text"`).

##### `Window.add_widget(widget, layout={})`
Adds the given widget to the window. Must be a valid instance of a tkinter derived widget. Layout rules go in the corresponding variable.


##### `Window.start()`
Starts the mainloop. Should be last call in program.


##### `Window.stop()`
Stops the program from running. **Beware - This does not work in IDLE.**


#### Function `gui.on(event, widget, function)`
Binds an event to the specified handler(function).
Valid events are:
+ btnPressbob
+ clickbob
* dblClick - When a widget is double clicked(clicked twice in succession).
* rightClick - When a widget is right clicked.
* hover - When the mouse 'hovers' over a widget.
* hoveroff - When the mouse no longer hovers over a widget.
* keyPressEnter - When the enter key is pressed on a widget.
* keyPress *[letter or number]* - When the specified key is pressed on a widget.

These **must** be a string.


The widget can be a widget returned from `add_button()` or `add_textbox()`.

The function, must be uncalled - e.g. if the function is called hello, you pass `hello` to gui.on() **not** `hello()`.

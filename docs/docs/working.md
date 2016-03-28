# How EasyTkinter Works


## 1. The Window Object
The window class derives from tk.Frame. When the object is initialised, it inits the Frame with the title. It then sets self.method to your layout method(string).
### Adding widgets
- Creates the widget, with the specified args(kwargs).
- Then passes the widget and the layout options to window._place() which uses the appriate layout method to add it to the Frame.
- It adds the widget to window.widgets(a list)
- Finally it returns the widget.

---

## 2. Setting Events
The gui.on() method has a dictionary that translates EasyTkinter's events to tkinter's methods.
- The btnPress event is not in the dict, instead it sets the "command" value of the widget.
- If the event you supply is not an EasyTkinter event, it tries to set it to a tkinter event.
- The on() method uses widget.bind() to bind the events.


---

And that is all you need to know.

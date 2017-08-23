"""The widget 'interface' for subclassing"""

class Widget:
    """The widget class, to be subclassed."""
    def __init__(self, **kwargs):
        self.options = kwargs
        self.widget = None
    def render(self, master):
        """Create the actual tkinter widget(called by parent)"""
        pass
    def on(self, event, handler):
        """Setup an event handler on the widget."""
        pass

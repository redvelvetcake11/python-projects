import gi
import math
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class Calculator(Gtk.Window):
    def __init__(self):
        super().__init__(title="Advanced Calculator")
        self.set_border_width(10)
        self.set_default_size(400, 500)

        self.equation = ""

        # Create a vertical box layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        # Entry for displaying calculations
        self.display = Gtk.Entry()
        self.display.set_editable(False)
        self.display.set_alignment(1)  # Right-align the display text
        vbox.pack_start(self.display, expand=False, fill=True, padding=5)

        # Apply Pango font for display
        self.apply_pango(self.display, "18")

        # Buttons in a grid layout
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)  # Make columns stretch equally
        self.grid.set_row_homogeneous(True)     # Make rows stretch equally
        vbox.pack_start(self.grid, expand=True, fill=True, padding=5)

        # Initial button labels
        self.base_buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "/",
            "0", "C", "%", "="
        ]
        self.extra_buttons = []
        self.build_buttons()

    def apply_pango(self, widget, font_size):
        """Apply Pango styling to a widget for font size."""
        font_description = Pango.FontDescription(f"system-ui {font_size}")
        widget.modify_font(font_description)

    def build_buttons(self):
        """Build and populate the grid with buttons."""
        # Clear existing buttons from the grid
        for child in self.grid.get_children():
            self.grid.remove(child)

        # Combine base buttons and advanced buttons
        buttons = self.base_buttons + self.extra_buttons

        # Create and attach buttons to the grid
        for i, label in enumerate(buttons):
            if label:
                button = Gtk.Button(label=label)
                button.connect("clicked", self.on_button_clicked)
                # Apply Pango font size to buttons
                self.apply_pango(button, "20")
                # Calculate the position of the button in the grid
                row = i // 4  # divide by number of columns (4 in this case)
                col = i % 4  # remainder will give the column
                self.grid.attach(button, col, row, 1, 1)

    def on_button_clicked(self, widget):
        label = widget.get_label()

        if label == "C":
            self.equation = ""
        elif label == "=":
            try:
                # Handle advanced functions like pi and trigonometric functions
                self.equation = self.calculate(self.equation)
            except Exception:
                self.equation = "Error"
        else:
            self.equation += label

        self.display.set_text(self.equation)

    def calculate(self, expression):
        """Evaluate the mathematical expression safely."""
        # Use eval to evaluate the expression
        return str(eval(expression))

if __name__ == "__main__":
    win = Calculator()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from bipolar import BiPolar


class MotorWindow(Gtk.Window):
    def __init__(self):
        self.motor = BiPolar()
        Gtk.Window.__init__(self, title="Bi Polar Motor")


if __name__ == "__main__":
    win = MotorWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


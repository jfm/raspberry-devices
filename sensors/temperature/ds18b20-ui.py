import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ds18b20 import Sensor


class SensorWindow(Gtk.Window):
    def __init__(self):
        self.sensor = Sensor()
        Gtk.Window.__init__(self, title="DS18B20 Temperature Sensor")

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        self.spinbutton.connect("value-changed", self.on_value_changed)
        hbox.pack_start(self.spinbutton, False, False, 0)

    def on_value_changed(self, widget):
        self.sensor.set_temperature(self.spinbutton.get_value())


if __name__ == "__main__":
    win = SensorWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

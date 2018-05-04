import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ds18b20 import Sensor


class SensorWindow(Gtk.Window):
    def __init__(self):
        self.sensor = Sensor()
        Gtk.Window.__init__(self, title="DS18B20 Temperature Sensor")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        device_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=5
        )
        device_label = Gtk.Label("Device")
        device_hbox.add(device_label)
        self.device_entry = Gtk.Entry()
        self.device_entry.set_text("/tmp/ds18b20")
        device_hbox.add(self.device_entry)

        temp_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        temp_label = Gtk.Label("Temperature")
        temp_hbox.add(temp_label)
        adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        self.spinbutton.connect("value-changed", self.on_value_changed)
        temp_hbox.add(self.spinbutton)

        vbox.add(device_hbox)
        vbox.add(temp_hbox)

    def on_value_changed(self, widget):
        self.sensor.set_temperature(
            self.device_entry.get_text(),
            self.spinbutton.get_value()
        )


if __name__ == "__main__":
    win = SensorWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

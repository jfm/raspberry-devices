import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib
from uln2003 import ULN2003
import os
import threading
import socket
import json
import time
import datetime


class MotorWindow(Gtk.Window):
    def __init__(self):
        self.motor = ULN2003('/tmp/uln2003')
        Gtk.Window.__init__(self, title="ULN2003 BiPolar Motor")

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(hbox)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        hbox.add(vbox)

        in1_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=5
        )
        in1_label = Gtk.Label("IN1")
        in1_hbox.add(in1_label)
        self.in1_switch = Gtk.Switch()
        self.in1_switch.set_active(False)
        in1_hbox.add(self.in1_switch)
        vbox.add(in1_hbox)

        in2_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=5
        )
        in2_label = Gtk.Label("IN2")
        in2_hbox.add(in2_label)
        self.in2_switch = Gtk.Switch()
        self.in2_switch.set_active(False)
        in2_hbox.add(self.in2_switch)
        vbox.add(in2_hbox)

        in3_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=5
        )
        in3_label = Gtk.Label("IN3")
        in3_hbox.add(in3_label)
        self.in3_switch = Gtk.Switch()
        self.in3_switch.set_active(False)
        in3_hbox.add(self.in3_switch)
        vbox.add(in3_hbox)

        in4_hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=5
        )
        in4_label = Gtk.Label("IN4")
        in4_hbox.add(in4_label)
        self.in4_switch = Gtk.Switch()
        self.in4_switch.set_active(False)
        in4_hbox.add(self.in4_switch)
        vbox.add(in4_hbox)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        log_view = Gtk.TextView()
        self.textbuffer = log_view.get_buffer()
        scrolledwindow.add(log_view)
        hbox.add(scrolledwindow)

    def update(self, jsonBytes):
        jsonString = jsonBytes.decode("utf-8")
        jsonDict = json.loads(jsonString)
        print(jsonDict)

        pin_name = self._set_pins(jsonDict['channel'], jsonDict['outmode'])

        self._log('PIN %s set to mode %s\n' % (pin_name, jsonDict['outmode']))
        return False

    def listening(self):
        listening_thread = threading.Thread(
            target=self._listening_worker
        )

        listening_thread.daemon = True
        listening_thread.start()

    def _listening_worker(self):
        try:
            os.unlink(self.motor.socket_path)
        except OSError:
            if os.path.exists(self.motor.socket_path):
                raise

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(self.motor.socket_path)
        sock.listen(1)

        while True:
            connection, address = sock.accept()
            event = connection.recv(1024)
            GLib.idle_add(self.update, event)

    def _set_pins(self, rpi_pin, mode):
        motor_pin = self.motor._pin_mapping(rpi_pin)
        if motor_pin == 1:
            self.in1_switch.set_active(mode)
            pin_name = 'IN1'
        if motor_pin == 2:
            self.in2_switch.set_active(mode)
            pin_name = 'IN2'
        if motor_pin == 3:
            self.in3_switch.set_active(mode)
            pin_name = 'IN3'
        if motor_pin == 4:
            self.in4_switch.set_active(mode)
            pin_name = 'IN4'

        return pin_name

    def _log(self, message):
        timestamp = time.time()
        logtime = datetime.datetime \
            .fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        start_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(start_iter, '%s - %s' % (logtime, message))


if __name__ == "__main__":
    GObject.threads_init()
    win = MotorWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    win.listening()
    Gtk.main()

class ULN2003:

    def __init__(self, socket_path):
        self.socket_path = socket_path

    def get_pins(self):
        pass

    def get_step(self):
        pass


    def _pin_mapping(self, rpi_pin):
        if rpi_pin == 1:
            return 1
        if rpi_pin == 2:
            return 2
        if rpi_pin == 3:
            return 3
        if rpi_pin == 4:
            return 4


class Sensor:
    def set_temperature(self, device, temperature):
        file = open(device, 'w')
        file.write('ab 12 34 56 78 bc 12 34 ff : crc=ff YES\n')
        file.write('ab 12 34 56 78 bc 12 34 ff t=%s' % str(temperature * 1000))
        file.close()

# Raspberry Devices
The goal of this little project is to build various small simulators I can use when testing various Raspberry Pi applications.

## Devices

### Sensors

#### DS18B20 Temperature Sensor
This simulator simply writes simulated DS18B20 data to a file.

Reading this from your applications should be pretty much identical to reading from the real sensor. Only difference is the location of the file. By default this will write to the file /tmp/ds18b20

##### Running
To run the simulator simply execute the ui file:
~~~
# python sensors/temperature/ds18b20-ui.py
~~~


import serial.tools.list_ports

# gaseste un port liber
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "COM" in p.device:
        print("Port disponibil: " + p.device)
        ser = serial.Serial(p.device)
        break

# creeaza un port virtual
ser = serial.serial_for_url('loop://', baudrate=9600)

# afiseaza numele portului creat
print("Port virtual creat: " + ser.name)

while True:
    data = ser.read()
    if data:
        print("Date primite: " + str(data))
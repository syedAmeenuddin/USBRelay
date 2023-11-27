import serial

# Define the serial port and baud rate
port = 'COM3'  # Replace with the actual port name for your relay module
baudrate = 9600

# Open the serial port
ser = serial.Serial(port=port, baudrate=baudrate)
print(ser)
# Function to turn on a specific relay
def turn_on_relay(relay_number):
    command = 'Relay ' + str(relay_number) + ' ON\r\n'
    ser.write(command.encode('utf-8'))

# Function to turn off a specific relay
def turn_off_relay(relay_number):
    command = 'Relay ' + str(relay_number) + ' OFF\r\n'
    ser.write(command.encode('utf-8'))

# Example usage
turn_on_relay(1)  # Turn on relay 1
turn_off_relay(2)  # Turn off relay 2

# Close the serial port
ser.close()
import tkinter as tk
import serial

class USBRelayApp:
    def __init__(self, window):
        self.serial_port = serial.Serial('COM3', baudrate=9600, timeout=1)
        print(self.serial_port)            
        device = 'None'
        devicemessage = 'Connected Device = '+''+device
        self.window = window
        dlable = tk.Label(window, text=devicemessage,font=('Inter',15))
        dlable.grid(column=5,row=0)
        # Realy 1
        rl1 = tk.Label(window, text='Realy 1',font=('Inter',10))
        rl1.grid(column=0,row=2)
        rb11 = tk.Button(window,text='Open', bg='orange',fg='black', command=self.turn_on_relay)
        rb11.grid(column=5,row=2)
        rb12 = tk.Button(window,text='Close', bg='orange',fg='black',  command=self.turn_off_relay)
        rb12.grid(column=10,row=2)
        # Realy 2
        rl2 = tk.Label(window, text='Realy 2',font=('Inter',10))
        rl2.grid(column=0,row=3)
        rb21 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb21.grid(column=5,row=3)
        rb22 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb22.grid(column=10,row=3)
        # Realy 3
        rl3 = tk.Label(window, text='Realy 3',font=('Inter',10))
        rl3.grid(column=0,row=4)
        rb31 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb31.grid(column=5,row=4)
        rb32 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb32.grid(column=10,row=4)
        # Realy 4
        rl4 = tk.Label(window, text='Realy 4',font=('Inter',10))
        rl4.grid(column=0,row=5)
        rb41 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb41.grid(column=5,row=5)
        rb42 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb42.grid(column=10,row=5)
        # Realy 5
        rl5 = tk.Label(window, text='Realy 5',font=('Inter',10))
        rl5.grid(column=0,row=6)
        rb51 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb51.grid(column=5,row=6)
        rb52 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb52.grid(column=10,row=6)
        # Realy 6
        rl6 = tk.Label(window, text='Realy 6',font=('Inter',10))
        rl6.grid(column=0,row=7)
        rb61 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb61.grid(column=5,row=7)
        rb62 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb62.grid(column=10,row=7)
        # Realy 7
        rl7 = tk.Label(window, text='Realy 7',font=('Inter',10))
        rl7.grid(column=0,row=8)
        rb71 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb71.grid(column=5,row=8)
        rb72 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb72.grid(column=10,row=8)
        # Realy 8
        rl8 = tk.Label(window, text='Realy 8',font=('Inter',10))
        rl8.grid(column=0,row=9)
        rb81 = tk.Button(window,text='Open', bg='orange',fg='black')
        rb81.grid(column=5,row=9)
        rb82 = tk.Button(window,text='Close', bg='orange',fg='black')
        rb82.grid(column=10,row=9)
        # open all close all
        opall_btn = tk.Button(window,text='Open All', bg='orange',fg='black')
        opall_btn.grid(column=4,row=10)
        clall_btn = tk.Button(window,text='Close All', bg='orange',fg='black')
        clall_btn.grid(column=7,row=10)
    def turn_on_relay(self):
        self.control_relay(self.serial_port)
    def turn_off_relay(self):
        self.control_relay(self.serial_port)
        
        # functions
    def control_relay(self,ser):
        self.ser = ser
        st = 'AFFF0101DF'
        command_bytes = bytes.fromhex(st)
        self.ser.write(command_bytes)
        

   
if __name__ == "__main__":
    window = tk.Tk()
    window.title('Continental USB Relay App')
    # window.geometry('700x500')
    app = USBRelayApp(window)
    window.mainloop()
        

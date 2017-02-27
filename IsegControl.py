import serial



class iseg(object):

    def __init__(self, port=None):

        if port == None:
            self.port = "/dev/ttyUSB0"
        else:
            self.port = port

        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE
        self.timeout = 0.5


    def init(self):

        try:
            self.ser = serial.Serial(port=self.port,
                                     baudrate=self.baudrate,
                                     bytesize=self.bytesize,
                                     parity=self.parity,
                                     stopbits=self.stopbits,
                                     timeout=self.timeout)

            print("Initializing...")

        except:
            raise ValueError("Comport is already claimed or can not be found!")

        return True


    def getPolarity(self):

        self.ser.write(b"P1\r\n")
        answer = self.ser.readline().decode("utf-8")

        return answer


    def getIDN(self):

        self.ser.write(b"#1\r\n")
        answer = self.ser.readline().decode("utf-8")

        return answer


    def getStatus(self):

        self.ser.write("S\r\n")
        answer = self.ser.readline().decode("utf-8")

        return answer



    def test(self):

        while True:
            cmd = input("Enter command:")

            if cmd == "q.":
                break
            else:
                for c in cmd + "\r\n":
                    self.ser.write(bytes(c, "utf-8"))
                    echo = self.ser.read(1)

                for i in range(1,10):
                    answer = self.ser.read(1).decode("utf-8")
                    print(answer)
                print("\r"+"\n")
                
                print("test")

        return True


# main loop
if __name__=='__main__':

    i = iseg("/dev/ttyUSB0")
    i.init()
    i.test()

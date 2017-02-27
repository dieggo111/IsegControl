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
        self.timeout = 0.25


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


    def getVoltage(self):

        self.send_iseg("U1")
        answer = self.read_iseg("U1",10).replace("\r\n","")

        return answer


    def getPolarity(self):

        self.send_iseg("P1")
        answer = self.read_iseg("P1",15).replace("\r\n","")

        return answer


    def getIDN(self):

        self.send_iseg("#1")
        answer = self.read_iseg("#1",28).replace("\r\n","")

        return answer


    def send_iseg(self, cmd):

        for c in cmd + "\r\n":
            self.ser.write(bytes(c, "utf-8"))
            echo = self.ser.read(1)

        return True


    def read_iseg(self, cmd, n):

        answer = self.ser.read(n).decode("utf-8").replace("\r\n"," ")

        return answer


    def test(self, n):

        answer = ""
        while True:
            cmd = input("Enter command:")

            if cmd == "q.":
                break
            else:
                self.send_iseg(cmd)
                answer = self.read_iseg(cmd, n)
                print(answer)
                answer = ""

        return True


# main loop
if __name__=='__main__':

    i = iseg("/dev/ttyUSB0")
    i.init()
    # i.test(30)
    print(i.getIDN())
    print(i.getVoltage())
    print(i.getPolarity())

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

        self.send_bitwise("U1")
        answer = self.read_bitwise("U1",10).replace("\r\n","")

        return answer


    def getPolarity(self):

        self.send_bitwise("P1")
        answer = self.read_bitwise("P1",15).replace("\r\n","")

        return answer


    def getIDN(self):

        self.send_bitwise("#1")
        answer = self.read_bitwise("#1",28).replace("\r\n","")

        return answer


    def send_bitwise(self, cmd):

        for c in cmd + "\r\n":
            self.ser.write(bytes(c, "utf-8"))
            echo = self.ser.read(1)

        return True


    def read_bitwise(self, cmd, n):

        temp = ""
        answer = ""
        for i in range(1,n):
            a = self.ser.read(1).decode("utf-8")
            temp += a

        answer = temp.replace(cmd,"")

        return answer


    def test(self):

        answer = ""
        while True:
            cmd = input("Enter command:")

            if cmd == "q.":
                break
            else:
                for c in cmd + "\r\n":
                    self.ser.write(bytes(c, "utf-8"))
                    echo = self.ser.read(1)

                for i in range(1,40):
                    a = self.ser.read(1).decode("utf-8")
                    answer += a
                print(self.convert_output(answer))
                answer = ""

        return True


# main loop
if __name__=='__main__':

    i = iseg("/dev/ttyUSB0")
    i.init()
    # print(i.getIDN())
    print(i.getPolarity())

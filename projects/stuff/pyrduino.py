import pyfirmata, serial, time



class arduino():
    def __init__(self, port):
        self.board = pyfirmata.Arduino(port)
        print "Setting up the connection to the board on port: " + port
        self.iterator = pyfirmata.util.Iterator(self.board)
        self.iterator.start()

    def pinon(self, number):
        self.board.digital[number].write(True)

    def pinoff(self, number):
        self.board.digital[number].write(False)

    def exitboard(self):
        self.board.exit()
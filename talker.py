import serial


class Talker:
    TERMINATOR = '\r'.encode('UTF8')

    def __init__(self, timeout=1):
        self.serial = serial.Serial('/dev/cu.usbmodem1101', 115200, timeout=timeout)

    def send(self, text: str):
        line = '%s\r\f' % text
        self.serial.write(line.encode('utf-8'))
        reply = self.receive()
        reply = reply.replace('>>> ','') # lines after first will be prefixed by a propmt
        if reply != text: # the line should be echoed, so the result should match
            raise ValueError('expected %s got %s' % (text, reply))

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def close(self):
        self.serial.close()

        
 '''
        
        On the host
Copy talker.py from this github gist into an editor and save it in a directory of your choice.
In that directory, run python3 to start an interactive session.
Type from talker import Talker
Type t = Talker(). If you are running on Windows, you will need to type t = Talker('COM6') replacing COM6 by whatever port the Pico is visible on.
Type t.send('2 + 2')
Type t.receive(). If all is well, this will print the result 4.
Type t.send('on()')     #  The on-board LED on the Pico should turn on.
Type t.send('off()')    #  The on-board LED on the Pico should turn off.
When you have finished, type t.close().

'''

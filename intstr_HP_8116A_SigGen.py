# ***************************************************************
#   Eric DuVall
#   4/7/2024
#
#   HP 8116A GPIB HP-IB software demonstration using pyvisa
#   HP 8116A is pre-GBIB unit and therefore does not use the
#   *IDN? command
# ****************************************************************

import pyvisa

class Instrument_8116A:
    def __init__(self, Center, Span):
        self.CF = Center    
        self.SP = Span
        #self.arr = self.arr.insert([99])

    def connect(self, Address):
        self.machine = 9
        RM = pyvisa.ResourceManager()
        try:
            #self.my_instrument = RM.open_resource('GPIB0::16::INSTR')
            self.my_instrument = RM.open_resource('GPIB0::' + str(Address) + '::INSTR')
        except:
            print('Not able to connect to GPIB')

    def default_state(self):
            #self.my_instrument.write('CLEAR')
        self.my_instrument.write('FRQ 1 KHZ')
        self.my_instrument.write('AMP .1 V')
        

    def output(self):

        print('Output Funciton')


def main():
    print('Test in the main 8116A')
    int_8116A = Instrument_8116A(2,2)
    int_8116A.connect(16)
    int_8116A.output()

if __name__=="__main__": 
    main() 

from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from time import sleep
import random


class PiLedContraption:
    '''A class to represent the LED experimental circuit board we built for the raspberry pi'''

    _led = []
    _sleeptime = .01


    def __init__(self):
        ''' initialize the class so everything is ready to use
        '''
        self._valid_leds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17]
        # setup the LEDs

        for i in range(0, 10):
            self._led.append(PWMLED(i + 2))
            self._led[i].off()

        self._sololed = PWMLED(17)
        self._sololed.off()

    def led_on(self, logical_led_number):
        ''' a function to turn ON a led specifid by it's logical number in the sequence *not the gpio pin number
        '''
        if(logical_led_number not in self._valid_leds):
            print("No LED is configured on pin {0}".format(logical_led_number))
            #raise IndexError
        else:
            self._led[logical_led_number].on()
            print("{} on".format(logical_led_number))


    def led_off(self, logical_led_number):
        ''' a function to turn OFF a led specifid by it's logical number in the sequence *not the gpio pin number
        '''
        if(logical_led_number not in self._valid_leds):
            print("No LED is configured on pin {0}".format(logical_led_number))
            #raise IndexError
        else:
            self._led[logical_led_number].off()
            print("{} off".format(logical_led_number))


    def race_up(self):
        ''' a function to run the LEDs up
        '''
        for i in range(0,10):
            print("{} on".format(i))
            self._led[i].on()
            sleep(self._sleeptime)
            print("{}  off".format(i))
            self._led[i].off()
            sleep(self._sleeptime)


    def race_down(self):
        ''' a function to run the LEDs down
        '''
        for i in range(9,-1,-1):
            print("{} on".format(i))
            self._led[i].on()
            sleep(self._sleeptime)
            print("{}  off".format(i))
            self._led[i].off()
            sleep(self._sleeptime)

    def dance_randomly(self):
        random.seed()
        for i in range(1,100):
            r=random.randint(0,9)
            print("{} on".format(r))
            self._led[r].on()
            sleep(self._sleeptime)
            print("{}  off".format(r))
            sleep(self._sleeptime)

if __name__ == "__main__":
    print("testing the pi led contraption")
    aPC=PiLedContraption()

    # test the ranges work ok
    for i in range(0,13):
        aPC.led_on(i)

    # test to see if all the lights light
    aPC.led_on(0)
    aPC.led_on(1)
    aPC.led_on(2)
    aPC.led_on(3)
    aPC.led_on(4)
    aPC.led_on(5)
    aPC.led_on(6)
    aPC.led_on(7)
    aPC.led_on(8)
    aPC.led_on(9)
    sleep(2)
    aPC.led_off(0)
    aPC.led_off(1)
    aPC.led_off(2)
    aPC.led_off(3)
    aPC.led_off(4)
    aPC.led_off(5)
    aPC.led_off(6)
    aPC.led_off(7)
    aPC.led_off(8)
    aPC.led_off(9)

    #test race functions
    aPC.race_up()
    sleep(2)
    aPC.race_up()

    #test dance function
    aPC.dance_randomly()





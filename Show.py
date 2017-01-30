import RPi.GPIO as GPIO
from time import sleep

def init():
  GPIO.setmode(GPIO.BOARD)
  displeje = (18,22,32,36,38,40)
  GPIO.setup(displeje,GPIO.OUT, initial=1)
  segments = (13,11,35,33,31,15,29,37)
  GPIO.setup(segments,GPIO.OUT, initial=1)

num = {' ':(1,1,1,1,1,1,1,1),
       'F':(0,1,1,1,0,0,0,1),
       'A':(0,0,0,1,0,0,0,1),
       'C':(0,1,1,0,0,0,1,1),
       'b':(1,1,0,0,0,0,0,1),
       'd':(1,0,0,0,0,1,0,1),
       'E':(0,1,1,0,0,0,0,1),
       'H':(1,0,0,1,0,0,0,1),
       'n':(1,1,0,1,0,1,0,1),
       'o':(1,1,0,0,0,1,0,1),
       'P':(0,0,1,1,0,0,0,1),
       'r':(1,1,1,1,0,1,0,1),
       'S':(0,1,0,0,1,0,0,1),
       'I':(1,1,1,1,0,0,1,1),
       'L':(1,1,1,0,0,0,1,1),
       '0':(0,0,0,0,0,0,1,1),
       'O':(0,0,0,0,0,0,1,1),
       '1':(1,0,0,1,1,1,1,1),
       '2':(0,0,1,0,0,1,0,1),
       '3':(0,0,0,0,1,1,0,1),
       '4':(1,0,0,1,1,0,0,1),
       '5':(0,1,0,0,1,0,0,1),
       '6':(0,1,0,0,0,0,0,1),
       '7':(0,0,0,1,1,1,1,1),
       '8':(0,0,0,0,0,0,0,1),
       '9':(0,0,0,1,1,0,0,1)
           }

#sprav tu funkciu tak, ze do nej mozes passovat argumenty
#vnutri si overis ci je to string, ak hej, tak ho vypises
#ak to bude integer, tak ho prevedies na string a vypises
def seg():
    for displej in range(4):
        GPIO.output(segments, (num[display_string[displej]]))
        GPIO.output(displeje[displej],1)
        sleep(.005)
        GPIO.output(displeje[displej],0)

try:
    while(1):
      display_string = 'HELL'
      seg()
finally:
    GPIO.cleanup()

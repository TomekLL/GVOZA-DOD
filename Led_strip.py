GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
def Blikaj(L,p): #L=císlo pinu, p=pocet
  for x in range(p):
      GPIO.output(L,True)
      sleep(.3)
      GPIO.output(L,False)
      sleep(.1)

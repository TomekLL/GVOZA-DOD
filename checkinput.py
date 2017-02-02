GPIO.setup(7,GPIO.in,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.in,pull_up_down=GPIO.PUD_UP)
def stlacene_tlacitko():
	if GPIO.inpu(7)==0:
		return 1
		sleep(.2)
	if GPIO.inpu(7)==0:
		return 2
		sleep(.2)
	return 0
	#vrati 1 ak je stlacene lave tlacitko, 2 ak pravea 0 ak ziadne

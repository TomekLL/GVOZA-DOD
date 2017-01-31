import disptime
import checkinput
import hra
import time

init()

while True:
	# stale dookola vypisuje cas
	disptime.print_time()
	if checkinput.stlacene_tlacitko() == 1:
		vitaz = hraj()
		# tu sa potom vytvori GUI, ktore pekne na par sekund vykresli kto vyhral a s akym casom
		# gui sa ukonci, vrati sa do vypisovania do konzoly
		# a potom sa to vrati do povodneho loopu na vypis stopiek
		# na GUI bude asi samostanta funkcia, este neviem :)
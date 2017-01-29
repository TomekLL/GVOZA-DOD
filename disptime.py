import datetime

def print_time():
	now = datetime.now()
	begin = datetime.datetime(2017, 1, 29, 13, 0, 0)
	#vypise cas ktory uplynul od 29.1.2017 1300
	print (now - begin).seconds
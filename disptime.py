import datetime

def print_time(begin = datetime.datetime(2017, 1, 29, 13, 0, 0)):
	now = datetime.datetime.now()
	begin = datetime.datetime(2017, 1, 29, 13, 0, 0)
	#vypise cas ktory uplynul od 29.1.2017 1300
	#seq((now - begin).seconds)
	seq((now - begin).seconds)
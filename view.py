import datetime

FORMAT_STR = '%Y-%m-%d %H:%M:%S'


def millis(start_time):
	"""
	Returns the elapsed milliseconds since the start of the program.

	:param start_time:
	:return: ms
	"""
	dt = datetime.datetime.now() - start_time
	ms = int(dt.total_seconds() * 1000)
	return ms


def difference(start_dt):
	"""
	1 minute = 60 seconds
	1 hour = 60 x 60 = 3600
	1 day = 3600 x 24 = 86400

	:param start_dt:
	:return:
	"""
	milliseconds = millis(start_dt)

	seconds_milli = 1000
	minutes_milli = seconds_milli * 60
	hours_milli = minutes_milli * 60
	days_milli = hours_milli * 24

	elapsed_days = milliseconds / days_milli
	milliseconds = milliseconds % days_milli

	elapsed_hours = milliseconds / hours_milli
	milliseconds = milliseconds % hours_milli

	elapsed_minutes = milliseconds / minutes_milli
	milliseconds = milliseconds % minutes_milli

	elapsed_seconds = milliseconds / seconds_milli

	return "{} days, {} hours, {} minutes, {} seconds".format(
		int(elapsed_days),
		int(elapsed_hours),
		int(elapsed_minutes),
		int(elapsed_seconds)
	)


date_str = '2018-12-04 10:22:48'
start_date = datetime.datetime.strptime(date_str, FORMAT_STR)
data = difference(start_date)
print(data)

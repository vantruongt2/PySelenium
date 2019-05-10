import datetime

#random string with current date time
now = datetime.datetime.now()
current_time = now.strftime('%m%d%y-%H%M%S')

def random_string(string):
    return string + "-" + current_time

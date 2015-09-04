#!/usr/bin/python

# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def s2hms(seconds):
    print seconds
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds %= 60
    return hours, minutes, seconds

def units2factor(units):
    factor = 1
    if units[0] == 'k': factor = pow(2, 10)
    if units[0] == 'M': factor = pow(2, 20)
    if units[0] == 'G': factor = pow(2, 30)
    if units[0] == 'T': factor = pow(2, 40)
    if units[1] == 'B': factor *= 8
    return factor
        
def download_time(filesize, filesizeUnits, bandwidth, bandwidthUnits):
    # return time taken in hms (1 = hour, else hours) (seconds in real)
    filesize *= units2factor(filesizeUnits)
    bandwidth *= units2factor(bandwidthUnits)
    speed = 1.0 * filesize / bandwidth
    h,m,s = s2hms(speed)
    if h == 1: hours = ' hour, '
    else: hours = ' hours, '
    if m == 1: minutes = ' minute, '
    else: minutes = ' minutes, '
    if s == 1: seconds = ' second'
    else: seconds = ' seconds'
    return str(h) + hours + str(m) + minutes + str(s) + seconds

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


from time import sleep, time
last_time = time()
while 1:
    if time()-last_time > 1:
        print('One second has passed')
        last_time = time()
    else:
        ## The print() and sleep() is just here for debug purposes
        ## And in a graphical application you can remove the two below.
        print('Still waiting for one second to pass')
        sleep(0.25)

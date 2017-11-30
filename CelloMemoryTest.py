import cello

try:
    print ("Wake Cello")
    if cello.wake():
        print ("Cello Awake")
        memory = bytearray(cello.read_memory(0x0040, 0x10))
        cello.sleep()
        result = ' '.join(str(i) for i in memory)

        print result
        print ("Finished")
    else:
        print "Failed to wake Cello"
except Exception as err:
    print (err)

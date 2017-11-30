import cello

try:
    print ("Wake Cello")
    if cello.wake():

        location = [0x40, 0x50]
        memory = []
        
        memory.append(bytearray(cello.read_memory(location[0], 0x10)))
        memory.append(bytearray(cello.read_memory(location[1], 0x10)))

        notepad_lines = []
        line = ""
        line_counter = 0
        while line[:2] != "!\r":
            line = cello.read_notepad_line(line_counter)
            notepad_lines.append(line)
            line_counter += 1
            if line_counter > 20:
                break
        
        cello.sleep()

        print ''.join('{:02X} '.format(i) for i in memory[0])
        print ''.join('{:02X} '.format(i) for i in memory[1])

        print ""
        print "Notepad"
        print "\n".join(notepad_lines)

        print ("Finished")
    else:
        print "Failed to wake Cello"
except Exception as err:
    print (err)


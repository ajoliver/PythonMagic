import serial
import time
import enhancedProtocol

serial_port = None


########################################################################################################################
# wake up the cello
#
def wake():
    global serial_port
    serial_port = serial.Serial('/dev/ttyS0', 1200, serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE
                                , timeout=0.8, xonxoff=0, rtscts=0, dsrdtr=0)
    serial_port.setDTR(True)
    serial_port.setRTS(True)

    retry = 0
    while retry < 4:
        print("Try " + str(retry))
        x = serial_port.write(bytearray([5, 'l']))
        time.sleep(0.2)

        version = read_version_number()
        if version != '':
            print ("Version: " + version)
            return True

        retry = retry + 1

    return False


########################################################################################################################
# put the cello to sleep
#
def sleep():
    global serial_port
    serial_port.write(b"Q\r")


########################################################################################################################
# read the cello memory
def read_memory(start, length):
    send_packet = read_memory_packet(start, length)
    serial_port.write(send_packet)

    response_packet = read_packet()
    if not enhancedProtocol.verify_packet(response_packet):
        raise Exception("EP packet failed to verify")

    return response_packet


########################################################################################################################
# read a packet from the serial port
def read_packet():
    global serial_port

    packet_length = serial_port.read(1)
    if packet_length != '':
        # read the rest of the packet
        packet = packet_length.join(serial_port.read(ord(packet_length)))

        # check the packet integrity
        if enhancedProtocol.verify_packet(packet):
            return enhancedProtocol.get_data(packet)
        else:
            raise Exception("Invalid packet")

    return bytearray(0)

########################################################################################################################
# build a "read memory" packet to send to a cello
def read_memory_packet(start, length):
    command = list()

    hi_byte = (start & 0xFF00) >> 8
    lo_byte = start & 0x00FF

    command.append(hi_byte)
    command.append(lo_byte)
    command.append(length)

    return enhancedProtocol.build_packet('D', command)


########################################################################################################################
# read the cello version number
def read_version_number():
    global serial_port

    send_packet = bytearray(enhancedProtocol.build_packet('V', []))

    serial_port.write(send_packet)

    data = bytearray(read_packet())
    return bytearray([data[0], data[2], data[4], data[6]])

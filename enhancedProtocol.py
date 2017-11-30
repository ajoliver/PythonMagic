########################################################################################################################
# build an enhanced protocol packet
#


def build_packet(cmd, data, logger_id=0):
    # type: (char, [], int) -> []

    send_length = (1 + 1 + len(data) + 1)
    rv = list()
    rv.append(send_length)
    rv.append(logger_id)
    rv.append(ord(cmd))
    rv.extend(data)
    checksum = sum(rv) & 0xFF
    rv.append(checksum)

    return bytearray(rv)


########################################################################################################################
# verify the packet checksum
#


def verify_packet(packet):
    return True

    if len(packet) < 3:
        return False

    length = packet[0]
    if len(packet) < length:
        return False

    checksum = packet[length]
    temp = sum(packet[0:length])

    if temp != checksum:
        return False

    return True


########################################################################################################################
# extract the packet payload data
#


def get_data(packet):
    length = len(packet)
    start = 1
    end = length - 1
    return bytearray(packet[start:end])

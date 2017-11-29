import unittest
import enhancedProtocol


class TestEnhancedProtocol(unittest.TestCase):
    def test_buildPacket(self):
        packet = enhancedProtocol.build_packet('M', [12, 34, 56], 13)
        self.assertEqual(len(packet), 7)
        self.assertEqual(packet[0], 6)
        self.assertEqual(packet[1], 13)
        self.assertEqual(packet[2], ord('M'))
        self.assertEqual(packet[3], 12)
        self.assertEqual(packet[4], 34)
        self.assertEqual(packet[5], 56)
        self.assertEqual(packet[6], 198)

        packet = enhancedProtocol.build_packet('V', [], 0)
        self.assertEqual(len(packet), 4)
        self.assertEqual(packet[0], 3)
        self.assertEqual(packet[1], 0)
        self.assertEqual(packet[2], ord('V'))
        self.assertEqual(packet[3], 89)

    def test_verifyPacket(self):
        packet = list()

        packet.append(3)
        packet.append(0)
        packet.append(ord('V'))
        packet.append(89)

        self.assertEquals(True, enhancedProtocol.verify_packet(packet))

    def test_getData(self):
        packet = list()

        packet.append(0x06)
        packet.append(0x00)
        packet.append(ord('C'))
        packet.append(ord('3'))
        packet.append(ord('9'))
        packet.append(ord('1'))
        packet.append(0xE6)

        data = enhancedProtocol.get_data(packet)
        version = ''.join(chr(i) for i in data)
        self.assertEquals("C391", version)

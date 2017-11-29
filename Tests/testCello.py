import unittest
import cello


class TestCello(unittest.TestCase):
    def test_read_memory_packet(self):
        packet = cello.read_memory_packet(0x0040, 0x10)
        self.assertEqual(len(packet), 7)
        self.assertEqual(packet[0], 6)
        self.assertEqual(packet[1], 0)
        self.assertEqual(packet[2], ord('D'))
        self.assertEqual(packet[3], 0x00)
        self.assertEqual(packet[4], 0x40)
        self.assertEqual(packet[5], 0x10)
        self.assertEqual(packet[6], 0x9A)

    def test_decode_version(self):
        data = ['C', '3', '0', '1']
        version = ''.join(i for i in data[1:])
        self.assertEquals(version[0], '3')

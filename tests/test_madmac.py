from unittest import TestCase


import madmac


class TestMadMac(TestCase):

    def test_extract_alphanumeric_case01(self):
        value = madmac.extract_alphanumeric('abc-def')
        self.assertEqual(value, 'abcdef')

    def test_extract_alphanumeric_case02(self):
        value = madmac.extract_alphanumeric('abc:def')
        self.assertEqual(value, 'abcdef')

    def test_extract_alphanumeric_case03(self):
        value = madmac.extract_alphanumeric('12:34-56')
        self.assertEqual(value, '123456')

    def test_pair_hexvalue(self):
        value = madmac.pair_hexvalue('abcdef', ':')
        self.assertEqual(value, 'ab:cd:ef')

    def test_int_to_hexstr(self):
        value = madmac.int_to_hexstr(255)
        self.assertEqual(value, '0000ff')

    def test_hexstr_to_int(self):
        value = madmac.hexstr_to_int('0000ff')
        self.assertEqual(value, 255)

    def test_access_object_member_case01(self):
        tmp = 1
        value = madmac.access_object_member(tmp, 'real')
        self.assertEqual(value, tmp.real)

    def test_access_object_member_case02(self):
        tmp = []
        value = madmac.access_object_member(tmp, 'copy')
        self.assertEqual(value, tmp)

    def test_validate_3octets_case01(self):
        tmp = 'aabbcc'
        result = madmac.validate_3octets(tmp)
        self.assertTrue(result)

    def test_validate_3octets_case02(self):
        tmp = '123456'
        result = madmac.validate_3octets(tmp)
        self.assertTrue(result)

    def test_validate_3octets_case03(self):
        tmp = 123456
        result = madmac.validate_3octets(tmp)
        self.assertFalse(result)

    def test_validate_3octets_case04(self):
        tmp = '12345'
        result = madmac.validate_3octets(tmp)
        self.assertFalse(result)

    def test_validate_MAC_case01(self):
        self.assertTrue(madmac.validate_MAC('12345678912'))

    def test_validate_MAC_case02(self):
        self.assertTrue(madmac.validate_MAC('ab-cd-ef-12-34-56'))

    def test_validate_MAC_case03(self):
        self.assertTrue(madmac.validate_MAC('ab:cd:ef:12:34:56'))

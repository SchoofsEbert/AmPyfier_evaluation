from pippin.util.validators import Validators
import os
import string
import unittest


class TestValidators(unittest.TestCase):

    def test_valid_block_hash(self):
        self.assertFalse(Validators.is_valid_block_hash(None))
        self.assertFalse(Validators.is_valid_block_hash('1234'))
        self.assertFalse(Validators.is_valid_block_hash('Appditto LLC'))
        self.assertFalse(Validators.is_valid_block_hash(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_block_hash(
            '5E5B7C8F97BDA8B90FAA243050D99647F80C25EB4A07E7247114CBB129BDA18'))
        self.assertFalse(Validators.is_valid_block_hash(
            '5E5B7C8F97BDA8B90FAA243050D99647F80C25EB4A07E7247114CBB129BDA1888'
            ))
        self.assertFalse(Validators.is_valid_block_hash(
            '5E5B7C8F97BDA8B90FAA243050D99647F80C25EB4A07E7247114CBB129BDA18Z')
            )
        self.assertTrue(Validators.is_valid_block_hash(
            '5E5B7C8F97BDA8B90FAA243050D99647F80C25EB4A07E7247114CBB129BDA188')
            )

    def test_valid_address(self):
        """Test address validation"""
        self.assertFalse(Validators.is_valid_address(None))
        os.environ['BANANO'] = '1'
        self.assertTrue(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))
        del os.environ['BANANO']
        self.assertTrue(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x')
            )
        self.assertTrue(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))

    def test_valid_address_str_dbl_7_str_hlf_7(self):
        """Test address validation"""
        self.assertFalse(Validators.is_valid_address(None))
        os.environ['BANANO'] = '1'
        self.assertTrue(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))
        del os.environ['BANANO']
        self.assertFalse(Validators.is_valid_address(
            'ie5swmoth87thi74qgbfrij7dcgjiij94xrnano_1bananobh5rat99qfgt1ptpie'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x')
            )
        self.assertTrue(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))

    def test_valid_address_str_dbl_3(self):
        """Test address validation"""
        self.assertFalse(Validators.is_valid_address(None))
        os.environ['BANANO'] = '1'
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xrban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr'
            ))
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))
        del os.environ['BANANO']
        self.assertTrue(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x')
            )
        self.assertTrue(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))

    def test_valid_address_str_dbl_7(self):
        """Test address validation"""
        self.assertFalse(Validators.is_valid_address(None))
        os.environ['BANANO'] = '1'
        self.assertTrue(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))
        del os.environ['BANANO']
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xrnano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa'
            ))
        self.assertFalse(Validators.is_valid_address(
            'nano_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x')
            )
        self.assertTrue(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xa')
            )
        self.assertFalse(Validators.is_valid_address(
            'xrb_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94x'))

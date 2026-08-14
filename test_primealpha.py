# test_primealpha.py
"""
Tests for PrimeAlpha module.
"""

import unittest
from primealpha import PrimeAlpha

class TestPrimeAlpha(unittest.TestCase):
    """Test cases for PrimeAlpha class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeAlpha()
        self.assertIsInstance(instance, PrimeAlpha)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeAlpha()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_zephyrwane.py
"""
Tests for ZephyrWane module.
"""

import unittest
from zephyrwane import ZephyrWane

class TestZephyrWane(unittest.TestCase):
    """Test cases for ZephyrWane class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZephyrWane()
        self.assertIsInstance(instance, ZephyrWane)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZephyrWane()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

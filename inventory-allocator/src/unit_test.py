from challenge import *
import unittest


class InventoryAllocatorTest(unittest.TestCase):
    def setUp(self):
        self.allocator = InventoryAllocator()

    def test_exact_allocation(self):
        self.allocator.set_order({"apple": 1})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {"apple": 1}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [{"owd": {"apple": 1}}])

unittest.main()

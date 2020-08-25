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

    def test_no_allocation(self):
        self.allocator.set_order({"apple": 1})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {"apple": 0}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [])

    def test_split_warehouse(self):
        self.allocator.set_order({"apple": 10})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}])

    def test_one_empty_warehouse(self):
        self.allocator.set_order({"apple": 10})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {}}, {"name": "dm", "inventory": {"apple": 10}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [{"dm": {"apple": 10}}])

    def test_only_empty_warehouses(self):
        self.allocator.set_order({"apple": 10})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {}}, {"name": "dm", "inventory": {}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [])

    def test_zero_items(self):
        self.allocator.set_order({"apple": 10})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 0}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [])

    def test_empty_order(self):
        self.allocator.set_order({})
        self.allocator.set_warehouse([{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 10}}])
        self.allocator.check_order()
        self.assertEqual(self.allocator.output, [])


if __name__ == '__main__':
    unittest.main()

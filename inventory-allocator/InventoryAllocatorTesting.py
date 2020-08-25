import unittest
from InventoryAllocator import InventoryAllocator


class MyTestCase(unittest.TestCase):
    def test_exact(self):
        allocator = InventoryAllocator()
        order = {'apple': 1}
        distribution = [{'name': 'owd', 'inventory': {'apple': 1}}]
        result = allocator.allocate(order, distribution)
        expected = [{'owd': {'apple': 1}}]
        self.assertEqual(expected, result)

    def test_no_allocation(self):
        allocator = InventoryAllocator()
        order = {'apple': 1}
        distribution = [{'name': 'owd', 'inventory': {'apple': 0}}]
        result = allocator.allocate(order, distribution)
        expected = []
        self.assertEqual(expected, result)

    def test_no_allocation_2(self):
        # Check if allocator returns empty list if only fill partial order
        allocator = InventoryAllocator()
        order = {'apple': 10, 'orange': 10}
        distribution = [{'name': 'owd', 'inventory': {'apple': 10, 'orange': 3}}]
        result = allocator.allocate(order, distribution)
        expected = []
        self.assertEqual(expected, result)

    def test_single_item_split(self):
        allocator = InventoryAllocator()
        order = {'apple': 10}
        distribution = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        result = allocator.allocate(order, distribution)
        expected = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(expected, result)

    def test_multiple_items_split(self):
        allocator = InventoryAllocator()
        order = {'apple': 10, 'orange': 10}
        distribution = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 3}},
                        {'name': 'dm', 'inventory': {'apple': 5, 'orange': 8}}]
        result = allocator.allocate(order, distribution)
        expected = [{'owd': {'apple': 5, 'orange': 3}}, {'dm': {'apple': 5, 'orange': 7}}]
        self.assertEqual(expected, result)

    def test_multiple_items_split_2(self):
        allocator = InventoryAllocator()
        order = {'apple': 10, 'orange': 10, 'fruit': 3}
        distribution = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 3}},
                        {'name': 'dm', 'inventory': {'apple': 5, 'orange': 8}},
                        {'name': 'abc', 'inventory': {'fruit': 4}}]
        result = allocator.allocate(order, distribution)
        expected = [{'owd': {'apple': 5, 'orange': 3}}, {'dm': {'apple': 5, 'orange': 7}}, {'abc': {'fruit': 3}}]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

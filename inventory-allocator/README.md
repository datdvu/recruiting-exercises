## InventoryAllocator.py 
- **allocate**(*order*, *distribution*): 
"""
:param *order*: a dictionary of items to order, e.g. `{apple: 5, banana: 5, orange: 5}`
:param *distribution*: a list of dictionary objects of warehouse and inventory, 
e.g. `[{ name: owd, inventory: { apple: 5, orange: 10 } }, { name: dm, inventory: { banana: 5, orange: 10 } } ]`  
:return: *shipment*: a list of dictionary objects of warehouse and respective shipment,
e.g. `[{owd: {apple: 5, orange:5}}, {dm: {banana:5}}]`  
"""

To run unit tests, run 
```bash
python InventoryAllocatorTesting.py
```
I have included 6 unit tests: 
- test_exact: test whether exact match shipment is returned
- test_no_allocation: test whether allocator returns empty list when inventory is not enough
- test_no_allocation_2: same as above test but with order already having partial number of items matched
- test_single_item_split: test whether an item is split across warehouse to completely ship
- test_multiple_item_split: same as above test but with multiple items split
- test_multiple_item_split_2: same as above test but with multiple items split and multiple warehouses


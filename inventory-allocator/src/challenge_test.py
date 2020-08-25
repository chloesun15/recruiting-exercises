from challenge import *


def main():
    print("-- RUNNING UNIT TESTS -- ")
    # Checks for case where the warehouse has exactly what order needs
    exact_unit_test()

    # Checks for case where warehouse can't fulfill the order
    no_allocation_unit_test()

    # Checks for case where order needs to be split across warehouses
    split_warehouse_unit_test()

    # Checks for when a warehouse is empty
    one_empty_warehouse_unit_test()

    # Checks for when all warehouses are empty
    only_empty_warehouse_unit_test()

    # Checks for one when a warehouse is not empty (i.e. has an item listed) but the value is 0
    zero_item_unit_test()

    # Checks for when the order provided is empty
    empty_order_unit_test()

    print("-- ALL UNIT TESTS PASSED --")


# Template for running and printing our test results
def test_template(order, warehouse, output, test):
    print("\n" + test + " test running...")

    # Create object with given order and warehouse
    test_inventory = InventoryAllocator(order, warehouse)

    # Get the cheapest shipment using check_order
    test_output = test_inventory.check_order()

    # Print our outputs for comparison
    print("Expected output: " + str(output))
    print("Output: " + str(test_output))

    # Run our assert to make sure it pasts our test, and if so, print to console.
    assert test_output == output
    print("" + test + " test passed.")


def exact_unit_test():
    test_order = {"apple": 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 1}}]
    expected_output = [{"owd": {"apple": 1}}]

    test_template(test_order, test_warehouse, expected_output, "Exact inventory match")


def no_allocation_unit_test():
    test_order = {"apple": 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 0}}]
    expected_output = []

    test_template(test_order, test_warehouse, expected_output, "No inventory")


def split_warehouse_unit_test():
    test_order = {"apple": 10}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
    expected_output = [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}]

    test_template(test_order, test_warehouse, expected_output, "Split warehouse")


def one_empty_warehouse_unit_test():
    test_order = {"apple": 10}
    test_warehouse = [{"name": "owd", "inventory": {}}, {"name": "dm", "inventory": {"apple": 10}}]
    expected_output = [{"dm": {"apple": 10}}]

    test_template(test_order, test_warehouse, expected_output, "One empty warehouse")


def only_empty_warehouse_unit_test():
    test_order = {"apple": 10}
    test_warehouse = [{"name": "owd", "inventory": {}}, {"name": "dm", "inventory": {}}]
    expected_output = []

    test_template(test_order, test_warehouse, expected_output, "Only empty warehouses")


def zero_item_unit_test():
    test_order = {"apple": 10}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 10}}]
    expected_output = [{"dm": {"apple": 10}}]

    test_template(test_order, test_warehouse, expected_output, "Zero items")


def empty_order_unit_test():
    test_order = {}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 0}}, {"name": "dm", "inventory": {"apple": 10}}]
    expected_output = []

    test_template(test_order, test_warehouse, expected_output, "Empty order")


if __name__ == '__main__':
    main()

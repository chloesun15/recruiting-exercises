from challenge import *


def main():
    print("-- RUNNING UNIT TESTS -- ")
    exact_unit_test()
    no_allocation_unit_test()


def test_template(order, warehouse, output, test):
    print("\n" + test + " test running...")
    test_order = order
    test_warehouse = warehouse
    expected_output = output

    test_inventory = InventoryAllocator(test_order, test_warehouse)
    output = test_inventory.check_order()
    print("Expected output: " + str(expected_output))
    print("Output: " + str(expected_output))
    assert output == expected_output
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


if __name__ == '__main__':
    main()

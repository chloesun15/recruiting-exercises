from challenge import *


def main():
    print("-- RUNNING UNIT TESTS -- ")
    exact_unit_test()
    no_allocation_unit_test()


def exact_unit_test():
    print("\nExact inventory match test running...\n")
    test_order = {"apple": 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 1}}]
    expected_output = [{"owd": {"apple": 1}}]

    test_inventory = InventoryAllocator(test_order, test_warehouse)
    output = test_inventory.check_order()
    print("Expected output: " + str(expected_output))
    print("Output: " + str(expected_output))
    assert output == expected_output
    print("\nExact inventory match test passed.")


def no_allocation_unit_test():
    print("\nNo allocation match test running...\n")
    test_order = {"apple": 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 0}}]
    expected_output = []

    test_inventory = InventoryAllocator(test_order, test_warehouse)
    output = test_inventory.check_order()
    print("Expected output: " + str(expected_output))
    print("Output: " + str(expected_output))
    assert output == expected_output
    print("\nNo allocation match test passed.")


if __name__ == '__main__':
    main()

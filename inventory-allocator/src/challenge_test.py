from challenge import *


def main():
    print("test running")
    exact_unit_test()


def exact_unit_test():
    test_order = {"apple", 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 1}}]

    test_inventory = InventoryAllocator(test_order, test_warehouse)
    output = test_inventory.check_order()
    assert output == [{"owd": {"apple": 1}}]


if __name__ == '__main__':
    main()

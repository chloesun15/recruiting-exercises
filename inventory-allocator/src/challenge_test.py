from challenge import *


def main():
    print("test running")
    test_order = {"apple": 5, "banana": 5, "orange": 20}
    test_warehouse = [
        {
            "name": "owd",
            "inventory": {"apple": 25, "orange": 10}
        },
        {
            "name": "dm",
            "inventory": {"banana": 5, "orange": 10}
        }
    ]

    my_inventory = InventoryAllocator(test_order, test_warehouse)
    print(my_inventory.check_order())


def exact_unit_test():
    test_order = {"apple", 1}
    test_warehouse = [{"name": "owd", "inventory": {"apple": 1}}]

    test_inventory = InventoryAllocator(test_order, test_warehouse)
    output = test_inventory.check_order
    assert output == [{"owd": {"apple": 1}}]


if __name__ == '__main__':
    main()
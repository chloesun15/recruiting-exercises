# ### Problem
#
# The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of
# warehouses (called inventory distribution).
#
# Your task is to implement InventoryAllocator class to produce the cheapest shipment.
#
# The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example
# an order of apples, bananas and oranges of 5 units each will be
#
# `{ apple: 5, banana: 5, orange: 5 }`
#
# The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for
# these items. For example the inventory across two warehouses called owd and dm for apples, bananas and oranges
# could look like
#
# `[
#     {
#     	name: owd,
#     	inventory: { apple: 5, orange: 10 }
#     },
#     {
#     	name: dm:,
#     	inventory: { banana: 5, orange: 10 }
#     }
# ]`
#
# You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to
# ship from than the second warehouse.
#
# You can use any language of your choice to write the solution (internally we use Typescript/Javascript, Python, and
# some Java). Please write unit tests with your code, a few are mentioned below, but these are not comprehensive.
# Fork the repository and put your solution inside of the src directory and include a way to run your tests!
#
# ### Examples
#
# *Happy Case, exact inventory match!**
#
# Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`
# Output: `[{ owd: { apple: 1 } }]`
#
# *Not enough inventory -> no allocations!*
#
# Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]`
# Output: `[]`
#
# *Should split an item across warehouses if that is the only way to completely ship an item:*
#
# Input: `{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]`
# Output: `[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]`
#
# ### What are we looking for
#
# We'll evaluate your code via the following guidelines in no particular order:
#
# 1. **Readability**: naming, spacing, consistency
# 2. **Correctness**: is the solution correct and does it solve the problem
# 1. **Test Code Quality**: Is the test code comprehensive and covering all cases.
# 1. **Tool/Language mastery**: is the code using up to date syntax and techniques.


class InventoryAllocator:

    # Initialize with order and warehouse
    def __init__(self, order={}, warehouse=[]):
        self.order = order
        self.warehouse = warehouse
        self.output = {}

    # Getters and Setters
    def get_order(self):
        return self.order

    def get_warehouse(self):
        return self.warehouse

    def get_output(self):
        return self.output

    def set_order(self, order):
        self.order = order

    def set_warehouse(self, warehouse):
        self.warehouse = warehouse

    # Our main function that will allocate our inventory
    def check_order(self):

        # Type check for order and warehouse inputs
        if not type(self.order) == dict:
            raise TypeError("Error: the provided order is not a dictionary.")
        elif not type(self.warehouse) == list:
            raise TypeError("Error: the provided warehouse is not a list.")

        # Initialize our return list, create copy of order
        source = []
        order_copy = self.order

        # Looping through each warehouse
        for warehouse in self.warehouse:

            # Create object of items to allocate for warehouse
            order_fulfillment = {}

            # Loop through each item in our order
            for item in order_copy.keys():

                # If the item we want is in the warehouse, then get how many items order needs / warehouse has
                if type(warehouse["inventory"]) == dict and item in warehouse["inventory"].keys():
                    order_amount = order_copy[item]
                    warehouse_amount = warehouse["inventory"][item]

                    # If the warehouse has what the order needs, we start allocating
                    if order_amount > 0 and warehouse_amount > 0:

                        # If order > warehouse, then we add all available items to our allocation + update order
                        if order_amount > warehouse_amount:
                            order_fulfillment[item] = warehouse_amount
                            order_copy[item] = order_amount - warehouse_amount

                        # If warehouse > order, take what we need + update order
                        else:
                            order_fulfillment[item] = order_amount
                            order_copy[item] = 0

            # If we took anything, add it to our list
            if order_fulfillment != {}:
                source.append({warehouse["name"]: order_fulfillment})

        # If the order was not completely fulfilled, then return an empty bracket
        for key in order_copy.keys():
            if order_copy[key] != 0:
                self.output = []
                return []

        # If our order was completely fulfilled, then we return the list of warehouses we allocated from
        self.output = source
        return source

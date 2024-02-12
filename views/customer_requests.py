CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

# Function that get all locations
def get_all_customers():
    return CUSTOMERS

# Function with a single parameter that gets employee by id
def get_single_customer(id):
    # Variable to hold the found employee, if it exists
    requested_customer = None
    # Iterate the EMPLOYEES list above. Very similar to the for..of loops used in JavaScript.
    for custromer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key instead of the dot notation that JavaScript used.
        if custromer["id"] == id:
            requested_customer = custromer

    return requested_customer

# Function that creates a new customer
def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

# Function that deletes a customer
def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


# Function that updates customer
def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

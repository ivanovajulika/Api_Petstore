from api import Store


store = Store()

""" You can run all tests at once by selecting a file
pytest -s -v tests/test_pet.py """


def test_get_pet_inventories():
    """Returns the list of pets, verifies if there are animals available for an order"""
    status, result = store.get_store_inventory()
    assert status == 200
    assert int(result["available"]) > 0


def test_post_new_order(random_order_id, headers):
    """Creates an order for a pet, verifies if the order is complete"""
    data = {"id": random_order_id, "status": "placed", "complete": True}
    status, result = store.post_order(data, headers)
    print(result)
    assert status == 200
    assert result["complete"] is True


def test_get_order_by_id(order_id, headers, random_order_id):
    """Gets an order by ID, if order not found, create a new one"""
    status, result = store.get_order_by_id(order_id)
    if status != 200:
        data = {"id": random_order_id, "status": "placed", "complete": "True"}
        status, result = store.post_order(data, headers)
        print(result)
    else:
        print(result)
    assert status == 200


def test_delete_order_by_id(order_id):
    """Delete an existing order"""
    status, result = store.delete_order_by_id(order_id)
    assert status == 200
    assert int(result["message"]) == order_id
    print(result["message"])

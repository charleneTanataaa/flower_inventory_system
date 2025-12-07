import os
import json
import project

TEST_FILE = "test_flowers.json"
def setup_function():
    """Runs before each test case."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    project.FLOWER_FILE = TEST_FILE

    sample_data = {
        "rose": {"price": 20, "stock": 10},
        "tulip": {"price": 15, "stock": 5}
    }

    with open(TEST_FILE, "w") as f:
        json.dump(sample_data, f)


def teardown_function():
    """Runs after each test case."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_flower():
    msg = project.add_flower("Lily", "30", "7")
    assert "Added" in msg

    data = project.load_json(TEST_FILE)
    assert "lily" in data
    assert data["lily"]["price"] == 30
    assert data["lily"]["stock"] == 7

def test_update_flower():
    msg = project.update_flower("rose", "25", "12")
    data = project.load_json(TEST_FILE)

    assert "updated" in msg.lower()
    assert data["rose"]["price"] == 25
    assert data["rose"]["stock"] == 12

def test_update_flower_keep_values():
    msg = project.update_flower("rose", "-", "-")
    data = project.load_json(TEST_FILE)

    assert data["rose"]["price"] == 20
    assert data["rose"]["stock"] == 10

def test_remove_flower():
    msg = project.remove_flower("rose")
    daata = project.load_json(TEST_FILE)

    assert "removed" in msg.lower()
    assert "rose" not in data

def test_sell_flower():
    msg = project.sell_flower("tulip", 3)
    data = project.load_json(TEST_FILE)

    assert "Remaining stock" in msg
    assert data["tulip"]["stock"] == 2


def test_sell_flower_not_enough_stock():
    msg = project.sell_flower("tulip", 100)
    assert msg == "Not enough stock."

def test_search_flower():
    result = project.search_flower("ro")
    assert "Rose" in result


def test_search_flower_no_match():
    result = project.search_flower("xxx")
    assert result == "No flower found."

def test_load_data():
    output = project.load_data()
    assert "Rose" in output
    assert "Tulip" in output

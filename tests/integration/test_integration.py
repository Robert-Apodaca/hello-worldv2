from app.main import add

def test_integration_add():
    # Simulate integration by calling multiple times
    result = add(add(1, 2), add(3, 4))
    assert result == 10

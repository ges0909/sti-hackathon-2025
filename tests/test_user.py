import pytest
from database.models.user import User


def test_user_creation():
    """Test User model creation with all fields."""
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)

    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@test.com"
    assert user.age == 30


def test_user_creation_without_age():
    """Test User model creation with nullable age field."""
    user = User(first_name="Jane", last_name="Smith", email="jane@test.com")

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.email == "jane@test.com"
    assert user.age is None


def test_user_repr():
    """Test User model string representation."""
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)

    repr_str = repr(user)
    assert "John" in repr_str
    assert "Doe" in repr_str
    assert "john@test.com" in repr_str
    assert "30" in repr_str


def test_user_tablename():
    """Test User model table name."""
    assert User.__tablename__ == "users"


def test_user_id_autoincrement():
    """Test User model has auto-increment primary key."""
    user = User(first_name="Test", last_name="User", email="test@test.com")

    # ID should be None before saving to database
    assert user.id is None


def test_user_with_id():
    """Test User model with explicit ID."""
    user = User(
        id=1,
        first_name="Test", 
        last_name="User", 
        email="test@test.com",
        age=25
    )
    
    assert user.id == 1
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.email == "test@test.com"
    assert user.age == 25

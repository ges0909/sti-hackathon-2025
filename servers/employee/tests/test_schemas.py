import pytest
from pydantic import ValidationError
from schemas import UserBase, UserDto


class TestUserBase:
    """Test UserBase validation."""

    def test_valid_user(self):
        """Test creating a valid user."""
        user = UserBase(
            first_name="John", last_name="Doe", email="john.doe@example.com", age=30
        )
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.age == 30

    def test_invalid_email(self):
        """Test invalid email format."""
        with pytest.raises(ValidationError):
            UserBase(first_name="John", last_name="Doe", email="invalid-email", age=30)

    def test_empty_first_name(self):
        """Test empty first name."""
        with pytest.raises(ValidationError):
            UserBase(first_name="", last_name="Doe", email="john@example.com", age=30)

    def test_empty_last_name(self):
        """Test empty last name."""
        with pytest.raises(ValidationError):
            UserBase(first_name="John", last_name="", email="john@example.com", age=30)

    def test_negative_age(self):
        """Test negative age."""
        with pytest.raises(ValidationError):
            UserBase(
                first_name="John", last_name="Doe", email="john@example.com", age=-1
            )

    def test_age_too_high(self):
        """Test age over 150."""
        with pytest.raises(ValidationError):
            UserBase(
                first_name="John", last_name="Doe", email="john@example.com", age=151
            )

    def test_age_none(self):
        """Test age can be None."""
        user = UserBase(first_name="John", last_name="Doe", email="john@example.com")
        assert user.age is None

    def test_boundary_ages(self):
        """Test boundary age values."""
        # Age 0
        user_0 = UserBase(
            first_name="Baby", last_name="Doe", email="baby@example.com", age=0
        )
        assert user_0.age == 0

        # Age 150
        user_150 = UserBase(
            first_name="Old", last_name="Doe", email="old@example.com", age=150
        )
        assert user_150.age == 150


class TestUserDto:
    """Test UserDto validation."""

    def test_valid_user_dto(self):
        """Test creating a valid UserDto."""
        user = UserDto(
            id=1, first_name="John", last_name="Doe", email="john@example.com", age=30
        )
        assert user.id == 1
        assert user.first_name == "John"

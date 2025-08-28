import pytest
from pydantic import ValidationError
from validation import CreateUserRequest, UpdateUserRequest
from models import Gender


def test_create_user_request_valid():
    """Test valid CreateUserRequest."""
    request = CreateUserRequest(
        first_name="John",
        last_name="Doe", 
        email="john@example.com",
        age=30,
        gender="male"
    )
    assert request.first_name == "John"
    assert request.gender == Gender.MALE


def test_create_user_request_gender_case_insensitive():
    """Test gender validation is case insensitive."""
    request = CreateUserRequest(
        first_name="Jane",
        last_name="Doe",
        email="jane@example.com", 
        age=25,
        gender="FEMALE"
    )
    assert request.gender == Gender.FEMALE


def test_create_user_request_gender_none():
    """Test gender can be None."""
    request = CreateUserRequest(
        first_name="Alex",
        last_name="Smith",
        email="alex@example.com",
        age=28
    )
    assert request.gender is None


def test_create_user_request_invalid_gender():
    """Test invalid gender raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        CreateUserRequest(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            age=30,
            gender="invalid"
        )
    assert "Invalid gender 'invalid'" in str(exc_info.value)


def test_update_user_request_valid():
    """Test valid UpdateUserRequest."""
    request = UpdateUserRequest(
        last_name="Doe",
        first_name="Johnny",
        gender="other"
    )
    assert request.last_name == "Doe"
    assert request.first_name == "Johnny"
    assert request.gender == Gender.OTHER


def test_update_user_request_partial():
    """Test UpdateUserRequest with only required fields."""
    request = UpdateUserRequest(last_name="Smith")
    assert request.last_name == "Smith"
    assert request.first_name is None
    assert request.gender is None


def test_update_user_request_invalid_gender():
    """Test invalid gender in UpdateUserRequest."""
    with pytest.raises(ValidationError) as exc_info:
        UpdateUserRequest(
            last_name="Doe",
            gender="wrong"
        )
    assert "Invalid gender 'wrong'" in str(exc_info.value)


def test_all_gender_values():
    """Test all valid gender enum values."""
    for gender_value in ["male", "female", "other"]:
        request = CreateUserRequest(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            age=25,
            gender=gender_value
        )
        assert request.gender == Gender[gender_value.upper()]
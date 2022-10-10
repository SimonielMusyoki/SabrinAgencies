from email.mime import base
import pytest


def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    """Test that the users model get_short_name method works"""
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    """Test that the user models get_full_name method workds"""
    full_name = f"{base_user.first_name.title()} {base_user.last_name.title}"
    assert base_user.get_full_name == full_name


def test_base_user_email_is_normalized(base_user):
    email = "simoniel@SIMONIEL.COM"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """Test that an admin's email is normalized"""
    email = "simoniel@SIMONIEL.COM"
    assert super_user.email == email.lower()


def test_super_user_is_staff(user_factory):
    """Test that an error is raised when an admin has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "superusers must is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    """Test that an error is raised when an admin user has is_superuser set to False"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "superusers must is_superuser=True"


def test_create_user_with_no_email(user_factory):
    """Test that creating a user with no email raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_with_no_username(user_factory):
    """test that creating a user with no username creates an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "Users must provide a username"


def test_create_user_with_no_first_name(user_factory):
    """Test that creating a user with no first_name creates an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must provide a first name"


def test_create_user_with_no_last_name(user_factory):
    """Test that creating a user with no last_name creates an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "users must provide a last name"


def test_create_superuser_with_no_email(user_factory):
    """Test that creating a superuser with no email raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"


def test_create_superuser_with_no_password(user_factory):
    """Test that creating a superuser with no password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "superusers must provide a password"


def test_user_email_incorrect(user_factory):
    """Test that an error is raised when incorrect email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="simoniel.com")
    assert str(err.value) == "You must provide a valid email"

import pytest
from UserRegistration import UserRegistration

@pytest.mark.parameterize("name, expected",[
    ("Lynda",True),
    ("lynda",False),
    ("Ly",False),
    ("Ly3nda",False),
])
def test_validate_first_name(name,expected):
    assert UserRegistration.validate_first_name(name) == expected
    
@pytest.mark.parametrize("name, expected",[
    ("Honest",True),
    ("hon",False),
    ("D",False),
])
def test_validate_last_name(name,expected):
    assert UserRegistration.validate_last_name(name) == expected
    
@pytest.mark.parametrize("email,expected",[
    ("lynda@example.com",True),
    ("lyndaexample.com",False),
    ("lynda@.com",False),
 ])
def test_validate_email(email,expected):
    assert UserRegistration.validate_email(email) == expected

@pytest.mark.parametrize("mobile, expected", [
    ("91 9876543211",True),
    ("919876543211",False),
    ("91 1234567",False),
])
def test_validate_mobile(mobile,expected):
    assert UserRegistration.validate_mobile(mobile) == expected
    
@pytest.mark.parametrize("password, expected", [
    ("Lynda@1234",True),
    ("Y@12",False),
    ("lynda@1234",False),
    ("Lynda@abcd",False),
    ("Lynda1234",False),
    ("Lynda@@1234",False),
])
def test_validate_password(password, expected):
    assert UserRegistration.validate_password(password) == expected
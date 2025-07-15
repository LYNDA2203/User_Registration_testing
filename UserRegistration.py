import re

class UserRegistration:
    @staticmethod
    def validate_first_name(name):
        return bool(re.fullmatch(r'[A-Z][a-z]{2,}',name))
    
    @staticmethod
    def validate_last_name(name):
        return bool(re.fullmatch(r'[A-Z][a-z]{1,}',name))
    
    @staticmethod
    def validate_email(email):
        return bool(re.fullmatch(r'[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}]',email))
    
    @staticmethod
    def validate_mobile(mobile):
        return bool(re.fullmatch(r'\d{1,3}\s\d{10}',mobile))

    @staticmethod
    def password_min_length(password):
        return len(password) >= 8
    
    @staticmethod
    def password_has_uppercase(password):
        return bool(re.search(r'[A-Z]',password))
    
    @staticmethod
    def password_has_numeric(password):
        return bool(re.search(r'\d',password))
    
    @staticmethod
    def password_has_extractly_one_special_char(password):
        return bool(re.search(r'[@#$%^&]',password))
    
    @staticmethod
    def validate_password(password):
        return(
            UserRegistration.password_min_length(password) and
            UserRegistration.password_has_uppercase(password) and
            UserRegistration.password_has_numeric(password) and
            UserRegistration.password_has_extractly_one_special_char(password)
        )
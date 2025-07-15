from UserRegistration import UserRegistration
import logging

logging.baseConfig(
    filename = "registration.log"
    level = logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(message)s'
)

def get_valid_input(prompt,validator,field_name):
    while True:
        try:
            value = input(f"{prompt}")
            if not validator(value):
                raise ValueError(f"Invalid {field_name}.Please try again")
            return value
        except ValueError as e:
            print(e)
            
def main():
    print("_"*10,"User Registration","-"*10)
    first_name = get_valid_input("Enter First Name: ",UserRegistration.validate_first_name,"First Name")
    last_name = get_valid_input("Enter the Last Name: ",UserRegistration.validate_last_name,"Last Name")
    email = get_valid_input("Enter Email id: ",UserRegistration.validate_email,"Email")
    mobile = get_valid_input("Enter mobile(e.g., 91 9876432510): ",UserRegistration.validate_mobile,"Mobile")
    password = get_valid_input("Enter Password: ",UserRegistration.validate_password,"Password")
    
    print("\n Registration Successful!!!")
    print(f"User: {first_name}{last_name}\nEmail:{email}\nMobile:{mobile}")
    
if __name__ == "__main__":
    main()
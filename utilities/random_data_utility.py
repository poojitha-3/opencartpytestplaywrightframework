from faker import Faker
import random
import string

class RandomDataUtility:
    def __init__(self):
        self.faker = Faker()

    def get_first_name(self):
        return self.faker.first_name()
    def get_last_name(self):
        return self.faker.last_name()
    def get_name(self):
        return self.faker.name()
    def get_email(self):
        return self.faker.email()
    def get_phone_number(self):
        return self.faker.phone_number()
    def get_username(self):
        return self.faker.user_name()

    def get_password(self):
        return self.faker.password()
    def get_confirm_password(self):
        return self.faker.confirm_password()

    def get_country(self):
        return self.faker.country()
    def get_city(self):
        return self.faker.city()
    def get_state(self):
        return self.faker.state()
    def get_pincode(self):
        return self.faker.pincode()
    def get_address(self):
        return self.faker.address()
    def get_random_alphanumeric(self,length:int):
        chars=string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    def get_random_numeric(self,length:int):
        return ''.join(random.choice(string.digits) for _ in range(length))




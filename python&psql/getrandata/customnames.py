from faker import Faker

# Instantiate the Faker object
fake = Faker()

# Generate fake data
def get_customer():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
    }

# this will run whenever you run the file using python app.file
if __name__ == '__main__':
    print(get_customer())
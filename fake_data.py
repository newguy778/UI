from faker import Faker

data = Faker()


def get_Name():
    return data


print(list(data))

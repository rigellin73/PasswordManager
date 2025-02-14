import json

FILENAME = "data.json"

def write_data_in_file(new_data):
    with open(FILENAME, mode="w") as file:
        json.dump(new_data, file, indent=4)

def read_data_from_file():
    try:
        with open(FILENAME) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def update_data_in_file(website, email, password):
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    data = read_data_from_file()
    data.update(new_data)
    write_data_in_file(data)

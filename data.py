FILENAME = "data.txt"

def write_data_in_file(website, email, password):
    with open(FILENAME, mode="a") as file:
        str_to_write = f"{website} | {email} | {password}\n"
        file.write(str_to_write)

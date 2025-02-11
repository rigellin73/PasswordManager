FILENAME = "data.txt"

class Data:
    def __init__(self):
        self.website = ""
        self.email = ""
        self.password = ""

    def add_data(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password

    def write_in_file(self):
        with open(FILENAME, mode="a") as file:
            str_to_write = f"{self.website} | {self.email} | {self.password}\n"
            file.write(str_to_write)

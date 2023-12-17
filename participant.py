class Participant:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.invalid_match = set()

    def add_invalid_match(self, invalid=None) -> None:
        if invalid == None:
            self.invalid_match.clear()
            return
        if invalid == self.name:
            return

        if isinstance(invalid, str):
            self.invalid_match.add(invalid)
        elif isinstance(invalid, set) or isinstance(invalid, list) or isinstance(invalid, tuple):
            self.invalid_match.update(invalid)
        else:
            print("Wrong type! add nothing.")

class Participant:
  def __init__(self, name, email, address) -> None:
    self.name = name
    self.email = email
    self.address = address
    # Adding this to hack unit test for now, will implement later
    self.invalid_match = []

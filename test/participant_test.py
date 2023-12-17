from ..participant import Participant

class TestParticipant:
    def setup_method(self):
        self.name = "name"
        self.email = "name@email.com"
        self.address = "address"

    def test_create_Participant(self):
        participant = Participant(self.name, self.email, self.address)
        assert participant.name == self.name
        assert participant.email == self.email
        assert participant.address == self.address

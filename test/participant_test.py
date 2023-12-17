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

    def test_add_invalid_match(self):
        name1 = "name1"
        name2 = "name2"
        name3 = "name3"
        name4 = "name4"
        participant = Participant(self.name, self.email, self.address)
        # add str
        participant.add_invalid_match(name1)
        participant.add_invalid_match(name2)
        assert name1 in participant.invalid_match and name2 in participant.invalid_match
        # no self name
        participant.add_invalid_match(self.name)
        assert not self.name in participant.invalid_match
        # add list
        participant.add_invalid_match([name3, name4])
        assert participant.invalid_match == set([name1, name2, name3, name4])
        # clear Set
        participant.add_invalid_match()
        assert not participant.invalid_match

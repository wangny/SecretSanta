import os
import json
from participant import Participant
from load_data import ParticipantLoader

class TestParticipantLoader():
    def setup_method(self):
        self.JSON_EXT = ".json"
        self.participant_loader = ParticipantLoader()

        filename = os.path.join(os.path.dirname(__file__), "Participants_test.json")
        self.participant_loader.load(filename=filename)

    def test_load(self):
        assert isinstance(self.participant_loader.participants, dict)
        assert isinstance(self.participant_loader.invalid_matches, list)

    # def test_create_Participant(self):
    #     if (self.participant_loader.participants):
    #         participant = self.participant_loader.participants[0]
    #         assert not participant.name == "", "No Name!"

    def test_check_participant_format(self):
        if (self.participant_loader.participants):
            assert isinstance(list(self.participant_loader.participants.values())[0], Participant), "Invalid format for ParticipantLoader.participants"

    def test_check_invalid_match(self):
        if (self.participant_loader.invalid_matches):
            assert len(self.participant_loader.invalid_matches[0]) == 2, "Invalid format for ParticipantLoader.invalid_matches"

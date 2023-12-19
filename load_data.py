import json
from participant import Participant

class ParticipantLoader():
    """
    Read JSON file and create Participant objects and invalid match list

    """

    def __init__(self):
        """
        self.participant: {name: Participant}
        self.invalid_match: [[str, str]]
        """
        self.participants = {}
        self.invalid_matches = []
        self.__error_tag = "Loading Error: "

    def load(self, filename="./data/Participants_test.json") -> list:
        with open(filename) as f:
            data = json.load(f)

        for participant in data["participants"]:
            if participant["name"] == None or participant["name"] == "":
                raise Exception(self.__error_tag + "name is null.")
            try:
                name = participant["name"]
                email = participant["email"]
                address = participant["address"]
            except Exception:
                raise Exception(self.__error_tag + "missing information")

            self.participants[name] = Participant(name, email, address)

        self.__set_matches_format(data["invalid_matches"])

        for match in self.invalid_matches:
            self.participants[match[0]].invalid_match.add(match[1])
            self.participants[match[1]].invalid_match.add(match[0])

        return self.participants

    def __set_matches_format(self, invalid_matches):
        for invalid_match in invalid_matches:
            if not len(invalid_match) == 2:
                raise Exception(self.__error_tag + "invalid format for invalid_matches")
        self.invalid_matches = invalid_matches

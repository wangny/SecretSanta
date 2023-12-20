import os
import random
from participant import Participant
from load_data import ParticipantLoader


def secret_santa():
    print("Secret Santa!")
    loader = ParticipantLoader()
    filename = os.path.join(os.path.dirname(__file__), "test", "Participants_test.json")
    participants = loader.load(filename)
    invalid_matches = get_matches(participants)
    for (p1, p2) in invalid_matches:
        print("[" + p1.name + ", " + p2.name + "]")

def get_matches(participants: Participant) -> [(Participant, Participant)]:
    """generate matches of Participant and assignee"""
    match = []
    while not check_valid(match):
        assignee = random.sample(participants, k=len(participants))
        match = list(zip(participants, assignee))
    return match


def check_valid(match) -> bool:
    """check if contain no invalid matches"""
    if len(match) == 0:
        return False

    for senta, assignee in match:
        if senta == assignee:
            return False
        if assignee.name in senta.invalid_match:
            return False

    return True


if __name__ == "__main__":
    secret_santa()

import random
import email_service as email
from participant import Participant
from load_data import ParticipantLoader


def secret_santa():
    print("=== Secret Santa starts ===")
    participants = ParticipantLoader().load()
    matches = get_matches(participants)
    for (receiver, sender) in matches:
        email.send_email(email.compose_email(receiver, sender))
    print("=== Secret Santa ends ===")

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

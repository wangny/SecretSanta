import smtplib
from email.message import EmailMessage
from .participant import Participant
import random


def secret_santa():
    print("secret_santa")


def load_participant() -> [Participant]:
    pass


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
        if senta.invalid_match.count(assignee.name) > 0:
            return False

    return True


def send_email() -> bool:
    pass


if __name__ == "__main__":
    secret_santa()

from email_service import compose_email
from participant import Participant

participants = [
    Participant("a", "a@email.com", "a address"),
    Participant("b", "b@email.com", "b address"),
    Participant("c", "c@email.com", "c address"),
]


def test_compose_email():
    result = compose_email(participants[0], participants[1])

    assert result.get_all("TO") == [participants[1].email]

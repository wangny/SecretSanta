from ..secretsanta import get_matches
from ..participant import Participant

participants = [
    Participant("a", "a@email.com", ""),
    Participant("b", "", ""),
    Participant("c", "", ""),
]


def test_get_matches_return_match_list():
    result = get_matches(participants)

    assert len(result) == len(participants)


def test_get_matches_no_self_match():
    result = get_matches(participants)

    for senta, assignee in result:
        assert senta != assignee

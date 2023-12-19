from secretsanta import get_matches
from participant import Participant

participants = [
    Participant("a", "a@email.com", "a address"),
    Participant("b", "b@email.com", "b address"),
    Participant("c", "c@email.com", "c address"),
]


# test everyone appears once and only once
def test_get_matches_return_match_list():
    result = get_matches(participants)

    assert len(result) == len(participants)
    assert (
        set([r[0].name for r in result]) - set([p.name for p in participants]) == set()
    )


def test_get_matches_no_self_match():
    result = get_matches(participants)
    for senta, assignee in result:
        assert senta != assignee

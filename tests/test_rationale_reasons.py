from resumeforge.tailoring.prioritizer import (
    TailoringPrioritizer,
)


def test_build_rationale_message():

    prioritizer = TailoringPrioritizer()

    assert prioritizer._build_rationale(
        "skill",
        "Azure",
    ) == (
        "Promoted skill: Azure"
    )

def test_build_rationale_message_with_reason():

    prioritizer = TailoringPrioritizer()

    assert prioritizer._build_rationale(
        "skill",
        "Azure",
        "matched requested skills",
    ) == (
        "Promoted skill: Azure (matched requested skills)"
    )




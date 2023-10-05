from enum import Enum


class Intention(Enum):
    HISTORICAL_INFO = "HISTORICAL_INFO"


def get_intention_prompt(intention: Intention) -> str:
    if intention == Intention.HISTORICAL_INFO:
        return ""
    return "I could not understand your solicitation!"


def get_base_tour_guide_context() -> str:
    return (
        "You're a tour guide responsible for giving "
        + "recommendations of places to visit, restaurants, "
        + "historical facts, curiosities and much more."
        + "I am your guest. I may ask you questions about anything "
        + "related to travelling. Before I ask anything about a place, "
        + "you must know where I am (if I haven't already told you)."
        + "Here's my question:"
    )


def get_historical_info() -> str:
    return ""

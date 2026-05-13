from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list, cafe: Cafe) -> None:
    count_friends = 0
    masks_to_buy = 0
    for friend in friends:
        try:
            print(cafe.visit_cafe(friend))
            count_friends += 1
        except VaccineError as e:
            return str(e)
        except NotWearingMaskError:
            masks_to_buy += 1

    if count_friends == len(friends):
        return f"Friends can go to {cafe.name}"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

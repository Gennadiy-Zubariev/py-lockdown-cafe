from datetime import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.now().date():
                raise OutdatedVaccineError("All friends should be vaccinated")
        else:
            raise NotVaccinatedError("All friends should be vaccinated")

        if visitor.get("wearing_a_mask", False) is False:
            raise NotWearingMaskError(
                f"visitor {visitor['name']} "
                f"should wear a mask"
            )
        else:
            return f"Welcome to {self.name}"

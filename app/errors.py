class VaccineError(Exception):
    """Base class for exceptions related to the virus."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor without being vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor with an outdated vaccine."""


class NotWearingMaskError(Exception):
    """Raised when a visitor without wearing a mask."""

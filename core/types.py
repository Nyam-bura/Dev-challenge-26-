# core/types.py

class DataType:
    """
    Base class for all data types.
    Represents the 'domain' concept from database theory.
    """

    def validate(self, value):
        raise NotImplementedError("Subclasses must implement validate()")


class Integer(DataType):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f"Expected INT, got {type(value).__name__}"
            )
        return True
    
class Text(DataType):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f"Expected TEXT, got {type(value).__name__}"
            )


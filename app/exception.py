class ValidationError(Exception):
    def __init__(self, msg: object) -> None:
        super().__init__(msg)
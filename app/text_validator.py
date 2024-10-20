class TextValidator:
    MAX_TEXT_LENGTH = 10000

    @staticmethod
    def validate(text: str) -> bool:

        if not text.strip():
            return False
        if len(text) > TextValidator.MAX_TEXT_LENGTH:
            return False
        return True

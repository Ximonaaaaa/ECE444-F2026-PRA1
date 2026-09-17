class utils:
    @staticmethod
    def reversed(number: int) -> int:
        if not isinstance(number, int):
            raise TypeError
        return int(str(number)[::-1])

    @staticmethod
    def formatter(number: int):
        if not isinstance(number, int):
            raise TypeError
        return bin(number), oct(number)
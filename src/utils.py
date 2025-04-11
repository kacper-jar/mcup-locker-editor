class Utils:
    @staticmethod
    def get_bool(value):
        if value.lower() in {'false', '0', 'no', 'off'}:
            return False
        elif value.lower() in {'true', '1', 'yes', 'on'}:
            return True
        else:
            raise ValueError(f"Invalid value for boolean.")
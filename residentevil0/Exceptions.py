from Options import OptionError

class RE0OptionError(OptionError):
    def __init__(self, msg):
        msg = f"There was a problem with your RE0 YAML options. {msg}"

        super().__init__(msg)


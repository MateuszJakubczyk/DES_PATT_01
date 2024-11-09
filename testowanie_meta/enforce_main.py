class EnforceAttributeMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_attribute' not in dct:
            raise TypeError(f"Klasa musi miec atrybut - 'required_attribute'")
        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=EnforceAttributeMeta):
    required_attribute = "Jestem obecny!!"
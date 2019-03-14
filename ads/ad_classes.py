from enum import Enum, auto


class AdClasses(Enum):
    GENERIC = auto()
    MIDDLE_AGED_MEN = auto()
    FAMILIES = auto()

    def get_image_path(self):
        if self == AdClasses.GENERIC:
            return "soccer_ball.jpg"

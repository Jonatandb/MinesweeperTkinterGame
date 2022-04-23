import settings


def height_percentage(percentage):
    return int(settings.HEIGHT * percentage / 100)


def width_percentage(percentage):
    return int(settings.WIDTH * percentage / 100)

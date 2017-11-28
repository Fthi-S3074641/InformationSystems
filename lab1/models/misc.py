import random

from lab1.config import IMG_WIDTH, IMG_HEIGHT, RAIN_SCARCITY


def gen_random_data():
    return [[gen_random_val() for _ in range(IMG_WIDTH)] for _ in range(IMG_HEIGHT)]


def gen_random_val():
    val = random.randint(0, 100)
    return val if val > RAIN_SCARCITY else 0

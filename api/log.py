import logging
import sys

import colorlog
from environs import Env

env = Env()
env.read_env()
config: dict = {}

LEVEL = env.str("S_LOGLEVEL", "INFO").upper()
FORMAT = (
    "%(asctime)s - %(process)-5d - %(log_color)s%(levelname)-8s%(reset)s | %(message)s"
)

handler = colorlog.StreamHandler(stream=sys.stdout)
handler.setFormatter(colorlog.ColoredFormatter(FORMAT))

log = logging.getLogger()
log.addHandler(handler)
log.setLevel(LEVEL)

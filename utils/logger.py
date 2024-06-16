import logging
from logging.handlers import TimedRotatingFileHandler
import datetime

from app.config import Config



logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
formatter.converter = lambda *args: datetime.datetime.now(tz=Config.TIMEZONE).timetuple()


handler = TimedRotatingFileHandler(f"logs/logfile.log", when="midnight", interval=1, backupCount=7)
handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(handler)


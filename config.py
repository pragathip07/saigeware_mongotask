import logging
import sys
import anticrlf


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(anticrlf.LogFormatter('%(asctime)s  %(levelname)s  %(message)s', '%Y-%m-%d %H:%M:%S'))
logger.addHandler(handler)


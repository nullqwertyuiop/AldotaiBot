from loguru import logger

from util.jsonTool import create_json, read_json

setting = read_json("./config.json5")
logger.info("config.json read")


def save_config():
    create_json("config.json5", setting)

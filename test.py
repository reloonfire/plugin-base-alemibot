from bot import alemiBot

import logging
import time

from plugins.help import HelpCategory
from util.message import edit_or_reply
from util.permission import is_allowed
from util.command import filterCommand

logger = logging.getLogger(__name__)

HELP = HelpCategory("Plugin-Test")

HELP.add_help(["test-plugin"], "Its lonely day...",
              "It's plugin day!")
@alemiBot.on_message(is_allowed & filterCommand(["test-plugin"], list(alemiBot.prefixes)))
async def test(client, message):
    logger.info("PogFace")
    before = time.time()
    msg = await edit_or_reply(message, "` → ` a sunny day")
    after = time.time()
    latency = (after - before) * 1000
    await msg.edit(f"` → ` a sunny day `({latency:.0f}ms)`")
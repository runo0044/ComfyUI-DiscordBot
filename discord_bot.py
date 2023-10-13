import os
from logging import getLogger, StreamHandler

import coloredlogs
import discord



def discord_bot():
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel("DEBUG")
    logger.addHandler(handler)
    logger.propagate = False
    coloredlogs.install("DEBUG", logger=logger, fmt="%(asctime)s %(levelname)s     %(name)s %(message)s",
                        field_styles={'asctime': {'color': 'green'}, 'levelname': {'color': 'blue', 'bold': True},
                                      'name': {'color': 'magenta'}, 'programname': {'color': 'cyan'}},
                        level_styles={'asctime': {'color': 'green'}, 'levelname': {'color': 'magenta', 'bold': True},
                                      'name': {'color': 'blue'}, 'programname': {'color': 'cyan'},
                                      'debug': {'color': 'blue', 'bold': True},
                                      'info': {'color': 'white', 'bold': True},
                                      'warning': {'color': 'yellow', 'bold': True},
                                      'error': {'color': 'red', 'bold': True},
                                      'critical': {'color': 'red', 'bold': True}})

    # get api key
    if os.getenv('DISCORD_API_KEY') is None:
        logger.critical(" Error : environment variable \"DISCORD_API_KEY\" is not found")
        exit(1)

    # set bot intents
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        logger.info(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author.id != client.user.id:
            logger.info('on_message')

    with open("api_log.txt", mode="a", encoding="utf-8") as f:
        f.write("Bot start at " + discord.utils.utcnow().strftime("%Y: %m/%d %H:%M:%S") + "\n")
    client.run(os.getenv('DISCORD_API_KEY'), log_handler=None)
    with open("api_log.txt", mode="a", encoding="utf-8") as f:
        f.write("Bot stop  at " + discord.utils.utcnow().strftime("%Y: %m/%d %H:%M:%S") + "\n")

from twitchio.ext import commands
from twitchio.errors import AuthenticationError
from .osc_client import OSCClient


class TwitchChatBotError:
    """Helper class to deal with try catches"""
    def __init__(self, config: dict) -> None:
        self._config = config

    def run(self) -> None:
        """Mimic the real twitch bot"""
        try:
            twitch_bot = TwitchChatBot(self._config)
            twitch_bot.run()
        except AuthenticationError as error:
            print(f"Error signing in: {error}. May need to make a new token")


class TwitchChatBot(commands.Bot):
    """A class to deal with twitch integration"""
    def __init__(self, config: dict) -> None:
        """Initialize the TwitchChatBot.

        Args:
            config (dict): The config file for the app
        """
        super().__init__(
            token=config["ACCESS_TOKEN"],
            prefix="!",
            initial_channels=config["CHANNEL"],
        )
        self._config = config
        self.osc = OSCClient(config)

    async def event_ready(self):
        """"Event handler for when the bot is ready.

        Called when the bot has successfully logged in and is ready to chat
        """
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        """Event handler for incoming chat messages.

        Args:
            message: The message containing information about the chat.
        """
        if message.echo:
            return
        msg = f"{message.author.name}:{message.content}"
        self.osc.append_message(msg)
        if self._config["PRINT_CHAT_LOG"]:
            print(msg)


if __name__ == '__main__':
    test = {}
    bot = TwitchChatBot(test)
    try:
        print("Bot Starting")
        bot.run()
    except AuthenticationError as e:
        print(f"{e} Please create a new token.")

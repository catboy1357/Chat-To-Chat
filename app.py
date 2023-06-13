from utls import FileManager
from utls import TwitchChatBotError

class App_Test:
    def __init__(self) -> None:
        fm = FileManager()
        if isinstance(fm.config, dict):
            bot = TwitchChatBotError(fm.config)
            bot.run()
        else:
            input()


if __name__ == '__main__':
    App_Test()

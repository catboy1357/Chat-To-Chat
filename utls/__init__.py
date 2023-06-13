"""A set of classes to deal with signing in and managing Twitch and VRChat OSC
"""
from .files import FileManager
# from .authenticator import Authenticator
from .twitch_bot import TwitchChatBot, TwitchChatBotError
from .osc_client import OSCClient
from .version import __version__
__all__ = [
    'FileManager',
    # 'Authenticator',
    'TwitchChatBot',
    "TwitchChatBotError",
    "OSCClient",
    "__version__"
]

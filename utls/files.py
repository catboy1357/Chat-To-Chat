"""Class to deal with file management."""
from os import path
import json
import sys


class FileManager:
    """A class to deal with the files for the app.

    Args:
        config_file str: The user config file. (Default Config.json)
    """

    def __init__(self, config_file: str = "config.json") -> None:
        required_data = {
            "CHANNEL": ["your_channel"],
            "ACCESS_TOKEN": "bots_client_token",
        }
        default_config = {
            "CLIENT_ID": "bots_client_id (not implemented)",
            "CLIENT_SECRET": "bots_client_id (not implemented)",
            "Comment": {
                "Required data": f"Please update {required_data.keys()}"
                .replace("dict_keys(['", "").replace("'", "").replace("])", ""),
                "Delay info": "A MSG_DELAY >1.5 will be rate limited by VRC",
                "Not implemented": "CLIENT_ID and CLIENT_SECRET do not do anything yet.",
            },
            "VRC_IP": "127.0.0.1",
            "VRC_PORT": 9000,
            "MSG_DELAY": 1.5,
            "BIG_MSG_DELAY": 3,
            "BIG_MSG_LENGTH": 100,
            "PRINT_CHAT_LOG": False
        }
        self.config = self.load_config(
            config_file,
            required_data,
            default_config
        )

    def load_config(
        self,
        config_file: str,
        required_data: dict,
        default_config: dict
    ) -> dict | None:
        """Checks the configuration file validity.

        Args:
            config_file (str): The path and extension of the config file.
            user_data (dict): The default values that need to be set.
            default_config (dict): The default values that dont need to be set.

        Returns:
            dict | None: Returns dict if the config file is ready to use.
        """
        # Get the absolute path of the current script
        # script_dir = path.dirname(path.abspath(__file__))
        # config_path = path.join(script_dir, config_file)

        # Running as a bundled executable
        if getattr(sys, 'frozen', False):
            script_dir = path.dirname(sys.executable)
            config_path = path.join(script_dir, config_file)

            if not path.exists(config_path):
                print(f"No config file found, generating new '{config_file}'")
                self.create_default_config(
                    config_path, required_data, default_config)
                return None

        # Running in a development environment
        else:
            script_dir = path.dirname(path.abspath(__file__))
            # Attempt to locate the config file
            search_dirs = [script_dir, path.dirname(script_dir)]
            for directory in search_dirs:
                config_path = path.join(directory, config_file)
                if path.isfile(config_path):
                    break
            else:
                # If the config file is not found, create a new one
                print(f"No config file found, generating new '{config_file}'")
                self.create_default_config(
                    config_path, required_data, default_config)
                return None

        # Load the file and check if it has been updated
        with open(config_path, encoding='utf-8') as file:
            config = json.load(file)

        # check if the config file as the required updates
        if self._is_config_valid(config, required_data):
            return config

        # if the config file has not been updated tell the user
        print(f"Please update the config file\
'{config_file}' before running the bot.")
        print(
            f"Make sure {required_data.keys()} are all set."
            .replace("dict_keys(['", "")
            .replace("'", "")
            .replace("])", "")
        )
        return None

    def create_default_config(
        self,
        config_file: str,
        required_data: dict,
        default_config: dict
    ) -> None:
        """Creates a default configuration file if it doesn't exist.

        Args:
            config_file (str): The path and extension of the config file.
            user_data (dict): The required values in the config.
            default_config (dict): The default values in the config.
        """

        # Create a new dictionary with user_data followed by default_config
        merged_config = {**required_data, **default_config}

        with open(config_file, 'w', encoding='utf-8') as file:
            json.dump(merged_config, file, indent=4)

    def _is_config_valid(self, config: dict, user_data: dict) -> bool:
        """A function to check for default values in user_data.
        These values need to be filled in in config.

        Args:
            config (dict): The in use data file for the application.
            user_data (dict): The default values that need to be set.

        Returns:
            bool: returns true if the values have been changed.
        """
        # Check if the key is not present in config
        # or if the value in config is the same as in user_data
        for key, value in user_data.items():
            if key not in config or config[key] == value:
                return False
        # If all user_data values have been changed, return True
        return True


if __name__ == '__main__':
    fm = FileManager()
    print(fm.config)

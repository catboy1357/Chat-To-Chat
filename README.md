# Chat to Chat

Chat to Chat is an application that bridges the gap between Twitch chat and the in-game chat box of VRChat. With Chat to Chat, you can display your Twitch chat messages directly in VRChat, allowing other users to see and interact with your chat in real-time.

## How it Works

Chat to Chat utilizes a Twitch chat bot that listens to incoming messages from your Twitch channel. The bot then sends these messages via the OSC protocol to a specified IP address and port associated with VRChat. The messages are received by VRChat and displayed in the in-game chat box, making it visible to other users.

## Version

Alpha Version: 0.1.0

# Installation

### Download

- Download the source code or the compiled EXE file from the [releases](https://github.com/catboy1357/chat-to-chat/releases) page.

## Configuration

1. Generate a Twitch bot token:
   - Visit [Twitch Token Generator](https://twitchtokengenerator.com/)
   - Generate a token for the bot with read permissions.
   - Copy the generated access token.

2. Edit the `config.json` file:
   - Open the downloaded source code folder.
   - Locate the `config.json` file.
   - Open the file in a text editor.
   - Update the following configuration options:
     - `"CHANNEL"`: Specify your Twitch channel name.
     - `"ACCESS_TOKEN"`: Paste the access token you generated.
   - Optional settings to update.
     - `"VRC_IP"`: Set the IP address of the computer running VRChat.
     - `"VRC_PORT"`: Set the port number for OSC communication.
     - `"MSG_DELAY"`: Specify the delay between sending individual messages.
     - `"BIG_MSG_DELAY"`: Specify the delay for sending longer messages.
     - `"BIG_MSG_LENGTH"`: Set the maximum length of a single message before using big message delay.
     - `"PRINT_CHAT_LOG"`: Enable/disable printing chat log messages to the console.
   - Save the file after making the necessary changes.

# Usage

### Enable OSC
Before using the application, make sure to enable the OSC feature in VRChat:

1. Open the **Action Menu** by pressing the *R*  key on desktop or *holding the menu button* in VR.
2. Navigate to **Options**.
3. Select **OSC**.
4. Toggle **Enable** to activate the OSC feature.
5. You may need to reboot VRChat for the changes to take effect.

Now, the application is ready to synchronize the Twitch chat messages with the VRChat in-game chat box.

## Running from compiled EXE

1. Double-click the downloaded `Chat-To-Chat` File
2. The application will start running. And will generate a new `config.json` file.
3. Update the `config.json` file with your Token and Twitch channel.
4. Double-click run `Chat-To-Chat` again.

The application will start running, and you will see the chat messages from your Twitch channel being displayed in the VRChat in-game chat box.

## Running from Source Code

1. Make sure you have Python 3.x installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).
2.  Download or clone the source code repository from GitHub.
```shell
git clone https://github.com/catboy1357/chat-to-chat.git
```
3. Install the required dependencies using pip.
```shell
pip install -r requirements.txt
```
4. Run the `app.py` file to generate a config file.
This will create a `config.json` file with default configuration options.
5. Edit the `config.json` file and update the necessary configuration options as mentioned in the "Configuration" section of this README.
6. Run the application again.
The application will start running, and you will see the chat messages from Twitch being displayed in the VRChat chat box.
7. Feel free to modify the source code and customize the application according to your needs.

## Contributing
**Contributions to this project are welcome**. Feel free to open issues and submit pull requests to help improve the application.

Application is in **alpha stage** of development. As such there maybe issues. Reporting issues and providing feed back about other Twitch integrations you wanna see can help shape this repo.

If you have specific requirements or want to add new features to the Chat to Chat application, you are encouraged to **fork the repository and extend it** to suit your needs. 
Feel free to modify the code, add new functionalities, or integrate with other platforms.

## Todo

- [ ] Add support for customizing chat message appearance.
- [ ] Add symbols for mods and vips
- [ ] Add bits and subs integration
- [ ] Add hype train support
- [ ] Add a ui to update config
- [ ] Add better oauth authentication
- [ ] More

# License
This project is licensed under the [MIT License.](https://en.wikipedia.org/wiki/MIT_License)
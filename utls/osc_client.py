"""Class to deal with OSC messages."""
from time import sleep
import threading
from pythonosc.udp_client import SimpleUDPClient


class OSCClient:
    """OSCClient class for sending messages via OSC protocol."""

    def __init__(self, config: dict) -> None:
        """Initializes the OSCClient object.

        Args:
            vrc_ip (str, optional): The Ip of the computer running VRChat. Defaults to "127.0.0.1".
            vrc_port (int, optional): Port number for OSC communication. Defaults to 9000.
        """
        self._client = SimpleUDPClient(config["VRC_IP"], config["VRC_PORT"])
        self._queue = []
        self._block = ""
        self._max_len = 144
        self._lock = threading.Lock()
        self._queue_notify = threading.Condition()
        self._config = config

        self._start_threads()

    def append_message(self, message: str) -> None:
        """Appends a message to the queue for sending.

        Args:
            message (str): Message to be sent
        """
        chunks = [
            message[i:i + self._max_len - 1]
            for i in range(0, len(message), self._max_len - 1)
        ]

        with self._lock:
            self._queue.extend(chunks)

            self._queue_notify.acquire()
            self._queue_notify.notify()
            self._queue_notify.release()

    def _proses_queue(self) -> None:
        """Processes the message queue. """
        while True:
            while not self._queue:
                self._queue_notify.acquire()
                try:
                    self._queue_notify.wait(timeout=1)
                finally:
                    self._queue_notify.release()

            self._check_len()

    def _check_len(self):
        """Checks the length of the current block and sends to send or wait."""
        new_line = "\u2028"
        msg = self._queue[0]

        if len(self._block) + len(msg) + len(new_line) <= self._max_len:
            with self._lock:
                if self._block != "":
                    self._block += new_line
                self._block += msg
                self._queue.pop(0)
        else:
            sleep(1)

    def _timer(self) -> None:
        """Sends the block of messages at regular intervals.
        """
        while True:
            # grabs the block of text data locally and clears it.
            with self._lock:
                block = self._block
                self._block = ""

            # if nothing is the queue do nothing
            if block != "":
                self._client.send_message(
                    "/chatbox/input",
                    [block, True, False]
                )

            sleep(self._dynamic_delay())

    def _dynamic_delay(self) -> float:
        """change the delay based off the block len

        Returns:
            float: The time before the next message
        """
        delay = self._config["MSG_DELAY"]
        if len(self._block) >= self._config["BIG_MSG_LENGTH"]:
            delay = self._config["BIG_MSG_DELAY"]

        return delay

    def _start_threads(self) -> None:
        """Starts the processing and timer threads. """
        threads = []
        threads.append(threading.Thread(target=self._proses_queue))
        threads.append(threading.Thread(target=self._timer))

        for thread in threads:
            thread.daemon = True
            thread.start()

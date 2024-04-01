from enum import Enum


class ObservationType(str, Enum):
    READ = "read"
    """The content of a file
    """

    BROWSE = "browse"
    """The HTML content of a URL
    """

    RUN = "run"
    """The output of a command
    """

    RECALL = "recall"
    """The result of a search
    """

    CHAT = "chat"
    """A message from the user
    """

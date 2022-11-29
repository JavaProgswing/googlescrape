class GoogleScrapeError(Exception):
    pass


class InvalidURLException(GoogleScrapeError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class InvalidPathException(GoogleScrapeError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

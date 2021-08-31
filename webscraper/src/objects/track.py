

class Track:
    def __init__(self, title: str, url: str, uploaded_by: str):
        self.title = title
        self.url = url
        self.uploaded_by = uploaded_by

    def __str__(self) -> str:
        encoded_bytes = "\"{0}\", \"{1}\", \"{2}\"".format(self.title, self.url, self.uploaded_by).encode('unicode-escape')
        return encoded_bytes.decode()

    def print(self):
        print(self.__str__())

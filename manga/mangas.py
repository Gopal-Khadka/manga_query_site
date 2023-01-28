class Manga:
    def __init__(self, **kwargs) -> None:
        self.title = kwargs.get("title")
        self.image = kwargs.get("image")
        self.genre = kwargs.get("genre")
        self.authors = kwargs.get("authors")
        self.status = kwargs.get("status")
        self.rank = kwargs.get("rank")
        self.release = kwargs.get("release")
        self.url = kwargs.get("url")
        self.plot = kwargs.get("plot")
        self.chapters = kwargs.get("chapters")
        self.story = kwargs.get("story")
        self.volumes = kwargs.get("volumes")
        self.type = kwargs.get("type")
        self.syn= kwargs["syn"].replace("[","").replace("]","").replace("'","")

        self.en_title = kwargs.get("title_en")

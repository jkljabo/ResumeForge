class DummyExporter:

    def __init__(self):
        self.document = None
        self.destination = None

    def export(
        self,
        document,
        destination,
    ):
        self.document = document
        self.destination = destination
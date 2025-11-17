from abc import ABC, abstractmethod
from parsers import InvoiceParse, TorgParse, UPDParse, BaseParser


class BaseRecognisers(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def recognise(self) -> list | dict:
        pass


class ParserFactory:
    parsers = {
        "УПД": UPDParse,
        "Фактура": InvoiceParse,
        "Торг": TorgParse
    }

    @staticmethod
    def get_parsers(doc_type, text) -> BaseParser:
        return ParserFactory.parsers.get(doc_type)(text)


class PDFRecogniser(BaseRecognisers):
    def recognise(self) -> list | dict:
        pass


class ImageRecogniser(BaseRecognisers):
    def recognise(self) -> list | dict:
        # позже перенеси в отдельный класс TypeDetector + нарушение SRP.
        recognised_text = f"based on {self.file_path}"
        recognised_text_type = "УПД"

        parser: BaseParser = ParserFactory.get_parsers(recognised_text_type, recognised_text)

        return parser.parse()

from abc import ABC, abstractmethod

from app.parsers import UPDParse
from parsers import BaseParser


class BaseRecognisers(ABC):
    def __init__(self, file_path, parser_factory):
        self.file_path = file_path
        self.parser_factory = parser_factory

    @abstractmethod
    def recognise(self) -> list | dict:
        pass


class PDFRecogniser(BaseRecognisers):
    def recognise(self) -> list | dict:
        pass


class ImageRecogniser(BaseRecognisers):
    def recognise(self) -> list | dict:
        # позже перенеси в отдельный класс TypeDetector + нарушение SRP.
        recognised_text = f"based on {self.file_path}"
        recognised_text_type = "УПД"

        parser: BaseParser = self.parser_factory.get_parser(recognised_text_type, recognised_text)

        return parser.parse()


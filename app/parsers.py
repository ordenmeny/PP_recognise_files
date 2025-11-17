from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, recognised_text: str):
        self.recognised_text = recognised_text

    @abstractmethod
    def parse(self) -> dict:
        pass


class InvoiceParse(BaseParser):
    def parse(self):
        pass


class UPDParse(BaseParser):
    def parse(self):
        return {"status": "parsed", "text": self.recognised_text}


class TorgParse(BaseParser):
    def parse(self):
        pass
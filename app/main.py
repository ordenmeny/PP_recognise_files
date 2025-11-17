from recognisers import ImageRecogniser, PDFRecogniser
from parsers import InvoiceParse, TorgParse, UPDParse, BaseParser


class ParserFactory:
    parsers = {
        "УПД": UPDParse,
        "Фактура": InvoiceParse,
        "Торг": TorgParse,
    }

    @staticmethod
    def get_parser(doc_type, text) -> BaseParser:
        parser_cls = ParserFactory.parsers.get(doc_type)

        if parser_cls is None:
            raise ValueError(f"Unknown document type: {doc_type}")

        return parser_cls(text)


class RecogniserFactory:
    @staticmethod
    def get_recogniser(file_path):
        ext = file_path.split('.')[-1]

        if ext in ('png', 'jpg'):
            return ImageRecogniser(file_path, ParserFactory())
        elif ext == 'pdf':
            return PDFRecogniser(file_path, ParserFactory())

        return None


class RunnerClass:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        rec = RecogniserFactory.get_recogniser(self.file_path)
        if rec is None:
            raise ValueError("Unsupported extension")

        return rec.recognise()


run = RunnerClass('test.png')
print(run.run())

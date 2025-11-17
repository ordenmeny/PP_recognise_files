from recognisers import ImageRecogniser, PDFRecogniser


class RecogniserFactory:
    @staticmethod
    def get_recogniser(file_path):
        ext = file_path.split('.')[-1]

        if ext in ('png', 'jpg'):
            return ImageRecogniser(file_path)
        elif ext == 'pdf':
            return PDFRecogniser(file_path)

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

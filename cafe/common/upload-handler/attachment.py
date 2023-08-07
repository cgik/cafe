class Attachment:
    def __init__(self, file_name: str, file_path: str):
        self.name = file_name
        self.path = file_path

    def file_type(self):
        return self.name.split('.')[-1]

    def attachment_text(self):
        with open(self.path, 'rb') as f:
            return f.read()

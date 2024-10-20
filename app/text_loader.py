class TextLoader:
    def load_bulk_text(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

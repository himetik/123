import spacy


class SentenceSplitter:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def replace_newlines(self, text):
        return text.replace('\n', ' ')

    def split_text(self, text):
        text = self.replace_newlines(text)
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents]


if __name__ == "__main__":
    splitter = SentenceSplitter()

    text = input("Введите текст: ")

    sentences = splitter.split_text(text)

    print("Предложения:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

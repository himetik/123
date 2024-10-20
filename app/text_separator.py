import spacy


class SentenceSplitter:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def split_text(self, text):
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]


if __name__ == "__main__":
    splitter = SentenceSplitter()

    text = input("Введите текст: ")

    sentences = splitter.split_text(text)

    print("Предложения:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{sentence}")

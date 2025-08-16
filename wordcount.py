class WordCounter:
    def __init__(self, filename):
        self.filename = filename
        self.text = ""

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8", errors="ignore") as f:
            self.text = f.read()
        print("File successfully read the file!")

    def count_words(self):
        words = self.text.split()
        total_words = len(words)
        print(f"Total number of words in '{self.filename}' is : {total_words}")

def main():
    counter = WordCounter("demo.txt")
    counter.read_file()
    counter.count_words()

if __name__ == "__main__":
    main()

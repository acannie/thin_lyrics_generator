import random

class ThinLyricsGenerator:
    nouns = {
        "夢": "ゆめ",
        "愛": "あい",
        "風": "かぜ",
        "翼": "つばさ",
        "風": "かぜ",
        "涙": "なみだ",
        "歌": "うた"
    }

    subjects = {
        "僕": "ぼく",
        "私": "わたし"
    }

    particles = ["を", "に", "で", "と", "に", "が"]
    
    verbs = {
        "結ぶ": "むすぶ",
        "祈る": "いのる",
        "そよぐ": "そよぐ",
        "流す": "ながす"
    }

    scats = ["la la la", "hu", "ah", "oh", "ルルル"]

    def __init__(self):
        pass

    def count_sound_num(self):
        pass

    def generate_phrase(self):
        random_num = random.randrange(len(ThinLyricsGenerator.nouns))
        word, furigana = random.choice(list(ThinLyricsGenerator.nouns.items()))
        print(word, end="")

        random_num = random.randrange(len(ThinLyricsGenerator.particles))
        print(ThinLyricsGenerator.particles[random_num], end="")

        random_num = random.randrange(len(ThinLyricsGenerator.verbs))
        word, furigana = random.choice(list(ThinLyricsGenerator.verbs.items()))
        print(word)

    def generate_scat(self):
        random_num = random.randrange(len(ThinLyricsGenerator.scats))
        for i in range(2):
            print(ThinLyricsGenerator.scats[random_num])

    def generate_lyrics(self):
        for i in range(10):
            self.generate_phrase()
        self.generate_scat()

if __name__ == "__main__":
    thin_lyrics_generator = ThinLyricsGenerator()
    thin_lyrics_generator.generate_lyrics()
import BrailleList


class BrailleToKorean:
    def __init__(self, brailles):
        self.brailles = brailles
        self.initial_consonant = BrailleList.ConsonantBraille.initial_consonant
        self.final_consonant = BrailleList.ConsonantBraille.final_consonant
        self.vowel = BrailleList.VowelBraille.vowel
        self.abbreviation = BrailleList.AbbreviationBraille.abbreviation
        self.number = BrailleList.NumberBraille.number
        self.mark = BrailleList.MarkBraille.mark
        self.result = ""
        self.word = ""
        self.idx = 0
        self.braille = ()

    def translate(self):
        while self.idx != len(self.brailles):
            rest_braille = len(self.brailles) - self.idx

            while True:
                if rest_braille >= 3 and self.three_braille():
                    self.get_mark()
                    self.idx += 3
                    break

                check = self.two_braille()
                if rest_braille >= 2 and check:
                    self.get_word(check)
                    self.idx += 2
                    break

                check = self.one_braille()
                if rest_braille >= 1 and check:
                    self.get_word(check)
                    self.idx += 1
                    break

    def three_braille(self):
        self.braille = self.brailles[self.idx:self.idx + 3]

        if self.mark.__contains__(self.braille):
            return True
        return False

    def two_braille(self):
        self.braille = self.brailles[self.idx:self.idx + 2]

        if self.mark.__contains__(self.braille):
            return 1
        if self.abbreviation.__contains__(self.braille):
            return 2
        if self.initial_consonant.__contains__(self.braille):
            return 3
        if self.final_consonant.__contains__(self.braille):
            return 4
        if self.vowel.__contains__(self.braille):
            return 5
        return 0

    def one_braille(self):
        self.braille = self.brailles[self.idx]

        if self.mark.__contains__(self.braille):
            return 1
        if self.abbreviation.__contains__(self.braille):
            return 2
        if self.number.__contains__(self.braille):
            return 6
        if self.initial_consonant.__contains__(self.braille):
            return 3
        if self.final_consonant.__contains__(self.braille):
            return 4
        if self.vowel.__contains__(self.braille):
            return 5
        return 0

    def get_mark(self):
        self.result += self.mark.get(self.braille)

    def get_abbreviation(self):
        except_word = "나다마바자카타파하"

        if except_word.__contains__(self.abbreviation.get(self.braille)) or len(self.abbreviation.get(self.braille)) == 2:
            self.word += self.abbreviation.get(self.braille)
        else:
            self.result += self.abbreviation.get(self.braille)

    def get_initial_consonant(self):
        self.word += self.initial_consonant.get(self.braille)

    def get_final_consonant(self):
        self.word += self.final_consonant.get(self.braille)

    def get_vowel(self):
        self.word += self.vowel.get(self.braille)

    def get_number(self):
        self.word += self.number.get(self.braille)

    def get_word(self, check):
        if check == 1:
            self.get_mark()
        elif check == 2:
            self.get_abbreviation()
        elif check == 3:
            self.get_initial_consonant()
        elif check == 4:
            self.get_final_consonant()
        elif check == 5:
            self.get_vowel()
        elif check == 6:
            self.get_number()

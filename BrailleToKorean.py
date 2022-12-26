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
        self.idx = 0
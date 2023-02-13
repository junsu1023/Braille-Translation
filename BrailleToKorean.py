import BrailleList
from hangul_utils import split_syllables, join_jamos


# 자모음 분리 함수
def split_word(word):
    return split_syllables(word)


class BrailleToKorean:
    def __init__(self, brailles):
        self.brailles = tuple(brailles)
        self.braille = ()
        self.initial_consonant = BrailleList.ConsonantBraille.initial_consonant
        self.final_consonant = BrailleList.ConsonantBraille.final_consonant
        self.vowel = BrailleList.VowelBraille.vowel
        self.abbreviation = BrailleList.AbbreviateBraille.abbreviation
        self.number = BrailleList.NumberBraille.number
        # self.mark = BrailleList.MarkBraille.mark
        self.elid_leeeung = BrailleList.AbbreviateBraille.elid_leeeung
        self.result = ""
        self.word = ""
        self.idx = 0
        self.except_word = "가나다마바사자카타파하까따빠싸짜"

    # 번역부
    def translate(self):
        try:
            while self.idx != len(self.brailles):  # 모든 점자를 순환
                rest_braille = len(self.brailles) - self.idx  # 남은 점자의 갯수

                self.check_braille_length(rest_braille)

            self.is_empty_word()
            return self.result

        except ValueError:
            return False

    # 갯수에 따른 점자 찾는 함수
    def check_braille_length(self, length):
        check = self.three_braille()
        if length >= 3 and check:
            self.get_word(check, 3)
            self.idx += 3
            return

        check = self.two_braille()
        if length >= 2 and check:
            self.get_word(check, 2)
            self.idx += 2
            return

        check = self.one_braille()
        if length >= 1 and check:
            self.get_word(check, 1)
            self.idx += 1
            return

        raise ValueError

    # 길이가 3인 점자가 있는지 확인
    def three_braille(self):
        self.braille = self.brailles[self.idx:self.idx + 3]

        if self.abbreviation.__contains__(self.braille):
            return 2
        # if self.mark.__contains__(self.braille):
        #     return 1
        return 0

    # 길이가 2인 점자가 있는지 확인(우선순위가 맞는지는 모르겠음)
    def two_braille(self):
        self.braille = self.brailles[self.idx:self.idx + 2]

        if self.abbreviation.__contains__(self.braille):
            return 2
        if self.initial_consonant.__contains__(self.braille):
            return 3
        if self.final_consonant.__contains__(self.braille):
            return 4
        if self.vowel.__contains__(self.braille):
            return 5
        # if self.mark.__contains__(self.braille):
        #     return 1
        return 0

    # 길이가 1인 점자가 있는지 확인(우선순위가 맞는지는 모르겠음)
    def one_braille(self):
        self.braille = self.brailles[self.idx]

        # 밑의 기호가 여러 개일 때 ex) ○○○ 처리
        # if self.braille == (0, 0, 0, 1, 1, 1):
        #     self.idx += 1
        #     closeIndex = self.brailles.index((1, 1, 1, 0, 0, 0))
        #     for i in range(self.idx, closeIndex + 1):
        #         if self.brailles[i] == (1, 0, 1, 1, 0, 1):
        #             self.result += "×"
        #         elif self.brailles[i] == (0, 0, 1, 0, 1, 1):
        #             self.result += "○"
        #         elif self.brailles[i] == (0, 0, 1, 1, 0, 1):
        #             self.result += "△"
        #         elif self.brailles[i] == (0, 1, 1, 0, 1, 1):
        #             self.result += "□"
        #         elif self.brailles[i] == (1, 1, 1, 0, 0, 0):
        #             self.result += ""
        #         self.idx += 1
        #     return 0

        # 맨 뒤가 온점(.)일 경우, 온점과 같은 점자가 있어 미리 처리
        # if self.idx == len(self.brailles) - 1 and self.brailles[self.idx] == (0, 1, 0, 0, 1, 1):
        #     self.is_empty_word()
        #     self.idx += 1
        #     self.result += "."
        #     return 0

        # 띄어쓰기일 경우 클래스로 만들 시 데이터가 단 한 개이므로 굳이 필요없다 생각하여 바로 처리
        if self.brailles[self.idx] == (0, 0, 0, 0, 0, 0):
            self.is_empty_word()
            self.idx += 1
            self.result += " "
            return 0
        if self.abbreviation.__contains__(self.braille):
            return 2
        if self.initial_consonant.__contains__(self.braille):
            return 3
        if self.final_consonant.__contains__(self.braille):
            return 4
        if self.vowel.__contains__(self.braille):
            return 5
        # if self.mark.__contains__(self.braille):
        #     return 1
        if self.number.__contains__(self.braille):
            return 6
        return 0

    # 각 점자 찾는 함수로 이동
    def get_word(self, check, braille_length):
        # if check == 1:
        #     self.get_mark_braille()
        if check == 2:
            self.get_abbreviate_braille(braille_length)
        elif check == 3:
            self.get_initial_consonant_braille()
        elif check == 4:
            self.get_final_consonant_braille()
        elif check == 5:
            self.get_vowel_braille()
        elif check == 6:
            self.get_number_braille()

    # 기호 점자 찾는 함수
    # def get_mark_braille(self):
    #     self.is_empty_word()
    #     self.result += self.mark.get(self.braille)

    # 약어 점자 찾는 함수
    def get_abbreviate_braille(self, braille_length):
        if self.elid_leeeung.__contains__(self.braille):  # 초성이 ㅇ인 약자는 word에 추가
            if self.word != "" and list(self.vowel.values()).__contains__(self.word[-1]):
                self.combine_word()
            self.word += self.abbreviation.get(self.braille)
            # 겹받침 처리
            if not (self.idx < len(self.brailles) - 1 and
                    (self.brailles[self.idx + braille_length] == (1, 0, 0, 0, 0, 0) or  # 종성 ㄱ
                     self.brailles[self.idx + braille_length] == (0, 1, 0, 0, 0, 1) or  # 종성 ㅁ
                     self.brailles[self.idx + braille_length] == (1, 1, 0, 0, 0, 0) or  # 종성 ㅂ
                     self.brailles[self.idx + braille_length] == (0, 0, 1, 0, 0, 0) or  # 종성 ㅅ
                     self.brailles[self.idx + braille_length] == (1, 0, 1, 0, 0, 0) or  # 종성 ㅈ
                     self.brailles[self.idx + braille_length] == (0, 1, 1, 0, 0, 1) or  # 종성 ㅌ
                     self.brailles[self.idx + braille_length] == (0, 1, 0, 0, 1, 1) or  # 종성 ㅍ
                     self.brailles[self.idx + braille_length] == (0, 0, 1, 0, 1, 1))):  # 종성 ㅎ
                self.combine_word()
            return

        if self.except_word.__contains__(self.abbreviation.get(self.braille)):  # 특정 약어이고, 다음에 모음이 오는 경우
            if self.idx == len(self.brailles) - 1:  # 마지막 위치이면 뒤에 모음 올 수 없으므로 result에 더하기
                self.is_empty_word()
                self.result += self.abbreviation.get(self.braille)
                return
            if (self.vowel.__contains__(self.brailles[self.idx + braille_length]) or
                    self.elid_leeeung.__contains__(self.brailles[self.idx + braille_length])):  # 현재: 가 + 다음: ㅏ -> 현재: ㄱ
                self.word += split_word(self.abbreviation.get(self.braille))[:1]
            else:  # 다음에 오는 단어가 모음이 아니라면 word에 있는 것을 미리 합치고 word에 추가(가나다마바사자카타파하는 앞에 붙일게 없으므로)
                self.is_empty_word()
                self.word += split_word(self.abbreviation.get(self.braille))
            return

        self.result += self.abbreviation.get(self.braille)

    # 초성 점자 찾는 함수
    def get_initial_consonant_braille(self):
        self.is_empty_word()
        self.word += self.initial_consonant.get(self.braille)

    # 종성 점자 찾는 함수
    def get_final_consonant_braille(self):
        self.word += self.final_consonant.get(self.braille)
        self.combine_word()

    # 모음 점자 찾는 함수
    def get_vowel_braille(self):
        if self.word != "":
            # word의 맨 뒤가 모음이라면 단어를 합침
            if list(self.vowel.values()).__contains__(self.word[-1]):
                self.combine_word()

            elif self.except_word.__contains__(self.word[0]):
                splitWord = split_word(self.word[0])
                self.word = splitWord

            self.word += self.vowel.get(self.braille)

        else:
            self.word += self.vowel.get(self.braille)

    # 숫자 점자 찾는 함수
    def get_number_braille(self):
        self.result += self.number.get(self.braille)

    # word가 비어있는지 확인, 비어있지 않다면 단어 합치기
    def is_empty_word(self):
        if self.word != "":
            self.combine_word()

    # 단어 합치는 함수
    def combine_word(self):
        self.replace_word()

        if list(self.vowel.values()).__contains__(self.word[0]):  # word의 맨 앞이 모음일 경우 ㅇ 추가
            self.word = "ㅇ" + self.word

        self.result += join_jamos(self.word)
        self.word = ""

    # 곁받침 처리 위한 함수
    def replace_word(self):
        if self.word.__contains__("ㄱㅅ"):
            self.word = self.word.replace("ㄱㅅ", "ㄳ")
        elif self.word.__contains__("ㄴㅈ"):
            self.word = self.word.replace("ㄴㅈ", "ㄵ")
        elif self.word.__contains__("ㄴㅎ"):
            self.word = self.word.replace("ㄴㅎ", "ㄶ")
        elif self.word.__contains__("ㄹㄱ"):
            self.word = self.word.replace("ㄹㄱ", "ㄺ")
        elif self.word.__contains__("ㄹㅁ"):
            self.word = self.word.replace("ㄹㅁ", "ㄻ")
        elif self.word.__contains__("ㄹㅂ"):
            self.word = self.word.replace("ㄹㅂ", "ㄼ")
        elif self.word.__contains__("ㄹㅅ"):
            self.word = self.word.replace("ㄹㅅ", "ㄽ")
        elif self.word.__contains__("ㄹㅌ"):
            self.word = self.word.replace("ㄹㅌ", "ㄾ")
        elif self.word.__contains__("ㄹㅍ"):
            self.word = self.word.replace("ㄹㅍ", "ㄿ")
        elif self.word.__contains__("ㄹㅎ"):
            self.word = self.word.replace("ㄹㅎ", "ㅀ")
        elif self.word.__contains__("ㅂㅅ"):
            self.word = self.word.replace("ㅂㅅ", "ㅄ")

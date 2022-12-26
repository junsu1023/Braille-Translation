class ConsonantBraille:
    initial_consonant = {(0, 0, 0, 1, 0, 0): "ㄱ",
                         (1, 0, 0, 1, 0, 0): "ㄴ",
                         (0, 1, 0, 1, 0, 0): "ㄷ",
                         (0, 0, 0, 0, 1, 0): "ㄹ",
                         (1, 0, 0, 0, 1, 0): "ㅁ",
                         (0, 0, 0, 1, 1, 0): "ㅂ",
                         (0, 0, 0, 0, 0, 1): "ㅅ",
                         (0, 0, 0, 1, 0, 1): "ㅈ",
                         (0, 0, 0, 0, 1, 1): "ㅊ",
                         (1, 1, 0, 0, 1, 0): "ㅋ",
                         (1, 1, 0, 0, 1, 0): "ㅌ",
                         (1, 0, 0, 1, 1, 0): "ㅍ",
                         (0, 1, 0, 1, 1, 0): "ㅎ",
                         ((0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 0, 0)): "ㄲ",
                         ((0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0)): "ㄸ",
                         ((0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 1, 0)): "ㅃ",
                         ((0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1)): "ㅆ",
                         ((0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 0, 1)): "ㅉ"}

    final_consonant = {(1, 0, 0, 0, 0, 0): "ㄱ",
                       (0, 1, 0, 0, 1, 0): "ㄴ",
                       (0, 0, 1, 0, 1, 0): "ㄷ",
                       (0, 1, 0, 0, 0, 0): "ㄹ",
                       (0, 1, 0, 0, 0, 1): "ㅁ",
                       (1, 1, 0, 0, 0, 0): "ㅂ",
                       (0, 0, 1, 0, 0, 0): "ㅅ",
                       (0, 1, 1, 0, 1, 1): "ㅇ",
                       (1, 0, 1, 0, 0, 0): "ㅈ",
                       (0, 1, 1, 0, 0, 0): "ㅊ",
                       (0, 1, 1, 0, 1, 0): "ㅋ",
                       (0, 1, 1, 0, 0, 1): "ㅌ",
                       (0, 1, 0, 0, 1, 1): "ㅍ",
                       (0, 0, 1, 0, 1, 1): "ㅎ",
                       ((0, 0, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0)): "ㄲ",
                       ((0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 1, 0)): "ㄸ",
                       ((0, 0, 0, 0, 0, 1), (1, 1, 0, 0, 0, 0)): "ㅃ",
                       ((0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 0)): "ㅆ",
                       ((0, 0, 0, 0, 0, 1), (1, 0, 1, 0, 0, 0)): "ㅉ",
                       ((1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0)): "ㄳ",
                       ((0, 1, 0, 0, 1, 0), (1, 0, 1, 0, 0, 0)): "ㄵ",
                       ((0, 1, 0, 0, 1, 0), (0, 0, 1, 0, 1, 1)): "ㄶ",
                       ((0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0)): "ㄺ",
                       ((0, 1, 0, 0, 0, 0), (0, 1, 0, 0, 0, 1)): "ㄻ",
                       ((0, 1, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0)): "ㄼ",
                       ((0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0)): "ㄽ",
                       ((0, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 1)): "ㄾ",
                       ((0, 1, 0, 0, 0, 0), (0, 1, 0, 0, 1, 1)): "ㄿ",
                       ((0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 1, 1)): "ㅀ",
                       ((1, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0)): "ㅄ"}


class VowelBraille:
    vowel = {(1, 1, 0, 0, 0, 1): "ㅏ",
             (0, 0, 1, 1, 1, 0): "ㅑ",
             (0, 1, 1, 1, 0, 0): "ㅕ",
             (1, 0, 1, 0, 0, 1): "ㅗ",
             (0, 0, 1, 1, 0, 1): "ㅛ",
             (1, 0, 1, 1, 0, 0): "ㅜ",
             (1, 0, 0, 1, 0, 1): "ㅠ",
             (0, 1, 0, 1, 0, 1): "ㅡ",
             (1, 0, 1, 0, 1, 0): "ㅣ",
             (1, 1, 1, 0, 1, 0): "ㅐ",
             (1, 0, 1, 1, 1, 0): "ㅔ",
             (1, 0, 1, 1, 1, 1): "ㅚ",
             (1, 1, 1, 0, 0, 1): "ㅘ",
             (1, 1, 1, 1, 0, 0): "ㅝ",
             (0, 1, 0, 1, 1, 1): "ㅢ",
             (0, 0, 1, 1, 0, 0): "ㅖ",
             ((1, 0, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0)): "ㅟ",
             ((0, 0, 1, 1, 1, 0), (1, 1, 1, 0, 1, 0)): "ㅒ",
             ((1, 1, 1, 0, 0, 1), (1, 1, 1, 0, 1, 0)): "ㅙ",
             ((1, 1, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0)): "ㅞ"}


class AbbreviationBraille:
    abbreviation = {(1, 1, 0, 1, 0, 1): "가",
                    (1, 0, 0, 1, 0, 0): "나",
                    (0, 1, 0, 1, 0, 0): "다",
                    (1, 0, 0, 0, 1, 0): "마",
                    (0, 0, 0, 1, 1, 0): "바",
                    (1, 1, 1, 0, 0, 0): "사",
                    (0, 0, 0, 1, 0, 1): "자",
                    (1, 1, 0, 1, 0, 0): "카",
                    (1, 1, 0, 0, 1, 0): "타",
                    (1, 0, 0, 1, 1, 0): "파",
                    (0, 1, 0, 1, 1, 0): "하",
                    ((0, 0, 0, 1, 1, 1), (0, 1, 1, 1, 0, 0)): "것",
                    ((1, 1, 0, 1, 0, 1), (0, 0, 1, 1, 0, 0)): "갓",
                    ((1, 0, 0, 1, 0, 0), (0, 0, 1, 1, 0, 0)): "낫",
                    ((0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 0)): "닷",
                    ((1, 0, 0, 0, 1, 0), (0, 0, 1, 1, 0, 0)): "맛",
                    ((0, 0, 0, 1, 1, 0), (0, 0, 1, 1, 0, 0)): "밧",
                    ((1, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0)): "샀",
                    ((1, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 0)): "캈",
                    ((1, 1, 0, 0, 1, 0), (0, 0, 1, 1, 0, 0)): "탔",
                    ((1, 0, 0, 1, 1, 0), (0, 0, 1, 1, 0, 0)): "팠",
                    ((0, 1, 0, 1, 1, 0), (0, 0, 1, 1, 0, 0)): "핬",
                    (1, 0, 0, 1, 1, 1): "ㅓㄱ",
                    (0, 1, 1, 1, 1, 1): "ㅓㄴ",
                    (0, 1, 1, 1, 1, 0): "ㅓㄹ",
                    (1, 0, 0, 0, 0, 1): "ㅕㄴ",
                    (1, 1, 0, 0, 1, 1): "ㅕㄹ",
                    (1, 1, 0, 1, 1, 1): "ㅕㅇ",
                    (1, 0, 1, 1, 0, 1): "ㅗㄱ",
                    (1, 1, 1, 0, 1, 1): "ㅗㄴ",
                    (1, 1, 1, 1, 1, 1): "ㅗㅇ",
                    (1, 1, 0, 1, 1, 0): "ㅜㄴ",
                    (1, 1, 1, 1, 0, 1): "ㅗㄹ",
                    (1, 0, 1, 0, 1, 1): "ㅡㄴ",
                    (0, 1, 1, 1, 0, 1): "ㅡㄹ",
                    (1, 1, 1, 1, 1, 0): "ㅣㄴ",
                    ((1, 0, 0, 0, 0, 0), (0, 1, 1, 1, 0, 0)): "그래서",
                    ((1, 0, 0, 0, 0, 0), (1, 0, 0, 1, 0, 0)): "그러나",
                    ((1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 1, 0)): "그러면",
                    ((1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 1)): "그러므로",
                    ((1, 0, 0, 0, 0, 0), (1, 0, 1, 1, 1, 0)): "그런데",
                    ((1, 0, 0, 0, 0, 0), (1, 0, 1, 0, 0, 1)): "그리고",
                    ((1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 1, 1)): "그리하여"}


class NumberBraille:
    number = {(0, 0, 1, 1, 1, 1): "",  # 수표(이 점자 다음 하나 이상의 숫자가 온다. 즉, 번역 시 생략.)
              (0, 1, 0, 1, 1, 0): "0",
              (1, 0, 0, 0, 0, 0): "1",
              (1, 1, 0, 0, 0, 0): "2",
              (1, 0, 0, 1, 0, 0): "3",
              (1, 0, 0, 1, 1, 0): "4",
              (1, 0, 0, 0, 1, 0): "5",
              (1, 1, 0, 1, 0, 0): "6",
              (1, 1, 0, 1, 1, 0): "7",
              (1, 1, 0, 0, 1, 0): "8",
              (0, 1, 0, 1, 0, 0): "9"}


# 문자를 점역할 것인지 의논
class MarkBraille:
    mark = {(0, 1, 1, 0, 0, 1): '"',
            (0, 0, 1, 0, 1, 1): '"',
            ((0, 0, 0, 0, 0, 1), (0, 1, 1, 0, 0, 1)): "'",
            ((0, 0, 1, 0, 1, 1), (0, 0, 1, 0, 0, 0)): "'",
            ((0, 0, 1, 0, 0, 1), (0, 0, 1, 0, 0, 1)): "~",
            ((0, 1, 0, 0, 1, 1), (0, 1, 0, 0, 1, 1), (0, 1, 0, 0, 1, 1)): "...",
            ((0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1)): "···",
            (0, 1, 1, 0, 1, 0): "!",
            (0, 1, 0, 0, 1, 1): ".",
            (0, 0, 0, 0, 1, 0): ",",
            (0, 1, 1, 0, 0, 1): "?",
            ((0, 0, 0, 0, 1, 0), (0, 1, 0, 0, 0, 0)): ":",
            ((0, 0, 0, 0, 1, 1), (0, 1, 1, 0, 0, 0)): ";",
            (0, 0, 1, 0, 0, 1): "-",
            ((0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1)): "_",
            ((0, 0, 1, 0, 0, 1), (0, 0, 1, 0, 0, 0)): "_",
            ((0, 0, 1, 0, 1, 0), (0, 0, 1, 0, 1, 0)): "※",
            ((0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 0, 0)): "(",
            ((0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 1, 1)): ")",
            ((0, 1, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0)): "{",
            ((0, 0, 0, 0, 1, 0), (0, 0, 1, 0, 1, 1)): "}",
            ((0, 1, 1, 0, 0, 1), (0, 1, 1, 0, 0, 0)): "(",
            ((0, 0, 0, 0, 1, 1), (0, 0, 1, 0, 1, 1)): ")",
            ((0, 0, 0, 0, 1, 0), (0, 1, 1, 0, 0, 0)): "·",
            ((0, 0, 0, 0, 1, 0), (0, 1, 1, 0, 0, 1)): "<",
            ((0, 0, 1, 0, 1, 1), (0, 1, 0, 0, 0, 0)): ">",
            ((0, 0, 0, 0, 1, 1), (0, 1, 1, 0, 0, 1)): "《",
            ((0, 0, 1, 0, 1, 1), (0, 1, 1, 0, 0, 0)): "》",
            ((0, 0, 0, 1, 1, 1), (0, 0, 1, 1, 0, 0)): "\\",
            ((0, 0, 0, 1, 1, 1), (1, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0)): "×",
            ((0, 0, 0, 1, 1, 1), (0, 0, 1, 0, 1, 1), (1, 1, 1, 0, 0, 0)): "○",
            ((0, 0, 0, 1, 1, 1), (0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0)): "△",
            ((0, 0, 0, 1, 1, 1), (0, 1, 1, 0, 1, 1), (1, 1, 1, 0, 0, 0)): "□",
            ((0, 0, 1, 0, 1, 0), (0, 0, 1, 0, 1, 0)): "*"}
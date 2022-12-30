import BrailleToKorean

if __name__ == "__main__":
    example = ((0, 0, 0, 1, 0, 1), (1, 0, 1, 1, 0, 0), (0, 1, 1, 0, 1, 1), (1, 1, 0, 0, 0, 1), (0, 1, 1, 0, 1, 1))  # 중앙
    example1 = ((0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1), (0, 1, 1, 0, 1, 1))  # 자앙
    example2 = ((0, 0, 0, 1, 1, 0), (0, 1, 0, 0, 0, 0), (0, 1, 0, 1, 0, 1), (0, 1, 0, 0, 0, 1))  # 발음
    print(BrailleToKorean.BrailleToKorean(example).translate())

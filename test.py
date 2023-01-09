from BrailleToKorean import BrailleToKorean


def test():
    test1 = ((0, 0, 0, 1, 0, 1), (1, 0, 1, 1, 0, 0), (0, 1, 1, 0, 1, 1), (1, 1, 0, 0, 0, 1), (0, 1, 1, 0, 1, 1))  # 중앙
    test2 = ((0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1), (0, 1, 1, 0, 1, 1))  # 자앙
    test3 = ((0, 0, 0, 1, 1, 0), (0, 1, 0, 0, 0, 0), (0, 1, 0, 1, 0, 1), (0, 1, 0, 0, 0, 1))  # 발음
    test4 = ((0, 1, 0, 1, 1, 0), (1, 1, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0), (0, 1, 0, 0, 1, 0))  # 하얀
    test5 = ((0, 0, 0, 0, 0, 1), (1, 1, 0, 1, 1, 1), (0, 1, 0, 1, 1, 0), (1, 0, 0, 0, 0, 1), (1, 0, 1, 0, 1, 0))  # 성현이
    test6 = ((0, 0, 0, 0, 0, 1), (1, 1, 0, 1, 1, 1), (0, 0, 0, 1, 0, 0), (1, 1, 1, 1, 1, 1))  # 성공
    test7 = ((0, 0, 0, 0, 1, 1), (1, 0, 1, 1, 0, 0), (1, 1, 0, 1, 1, 0), (0, 0, 0, 1, 0, 0), (1, 0, 0, 0, 1, 1),
             (1, 1, 1, 1, 0, 1), (1, 0, 1, 0, 1, 0), (0, 0, 0, 1, 0, 1), (1, 0, 1, 0, 1, 0), (1, 0, 0, 0, 1, 0),
             (0, 1, 0, 0, 1, 0), (0, 1, 0, 1, 0, 0), (0, 1, 1, 1, 0, 0), (1, 1, 0, 0, 0, 0),
             (0, 1, 0, 1, 0, 0))  # 추운겨울이지만덥다
    test8 = ((1, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1), (0, 0, 1, 1, 0, 0))  # 아예
    test9 = ((1, 1, 1, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0))  # 삯
    test10 = ((1, 1, 0, 0, 0, 1), (0, 1, 0, 0, 1, 0), (1, 0, 1, 0, 0, 0), (0, 1, 0, 1, 0, 0))  # 앉다
    test11 = ((0, 1, 1, 1, 0, 1), (0, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0))  # 읊다
    test12 = ((1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 1, 1), (0, 1, 0, 1, 0, 0))  # 옳다
    test13 = ((1, 0, 1, 1, 1, 1), (0, 0, 0, 1, 0, 0), (1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0))  # 외곬
    test14 = ((1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (0, 1, 0, 0, 0, 1), (0, 0, 0, 1, 0, 0), (1, 0, 1, 0, 1, 0),
              (0, 1, 0, 1, 0, 0))  # 옮기다
    test15 = ((0, 0, 0, 0, 0, 1), (1, 1, 0, 1, 0, 1), (1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0, 1),
              (0, 0, 1, 1, 0, 0), (0, 1, 0, 1, 0, 0))  # 깎았다
    test16 = ((1, 0, 0, 0, 1, 1), (1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 1, 1, 1, 0, 0), (0, 0, 1, 1, 0, 0),
              (0, 1, 0, 1, 0, 0))  # 엮었다
    test17 = ((1, 0, 0, 0, 1, 0), (1, 0, 1, 1, 0, 0), (0, 0, 1, 0, 0, 1), (0, 0, 1, 1, 0, 0))  # 무예
    test18 = ((0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (0, 1, 1, 0, 1, 1), (0, 1, 1, 1, 0, 1), (0, 0, 0, 0, 0, 0),
              (1, 0, 0, 1, 1, 0), (1, 1, 0, 0, 0, 1), (0, 0, 1, 1, 0, 0), (0, 1, 0, 1, 0, 0), (0, 1, 0, 0, 1, 1))  # 땅을 팠다.

    print(BrailleToKorean(test1).translate())
    print(BrailleToKorean(test2).translate())
    print(BrailleToKorean(test3).translate())
    print(BrailleToKorean(test4).translate())
    print(BrailleToKorean(test5).translate())
    print(BrailleToKorean(test6).translate())
    print(BrailleToKorean(test7).translate())
    print(BrailleToKorean(test8).translate())
    print(BrailleToKorean(test9).translate())
    print(BrailleToKorean(test10).translate())
    print(BrailleToKorean(test11).translate())
    print(BrailleToKorean(test12).translate())
    print(BrailleToKorean(test13).translate())
    print(BrailleToKorean(test14).translate())
    print(BrailleToKorean(test15).translate())
    print(BrailleToKorean(test16).translate())
    print(BrailleToKorean(test17).translate())
    print(BrailleToKorean(test18).translate())


test()
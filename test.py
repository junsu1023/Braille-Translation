from BrailleToKorean import BrailleToKorean
import webbrowser
# from TTS import tts


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
              (1, 0, 0, 1, 1, 0), (1, 1, 0, 0, 0, 1), (0, 0, 1, 1, 0, 0), (0, 1, 0, 1, 0, 0))  # 땅을 팠다
    test19 = ((1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0), (1, 0, 1, 0, 1, 0), (0, 0, 0, 0, 0, 1),
              (0, 1, 1, 1, 0, 1), (1, 0, 0, 0, 0, 0))  # 산기슭
    test20 = ((1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 1, 1), (0, 0, 1, 0, 0, 0), (0, 1, 1, 1, 0, 1), (0, 0, 0, 0, 0, 0),
              (1, 0, 0, 1, 0, 0), (1, 0, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1), (0, 1, 0, 1, 0, 0))  # 넋을 놓다
    test21 = ((0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 1), (1, 0, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 0, 0, 0, 0, 1),
              (0, 1, 0, 1, 0, 1), (1, 0, 1, 1, 1, 0), (0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0),
              (1, 0, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1),
              (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1), (1, 1, 1, 0, 0, 0),
              (0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0), (0, 1, 0, 0, 0, 1),
              (0, 0, 0, 0, 0, 1), (1, 1, 1, 0, 0, 0), (0, 1, 1, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 0, 1, 1, 0, 0),
              (0, 1, 1, 0, 1, 1), (1, 0, 1, 0, 1, 0))  # 스위스에 사는 삼십삼살 샴쌍둥이
    test22 = ((1, 0, 1, 1, 1, 1), (1, 1, 0, 0, 0, 1), (0, 1, 0, 0, 1, 0), (0, 1, 0, 1, 0, 0), (1, 0, 1, 1, 1, 1),
              (0, 0, 1, 1, 0, 0), (0, 1, 0, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 1, 0, 0, 0, 1))  # 외안됬댐
    test23 = ((0, 0, 0, 1, 1, 0), (1, 1, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0),
              (0, 0, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0),
              (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 1), (0, 0, 1, 0, 1, 1))  # 뷁궭뚫
    test24 = ((0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 1, 1),
              (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0),
              (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0))  # 똻똵똷
    test25 = ((0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 1, 1),
              (0, 0, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 1, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0),
              (0, 0, 0, 0, 1, 0), (1, 1, 1, 1, 0, 1), (0, 0, 1, 0, 1, 1))  # 꿣궯룷
    test26 = ((0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 0, 1), (1, 1, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 1, 1),
              (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0), (1, 0, 1, 0, 0, 0),
              (0, 0, 0, 0, 0, 1), (0, 0, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0), (1, 1, 1, 0, 1, 0), (0, 1, 0, 0, 0, 0),
              (1, 0, 0, 0, 0, 0))  # 쫧뚽꿹

    test27 = ((0, 1, 0, 1, 0, 0), (1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 1, 0), (0, 1, 0, 1, 1, 0), (1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 0, 0))

    test28 = ((0, 0, 0, 1, 0, 1), (1, 0, 1, 1, 1, 0), (0, 0, 1, 1, 1, 1), (0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 0, 0),
              (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 1), (1, 1, 0, 0, 1, 0), (0, 1, 1, 1, 0, 0), (0, 1, 0, 1, 0, 0),
              (1, 0, 1, 0, 1, 0), (0, 0, 0, 0, 1, 0), (1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 0, 1)) # 제999스터디룸

    print(BrailleToKorean(test1).translate())
    # tts(BrailleToKorean(test1).translate())

    print(BrailleToKorean(test2).translate())
    # tts(BrailleToKorean(test2).translate())

    print(BrailleToKorean(test3).translate())
    # tts(BrailleToKorean(test3).translate())

    print(BrailleToKorean(test4).translate())
    # tts(BrailleToKorean(test4).translate())

    print(BrailleToKorean(test5).translate())
    # tts(BrailleToKorean(test5).translate())

    print(BrailleToKorean(test6).translate())
    # tts(BrailleToKorean(test6).translate())

    print(BrailleToKorean(test7).translate())
    # tts(BrailleToKorean(test7).translate())

    print(BrailleToKorean(test8).translate())
    # tts(BrailleToKorean(test8).translate())

    print(BrailleToKorean(test9).translate())
    # tts(BrailleToKorean(test9).translate())

    print(BrailleToKorean(test10).translate())
    # tts(BrailleToKorean(test10).translate())

    print(BrailleToKorean(test11).translate())
    # tts(BrailleToKorean(test11).translate())

    print(BrailleToKorean(test12).translate())
    # tts(BrailleToKorean(test12).translate())

    print(BrailleToKorean(test13).translate())
    # tts(BrailleToKorean(test13).translate())

    print(BrailleToKorean(test14).translate())
    # tts(BrailleToKorean(test14).translate())

    print(BrailleToKorean(test15).translate())
    # tts(BrailleToKorean(test15).translate())

    print(BrailleToKorean(test16).translate())
    # tts(BrailleToKorean(test16).translate())

    print(BrailleToKorean(test17).translate())
    # tts(BrailleToKorean(test17).translate())

    print(BrailleToKorean(test18).translate())
    # tts(BrailleToKorean(test18).translate())

    print(BrailleToKorean(test19).translate())
    # tts(BrailleToKorean(test19).translate())

    print(BrailleToKorean(test20).translate())
    # tts(BrailleToKorean(test20).translate())

    print(BrailleToKorean(test21).translate())
    # tts(BrailleToKorean(test21).translate())

    print(BrailleToKorean(test22).translate())
    # tts(BrailleToKorean(test22).translate())

    print(BrailleToKorean(test23).translate())
    # tts(BrailleToKorean(test23).translate())

    print(BrailleToKorean(test24).translate())
    # tts(BrailleToKorean(test24).translate())

    print(BrailleToKorean(test25).translate())
    # tts(BrailleToKorean(test25).translate())

    print(BrailleToKorean(test26).translate())
    # tts(BrailleToKorean(test26).translate())

    print(BrailleToKorean(test27).translate())

    print(BrailleToKorean(test28).translate())

    #webbrowser.open("translate.mp3")


test()

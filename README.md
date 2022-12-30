# Braille-Translation  
* BrailleList  
  - 자음(초성, 종성), 모음, 약어, 숫자, 기호의 각 점자를 저장
* RecognizeBraille  
  - 입력받은 사진을 openCV를 통해 점자를 인식하여 점자가 있는 위치는 1, 없는 위치는 0으로 하여 튜플 형식으로 데이터를 반환한다.
  - ex) ![plz0](https://user-images.githubusercontent.com/55648193/210055104-8a1a9a76-1f4e-4623-9ed4-84a0e96ba4f5.jpg)
((0, 0, 1, 1, 1, 1), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1), (0, 1, 0, 1, 0, 1), (0, 1, 1, 0, 1, 1), (1, 1, 0, 0, 0, 1), (0, 1, 0, 0, 1, 0), (1, 0, 0, 1, 0, 0), (1, 1, 1, 0, 1, 0))
* BrailleToKorean
  - RecognizeBraille에서 받은 데이터를 해석하는 역할을 한다.

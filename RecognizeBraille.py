import cv2
import numpy as np


def standard(location):
    line = []
    location = np.sort(location)
    for i in location:
        if len(line) == 0 or i - np.average(line[-1]) > 10:
            line.append([i])
        else:
            line[-1].append(i)

    avg = [int(np.average(i)) for i in line]

    return line, avg


def modify(classify, standard_loc, clist, i):
    for c in range(len(clist)):
        for cl in range(len(classify)):
            if clist[c][i] in classify[cl]:
                clist[c][i] = standard_loc[cl]

    return clist


def findAll_x(dist, center_list):
    x_list = []
    temp = [i[0] for i in center_list]

    for x in temp:
        if x not in x_list:
            x_list.append(x)

    if not ((x_list[1] - x_list[0]) > dist - 10 or (x_list[1] - x_list[0]) < dist + 10):
        x_list.insert(0, x_list[0] - dist)

    i = 0
    while True:
        if i == len(x_list) - 1:
            break

        if x_list[i + 1] - x_list[i] >= int(1.8 * dist):
            if i + 1 % 2 != 0 and x_list[i + 1] - x_list[i] <= 2 * dist and (
                    x_list[i + 2] - (x_list[i + 1] + dist) > 15):
                x_list.insert(i + 2, x_list[i + 1] + dist)

            elif x_list[i + 1] - x_list[i] > 2 * dist:
                x_list.insert(i + 1, x_list[i + 1] - dist)

            i += 1

        else:
            i += 1

    last = len(x_list)
    if last % 2 != 0 and (x_list[last - 1] - x_list[last - 2] >= int(1.7 * dist)):
        x_list.append(x_list[last - 1] + dist)

    return x_list


def pre_processing(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    img = cv2.fastNlMeansDenoising(img, None, 100, 11, 21)

    # 바이너리 이미지 만들기
    ret, thresh_cv = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    # Hough Transition 회전 보정
    lines = cv2.HoughLines(thresh_cv, 1, np.pi / 360, 10, min_theta=np.pi * 0.48, max_theta=np.pi * 0.52)

    if lines is not None:
        lines = lines.reshape([-1, 2])

        theta_avg = np.average(lines[:10, 1])
        angle = (theta_avg - np.pi * 0.5) * 180 / np.pi

        matrix = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), angle, 1)
        thresh_cv = cv2.warpAffine(thresh_cv, matrix, (img.shape[1], img.shape[0]), flags=cv2.INTER_NEAREST)

        return thresh_cv


def find_location(thresh_cv):
    # 중심점 저장 ndarray
    center = np.empty((0, 2), int)

    # 중심점 저장 리스트
    center_list = []

    # Contour
    contours, hierarchies = cv2.findContours(thresh_cv, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 중심점
    for i in contours:
        if 100 < cv2.contourArea(i) < 2000 and cv2.contourArea(i) != 0:
            M = cv2.moments(i)

            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            center_list.append([cx, cy])

            center = np.append(center, np.array([[cx, cy]]), axis=0)  # 클러스터링을 위한 ndarray 추가

    return center, center_list


def modify_location(blank, center, center_list):
    classify_x, standard_x = standard(center[:, 0])
    classify_y, standard_y = standard(center[:, 1])

    dist = (max(standard_y) - min(standard_y)) // 2
    standard_y[1] = standard_y[0] + dist
    standard_y[2] = standard_y[1] + dist

    center_list = modify(classify_x, standard_x, center_list, 0)
    center_list = modify(classify_y, standard_y, center_list, 1)

    center_list = sorted(center_list, key=lambda i: (i[0], i[1]))

    num = 1

    for i in center_list:
        cv2.circle(blank, (i[0], i[1]), 20, (0, 0, 0), 10)
        cv2.putText(blank, str(num), (i[0], i[1]), cv2.FONT_ITALIC, 3.8, (0, 0, 0), 3)

        num += 1

    return dist, center_list


def find_braille(test, dist, center_list):
    x_list = findAll_x(dist, center_list)
    y_list = [i[1] for i in center_list]
    all_list = []
    for x in x_list:
        for y in y_list:
            if [x, y] not in all_list:
                all_list.append([x, y])

    all_list = sorted(all_list, key=lambda i: (i[0], i[1]))

    overlap = []

    for i in range(len(all_list)):
        if all_list[i] in center_list:
            cv2.circle(test, (all_list[i][0], all_list[i][1]), 35, (0, 0, 0), -1)
            overlap.append(1)
        else:
            cv2.circle(test, (all_list[i][0], all_list[i][1]), 20, (0, 0, 0), 10)
            overlap.append(0)

    temp = [overlap[i * 6:(i + 1) * 6] for i in range((len(overlap) - 1 + 6) // 6)]

    braille = [tuple(i) for i in temp]

    return braille


def logic():
    # 이미지 전처리
    thresh_cv = pre_processing('plz0.jpg')

    # 점자 좌표 탐색
    center, center_list = find_location(thresh_cv)

    # 흰색 배경
    blank = np.full(thresh_cv.shape[:], 255, dtype='uint8')
    test = np.full(thresh_cv.shape[:], 255, dtype='uint8')

    # 점자 좌표 보정
    dist, center_list = modify_location(blank, center, center_list)

    # 점자 추출
    braille = tuple(find_braille(test, dist, center_list))
    return braille

import cv2

img_name = input('사진명을 입력해주세요.\n')
img = cv2.imread(f'{img_name}')


def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 밝은 곳은 더 밝게 어두운 곳은 더 어둡게 해야 스케치스러운 느낌을 받을 수 있다
    blr = cv2.GaussianBlur(gray, (71, 71), 0)
    dst = cv2.divide(gray, blr, scale=255)  # 흑백영상을 블러로 나눈 값을 255로 곱함.
    return dst


def cartoonizing(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

    color = cv2.bilateralFilter(image, 12, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


img = pencil_sketch(img)
cv2.imwrite('./img.jpeg', img)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

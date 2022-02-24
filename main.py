# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import cv2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    filenames = [
        "photo_2022-02-24_08-27-31.jpg",
        "photo_2022-02-24_08-27-57.jpg"
    ]
    resultname = "result_"

    imm = [0]*(len(filenames))
    img = [0]*(len(filenames))
    resultm = [0]*(len(filenames)-1)

    for i,f in enumerate(filenames):
        imm[i]=cv2.imread(f)
        img[i]=cv2.cvtColor(imm[i],cv2.COLOR_BGR2GRAY)

    stereo_obj = cv2.StereoBM_create(numDisparities=128, blockSize=15)

    for i in range(len(filenames)-1):
        resultm[i] = stereo_obj.compute(img[i],img[i+1])
        cv2.imwrite(resultname+str(i)+".jpeg",resultm[i])
        cv2.namedWindow(resultname+str(i))
        cv2.imshow(resultname+str(i), resultm[i])

    cv2.waitKey()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

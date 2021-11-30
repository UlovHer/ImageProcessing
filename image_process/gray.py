import cv2

# img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# #灰度化：彩色图像转为灰度图像
# img3 = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# #彩色化：灰度图像转为彩色图像
# # cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS


def gray_cvt(img_path, window_name, ouput_img):
    '''直接使用opencv自带图像颜色空间转换函数'''
    img = cv2.imread(img_path)
    # 读取图像，返回的是一个装有每一个像素点的bgr值的三维矩阵
    gray_cvt_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 灰度化：彩色图像转为灰度图像
    cv2.namedWindow(window_name)
    # 控制显示图片窗口的名字
    cv2.imshow(window_name, gray_cvt_image)
    #显示灰度化后的图像
    cv2.imwrite(ouput_img, gray_cvt_image)
    # 保存当前灰度值处理过后的文件
    cv2.waitKey(0)
    #等待操作
    cv2.destroyAllWindows()
    #关闭显示图像的窗口


def gray_max_rgb(img_path, window_name, ouput_img):
    img = cv2.imread(img_path)
    gray_max_rgb_image = img.copy()
    # 复制图像，用于后面保存灰度化后的图像bgr值矩阵
    img_shape = img.shape
    # 返回一位数组（高，宽，3）获得原始图像的长宽以及颜色通道数，一般彩色的颜色通道为3，黑白为1
    for i in range(img_shape[0]):
        # 按行读取图片的像素bgr
        for j in range(img_shape[1]):
            # 对每一行按照列进行每一个像素格子进行读取
            gray_max_rgb_image[i, j] = max(img[i, j][0], img[i, j][1],
                                           img[i, j][2])
            # 求灰度值
    print(gray_max_rgb_image)
    cv2.namedWindow(window_name)
    # 控制显示图片窗口的名字
    cv2.imshow(window_name, gray_max_rgb_image)
    # 显示灰度化后的图像
    cv2.imwrite(ouput_img, gray_max_rgb_image)
    # 保存当前灰度值处理过后的文件
    cv2.waitKey(0)
    #等待操作
    cv2.destroyAllWindows()
    # 关闭显示图像的窗口


def gray_mean_rgb(input_img, window_name, output_img):
    img = cv2.imread(input_img)
    gray_mean_rgb_image = img.copy()
    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            gray_mean_rgb_image[i,
                                j] = (int(img[i, j][0]) + int(img[i, j][1]) +
                                      int(img[i, j][2])) / 3
    print(gray_mean_rgb_image)
    cv2.namedWindow(window_name)
    #控制显示图片窗口的名字
    cv2.imshow(window_name, gray_mean_rgb_image)
    #显示灰度化后的图像
    cv2.imwrite(output_img, gray_mean_rgb_image)
    # 保存当前灰度值处理过后的文件
    cv2.waitKey()
    #等待操作
    cv2.destroyAllWindows()
    #关闭显示图像的窗口


def gray_weightmean_rgb(wr, wg, wb, input_img, window_name, output_img):
    img = cv2.imread(input_img)
    gray_weightmean_rgb_image = img.copy()
    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            gray_weightmean_rgb_image[i, j] = (int(wr * img[i, j][2]) + int(
                wg * img[i, j][1]) + int(wb * img[i, j][0])) / 3
    print(gray_weightmean_rgb_image)
    cv2.namedWindow(window_name)
    #控制显示图片窗口的名字
    cv2.imshow(window_name, gray_weightmean_rgb_image)
    #显示灰度化后的图像
    cv2.imwrite(output_img, gray_weightmean_rgb_image)
    # 保存当前灰度值处理过后的文件
    cv2.waitKey()
    #等待操作
    cv2.destroyAllWindows()
    #关闭显示图像的窗口


def gray_gamma_weightmean_rgb(wr, wg, wb, gamma, input_img, window_name,
                              output_img):
    img = cv2.imread(input_img)
    gray_gamma_weightmean_rgb_image = img.copy()
    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            fenzi = int((wr * img[i, j][2])**gamma) + int(
                (wg * img[i, j][1])**gamma) + int((wb * img[i, j][0])**gamma)
            fenmu = wr**gamma + wg**gamma + wb**gamma
            gray_gamma_weightmean_rgb_image[i, j] = int(
                (fenzi / fenmu)**(1 / gamma))

    print(gray_gamma_weightmean_rgb_image)
    cv2.namedWindow(window_name)
    #控制显示图片窗口的名字
    cv2.imshow(window_name, gray_gamma_weightmean_rgb_image)
    #显示灰度化后的图像
    cv2.imwrite(output_img, gray_gamma_weightmean_rgb_image)
    # 保存当前灰度值处理过后的文件
    cv2.waitKey()
    #等待操作
    cv2.destroyAllWindows()
    #关闭显示图像的窗口


if __name__ == '__main__':
    input_image = '../data/g.png'
    window_name = 'gray_cvt'
    output_image = "../result/gray/gray_cvt.png"
    gray_cvt(input_image, window_name, output_image)

    window_name = 'gray_max_rgb'
    output_image = "../result/gray/gray_max_rgb.png"
    gray_max_rgb(input_image, window_name, output_image)

    window_name = 'gray_mean_rgb'
    output_image = "../result/gray/gray_mean_rgb.png"
    gray_mean_rgb(input_image, window_name, output_image)

    wr = 0.299
    wg = 0.587
    wb = 0.114
    window_name = 'gray_weightmean_rgb'
    output_image = "../result/gray/gray_weightmean_rgb.png"
    gray_weightmean_rgb(wr, wg, wb, input_image, window_name, output_image)

    wr = 1
    wg = 1.5
    wb = 0.6
    gamma = 2.2
    window_name = 'gray_gamma_weightmean_rgb'
    output_image = "../result/gray/gray_gamma_weightmean_rgb.png"
    gray_gamma_weightmean_rgb(wr, wg, wb, gamma, input_image, window_name,
                              output_image)

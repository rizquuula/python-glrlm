import cv2
from libMatrixByDegree import degree0GLRLM, degree45GLRLM, degree90GLRLM, degree135GLRLM
from libNormalization import normalizationImage
from libGLRLMoperation import SRE, LRE, GLU, RLU, RPC

def prepocessing(firstImage, file):
    max_height = 200
    ratio = firstImage.shape[0]/max_height
    new_width = int(firstImage.shape[1]/ratio)
    # print(max_height, new_width)
    firstImage = cv2.resize(firstImage, (new_width, max_height))

    grayscaling = cv2.cvtColor(firstImage, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayscaling, 100, 255, cv2.THRESH_TOZERO_INV)
    segmentation = cv2.erode(thresh, (5, 5))
    denoise = cv2.erode(thresh, (5, 5))
    # print("Matriks Awal")
    # print(firstImage)
    # cv2.imshow('seg', segmentation)
    bitConversion = 8
    firstImage = normalizationImage(image=denoise,
                                    maxScale=bitConversion)

    # print("\n Setelah Normalisasi")
    # print(firstImage)
    # bitConversion=5
    mat0 = degree0GLRLM(sourceImg=firstImage,
                        grayLevel=bitConversion,
                        runLength=max(firstImage.shape))
    mat45 = degree45GLRLM(sourceImg=firstImage,
                          grayLevel=bitConversion,
                          runLength=max(firstImage.shape))
    mat90 = degree90GLRLM(sourceImg=firstImage,
                          grayLevel=bitConversion,
                          runLength=max(firstImage.shape))
    mat135 = degree135GLRLM(sourceImg=firstImage,
                            grayLevel=bitConversion,
                            runLength=max(firstImage.shape))

    sre = SRE(mat0, mat45, mat90, mat135)
    lre = LRE(mat0, mat45, mat90, mat135)
    glu = GLU(mat0, mat45, mat90, mat135)
    rlu = RLU(mat0, mat45, mat90, mat135)
    rpc = RPC(mat0, mat45, mat90, mat135)
    index = file.split(' ')
    index = index[0]
    # operationType = ['sre', 'lre', 'glu', 'rlu', 'rpc']
    operationresult = [sre, lre, glu, rlu, rpc, index]
    # print('Data Result')
    # print(sre, lre, glu, rlu, rpc, index)

    return operationresult, grayscaling, segmentation

# img = 'database/1 latih nanas 01.jpg'
# imgopen = cv2.imread(img)
# pre = prepocessing(imgopen, '1 latih nanas 01.jpg')
# print(pre)
# cv2.imshow('nee', pre[2])
# cv2.waitKey(0)
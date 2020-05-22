import numpy

def degree0GLRLM(sourceImg, grayLevel=5, runLength=5):
    degree0Matrix = numpy.zeros([grayLevel, runLength])
    counter = 0
    for y in range(sourceImg.shape[0]):
        for x in range(sourceImg.shape[1]):
            # print('coordinate ',y,x)
            nowVal = sourceImg[y][x]
            if x + 1 >= sourceImg.shape[1]:
                nextVal = None
            else:
                nextVal = sourceImg[y][x + 1]

            if nextVal != nowVal and counter == 0:
                # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                degree0Matrix[int(nowVal)][counter] += 1
            elif nextVal == nowVal:
                counter += 1
                # print(y, " val,counter 2 |",nowVal, nextVal, counter)
            elif nextVal != nowVal and counter != 0:
                degree0Matrix[int(nowVal)][counter] += 1
                counter = 0
                # print(y, " val,counter 3 |",nowVal, nextVal, counter)
    # print()
    # print("Gray Level Run Length Matrix degree 0")
    return degree0Matrix

def degree90GLRLM(sourceImg, grayLevel=5, runLength=5):
    degree90Matrix = numpy.zeros([grayLevel, runLength])
    counter = 0
    for x in range(sourceImg.shape[1]):
        for y in range(sourceImg.shape[0]):
            nowVal = sourceImg[y][x]
            if y + 1 >= sourceImg.shape[0]:
                nextVal = None
            else:
                nextVal = sourceImg[y + 1][x]

            if nextVal != nowVal and counter == 0:
                # print(x, " val,counter 1 |",nowVal, nextVal, counter)
                degree90Matrix[int(nowVal)][counter] += 1
            elif nextVal == nowVal:
                counter += 1
                # print(x, " val,counter 2 |",nowVal, nextVal, counter)
            elif nextVal != nowVal and counter != 0:
                degree90Matrix[int(nowVal)][counter] += 1
                counter = 0

    # print()
    # print("Gray Level Run Length Matrix degree 90")
    return degree90Matrix

def degree45GLRLM(sourceImg, grayLevel=5, runLength=5):
    degree45Matrix = numpy.zeros([grayLevel, runLength])

    for y in range(sourceImg.shape[0]):
        # print()
        counter = 0
        i_range = max(sourceImg.shape)
        for i in range(i_range):
            y1 = y - i
            if i >= sourceImg.shape[1] or y1 < 0:
                break
            else:
                nowVal = sourceImg[y1][i]
            # print(y1, i)
            if y1 - 1 < 0 or i + 1 >= sourceImg.shape[1]:
                nextVal = None
            else:
                nextVal = sourceImg[y1 - 1][i + 1]
            # print(y1, i , ' and ', nowVal, nextVal)
            # print(y1,i , ' and ', sourceImg[y1][i])
            if nextVal != nowVal and counter == 0:
                # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                degree45Matrix[int(nowVal)][counter] += 1
            elif nextVal == nowVal:
                counter += 1
                # print(y, " val,counter 2 |",nowVal, nextVal, counter)
            elif nextVal != nowVal and counter != 0:
                degree45Matrix[int(nowVal)][counter] += 1
                counter = 0
                # print(y, " val,counter 3 |",nowVal, nextVal, counter)

    for x in range(sourceImg.shape[1]):
        if x == sourceImg.shape[1] - 1:
            break
        # print()
        counter = 0
        i_range = max(sourceImg.shape)
        for i in range(i_range):
            y_i = -1 - i
            x_i = -1 + i - x
            # print(y_i, x_i)
            if x_i >= 0 or y_i <= -1 - sourceImg.shape[0]:
                break
            else:
                nowVal = sourceImg[y_i][x_i]

            if y_i - 1 <= -(sourceImg.shape[0] + 1) or x_i + 1 >= 0:
                nextVal = None
            else:
                nextVal = sourceImg[y_i - 1][x_i + 1]

            # print(y_i,x_i, ' and ', nowVal, nextVal)
            if nextVal != nowVal and counter == 0:
                # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                degree45Matrix[int(nowVal)][counter] += 1
            elif nextVal == nowVal:
                counter += 1
                # print(y, " val,counter 2 |",nowVal, nextVal, counter)
            elif nextVal != nowVal and counter != 0:
                degree45Matrix[int(nowVal)][counter] += 1
                counter = 0
                # print(y, " val,counter 3 |",nowVal, nextVal, counter)

    # print()
    # print("Gray Level Run Length Matrix degree 45")
    return degree45Matrix

def degree135GLRLM(sourceImg, grayLevel=5, runLength=5):
    degree135Matrix = numpy.zeros([grayLevel, runLength])

    for y in range(sourceImg.shape[0]):
        # print()
        counter = 0
        i_range = max(sourceImg.shape)
        for i in range(i_range):
            y1 = y + i
            if y1 >= sourceImg.shape[0] or i >= sourceImg.shape[1]:
                # print('Break in coordinate = ', y1, i)
                break
            else:
                nowVal = sourceImg[y1][i]
                # print(nowVal)
                if y1 >= sourceImg.shape[0] - 1 or i >= sourceImg.shape[1] - 1:
                    nextVal = None
                else:
                    nextVal = sourceImg[y1 + 1][i + 1]
                # print('First step', nowVal, nextVal)
                if nextVal != nowVal and counter == 0:
                    # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                    degree135Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree135Matrix[int(nowVal)][counter] += 1
                    counter = 0
                    # print(y, " val,counter 3 |",nowVal, nextVal, counter)

    for x in range(sourceImg.shape[1]):
        if x == 0:
            continue
        # print()
        i_range = max(sourceImg.shape)
        counter = 0
        for i in range(i_range):
            x1 = x + i
            if i >= sourceImg.shape[0] or x1 >= sourceImg.shape[1]:
                # print('Break in coordinate = ',i,x)
                break
            else:
                nowVal = sourceImg[i][x1]
                # print(nowVal)
            if i >= sourceImg.shape[0] - 1 or x1 >= sourceImg.shape[1] - 1:
                nextVal = None
            else:
                nextVal = sourceImg[i + 1][x1 + 1]
            # print('Second step', nowVal, nextVal)
            if nextVal != nowVal and counter == 0:
                # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                degree135Matrix[int(nowVal)][counter] += 1
            elif nextVal == nowVal:
                counter += 1
                # print(y, " val,counter 2 |",nowVal, nextVal, counter)
            elif nextVal != nowVal and counter != 0:
                degree135Matrix[int(nowVal)][counter] += 1
                counter = 0
                # print(y, " val,counter 3 |",nowVal, nextVal, counter)

    # print()
    # print("Gray Level Run Length Matrix degree 135")
    return degree135Matrix

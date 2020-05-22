def normalization(value, min=0, max=255, newmin=0, newmax=10):
    newValue = (value-min)*((newmax-1-newmin)/(max-min))-newmin
    return newValue

def normalizationImage(image=None, minScale=0, maxScale=9):
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            image[y][x] = round(normalization(value=image[y][x],
                                                   newmin=minScale,
                                                   newmax=maxScale,
                                                   ))
    return image
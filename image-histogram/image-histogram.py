import numpy as np

def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here

    hist = []

    for i in range(0,256):
        hist.append(0)
    
    for row in image:
        for pixel in row:
                hist[pixel] += 1
            
    return hist

            
            
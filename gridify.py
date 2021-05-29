import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# constants
DOWNLOADS_FOLDER = r'C:\Users\aberr\Downloads'
TEST_IMG = DOWNLOADS_FOLDER + r'\ironman.jpg'
POST_IT_SIZE = 3 # inches
SIDE_LENGTH = 60 # inches


def partition(img, post_it_size, max_height=None, max_width=None, square=None):
    
    # set limiting dimension
    if max_height:
        max_size = max_height
    elif max_width:
        max_size = max_width
    else:
        max_size = square



if __name__ == '__main__':

    img = io.imread(TEST_IMG)
    partition(img, POST_IT_SIZE, square=SIDE_LENGTH)

    # plt.imshow(img)
    # plt.show()
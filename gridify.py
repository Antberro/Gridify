import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
from skimage import io
from math import ceil
import sys
import utils

# constants
DOWNLOADS_FOLDER = r'C:\Users\aberr\Downloads'
TEST_IMG = DOWNLOADS_FOLDER + r'\ironman.jpg'
POST_IT_SIZE = (2,1.5) # inches
SIDE_LENGTH = 48 # inches
GRID_STEP = 5
GRID_COLOR = 'black'
GRID_WEIGHT = 1.0

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)
COLORS = [RED, BLUE, YELLOW, BLACK, WHITE]
# COLORS = [
#     (255,126,185),
#     (255,101,163),
#     (122,252,255),
#     (254,255,156),
#     (255,247,64)
# ]


def partition(img, note_size: tuple, height:float = None, width:float = None):
    '''
    Type description here.

    Args:
        img (ndarray): image array to partition with shape (height, width, 3)
        note_size (tuple): width, height of post-it note in inches
        height (float): [optional] output height in inches
        width (float): [optional] output width in inches

    Returns:
        fig (matplotlib.figure): figure containing plots of design
        output_width, output_height (tuple): dimensions of resulting design in inches
        num_notes_x, num_notes_y (tuple): dimensions of resulting design in terms of post-it notes
        total_num_notes (int): number of post-it notes needed for design
    '''


    # assert input is correct
    width_is_arg = height is None and width is not None
    height_is_arg = width is None and height is not None
    assert (width_is_arg or height_is_arg), 'expected either only a width or only a height to be entered'


    # define variables
    original_img = np.copy(img)
    imgy = img.shape[0]  # in pixels
    imgx = img.shape[1]  # in pixels
    width = width if width else (imgx / imgy) * height  # in inches
    height = height if height else (imgy / imgx) * width  # in inches
    note_size_x = note_size[0]
    note_size_y = note_size[1]


    # calculate number of notes and pixels per note for each dimension
    num_notes_x = ceil(width / note_size_x)
    num_notes_y = ceil(height / note_size_y)
    px_per_note_x = ceil(imgx / num_notes_x)
    px_per_note_y = ceil(imgy / num_notes_y)


    # calculate output data
    output_height = num_notes_y * note_size_y  # in inches
    output_width = num_notes_x * note_size_x  # in inches
    total_num_notes = num_notes_x * num_notes_y


    # color each grid square
    for xd in range(num_notes_x+1):
        for yd in range(num_notes_y+1):
            
            # select gridsquare
            y0 = yd * px_per_note_y
            y1 = y0 + px_per_note_y
            x0 = xd * px_per_note_x
            x1 = x0 + px_per_note_x
            gridsquare = img[y0:y1, x0:x1]

            if gridsquare.any():
                img[y0:y1, x0:x1] = colorize(gridsquare)


    # create plots
    fig, axes = plt.subplots(nrows=1, ncols=3)

    for ind in (0, 1):
        axes[ind].set_xticks([i*px_per_note_x for i in range(0,num_notes_x+1,GRID_STEP)])
        axes[ind].set_xticklabels([i for i in range(0,num_notes_x+1,GRID_STEP)])
        axes[ind].set_yticks([i*px_per_note_y for i in range(0,num_notes_y+1,GRID_STEP)])
        yticklabels = [i for i in range(0,num_notes_y+1,GRID_STEP)]
        axes[ind].set_yticklabels(yticklabels[::-1])

    axes[2].set_xticks([])
    axes[2].set_yticks([])

    info_title = '{}" x {}" = {} notes x {} notes \n {} notes of size {}" x {}" required'.format(output_width, output_height, num_notes_x, num_notes_y, total_num_notes, note_size_x, note_size_y)
    fig.suptitle(info_title)


    # draw grid lines
    for xd in range(num_notes_x+1):
        axes[0].vlines(xd*px_per_note_x, 0, imgy, colors=GRID_COLOR, lw=GRID_WEIGHT)
        axes[1].vlines(xd*px_per_note_x, 0, imgy, colors=GRID_COLOR, lw=GRID_WEIGHT)
        for yd in range(num_notes_y+1):
            axes[0].hlines(yd*px_per_note_y, 0, imgx, colors=GRID_COLOR, lw=GRID_WEIGHT)
            axes[1].hlines(yd*px_per_note_y, 0, imgx, colors=GRID_COLOR, lw=GRID_WEIGHT)
    axes[0].vlines((num_notes_x+1)*px_per_note_x, 0, imgy, colors=GRID_COLOR, lw=GRID_WEIGHT)
    axes[0].hlines((num_notes_y+1)*px_per_note_y, 0, imgx, colors=GRID_COLOR, lw=GRID_WEIGHT)
    axes[1].vlines((num_notes_x+1)*px_per_note_x, 0, imgy, colors=GRID_COLOR, lw=GRID_WEIGHT)
    axes[1].hlines((num_notes_y+1)*px_per_note_y, 0, imgx, colors=GRID_COLOR, lw=GRID_WEIGHT)


    # draw images
    axes[0].imshow(original_img)
    axes[1].imshow(img)
    axes[2].imshow(img)

    return fig, (output_width, output_height), (num_notes_x, num_notes_y), total_num_notes




def colorize(gridsquare):
    '''
    Type description here.

    Args:
        gridspace (ndarry): array representing a gridspace
    '''

    dist2 = lambda a,b: (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
    avg_color = np.mean(gridsquare, axis=(0,1))
    color_dists = list(map(lambda x: dist2(avg_color, x), COLORS))

    return COLORS[np.argmin(color_dists)]



if __name__ == '__main__':


    # parse inputs
    args = sys.argv[1:]
    filename, note_size, width, height, savepath = utils.parse(args)
    img = io.imread(DOWNLOADS_FOLDER + r'\{}'.format(filename))


    # partition image into grid art
    fig, dims_inches, dims_notes, total_notes = partition(img, note_size, width=width, height=height)


    if savepath:
        fig.savefig(DOWNLOADS_FOLDER + r'\{}'.format(savepath), dpi=200)


    # display output data
    output_width, output_height = dims_inches
    num_notes_x, num_notes_y = dims_notes

    print('\nOutput Dimensions:')
    print('\t{}" x {}"'.format(output_width, output_height))
    print('\t{} notes x {} notes'.format(num_notes_x, num_notes_y))
    print('Total Notes Required: {}'.format(total_notes))
    print('\n')

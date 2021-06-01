import numpy as np
from settings import *


def colorize(gridsquare):
    '''
    Recolor the specified gridsquare according to a certain color
    algorithm.

    Args:
        gridspace (ndarry): array representing a gridspace

    Returns:
        new_color (ndarry): RGB values of new color for gridspace    
    '''

    if COLOR_ALG == 'average':
        new_color = np.mean(gridsquare, axis=(0,1))

    elif COLOR_ALG == 'euclidean-similarity':

        dist2 = lambda a,b: (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
        avg_color = np.mean(gridsquare, axis=(0,1))
        color_dists = list(map(lambda x: dist2(avg_color, x), COLORS))
        new_color = COLORS[np.argmin(color_dists)]

    return new_color




def parse(args):
    '''
    Parse user input to main script into arguments for partition() function.

    Args:
        args (list): list of user arguments to script

    Returns:
        filename (string): filename of image to use
        note_size_x, note_size_y (tuple): dimensions of post-it note in inches
        width (float): width of output design in inches
        height (float): height of output design in inches
        savepath (string): filename of saved output image
    '''
    
    filename = None
    note_size_x = None
    note_size_y = None
    width = None
    height = None
    savepath = None

    for token in args:

        # look for filename
        if token.split('.')[-1] in IMAGE_TYPES and '-save=' not in token:
            filename = token

        # look for -s arg
        if '-s=' in token:
            text = token[3:]
            x, y = text.split(',')
            note_size_x, note_size_y = float(x), float(y)

        # look for -w arg
        if '-w=' in token:
            width = float(token[3:])

        # look for -h arg
        if '-h=' in token:
            height = float(token[3:])

        # look for -save arg
        if '-save=' in token:
            savepath = token[6:]
            print("here: ", savepath)
    
    return filename, (note_size_x, note_size_y), width, height, savepath

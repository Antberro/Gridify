# File I/O folder path
IMAGE_FOLDER = r'C:\Users\aberr\Downloads'

# Image types that can be read
IMAGE_TYPES = ['jpg', 'JPG', 'png', 'PNG']

# Grid Appearance
AUTO_SHOW_GRID = True
GRID_STEP = 5
GRID_COLOR = 'black'
GRID_WEIGHT = 1.0

# Color algorithm
COLOR_ALG_OPTIONS = ['average', 'euclidean-similarity']
COLOR_ALG = COLOR_ALG_OPTIONS[1]  # <---- set colorizer algorithm

# Color scheme
COLORS = [
    (0, 0, 0),        # black
    (255, 255, 255),  # white
    #(128, 128, 128),  # gray
    (255, 0, 0),      # red
    #(0, 0, 255),      # blue
    #(0, 255, 0),      # green
    #(50, 0, 50),      # purple
    (255, 255, 0),    # yellow
    #(100, 65, 0),     # orange
    #(165, 42, 42),    # brown
]
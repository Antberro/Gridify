# Gridify
A tool for generating Post-It Note art from images.

## Description
Interested in Post-It Note art? Or pixelated art in general? Use Gridify to easily generate artistic Post-It Note art!

## Running Gridify
* First make sure to edit settings.py and specifiy a path to where you want to load and store your images. Here you can also change settings relating to the plots/colors/colorizing algorithm etc.
```
# File I/O folder path
IMAGE_FOLDER = r'C:\Users\User1\example_folder'
```
* In the terminal when running the gridify.py script, you will need to pass in some parameters: the filename of the image to use, the dimensions of the Post-It Notes to use in inches via the -s parameter e.g. -s=width,height, and ONE of either: the desired output width (using -w paramter) OR the desired output height (using -h paramter) in inches. In addition, you can optionally add the -savepath parameter to specifiy the filename of the saved output image.
```
>> python gridify.py monalisa.jpg -s=1,1 -h=48 -savepath=output.png
```
* Finally, watch Gridify output an artistic representation of your image. Feel free to play around with the settings in order to find a good result.

![Interesting Post-It Note art.](https://github.com/Antberro/Gridify/blob/main/examples/output.png)

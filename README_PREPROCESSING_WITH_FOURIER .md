READ ME FILE FOR PREPROCESSING_WITH_FOURIER.py
Import the necessary packages as mentioned in the requirements.txt
Import the transform.py file.

WALK-THROUGH OF THE CODE:
>Arguments for the parser are constructed.
>The image is loaded, cloned and resized. Cloned so as not to lose the original data.
>Image is coverted to grayscale, blured. On this image, edge detection is performed.
>On the edged image,perform contour detection.
>Find outline of the paper.
>Apply four-point transform to obtain top-down image.
>Convert the warped image to grayscale, then threshold it to give it that 'black and white' paper effect.
>Show the original and scanned images

    

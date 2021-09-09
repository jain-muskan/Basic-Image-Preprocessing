READ ME FILE FOR TRANSFORM.py
Import the necessary packages as mentioned in the requirements.txt

WALK-THROUGH OF THE CODE:

Function order_points:
>Initialize a list of coordinates that will be ordered
>Now, compute the difference between the points.
> Return the ordered coordinates

Function four_point_transform:
>Obtain a consistent order of the points and unpack them individually.
>Compute the width of the new image, which will be the maximum distance between bottom-right and bottom-left x-coordiates or the top-right and top-left x-coordinates.
>Compute the height of the new image, which will be the maximum distance between the top-right and bottom-right y-coordinates or the top-left and bottom-left y-coordinates.
>Construct the set of destination points to obtain a "birds eye view".
>Compute the perspective transform matrix and then apply it.
>Return the warped image.




    

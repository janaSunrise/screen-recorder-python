import cv2
import numpy as np
from PIL import ImageGrab

four_cc = cv2.VideoWriter_fourcc(*"MP4V")
size = (ImageGrab.grab()).size

output_file = cv2.VideoWriter("recording.mp4", four_cc, 20.0, size)

while True:
    # Grab the image, and add it to array
    image = ImageGrab.grab(bbox=(0, 0, size[0], size[1]))
    image = np.array(image)

    # Make the Numpy Image BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # If you need the preview, use cv2, else comment the line below.
    cv2.imshow("Screen recording preview", image)

    # Write to video file
    output_file.write(image)

    # If user hists, esc, then exit!
    if cv2.waitKey(1) == 27:
        break

output_file.release()
cv2.destroyAllWindows()

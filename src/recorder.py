import cv2
import numpy as np
from PIL import ImageGrab

four_cc = cv2.VideoWriter_fourcc(*"X264")
size = (ImageGrab.grab()).size()

output_file = cv2.VideoWriter("recording.mp4", four_cc, 5.0, size)

while True:
    # Grab the image, and add it to array
    image = np.array(ImageGrab.grab())

    # If you need the preview, use cv2, else comment the line below.
    cv2.imshow("Screen recording preview", image)

    # Write to video file
    output_file.write(image)

    # If user hists, esc, then exit!
    if cv2.waitKey(1) == 27:
        break

output_file.release()
cv2.destroyAllWindows()

import cv2 as cv

# Start video capture
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    # Convert the frame to grayscale
    filtered = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Show the grayscale frame
    cv.imshow("Gray Video", filtered)

    # Break the loop when 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object
capture.release()
cv.destroyAllWindows()

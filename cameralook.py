import cv2

def main():
    # Open cameras on ports 6 and 12
    cap_port_6 = cv2.VideoCapture(6)
    cap_port_12 = cv2.VideoCapture(12)

    # Check if the cameras opened successfully
    if not (cap_port_6.isOpened() and cap_port_12.isOpened()):
        print("Error: Unable to open one or both cameras.")
        return

    # Create windows to display camera streams
    cv2.namedWindow("Camera Port 6", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Camera Port 12", cv2.WINDOW_NORMAL)

    while True:
        # Read frames from the cameras
        ret_port_6, frame_port_6 = cap_port_6.read()
        ret_port_12, frame_port_12 = cap_port_12.read()

        # Check if frames were read successfully
        if not (ret_port_6 and ret_port_12):
            print("Error: Unable to read frames from one or both cameras.")
            break

        # Display frames in their respective windows
        cv2.imshow("Camera Port 6", frame_port_6)
        cv2.imshow("Camera Port 12", frame_port_12)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera objects and close windows
    cap_port_6.release()
    cap_port_12.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

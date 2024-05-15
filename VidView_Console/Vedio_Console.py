import cv2
import os
import sys

video_path = r"C:\Users\DELL\Desktop\Python_Helper_Bot\VidView_Console\Satoru Gojo vs Toji Fushiguro - Jujutsu Kaisen Season 2 _Hidden Inventory_「AMV」- Numb The Pain ᴴᴰ.mp4"


if not os.path.exists(video_path):
    print("Invalid path!")
    sys.exit(1)

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Unable to open video file.")
    sys.exit(1)

try:
    while True:
        try:
            height = int(input("Enter the height you want the video to be inside the terminal (from 31-256): "))
            if height < 31:
                print("The height can't be smaller than 31!")
            elif height > 256:
                print("The max height is 256!")
            else:
                break
        except ValueError:
            print("The height needs to be an integer!")

    while True:
        amount_of_frames = input("Enter the amount of frames you want to play (type ALL if you want to play the entire video): ")
        if amount_of_frames.isdigit():
            amount_of_frames = int(amount_of_frames)
            break
        elif amount_of_frames.lower() == "all":
            amount_of_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            break
        else:
            print("The amount of frames needs to be an integer!")

    if amount_of_frames > int(video.get(cv2.CAP_PROP_FRAME_COUNT)):
        amount_of_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get screen dimensions
    screen_width = 1920
    screen_height = 1080

    # Create a full-screen window
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Play the video according to the specified settings
    frame_count = 0
    while frame_count < amount_of_frames:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.resize(frame, (int(frame.shape[1] * height / frame.shape[0]), height))
        cv2.imshow('Video', frame)
        key = cv2.waitKey(25)
        if key & 0xFF == ord('q'):
            break
        frame_count += 1

except KeyboardInterrupt:
    # Release the video capture object and close any open windows if the user interrupts the program
    video.release()
    # close all  thinks the console
    cv2.destroyAllWindows()

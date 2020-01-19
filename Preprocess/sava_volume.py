import set_params
import os
import cv2
import scipy.io as sio

videosPath = ""
outputPath = ""

if not os.path.exists(outputPath):
    os.mkdir(outputPath)

if not os.path.exists(videosPath):
    print("videosPath not exist!")

videos = os.listdir(videosPath)

for v in videos:
    if not v.startswith('Test'):
        videos.remove(v)
    if v.endswith('_gt'):
        videos.remove(v)

for v in videos:

    videoAbsolutePath = os.path.join(videosPath, v)

    if os.path.isfile(videoAbsolutePath):

        cap = cv2.VideoCapture(v)
        fps = cap.get(cv2.CAP_PROP_FPS)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        frameList = []
        while cap.isOpened():

            ret, frame = cap.read()
            if ret:

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray, (set_params.W, set_params.H), interpolation=cv2.INTER_CUBIC)
                print(gray.shape)
                frameList.append(gray)
                print('frame', ret, "of Video", v, "has been saved!")

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        sio.savemat(os.path.join(outputPath, v) + ".mat", {'vol': frameList})
        cap.release()
        cv2.destroyAllWindows()

    elif os.path.isdir(videoAbsolutePath):

        frameList = []
        frames = os.listdir(videoAbsolutePath)

        for frameName in frames:

            if not frameName.endswith('.tif'):

                frames.remove(frameName)
        print(len(frames))
        for frameName in frames:

            frame = cv2.imread(os.path.join(videoAbsolutePath, frameName), cv2.IMREAD_GRAYSCALE)
            if frame is None:
                print('fail to load image!')
            frame = cv2.resize(frame, (set_params.W, set_params.H), interpolation=cv2.INTER_CUBIC)
            print(frame.shape)
            frameList.append(frame)
            print('frame', frameName, "of Video", v, "has been saved!")

        sio.savemat(os.path.join(outputPath, v) + ".mat", {'vol': frameList})

    else:
        print(videoAbsolutePath, "is not a right path or file!")

    print("Video", v, "has been saved!")

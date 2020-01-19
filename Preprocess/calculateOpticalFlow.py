import cv2


def calculateOpticalFlowFarneback(prevGray, currGray):

    flow = cv2.calcOpticalFlowFarneback(prevGray, currGray,
                                        flow=None, pyr_scale=0.5, levels=3, winsize=10,
                                        iterations=3, poly_n=5, poly_sigma=1.1, flags=0)
    print(flow.shape)
    xFlow, yFlow = flow[..., 0], flow[..., 1]
    print("xFlow", "\n", xFlow)
    print("yFlow", "\n", yFlow)

    # obtain the optical flow magnitude and direction angle
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    print("optical flow magnitude", "\n", mag.shape, "\n", mag)
    print("optical flow direction angle", "\n", ang.shape, "\n", ang)

    # normalize horizontal and vertical components
    hor = cv2.normalize(flow[..., 0], None, 0, 255, cv2.NORM_MINMAX)
    ver = cv2.normalize(flow[..., 1], None, 0, 255, cv2.NORM_MINMAX)
    hor = hor.astype('uint8')
    ver = ver.astype('uint8')
    print("Normalized horizontal flow", "\n", hor)
    print("Normalized vertical flow", "\n", ver)

    # show the components as images
    # cv2.imshow('Horizontal Component', hor)
    # cv2.imshow('Vertical Component', ver)
    # cv2.waitKey()

    return flow, hor, ver


if __name__ == '__main__':

    prevFrame = cv2.imread("C:\\Users\\admin\\Documents\\Surveillance\\UCSD_Anomaly_Dataset.v1p2\\UCSDped1\\Train"
                           "\\Train001\\001.tif")

    currFrame = cv2.imread("C:\\Users\\admin\\Documents\\Surveillance\\UCSD_Anomaly_Dataset.v1p2\\UCSDped1\\Train"
                           "\\Train001\\008.tif")

    prevGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)
    currGray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    calculateOpticalFlowFarneback(prevGray, currGray)

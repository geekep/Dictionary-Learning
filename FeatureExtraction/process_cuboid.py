import set_params
import C3D.get_feature as get_feature
import numpy as np
import scipy.io as sio
import os


def main(videosPath, C3DfeaturesPath):

    if not os.path.exists(C3DfeaturesPath):
        os.mkdir(C3DfeaturesPath)

    if not os.path.exists(videosPath):
        print("videosPath not exist!")

    videos = os.listdir(videosPath)

    for v in videos:

        videoMatrix = sio.loadmat(os.path.join(videosPath, v)).get('vol')
        C3DfeatureList = []
        locationOfCubeList = []
        numOfFrame = np.shape(videoMatrix)[0]

        # sampling in temporal axis
        for frameID in range(int(set_params.tprLen / 2), videoMatrix.shape[0], set_params.trs):
            # sampling in spatial axis
            for x in range(int(round(set_params.patchH / 2)), set_params.H - int(round(set_params.patchH / 2)) + 1,
                           set_params.srs):
                for y in range(int(round(set_params.patchW / 2)), set_params.W - int(round(set_params.patchW / 2)) + 1,
                               set_params.srs):

                    cuboid = videoMatrix[int(frameID - set_params.tprLen / 2): int(frameID + set_params.tprLen / 2),
                             x - int(np.floor(set_params.patchH / 2)): x + int(np.floor(set_params.patchH / 2)),
                             y - int(np.floor(set_params.patchW / 2)): y + int(np.floor(set_params.patchW / 2))]

                    C3Dfeature = get_feature.get_C3Dfeature(cuboid)
                    C3DfeatureList.append(C3Dfeature.flatten().tolist())
                    locationOfCubeList.append([int((frameID - set_params.tprLen / 2) / 16),
                                               int((x - int(np.floor(set_params.patchH / 2))) / 40),
                                               int((y - int(np.floor(set_params.patchW / 2))) / 40)])

                    # print("C3DFeature and location of", "cube[", int(frameID - set_params.tprLen / 2), ":",
                    #       int(frameID + set_params.tprLen / 2), "]",
                    #       "[", x - int(np.floor(set_params.patchH / 2)), ":", x + int(np.floor(set_params.patchH / 2)), "]",
                    #       "[", y - int(np.floor(set_params.patchW / 2)), ":", y + int(np.floor(set_params.patchW / 2)), "]",
                    #       "in video", v, "has been saved!")

        sio.savemat(os.path.join(C3DfeaturesPath, v), {'C3Dfeature': C3DfeatureList, 'locationOfCube': locationOfCubeList, 'numOfFrame': numOfFrame})
        print("C3DFeature and location in video", v, "has been saved!")


if __name__ == '__main__':
    videosPath = '../Test_vol'
    C3DfeaturesPath = '../Test_feature'
    main(videosPath, C3DfeaturesPath)

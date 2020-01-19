from sklearn.decomposition import PCA
import scipy.io as sio
import os
import set_params


def PCAdecomposition(X):
    # PCAdim = set_params.PCAdim
    pca = PCA(n_components='mle')
    reduced_x = pca.fit_transform(X)
    return reduced_x


def main(featurePath, reduceDimFeaturePath):

    if not os.path.exists(reduceDimFeaturePath):
        os.mkdir(reduceDimFeaturePath)

    if not os.path.exists(featurePath):
        print("featurePath not exist!")

    videoFeature = os.listdir(featurePath)

    for v in videoFeature:

        X = sio.loadmat(os.path.join(featurePath, v)).get('C3Dfeature')
        locationOfCube = sio.loadmat(os.path.join(featurePath, v)).get('locationOfCube')
        numOfFrame = sio.loadmat(os.path.join(featurePath, v)).get('numOfFrame')
        X = PCAdecomposition(X)
        sio.savemat(os.path.join(reduceDimFeaturePath, v), {'reduceDimFeature': X, 'locationOfCube': locationOfCube, 'numOfFrame': numOfFrame})


if __name__ == '__main__':
    featurePath = '../Test_feature'
    reduceDimFeaturePath = '../test_reduceDimFeature'
    main(featurePath, reduceDimFeaturePath)

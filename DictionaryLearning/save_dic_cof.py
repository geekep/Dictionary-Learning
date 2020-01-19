import os
import scipy.io as sio
import DictionaryLearning.ODL as ODL
import set_params
import numpy as np


def dictionaryLearning(X):
    k = set_params.k
    clf = ODL.ODL(k, lambd=0.01)
    dic, cof = clf.fit(X, verbose=True, iterations=10)
    return dic, cof


def main(featurePath):

    if not os.path.exists(featurePath):
        print("featurePath not exist!")

    features = os.listdir(featurePath)
    matrixList = []

    for v in features:
        if not v.endswith('.mat'):
            features.remove(v)

    for C3DFeature in features:

        featureMatrix = sio.loadmat(os.path.join(featurePath, C3DFeature)).get('reduceDimFeature')
        matrixList.append(featureMatrix)

    X = np.concatenate(tuple(matrixList), axis=0)

    print("Online Dictionary Learning (ODL)")
    dic, cof = dictionaryLearning(X.T)
    sio.savemat(os.path.join(os.path.dirname(featurePath), "Train_dic_cof.mat"), {'dic': dic, 'cof': cof})


if __name__ == '__main__':
    trainFeaturePath = "C:/Users/admin/Documents/Surveillance/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Test_reduce_dim_feature"
    main(trainFeaturePath)

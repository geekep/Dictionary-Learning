import numpy as np
import os
import scipy.io as sio
import DictionaryLearning.optimize as optimize
import DictionaryLearning.utils as utils


def get_sparseCombination(D, X, lambd=0.01, iterations=10):
    reconErrList = []
    coef = np.zeros((D.shape[1], X.shape[1]))
    for i in range(X.shape[1]):

        for it in range(iterations):
            # update X
            lasso = optimize.Lasso(D, lambd)
            lasso.fit(X, Xinit=coef)
            coef = lasso.coef_
            loss = loss(D, X[:, 1], coef)
            reconErrList.append(loss)
    return coef


def loss(D, x, coef, lambd=0.01):
    loss = utils.normF2(x - np.dot(D, coef))
    print(loss)
    return loss


if __name__ == '__main__':
    dicPath = "C:/Users/admin/Documents/Surveillance/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Train_dic_cof.mat"
    testReduceDimFeaturePath = "C:/Users/admin/Documents/Surveillance/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Test_reduce_dim_feature"

    if os.path.exists(dicPath):
        dic = sio.loadmat(dicPath).get('dic')
    else:
        print("dicPath not exist")

    testReduceDimFeature = []
    if os.path.exists(testReduceDimFeaturePath):
        testReduceDimFeature = os.listdir(testReduceDimFeaturePath)
        for v in testReduceDimFeature:
            if not v.endswith('.mat'):
                testReduceDimFeature.remove(v)
    else:
        print("testReduceDimFeaturePath not exist!")

    for v in testReduceDimFeature:

        X = sio.loadmat(os.path.join(testReduceDimFeaturePath, v)).get('reduceDimFeature')
        cof = get_sparseCombination(dic, X.T)
        print(cof)

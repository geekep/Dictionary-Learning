import numpy as np
import C3D.utils as utils
import DictionaryLearning.ODL as ODL


def test_unit():
    print('\n===========================================================')
    print('Unit test: Online Dictionary Learning (ODL)')
    d = 10
    N = 50
    k = 20
    Y = utils.normc(np.random.randn(d, N))
    clf = ODL.ODL(k, lambd=0.01)
    clf.fit(Y, verbose=True, iterations=100)


if __name__ == '__main__':
    test_unit()

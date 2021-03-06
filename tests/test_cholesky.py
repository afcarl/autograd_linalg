from __future__ import division
import autograd.numpy as np
import autograd.numpy.random as npr
from autograd.util import *
from autograd.numpy.linalg import solve
from itertools import product

from autograd_linalg.linalg import cholesky
from autograd_linalg.util import T, symm, rand_psd, check_symmetric_matrix_grads

def test_cholesky():
    fun = lambda A: to_scalar(cholesky(A))
    fun2 = lambda A: to_scalar(grad(fun)(A))
    check_symmetric_matrix_grads(fun, rand_psd(6))
    check_symmetric_matrix_grads(fun2, rand_psd(6))

def test_cholesky_broadcast():
    fun = lambda A: to_scalar(cholesky(A))
    fun2 = lambda A: to_scalar(grad(fun)(A))
    A = np.concatenate([rand_psd(6)[None, :, :] for i in range(3)], axis=0)
    check_symmetric_matrix_grads(fun, A)
    check_symmetric_matrix_grads(fun2, A)

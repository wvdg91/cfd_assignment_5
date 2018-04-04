import numpy as np
from mod_library import *

######### Test Routines at Gridpoint #############

xi_o = 2
xi_t = np.pi / 4.

jac_mat_ap = jacobian_matrix_at_gridpoint(xi_o, xi_t)
print(jac_mat_ap)

a_cov_o, a_cov_t = covariant_basis_vectors_at_gridpoint(jac_mat_ap)
print(a_cov_o)
print(a_cov_t)

jac_ap = jacobian_at_gridpoint(jac_mat_ap)
print(jac_ap)

a_contra_o, a_contra_t = contravariant_basis_vectors_at_gridpoint(a_cov_o, a_cov_t, jac_ap)
print(a_contra_o)
print(a_contra_t)

metric_tensor_ap = metric_tensor_contra_at_gridpoint(a_contra_o, a_contra_t)
print(metric_tensor_ap)

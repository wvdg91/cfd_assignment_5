import numpy as np

####### Gridpoint Routine #############


def jacobian_matrix_at_gridpoint(xi_one, xi_two):
    """
    Purpose: Generate 2D Jacobian Matrix for POLAR -> CARTESIAN coordinate transformation.
    Input: Two general coordinates of gridpoint (xi_1, xi_2)
    Output: 2x2 numpy array
    """
    return np.array([[np.cos(xi_two), -xi_one * np.sin(xi_two)],
                     [np.sin(xi_two), xi_one * np.cos(xi_two)]])


def jacobian_matrix_at_gridpoint_ass(xi_one, xi_two):
    """
    Purpose: Generate 2D Jacobian Matrix for GENERAL -> CARTESIAN coordinate transformation of assignment.
    Input: Two general coordinates of gridpoint (xi_1, xi_2)
    Output: 2x2 numpy array
    """
    return np.array([[-0.5 * np.pi * np.sin(0.5 * np.pi * xi_one) * (1 + 4 * xi_two), 4 * np.cos(0.5 * np.pi * xi_one)],
                     [0.5 * np.pi * np.cos(0.5 * np.pi * xi_one) * (1 + 4 * xi_two), 4 * np.sin(0.5 * np.pi * xi_one)]])


def covariant_basis_vectors_at_gridpoint(jacobian_matrix):
    """
    Purpose: Generates the two covariant basis vectors at point
    Input: jacobian_matrix at point: numpy array (2x2)
    Output: 2 numpy arrays (2)
    """
    return jacobian_matrix.T[0], jacobian_matrix.T[1]


def jacobian_at_gridpoint(jacobian_matrix):
    """
    Purpose: To generate jacobian sqrt(g) at point
    Input: jacobian matrix at point: numpy array (2x2)
    Output: real number
    """
    determinant = np.linalg.det(jacobian_matrix)
    return np.sqrt(determinant)


def contravariant_basis_vectors_at_gridpoint(a_cov_one, a_cov_two, jacobian):
    """
    Purpose: Generate contravariant basis vectors at point
    Input: covariant basis vectors: 2x nummpy arrays (len 2), jacobian: real
    Output: Contravariant basis vectors at point: 2x numpy arrays (2x2)
    """
    a_cov_one_3d = np.append(a_cov_one, 0)
    a_cov_two_3d = np.append(a_cov_two, 0)
    a_cov_three = np.array([0, 0, 1])
    return 1. / jacobian * np.cross(a_cov_two, a_cov_three), 1. / jacobian * np.cross(a_cov_three, a_cov_one)


def metric_tensor_contra_at_gridpoint(a_contra_one, a_contra_two):
    """
    Purpose: To generate contravariant metric tensor
    Input: Contravariant basis vector: 2x numpy arrays (len 2)
    Output: contravariant metric tensor: numpy array (2x2)
    """
    return np.array([[np.inner(a_contra_one, a_contra_one), np.inner(a_contra_one, a_contra_two)],
                     [np.inner(a_contra_two, a_contra_one), np.inner(a_contra_two, a_contra_two)]])

####### ELEM #######


def eval_h(K):
    """
    Purpose: To evaluate h, i.e. meshsize in direction
    Input:  K -> Range
    Output: h
    """
    return 1. / (K - 1)


def construct_elem_list(I, J):
    """
    Purpose: To construct a list of the gcors of all the elems
    Input:  I -> range in x direction
            J -> range in j direction
    Output: list with len = # elems,
            and corresponding gcors
    """
    elem_list = []
    x = np.linspace(0, 1, I, True)
    y = np.linspace(0, 1, J, True)
    xx, yy = np.meshgrid(x, y)
    for i in range(I):
        for j in range(J):
            elem_list.append([xx[i, j], yy[i, j]])
    return elem_list


def eval_elem_type(elem):
    """
    Purpose: To determine the element type (what boundary/fluid)
    Input:  gcors (x,y)
    Output: string with elem_type
    """
    if (elem[0] == 0 and elem[1] == 0):
        elem_type = 'left_bottom_corner'
    elif (elem[0] == 0 and elem[1] == 1):
        elem_type = 'left_top_corner'
    elif (elem[0] == 1 and elem[1] == 0):
        elem_type = 'right_bottom_corner'
    elif (elem[0] == 1 and elem[1] == 1):
        elem_type = 'right_top_corner'
    elif (elem[0] == 0):
        elem_type = 'left_boundary'
    elif (elem[0] == 1):
        elem_type = 'right_boundary'
    elif (elem[1] == 0):
        elem_type = 'bottom_boundary'
    elif (elem[1] == 1):
        elem_type = 'top_boundary'
    else:
        elem_type = 'Fluid'

    return elem_type


def eval_coors_sides(coors_elem, h1, h2):
    """
    Purpose: To obtain the coors of the sides of the elem
    Input:  coordinates cp of elem, h1, h2
    Output: 4 ndarray with coors of sides
    """
    l_coors = np.array([coors_elem[0] - h1 / 2., coors_elem[1]])
    r_coors = np.array([coors_elem[0] + h1 / 2., coors_elem[1]])
    t_coors = np.array([coors_elem[0], coors_elem[1] + h2 / 2.])
    b_coors = np.array([coors_elem[0], coors_elem[1] - h2 / 2.])
    return l_coors, r_coors, t_coors, b_coors


def construct_matrix(elem_list):
    """
    Purpose: To construct zeros matrix from elem_list
    Input:  elem_list
    Output: ndarray zeros (len x len)
    """
    length_elem_list = len(elem_list)
    matrix = np.zeros([length_elem_list, length_elem_list])
    return matrix


def construct_source_vector(elem_list):
    """
    Purpose: To construct zeros source vector from elem_list
    Input:  elem_list
    Output: ndarray zeros (len )
    """
    length_elem_list = len(elem_list)
    vector = np.zeros(length_elem_list)
    return vector


###### Stencils ######
# Fluid


def fluid_left_coeff(coors_elem, l_coors):
    pass


def fluid_right_coeff(coors_elem, r_coors):
    pass


def fluid_top_coeff(coors_elem, t_coors):
    pass


def fluid_bottom_coeff(coors_elem, b_coors):
    pass


def fluid_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Left Boundary


def lb_right_coeff(coors_elem, r_coors):
    pass


def lb_top_coeff(coors_elem, t_coors):
    pass


def lb_bottom_coeff(coors_elem, b_coors):
    pass


def lb_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Right Boundary


def rb_left_coeff(coors_elem, l_coors):
    pass


def rb_top_coeff(coors_elem, t_coors):
    pass


def rb_bottom_coeff(coors_elem, b_coors):
    pass


def rb_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Top Boundary


def tb_right_coeff(coors_elem, r_coors):
    pass


def tb_left_coeff(coors_elem, l_coors):
    pass


def tb_bottom_coeff(coors_elem, b_coors):
    pass


def tb_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Bottom Boundary


def bb_right_coeff(coors_elem, r_coors):
    pass


def bb_left_coeff(coors_elem, l_coors):
    pass


def bb_top_coeff(coors_elem, t_coors):
    pass


def bb_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass
# Left Bottom Corner


def lbc_right_coeff(coors_elem, r_coors):
    pass


def lbc_top_coeff(coors_elem, t_coors):
    pass


def lbc_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Right Bottom Corner


def rbc_left_coeff(coors_elem, l_coors):
    pass


def rbc_top_coeff(coors_elem, t_coors):
    pass


def rbc_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Left Top Corner


def ltc_right_coeff(coors_elem, r_coors):
    pass


def ltc_bottom_coeff(coors_elem, b_coors):
    pass


def ltc_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

# Right Top Corner


def rtc_left_coeff(coors_elem, l_coors):
    pass


def rtc_bottom_coeff(coors_elem, b_coors):
    pass


def rtc_center_coeff(coors_elem, l_coors, r_coors, t_coors, b_coors):
    pass

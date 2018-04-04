import numpy as np
from mod_library import *
from stencil_lib import *

# Options
np.set_printoptions(linewidth=200)

################################# Generate Mesh #######################################
I = 4
J = 4
h1 = mods.eval_h(I)
h2 = mods.eval_h(J)

elem_list = construct_elem_list(I, J)
matrix = construct_matrix(elem_list)
source_vector = construct_source_vector(elem_list)

for elem in elem_list:
    elem_type = eval_elem_type(elem)
    elem_no = elem_list.index(elem)
    ls_coors, rs_coors, ts_coors, bs_coors = eval_coors_sides(elem, h1, h2)
    if (elem_type == 'Fluid'):
        matrix[elem_no, elem_no] = fluid_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = fluid_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no + 1] = fluid_left_coeff(elem, rs_coors)
        matrix[elem_no, elem_no - I] = fluid_left_coeff(elem, bs_coors)
        matrix[elem_no, elem_no + I] = fluid_left_coeff(elem, ts_coors)
    elif (elem_type == 'left_bottom_corner'):
        matrix[elem_no, elem_no] = lbc_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no + 1] = lbc_right_coeff(elem, rs_coors)
        matrix[elem_no, elem_no + I] = lbc_top_coeff(elem, ts_coors)

        source_vector[elem_no] = lbc_source()
    elif (elem_type == 'left_top_corner'):
        matrix[elem_no, elem_no] = ltc_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no + 1] = ltc_right_coeff(elem, rs_coors)
        matrix[elem_no, elem_no - I] = ltc_bottom_coeff(elem, bs_coors)

        source_vector[elem_no] = ltc_source()
    elif (elem_type == 'right_bottom_corner'):
        matrix[elem_no, elem_no] = rbc_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = rbc_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no + I] = rbc_top_coeff(elem, ts_coors)

        source_vector[elem_no] = rbc_source()
    elif (elem_type == 'right_top_corner'):
        matrix[elem_no, elem_no] = rtc_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = rtc_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no - I] = rtc_bottom_coeff(elem, bs_coors)

        source_vector[elem_no] = rtc_source()
    elif (elem_type == 'left_boundary'):
        matrix[elem_no, elem_no] = lb_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no + 1] = lb_right_coeff(elem, rs_coors)
        matrix[elem_no, elem_no - I] = lb_bottom_coeff(elem, bs_coors)
        matrix[elem_no, elem_no + I] = lb_top_coeff(elem, ts_coors)

        source_vector[elem_no] = lb_source()
    elif (elem_type == 'right_boundary'):
        matrix[elem_no, elem_no] = rb_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = rb_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no - I] = rb_bottom_coeff(elem, bs_coors)
        matrix[elem_no, elem_no + I] = rb_top_coeff(elem, ts_coors)

        source_vector[elem_no] = rb_source()
    elif (elem_type == 'bottom_boundary'):
        matrix[elem_no, elem_no] = bb_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = bb_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no + 1] = bb_right_coeff(elem, rs_coors)
        matrix[elem_no, elem_no + I] = bb_top_coeff(elem, ts_coors)

        source_vector[elem_no] = bb_source()
    elif (elem_type == 'top_boundary'):
        matrix[elem_no, elem_no] = tb_center_coeff(elem, ls_coors, rs_coors, ts_coors, bs_coors)
        matrix[elem_no, elem_no - 1] = tb_left_coeff(elem, ls_coors)
        matrix[elem_no, elem_no + 1] = tb_right_coeff(elem, rs_coors)
        matrix[elem_no, elem_no - I] = tb_bottom_coeff(elem, bs_coors)

        source_vector[elem_no] = tb_source()
    else:
        print('Error')

############################### Solve Linear System ###################################

phi = np.linalg.solve(matrix, source_vector)

import numpy as np
import mod_library as mods

###########################################################################
############################### Stencil ###################################
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

################################### Source ##################################


def lb_source():
    pass


def rb_source():
    pass


def tb_source():
    pass


def bb_source():
    pass


def lbc_source():
    pass


def rbc_source():
    pass


def ltc_source():
    pass


def rtc_source():
    pass

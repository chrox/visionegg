#!/usr/bin/env python

# Display a sinusoidal grating

############################
#  Import various modules  #
############################

from VisionEgg.Core import *
from VisionEgg.Gratings import *
from VisionEgg.AppHelper import *

#####################################
#  Initialize OpenGL window/screen  #
#####################################

screen = get_default_screen()

######################################
#  Create sinusoidal grating object  #
######################################

stimulus = SinGrating2D(center           = ( screen.size[0]/2.0, screen.size[1]/2.0 ),
                        size             = ( 300.0 , 300.0 ),
                        spatial_freq     = 10.0 / screen.size[0], # units of cycles/pixel
                        temporal_freq_hz = 5.0,
                        orientation      = 45.0 )

###############################################################
#  Create viewport - intermediary between stimuli and screen  #
###############################################################

viewport = Viewport( screen=screen, stimuli=[stimulus] )

########################################
#  Create presentation object and go!  #
########################################

p = Presentation(duration=(5.0,'seconds'),viewports=[viewport])
p.go()

#!/usr/bin/env python
"""Random dot stimulus"""

############################
#  Import various modules  #
############################

from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation
from VisionEgg.Dots import *

#####################################
#  Initialize OpenGL window/screen  #
#####################################

screen = get_default_screen()
screen.parameters.bgcolor = (0.0,0.0,0.0,0.0) # make black (RGBA)

######################################
#  Create random dot stimulus        #
######################################

stimulus = DotArea2D( center                  = ( screen.size[0]/2.0, screen.size[1]/2.0 ),
                      size                    = ( 300.0 , 300.0 ),
                      signal_fraction         = 0.1,
                      signal_direction_deg    = 180.0,
                      velocity_pixels_per_sec = 10.0,
                      dot_lifespan_sec        = 5.0,
                      dot_size                = 3.0,
                      num_dots                = 100)

###############################################################
#  Create viewport - intermediary between stimuli and screen  #
###############################################################

viewport = Viewport( screen=screen, stimuli=[stimulus] )

########################################
#  Create presentation object and go!  #
########################################

p = Presentation(go_duration=(10.0,'seconds'),viewports=[viewport])
p.go()

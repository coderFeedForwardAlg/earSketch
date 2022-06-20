#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(120)

fitMedia(MAX3210000_PAPER3,1,1,9)
makeBeat(CIARA_SET_PERC_DISTBASS, 2, 1.2, "---------------0+")
makeBeat(CIARA_SET_PERC_DISTBASS, 2, 2.45, "---------------0+")
makeBeat(CIARA_SET_PERC_DISTBASS, 2, 3.7, "---------------0+")
makeBeat(CIARA_SET_PERC_DISTBASS, 2, 4.95, "---------------0+")

fitMedia(MAX3210000_TAIR_PAPER,4,7.1,7.2)
fitMedia(MAX3210000_TAIR_PAPER,4,8.4,8.5)

fitMedia(MAX3210000_PAPER_HIT,3,6,7)
fitMedia(MAX3210000_PAPER_HIT,3,7.3,9)


finish()

import os
import tempfile
from nMOLDYN.GlobalVariables import GVAR

units_length = 1.0
title = 'Velocity Auto-Correlation Function'
trajectory = [os.path.join(GVAR['nmoldyn_trajs'], "TrajectoryTest1.nc")]
log_file = 'logfile.log'
projection_vector = None
output_files = {'vacf': os.path.join(tempfile.gettempdir(),'test.plot')}
deuter = {'Protein.0': ['SideChain']}
atoms = {'Protein.0': ['BackBone', 'SideChain']}
weights = 'none'
time_info = (1, 20, 2)

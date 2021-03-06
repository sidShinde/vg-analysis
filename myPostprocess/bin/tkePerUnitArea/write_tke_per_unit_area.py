import numpy as np
import os
import argparse
from myPostprocess.readers.reader_support_functions import *
from myPostprocess.readers.reader import *
from .get_tke_per_unit_area import *

def main():
    parser = argparse.ArgumentParser(description='calculate the turbulent KE \
    per unit area in the separation region')

    parser.add_argument('-config',
                        type=str,
                        help='file with the essential inputs',
                        required=True)

    args = parser.parse_args()

    # parse the config:
    configFile = open(args.config, mode='r')

    coordPlane, tkePerArea = get_tke_per_unit_area(configFile)
    solution = np.vstack((coordPlane, tkePerArea))

    caseDir = os.getcwd()
    caseDir = caseDir + '/postProcessing/my-postprocess'
    if not os.path.exists(caseDir):
        os.mkdir(caseDir)

    fname = caseDir + '/tke_per_unit_area.csv'
    np.savetxt(fname, solution.T, fmt='%.1f, %1.2e',
               delimiter=', ', newline='\n', header='x/h, tke/area')


if __name__=='__main__':
    main()

import os

path = os.path.abspath(os.path.dirname(__file__))
name = os.path.basename(__file__)

import sys
sys.path.append(path)

package_root = os.path.dirname(os.path.abspath(__file__))

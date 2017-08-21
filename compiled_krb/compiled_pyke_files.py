# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'fc_area_recommend.krb'):
           [1501575617.624, 'fc_area_recommend_fc.py'],
         ('', '', 'coil_area.kfb'):
           [1501575617.651, 'coil_area.fbc'],
        },
        compiler_version)


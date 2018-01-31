# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Tue 30 Jan 2018 20:16:53


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = 'complex(0,1)*cmath.sqrt(cmath.pi/aEW)*GCH',
                order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '2*complex(0,1)*(cmath.pi/aEW)*GCH**2',
                order = {'QED':4})


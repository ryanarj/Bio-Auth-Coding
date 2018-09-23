"""
Author: Karshan Arjun
Using Python3
"""
import pandas as pan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold


column_headers = ['Hold .', 'Hold t', 'Hold i', 'Hold e', 'Hold Shift',
                  'Hold 5', 'Hold Shift.1', 'Hold Caps', 'Hold r', 'Hold o', 'Hold a',
                  'Hold n', 'Hold l', 'Hold Enter', 'DD ..t', 'DD t.i', 'DD i.e',
                  'DD e.Shift', 'DD Shift.5', 'DD 5.Shift', 'DD Shift.Caps', 'DD Caps.r',
                  'DD r.o', 'DD o.a', 'DD a.n', 'DD n.l', 'DD l.Enter', 'UD ..t',
                  'UD t.i', 'UD i.e', 'UD e.Shift', 'UD Shift.5', 'UD 5.Shift',
                  'UD Shift.Caps', 'UD Caps.r', 'UD r.o', 'UD o.a', 'UD a.n', 'UD n.l',
                  'UD l.Enter', 'Pressure .', 'Pressure t', 'Pressure i', 'Pressure e',
                  'Pressure Shift', 'Pressure 5', 'Pressure Shift.1', 'Pressure Caps',
                  'Pressure r', 'Pressure o', 'Pressure a', 'Pressure n', 'Pressure l',
                  'Pressure Enter', 'Size .', 'Size t', 'Size i', 'Size e', 'Size Shift',
                  'Size 5', 'Size Shift.1', 'Size Caps', 'Size r', 'Size o', 'Size a',
                  'Size n', 'Size l', 'Size Enter', 'AvH', 'AvP', 'AvA']

# Get all the values
data = pan.read_csv('touchData.csv', names=column_headers)
varience = np.var(data)
m = np.mean(varience)
vt = VarianceThreshold(threshold=m)
data = vt.fit_transform(data)

plt.figure()
plt.title('Enhanced Data')
plt.plot(data)
plt.show()

x = 1
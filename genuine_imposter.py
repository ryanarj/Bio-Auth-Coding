from math import sqrt
import numpy as npy
import matplotlib.pyplot as plt

g_scale = 0.05
g_loc = 0.23
i_scale = 0.01
i_loc = 0.51
size = 500

npy.random.seed(0)

# genunine = npy.random.normal(loc=g_loc, scale=g_scale, size=size)
# imposter = npy.random.normal(loc=i_loc, scale=i_scale, size=size)

genuine_scores = [0.45,0.47,0.33,0.33,0.39,0.46,0.45,0.44,0.48,0.35,0.49,0.43,0.43,0.41,0.41,0.33,0.41,0.32,0.42, 0.42]
impostor_scores = [0.52,0.5,0.54,0.46,0.45,0.47,0.48,0.48,0.53,0.51,0.53,0.55,0.51,0.46,0.47,0.46,0.49,0.54,0.52, 0.51,0.49,0.5,0.53,0.54,0.54,0.51,0.46,0.51,0.48,0.47,0.51,0.52,0.51,0.52,0.46,0.54,0.48,0.46, 0.53,0.45,0.48,0.48,0.5,0.46,0.46,0.49,0.53,0.54,0.53,0.47]
a = float(sqrt(2)*abs(g_loc-i_loc))
b = float(sqrt((g_scale**2)+(i_scale**2)))
d_prime = float(a/b)

plt.title(s=d_prime)
plt.hist(genuine_scores, color='green', alpha=0.5)
plt.hist(impostor_scores, color='red', alpha=0.5)
plt.show()

threshold = npy.linspace(0, 1, 100)
far = []
tpr = []
frr = []

for t in threshold:
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for g in genuine_scores:
        if g <= t:
            tp += 1
        else:
            fn += 1
    
    for i in impostor_scores:
        if i <= t:
            fp += 1
        else:
            tn += 1
    far.append(fp / (fp + tn))
    tpr.append(tp / (tp + fn))
    frr.append(fn / (fn + tp))

far_eer = round(sum(far) / len(far), 2)
frr_eer = round(sum(frr) / len(frr), 2)

eer = (far_eer, frr_eer)
plt.title('{0} {1}'.format('EER', eer))
plt.plot(far, frr, lw=2, color='blue')
plt.plot([0,1], [0,1], lw=1, color='black')
plt.show()


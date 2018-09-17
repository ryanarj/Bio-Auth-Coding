import numpy as npy 
import matplotlib.pyplot as plt
import math

g_scale = 0.05
g_loc = 0.23
i_scale = 0.1
i_loc = 0.51
size = 500

npy.random.seed(0)

genunine = npy.random.normal(loc=g_loc, scale=g_scale, size=size)
imposter = npy.random.normal(loc=i_loc, scale=i_scale, size=size)

a = float(math.sqrt(2)*abs(g_loc-i_loc))
b = float(math.sqrt((g_scale**2)+(i_scale**2)))
d_prime = float(a/b)

plt.title(s=d_prime)
plt.hist(genunine, color='green', alpha=0.5)
plt.hist(imposter, color='red', alpha=0.5)
plt.show()

threshold = npy.linspace(0, 1, 200)
far = []
tpr = []
frr = []

for t in threshold:
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for g in genunine:
        if g <= t:
            tp += 1
        else:
            fn += 1
    
    for i in imposter:
        if i <= t:
            fp += 1
        else:
            tn += 1
    far.append(fp / (fp + tn))
    tpr.append(tp / (tp + fn))
    frr.append(fn / (fn + tp))

far_eer = round(sum(far) / len(far), 2)
frr_eer = round(sum(frr) / len(frr), 2)

eer = (far_eer, far_eer)
plt.title('{0} {1}'.format('EER', eer))
plt.plot(far, frr, lw=2, color='blue')
plt.plot([0,1], [0,1], lw=1, color='black')
plt.show()

plt.title('ROC curve')
plt.plot(far, tpr, lw=2, color='blue')
plt.show()

import numpy as np
import scipy.stats as stats


exp = [61, 102, 119, 128, 62, 158, 271, 57, 266, 137]
cont = [24, 125, 43, 62, 32, 138, 53, 117, 97, 63]

t_crit = 1.734

xbar_exp = np.mean(exp)
xbar_cont = np.mean(cont)

s_exp = np.std(exp, ddof=1)
s_cont = np.std(cont, ddof=1)

n_exp = len(exp)
n_cont = len(cont)

sp2_num = ((n_exp - 1) * s_exp**2 + ((n_cont - 1)) * s_cont**2)
sp2_denom = n_exp + n_cont - 2
sp2 = sp2_num / sp2_denom

t_computed = (xbar_exp - xbar_cont) / np.sqrt(sp2 * (1/n_exp + 1/n_cont))

print(f"t_computed: {t_computed}")

t_computed, p_val = stats.ttest_ind(exp, cont)
print(f"t_computed: {t_computed}")

if p_val < 0.05:
    print("Reject the null hypothesis")
else:
    print("Do not reject the null hypothesis")
import scipy.stats as stats

t_computed, pvalue = stats.ttest_1samp(mpgs,31)
print(f"tcomputed: {t_computed}")
print(f"pval: {t_computed}")

alpha = 0.05

if pvalue < alpha:
    print("Reject the null hypothesis")
else:
    print("Do not reject the null hypothesis")
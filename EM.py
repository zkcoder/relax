import numpy as np
from scipy.stats import norm
np.random.seed(0)
data = np.concatenate([np.random.normal(0, 1, 50), np.random.normal(4, 1, 50)])
print(data)
mu1, sigma1 = -2, 1
mu2, sigma2 = 2, 1
pi = 0.5
# EM算法
for i in range(10):
    # E步骤
    prob1 = pi * norm.pdf(data, mu1, sigma1)
    if i == 1:
        print(prob1)
    prob2 = (1-pi) * norm.pdf(data, mu2, sigma2)
    gamma = prob1/(prob1 + prob2)
    print(gamma)
    # M步骤
    mu1 = np.sum(gamma * data) / np.sum(gamma)
    sigma1 = np.sqrt(np.sum(gamma * (data - mu1)**2) / np.sum(gamma))
    mu2 = np.sum((1 - gamma) * data) / np.sum(1 - gamma)
    sigma2 = np.sqrt(np.sum((1 - gamma) * (data - mu2)**2) / np.sum(1 - gamma))
    pi = np.mean(gamma)
    print(pi)
print(f"mu1 = {mu1:.2f}, sigma1 = {sigma1:.2f},mu2 = {mu2:.2f},sigmm2 = {sigma2:.2f}")


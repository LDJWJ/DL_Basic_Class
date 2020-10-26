# -*- coding: utf-8 -*-

#%%
# 한글
import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

#%%
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from sklearn.datasets import make_blobs
X, y = make_blobs(random_state=42)
print(X.shape, y.shape)
print(X[:5], y[:5])

#%%
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("특성 0")
plt.ylabel("특성 1")
plt.legend(["클래스 0", "클래스 1", "클래스 2"])

#%%
# 이진분류 : 로지스틱(LogisticRegression), 서포트벡터머신(SVM)
# 

# 일대다방법 
# 일대일방법 

#%% LinearSVC 분류기로 학습을 진행
from sklearn.svm import LinearSVC
linear_svm = LinearSVC().fit(X, y)
print("계수 배열의 크기 :", linear_svm.coef_.shape)
print("절편 배열의 크기 :", linear_svm.intercept_.shape)

#%%
import numpy as np

mglearn.discrete_scatter( X[:, 0], X[:, 1], y)
line = np.linspace(-15, 15)

for coef, intercept, color in zip(linear_svm.coef_, 
                                  linear_svm.intercept_, 
                                  mglearn.cm3.colors):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)

plt.ylim(-10, 15)
plt.xlim(-10, 8)
plt.xlabel("특성 0")
plt.ylabel("특성 1")

label_list = ['클래스 0', '클래스 1', '클래스 2', 
              '클래스 0 경계', '클래스 1 경계', '클래스 2 경계']

plt.legend(label_list, loc=(1.01, 0.3))

#%%
mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=0.7)
mglearn.discrete_scatter( X[:, 0], X[:, 1], y)
line = np.linspace(-15, 15)

for coef, intercept, color in zip(linear_svm.coef_, 
                                  linear_svm.intercept_, 
                                  mglearn.cm3.colors):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)


label_list = ['클래스 0', '클래스 1', '클래스 2', 
              '클래스 0 경계', '클래스 1 경계', '클래스 2 경계']
plt.legend(label_list, loc=(1.01, 0.3))
plt.xlabel("특성 0")
plt.ylabel("특성 1")

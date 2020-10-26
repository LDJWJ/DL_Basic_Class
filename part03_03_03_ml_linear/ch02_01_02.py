# -*- coding: utf-8 -*-


#%% 한글 
# 한글
import matplotlib
from matplotlib import font_manager, rc
font_loc = "C:/Windows/Fonts/malgunbd.ttf"
font_name = font_manager.FontProperties(fname=font_loc).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

#%%
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import mglearn
import matplotlib.pyplot as plt

#%%
X, y = mglearn.datasets.make_forge()
print(X.shape, y.shape)
print(X[:5], y[:5])

#%%
a = [1,2,3]
b = [4,5,6]

ab = [ [1,4], [2,5], [3,6]]

for i, j in zip(a,b):
    print(i,j)

#%%
fig, axes = plt.subplots(1, 2, figsize=(10,3))

for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=0.7)
    mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
    ax.set_title(clf. __class__.__name__)
    ax.set_xlabel("특성 0")
    ax.set_ylabel("특성 1")
    
axes[0].legend()
    
#%% C값에 따른 그래프
# C값은 크면 클수록 규제를 안하고 -> 릿지,랏소 alpha값이 크면 클수록 규제가 크다.
# C값은 작으면 작을수록 규제가 강하다 -> 릿지, 랏소 alpha값이 작으면 작을수록 원래 회귀모형과 비슷

mglearn.plots.plot_linear_svc_regularization()

#%% 
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
from sklearn.model_selection import train_test_split

X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                stratify=y,
                                                random_state=42)

# C의 기본값은 1
logreg = LogisticRegression(C=1).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg.score(X_test, y_test)))

## 실습 2-1 
# 2-1 C값을 0.001, 0.01, 10, 100 각각 score값을 구해보기
# C = 1 score : 0.948, 0.958

#%%
### C값이 0.001
logreg001 = LogisticRegression(C=0.001).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg001.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg001.score(X_test, y_test)))

### C값이 0.01
logreg01 = LogisticRegression(C=0.01).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg01.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg01.score(X_test, y_test)))

# C의 기본값은 1
logreg = LogisticRegression(C=1).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg.score(X_test, y_test)))

### C값이 10
logreg10 = LogisticRegression(C=10).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg10.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg10.score(X_test, y_test)))

### C값이 100
logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg100.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg100.score(X_test, y_test)))

#%%
### C값이 1000
logreg1000 = LogisticRegression(C=1000).fit(X_train, y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg100.score(X_train, y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg100.score(X_test, y_test)))

#%% 시각화
plt.plot(logreg001.coef_.T, '^', label="C=0.001")
plt.plot(logreg01.coef_.T, '^', label="C=0.01")
plt.plot(logreg.coef_.T, '^', label="C=1")
plt.plot(logreg10.coef_.T, 'o', label="C=10")
plt.plot(logreg100.coef_.T, 'v', label="C=100")

xlims = plt.xlim()
plt.hlines(0, xlims[0], xlims[1])

plt.ylim(-5, 5)
plt.xlabel("특성")
plt.ylabel("계수 크기")
plt.legend()




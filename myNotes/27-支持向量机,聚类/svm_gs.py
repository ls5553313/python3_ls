# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('../../data/multiple2.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=5)
# 超参数组合列表
params = [
    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]},
    {'kernel': ['poly'], 'C': [1], 'degree': [2, 3]},
    {'kernel': ['rbf'], 'C': [1, 10, 100, 1000],
     'gamma': [1, 0.1, 0.01, 0.001]}]
# 网格搜索寻优
model = ms.GridSearchCV(
    svm.SVC(probability=True), params, cv=5)
model.fit(train_x, train_y)
for param, score in zip(
        model.cv_results_['params'],
        model.cv_results_['mean_test_score']):
    print(param, score)
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
cr = sm.classification_report(test_y, pred_test_y)
print(cr)
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
print(prob_x)
pred_prob_y = model.predict(prob_x)
print(pred_prob_y)
probs = model.predict_proba(prob_x)
print(probs)
mp.figure('Grid Search', facecolor='lightgray')
mp.title('Grid Search', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y,
              cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y,
           cmap='brg', s=80)
mp.scatter(prob_x[:, 0], prob_x[:, 1], c=pred_prob_y,
           cmap='cool', s=70, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})
mp.show()

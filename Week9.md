# How Can Machines Learn?

<br />

## Linear Regression

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/roadmap.PNG)

<br />

```
上次花力氣在二元分類Binary Classification上面證明了VC bound是可以用在各種不同的Error Measure,
也可以用在有Noise的情形, 當然也可用在這次的主題Regression
所以想像我們已經有這個Bound, 而演算法上我們該如何設計Regression這類問題?
```

<br />

***

### Linear Regression Problem

#### Credit Limit Problem

<br />

![credit limit](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/credit%20limit.PNG)

<br />

#### Lineear Regression Hypothesis

<br />

![linear regression hypothesis](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/linear%20regression%20hypothesis.PNG)

<br />

#### Illustration of Linear Regression

<br />

```
找到一條線/平面, 使得每個點到線/平面的距離和(誤差)最小
```

<br />

![illustration](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/illustration.PNG)

<br />

#### The Error Measure

<br />

![error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/error%20measure.PNG)

<br />

***

### Linear Regression Algorithm

#### Matrix Form of Ein(w)

<br />

```
向量v = (v1, v2, ..., vn)
向量v長度 = sqrt(v1^2 + v2^2 + ... + vn^2)
向量v長度平方 = v1^2 + v2^2 + ... + vn^2
```

<br />

![matrix form of ein](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/matrix%20form%20of%20ein.PNG)
![min einw](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/min%20einw.PNG)

<br />

#### The Gradient ∇Ein(w)

<br />

![the gradient einw](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/the%20gradient%20einw.PNG)

<br />

```
A = (d+1) x (d+1) 矩陣
B = (d+1) x 1 向量
C = 1 x 1 常數
```

<br />

#### Optimal Linear Regression Weights

<br />

```
AX = b
A是可逆矩陣 => 有唯一解(X = A^(-1)b), detA不為0
A是奇異矩陣 => 無限多解, detA=0
```

<br />

![optimal lin reg w](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/optimal%20lin%20reg%20w.PNG)

<br />

```
當N<d+1時, 
X的rank <= min(N,d+1), 所以當N<d+1時, X的rank < d+1
=> X^T*X的rank也會是<d+1
故 X^T*X為不可逆

實務上若平台已有寫好的pseudo-inverse程式, 建議直接使用
因為直接使用可以避免需要去判斷到底是不是可逆矩陣,
而且在那些看起來很接近singular的矩陣, 數值上也能處理得很好
```
<br />

#### Linear Regression Algorithm

<br />

![lin reg algorithm](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/lin%20reg%20algorithm.PNG)

<br />

***




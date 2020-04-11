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

### Generalization Issue

#### Is Linear Regression a 'Learning Algorithm'?

<br />

![is lin reg a learning algorithm](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/is%20lin%20reg%20a%20learning%20algorithm.PNG)

<br />

#### Benefit of Analytic Solution: 'Simpler-than-VC' Guarantee

```
d+1 => 代表自由度, 有多少種w
N => 代表資料量
資料量越多(N>>d+1), Ein平均的資料量越少
```

<br />

![benefit of analytic sol](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/benefit%20of%20analytic%20sol.PNG)

<br />

#### Geometric View of Hat Matrix

<br />

```
w 把X的每一個column拿來做線性組合, 每一個column也都是N維向量
=> 生成一個線性向量空間 span of X columns

H (hat matrix): 將y投影到span上變成y_hat
I-H (matrix): 將y向量轉換成垂直於span的y-y_hat

trace(I-H): (I-H)矩陣的對角線上所有值相加

物理意義: 原本有一個N個自由度的向量在N維空間轉來轉去, 
現在要把它投影到一個d+1維的空間, 然後取餘數,
[因為X由d+1個向量組成, 最多就是d+1維空間]
所以餘數剩下的自由度最多就是N-(d+1)個
```

<br />

![geometric view of hat matrix](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/geometric%20view%20of%20hat%20matrix.PNG)

<br />

#### An Illustrative Proof

<br />

![an illustrative proof](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/an%20illustrative%20proof.PNG)

<br />

```
noise向量可以經由I-H矩陣轉換成y-y_hat
I-H有多少自由度(能量)? => trace(I-H)=N-(d+1)
noise的能量最多就是N-(d+1)這麼多

Ein的平均就是對所有noise做平均的結果

Ein是看到的東西, 有noise的話會看到那一條線往noise那邊偏一點點 => Ein會好看一點
新資料的雜訊可能是在另一邊, 會比看到的那一條再往另一邊偏一點點 => Eout會差一點
```

<br />

#### The Learning Curve

<br />

```
由Ein和Eout平均的公式可以畫出learning curve的圖,
描述的是資料量與平均Ein和Eout的關係
```

<br />

![the learning curve](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/the%20learning%20curve.PNG)

<br />

***

### Linear Regression for Binary Classification

#### Linear Classification vs. Linear Regression

<br />

![lin class vs. lin reg](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/lin%20class%20vs.%20lin%20reg.PNG)

<br />

```
將linear regression得到的值一正負分成+1和-1兩類
是否就可以用在binary classification上?
```

<br />

#### Relation of Two Errors

<br />

![relation of two errors](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/relation%20of%20two%20errors.PNG)

<br />

#### Linear Regression for Binary Classification

Recap

<br />

![recap eout upper bound](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/recap%20eout%20upper%20bound.PNG)

<br />

![lin reg for binary class](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/lin%20reg%20for%20binary%20class.PNG)

<br />

### Summary

<br />

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%209/summary.PNG)





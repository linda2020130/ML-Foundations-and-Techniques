# How Can Machines Learn?

<br />

## Logistic Regression

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/roadmap.PNG)

<br />

***

### Logistic Regression Problem

#### Heart Attack Prediction Problem

<br />

```
有noise的狀況下可以用一個target distribution(目標的分布)來描述這個問題,
而這個理想的目標函數實際上就是把目標分布去取說他到底大於0.5(在機率比較大的那邊=>+1), 
還是小於0.5(在機率比較小的那邊=>-1) => binary classification
```

<br />

Heart Disese? 
* **Yes/No** => Binary Classification

<br />

![heart attack pred problem1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/heart%20attack%20pred%20problem1.PNG)

<br />

Heart Attack?
* **Probability** => *Soft* Binary Classification

<br />

![heart attack pred problem2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/heart%20attack%20pred%20problem2.PNG)

<br />

#### Soft Binary Classification

<br />

```
拿不到ideal data(y'N = probability between 0 and 1),
只拿得到y={+1, -1}的資料...

我們有興趣的target function是0到1之間的輸出,
然而, 我們手上有的是和以前binary classification一樣的這些OOXX資料,
我們要怎麼做才能求到一個好的hypothesis來解決這樣的問題?
```

<br />

![soft binary class](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/soft%20binary%20class.PNG)

<br />

#### Logistic Hypothesis

<br />

```
將每個features拿來算一個加權分數, 多加一個x0代表常數項
算出來的分數越高, 代表風險越大

Logistic Function可以將任意一個實數轉化成一個0到1之間的值
```

<br />

![logistic hypothesis](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/logistic%20hypothesis.PNG)

<br />

#### Logistic Function

<br />

![logistic function](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/logistic%20function.PNG)

<br />

#### Fun Time

<br />

![fun time](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/fun%20time.PNG)

<br />

```
logistic hypothesis 實際上只是binary classification 的hypothesis的一個相對應的版本
```

<br />

***

### Logistic Regression Error

<br />

```
要如何定義Logistic Regression的Error Function?
```

<br />

#### Three Linear Models

<br />

* Linear Classification: error=**0/1**
* Linear Regression: error=**squared**
* Logistic Regression: err=?

<br />

![three linear models](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/three%20linear%20models.PNG)

<br />

#### Likelihood

<br />

```
Logistic Regression的目標是找到h(x)接近f(x)=P(+1|x) [P of +1 given x]
例:心臟病發(y=+1)的機率P是多少?

將f(x)=P(+1|x)反過來寫:
P(y|x)=f(x) for y=+1
      =1-f(x) for y=-1 [因為機率P加起來要是1]
```

<br />

![likelihood1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/likelihood1.PNG)

![likelihood2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/likelihood2.PNG)

<br />

```
error measure是用來衡量h和f有多接近
若h和f很接近, 那麼h產生這些資料的可能性和f產生這些資料的可能性就應該很接近

f是真正已經產生這些資料D的機率函數=>通常是因為f產生這些資料D的機率大
```

<br />

#### Likelihood of Logistic Hypothesis

<br />

```
h的可能性和f的機率應該要是差不多"大"的
在所有的h裡面找可能性最高的h來當作g

logistic function的對稱性: 1-h(x)=h(-x)

likelihood(h)=P(x1)h(+x1)*P(x2)h(-x2)*...*P(xN)h(-xN)

因為我們是要在所有h裡找出可能性最高的,
P(x1),...,P(xN)在每個h裡都是一樣的,
所以likelihood(h)會正比於h(y1x1)*h(y2x2)*...*h(yNxN)
其中的y={+1,-1}
```

<br />

![likelihood of logistic hypothesis1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/likelihood%20of%20logistic%20hypothesis1.PNG)
![likelihood of logistic hypothesis2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/likelihood%20of%20logistic%20hypothesis2.PNG)

<br />

#### Cross-Entropy Error

<br />

![cross-entropy error1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/cross-entropy%20error1.PNG)
![cross-entropy error2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/cross-entropy%20error2.PNG)
![cross-entropy error3](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/cross-entropy%20error3.PNG)

<br />

```
最大化某個值=最小化某個值的負數
(因為error measure都是找Ein最小值, 所以必須推導一個Ein做minimize的動作)

多乘一個scaling=1/N是為了使logistic regression的error measure長得更像我們熟悉的長相
Ein應該要再包含1/N的部分

產生的err measure是一個pointwise error(在一個X一個Y上面就可以衡量error)
```

<br />

![cross-entropy error4](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2010/cross-entropy%20error4.PNG)

<br />







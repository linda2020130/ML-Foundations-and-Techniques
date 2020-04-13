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








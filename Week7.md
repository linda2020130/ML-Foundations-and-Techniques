# Why Can Machines Learn?

<br />

## The VC Dimension

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/roadmap.PNG)

<br />

***

### Definition of VC Dimension

#### Recap: More on Growth Function

```
當N >= 2, k >= 3 時,
B(N, k)會被 N^(k-1) bound住
```

<br />

![recap_growth func](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/recap_growth%20func.PNG)

<br />

#### Recap: More on Vapnik-Chervonenkis (VC) Bound

```
任一Hypothesis g遇到壞事情的機率很小
當N夠大時, 可將成長函數代換成上限
```
<br />

![recap_vc bound](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/recap_vc%20bound.PNG)

<br />

#### VC Dimension

![vc dimension](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/vc%20dimension.PNG)

<br />

```
在VC Dimension上, Hypothesis set可以shatter某N個點
但如果超過VC Dimension, 就開始不能shatter => break point k
所以 d_vc = (min k) - 1
```

<br />

#### The Four VC Dimensions

![the four vc dimension](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/the%20four%20vc%20dimensions.PNG)

<br />

#### VC Dimension and Learning

```
VC Dimension是有限的 => 好的hypothesis set (Ein近似Eout)
與演算法, input資料的分布, 和目標函數都無關
```

<br />

![vc dimension and learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/vc%20dimension%20and%20learning.PNG)

<br />

***

### VC Dimension of Perceptrons

#### 2D PLA Revisited

![2d pla revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/2d%20pla%20revisited.PNG)

<br />

#### VC Dimension of Perceptrons

![vc dimension of perceptrons](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/vc%20dimension%20of%20perceptrons.PNG)

<br />

1. There are **some** d+1 inputs we can shatter  =>  **d_vc >= d+1**
2. We cannot shatter **any** set of d+2 inputs  =>  **d_vc <= d+1**

<br />

#### d_vc >= d+1

```
假設X為some trivial inputs...(加上x0代表threshold)
=> X 為可逆矩陣
```

<br />

![can we shatter x](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/can%20we%20shatter%20x.PNG)

<br />

```
我們假設的X(some trivial inputs)可以被shattered(所有的dichotomy都可以被找到)
```

<br />

#### d_vc <= d+1

More rows than columns  =>  Linear Dependence 

```
因為線性相依產生, d+2的向量可以表示成其他向量的線性組合
```

![d_vc](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/d_vc.PNG)

<br />

Linear dependence restricts dichotomy

```
假設在d+2 inputs下, 
已知sign(a1),...,sign(a_d+1) 
只能產生出sign(a_d+2)=1 (假設生成-1會得到矛盾)
```

<br />

***

### Physical Intuition of VC Dimension

```
d_vc = d+1  => VC Dimension 與 perceptrons的維度有關
```
<br />

#### Degrees of Freedom

hypothesis parameters w = (w0, w1,..., wd): creates **degree of freedom**

![degrees of freedom](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/degrees%20of%20freedom.PNG)

<br />

```
VC Dimension的物理意義大致上就是我的hypothesis set在我要做二元分類的時候,到底多少有效的自由度?
=> 也就是到底可以產生多少種dichotomy
```

<br />

#### Two Old Friends

```
d_vc 近似於 可調整旋鈕的個數
```

<br />

![two old friends](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/two%20old%20friends.PNG)

<br />

#### M and d_vc

```
遇到壞資料的機率大時,hypothesis set自由度也大(演算法的選擇變多)
```
<br />

![m and d_vc](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%207/m%20and%20d_vc.PNG)

<br />

***

### Interpreting VC Dimension

#### VC Bound Rephrase: Penalty for Model Complexity

```
壞事情發生的機率很小 => 好事情發生的機率很大
```

<br />

![penalty for model complexity]()

<br />

```
這個式子代表有很高的機會Ein和Eout的差別會被限制在這個根號項裡
=> 差別小代表好事情發生(Ein和Eout會很靠近)
一般稱做 generalization error
=> 說明舉一反三這個部分做得多好
```







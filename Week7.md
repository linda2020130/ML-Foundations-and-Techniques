# Why Can Machines Learn?

<br />

## The VC Dimension

<br />

![roadmap]()

<br />

***

### Definition of VC Dimension

#### Recap: More on Growth Function

```
當N >= 2, k >= 3 時,
B(N, k)會被 N^(k-1) bound住
```

<br />

![recap_growth func]()

<br />

#### Recap: More on Vapnik-Chervonenkis (VC) Bound

```
任一Hypothesis g遇到壞事情的機率很小
當N夠大時, 可將成長函數代換成上限
```
<br />

![recap_vc bound]()

<br />

#### VC Dimension

![vc dimension]()

<br />

```
在VC Dimension上, Hypothesis set可以shatter某N個點
但如果超過VC Dimension, 就開始不能shatter => break point k
所以 d_vc = (min k) - 1
```

<br />

#### The Four VC Dimensions

![the four vc dimension]()

<br />

#### VC Dimension and Learning

```
VC Dimension是有限的 => 好的hypothesis set (Ein近似Eout)
與演算法, input資料的分布, 和目標函數都無關
```

<br />

![vc dimension and learning]()

<br />

***








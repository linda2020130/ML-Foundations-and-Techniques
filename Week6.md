# Why Can Machines Learn?

<br />

## Theory of Generalization

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/roadmap.PNG)

<br />

***

### Restriction of Break Point

```
growth function mH(N): N個點時，max number of dichotomies
當mH(k) < 2^k 時，k稱為 break point (k+1, k+2,...也是break point)
當mH(k) = 2^k 時，Hypothesis Set 可以被shattered(k個點shatter H)
```

<br />

#### The Four Break Points

![four break points](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/the%20four%20break%20points.PNG)

<br />

```
成長函數mH(N)與break point的關聯?
```

<br />

#### Restriction of Break Point

> **min break point k** restricts **max possible mH(N)** a lot for N > k

![restriction of break point](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/restriction%20of%20break%20point.PNG)

<br />

***

### Bounding Function: Basic Cases

#### Bounding Function

```
假設dichotomy是由OOXX組合而成的一堆向量，其長度為N
然而，其中k個維度(break point=k)都不希望看到OOXX的所有組合(2^k個組合)
也就是說不能出現shatter，不能讓這k個點組成所有2^k個組合
```
<br />

![example](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/example.PNG)

<br />

![bounding function](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/bounding%20function.PNG)

<br />

#### Table of Bounding Function

* B(N, k) = 2^N - 1 for N = k

![table of bounding function](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/table%20of%20bounding%20function.PNG)

<br />

***

### Bounding Function: Inductive Cases

#### Estimating B(4, 3)
![estimating B(4,3)](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/estimating.PNG)

<br />

#### Estimating Part of B(4, 3)

```
先用電腦計算出B(4, 3)= 11
再試圖將11拆解...
```
<br />

![estimating part of B(4, 3)-1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/estimating%20part%20of%20B(4%2C%203)_1.PNG)

<br />

```
得到 a + b <= B(3, 3)
```

<br />

![estimating part of B(4, 3)-2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/estimating%20part%20of%20B(4%2C%203)_2.PNG)

<br />

```
得到a <= B(3, 2)
```

<br />

#### Putting It All Together

![put together](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/put%20together.PNG)

<br />

**Generalized**

![generalized upper bound](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/generalized%20upper%20bound.PNG)

Now have **upper bound** of bounding function

<br />

#### Bounding Function: The Theorem

![bounding function theorem](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/bounding%20function%20theorem.PNG)

<br />

```
Bounding Function B(N, k)的上限的上限會是某個多項式函數
=> 若成長函數mH(N)存在break point, mH(N)則會是poly(N)
```

<br />

#### The Three Break Point

```
當知道break point時, 就可以知道成長函數mH(N)的上限
```

<br />

![the three break points](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/the%20three%20break%20points.PNG)

<br />




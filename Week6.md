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

![bounding function]()

<br />

#### Table of Bounding Function

![table of bounding function]()

<br />









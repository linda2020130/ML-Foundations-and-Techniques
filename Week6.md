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

***

### A Pictorial Proof
```
已知成長函數可能是隨著多項式長大, 能不能把這個成長函數丟進去原本finite bin的Hoeffding裡面
使得無限多點的情況下Hoeffding也成立???
```
<br />

![BAD Bound](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/bad%20bound.PNG)

<br />

```
僅需要了解這一個證明所用到的技巧就好
```

<br />

#### Step 1: Replace Eout by E'in

```
拿用來做verfication的另外N個點(D')計算出E'in
當Ein離Eout很遠時, 抽一組E'in時, 會有超過一半的機率Ein和E'in的機率也會很近
```

<br />

![step 1_replace eout by e'in](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/step%201_replace%20eout%20by%20ein.PNG)

<br />

#### Step 2: Decompose H by Kind

```
選用其中一個hypothesis, 來看Ein with D和E'in with D'遇到Bad Data的時機是否重疊
重疊越多=>mH(2N)越小[越接近mH(N)]
```

<br />

![step 2_decompose h by kind](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/step%202_decompose%20h%20by%20kind.PNG)

<br />

#### Step 3: Use Hoeffding without Replacement

```
用一個比較小的bin, 裡面裝2N個珠子, 取N個出來, 取後不放回
比較一個sample和所有的平均=>Hoeffding
```

<br />

![step 3_use hoeffding without replacement](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/step%203_use%20hoeffding%20without%20replacement.PNG)

<br />

#### That's All!

```
2D perceptron
break point = 4  => 成長函數最多不會比N^3快
N夠大時  =>  壞事情發生的機率較會很小
         =>  演算法選Ein最小的那個
         =>  g最後也大概會是最小Eout

所以說, 點夠多時, 2D perceptron真的能夠達到機器學習的效果
```

<br />

![that's all](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/that's%20all.PNG)

How about perceptron in other dimension?

<br />

#### Summary 

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%206/summary.PNG)


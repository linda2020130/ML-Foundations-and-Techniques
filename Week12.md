# How Can Machines Learn?

## Nonlinear Transformation?

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/roadmap.PNG)

<br />

```
上週講的是三個Linear Models(Linear Classification, Linear Regression, Logistic Regression),
都可以用在各式Classification問題上, 
包括Binary Classification和Multiclass的問題, 但是這些Models都是用線性的方式算一個分數, 
那我們現在就是要把這樣的Models延伸到Nonlinear的情況做資料分類
```

<br />

***

### Quadratic Hypothesis

#### Linear Hypotheses

<br />

```
理論上VC Dimension(複雜度)是受到控制的 => Ein與Eout不會差太遠
實務上遇到用線無法完美切開的點時, Ein會很大 => Eout跟著也很大
```

<br />

![linear hypotheses](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/linear%20hypotheses.PNG)

<br />

#### Circular Separable

<br />

```
用圓圈(以原點為中心, 根號0.6為半徑)將圈圈叉叉分開,
x1^2 + x2^2 > 0.6 => 叉叉
x1^2 + x2^2 < 0.6 => 圈圈
=> 圓圈圈可分

如何有系統的將過去學過的線性演算法修改成圓圈圈適用?
```

<br />

![circular separable](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/circular%20separable.PNG)

<br />

#### Circular Separable and Linear Separable

Feature Transform: z1 = x1^2, z2 = x2^2, ...

<br />

![circular separable and linear separable](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/circular%20separable%20and%20linear%20separable.PNG)

<br />

```
如果原來的資料X是用圈圈可以分開的, 那經過一番轉換, 新資料Z就可以用線性來分開
但反過來的話呢?
```

<br />

#### Linear Hypotheses in Z-Space

<br />

```
在Z空間裡的每條線不見得在X空間都對應到正圓,
依照w不同可能會是正圓, 橢圓, 雙曲線,常數...(不同的二次曲線)
然而對應到的都會是"通過原點"的二次曲線
```

<br />

![linear hypotheses in z-space](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/linear%20hypotheses%20in%20z-space.PNG)

<br />

#### General Quadratic Hypothesis Set

<br />

![general quadratic hypothesis set](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/general%20quadratic%20hypothesis%20set.PNG)

<br />

```
在Z空間裡的每一個perceptron可以幫助我們實現某一個在X空間裡對應的這個分類方式

現在我們知道如何定義一個二次曲線集合起來的Hypothesis Set,
下一步: 要怎樣學到一個好的二次hypotheses?
```

<br />

***

### Nonlinear Transform

#### Good Quadratic Hypothesis

<br />

![good quadratic hypothesis](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/good%20quadratic%20hypothesis.PNG)

<br />

#### The Nonlinear Transform Steps

<br />

![nonlinear transform steps](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/nonlinear%20transform%20steps.PNG)

<br />

```
想像是透過反運算將Z空間得到的perceptron轉化為X空間的perceptron,
然而...反運算不一定存在, 因為X到Z的關係可能不是一對一
所以實際上是把任何一個在X空間裡的點, 把它對應到Z空間裡面, 
得到在Z空間時是圈圈或叉叉後, 再把X空間的點標圈圈或叉叉
```

<br />

#### Nonlinear Model via Nonlinear Φ + Linear Models

<br />

Two choices:
* Feature Transform Φ
* Linear Model A

<br />

![nonlinear model via nonlinear phi + linear models](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/nonlinear%20model%20via%20nonlinear%20phi%20%2B%20linear%20models.PNG)

<br />

#### Feature Transform Φ

<br />

![feature transform](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/feature%20transform.PNG)

<br />

```
透過Feature Transform(需要人的智慧)將raw feature轉換為concrete feature(機器易學)
但是做Feature Transform所犧牲的代價是...?
```

<br />

***

### Price of Nonlinear Transform

#### Computation/Storage Price

<br />

![computation_storage price](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/computation_storage%20price.PNG)

<br />

```
Q次多項式轉換需要多少dimensions? (Z有多少個組成?)
有d種不同的東西(x1, x2, ..., xd), 要取小於等於Q個東西出來, 
在允許重複取的情形下, 有多少種取法? => C Q+d取Q

做Feature Transform需要花Q^d的力氣去做計算和儲存,
所以當Q很大時, 計算/儲存上會出現困難
```

<br />

#### Model Complexity Price

<br />

![model complexity price](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/model%20complexity%20price.PNG)

<br />

```
原本在X空間是d+1的自由度(d_vc), 轉換到Z空間自由度大概會是~d+1(C Q+d取Q)

任何一個在Z空間裡的d加2個點是沒有任何一條直線(perceptron)可以shatter的
=> 回到X空間裡的d加2個點也不能夠被任何Q次曲線shatter
```

<br />

#### Generalization Issue

<br />

![generalization issue](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/generalization%20issue.PNG)

<br />

```
Tradeoff: Q很大時 => Ein可以很小, 但Ein和Eout可能隔很遠
          Q很小時 => Ein和Eout靠很近, 但Ein可能很大
          
該如何選擇Q的大小? 用眼睛看可以嗎?
```

<br />

#### Danger of Visual Choices

<br />

![danger of visual choices](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/danger%20of%20visual%20choices.PNG)

<br />

```
用眼睛看的過程中已使用了"人腦"來主觀判斷資料適合用多大的Q
忽略了使用人腦的代價 => 高估機器學習可以做到的事情
```

<br />

***

### Structured Hypothesis Sets

#### Polynomial Transform Revisited

<br />

![polynomial transform revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/polynomial%20transform%20revisited.PNG)

<br />

#### Structured Hypothesis Sets

<br />

![structured hypo sets](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/structured%20hypo%20sets.PNG)

<br />

```
d_vc越大 => 選擇(hypothesis)越多 => 越有機會找到Ein比較小的g
```

<br />

#### Linear Model First

<br />

![linear model first](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/linear%20model%20first.PNG)

<br />

```
Ein只要夠小就好, 不用追求最小, 甚至是等於0
實務上來說Linear Model其實就可以做得不錯
```

<br />

***

### Summary

<br />

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2012/summary.PNG)


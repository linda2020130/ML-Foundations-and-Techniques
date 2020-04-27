# How Can Machines Learn?

## Nonlinear Transformation?

<br />

![roadmap]()

<br />

```
上週講的是三個Linear Models(Linear Classification, Linear Regression, Logistic Regression)都可以用在各式Classification問題上, 包括Binary Classification和Multiclass的問題, 但是這些Models都是用線性的方式算一個分數, 那我們現在就是要把這樣的Models延伸到Nonlinear的情況做資料分類
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

![linear hypotheses]()

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

![circular separable]()

<br />

#### Circular Separable and Linear Separable

Feature Transform: z1 = x1^2, z2 = x2^2, ...

<br />

![circular separable and linear separable]()

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

![linear hypotheses in z-space]()

<br />

#### General Quadratic Hypothesis Set

<br />

![general quadratic hypothesis set]()

<br />

```
在Z空間裡的每一個perceptron可以幫助我們實現某一個在X空間裡對應的這個分類方式
```

<br />










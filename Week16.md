# How Can Machines Learn Better?

## Three Learning Principles

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/roadmap.PNG)

```
三個對做機器學習時的錦囊妙計
```

<br />

***

### Occam's Razor

* An explanation of the data should be made **as simple as possible**, but no simpler.
* Entities must not be multiplied **beyond necessity**.
* **Occam's razor** for trimming down unnecessary explanation.

<br />

#### Occam's Razor for Learning

The **simplest model** that fits the data is also the most plausible.

<br />

```
1. 怎樣的模型叫做簡單?
2. 為什麼簡單的模型比較好?
```

<br />

#### Simple Model

<br />

```
simple hypothesis => 看起來很簡單, 只有幾個參數而已(e.g. 一個圓心一個半徑所形成的圓)
simple model => 有效Hypotheses不是很多, 成長函數成長緩飯

simple model => simple hypothesis
```

<br />

![simple model](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/simple%20model.PNG)

<br />

#### Simple is Better

<br />

```
亂亂的資料 => 大概不可以分開
可以分開的資料 => 應該不是亂亂的資料(有某種程度的規律性)

先試linear model
是否先從簡單的模型開始用?
```

<br />

![simple is better](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/simple%20is%20better.PNG)

<br />

***

### Sampling Bias

If the data is sampled in a biased way, learning will produce a similiarly biased outcome.

<br />

```
做機器學習的前提假設: 
做訓練的抽樣資料和做測試的抽樣資料並須來自同一個分布
data and testing both iid from P
```

<br />

![sampling bias]()

<br />

#### Dealing with Sampling Bias

<br />

```
了解測試環境, 然後讓訓練環境盡可能接近測試環境
```

<br />

![dealing with sampling bias]()

<br />

***




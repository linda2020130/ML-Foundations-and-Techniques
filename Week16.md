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

```
做機器學習的前提假設: 
做訓練的抽樣資料和做測試的抽樣資料並須來自同一個分布
data and testing both iid from P
```

<br />

![sampling bias](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/sampling%20bias.PNG)

<br />

#### Dealing with Sampling Bias

<br />

```
了解測試環境, 然後讓訓練環境盡可能接近測試環境
```

<br />

![dealing with sampling bias](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/dealing%20with%20sampling%20bias.PNG)

<br />

***

### Data Snooping

#### Visual Data Snooping

<br />

```
肉眼偷看資料 => 腦袋裡的d_vc會被忽略掉
=> 計算出來的d_vc會失準
```

<br />

![visual data snooping](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/visual%20data%20snooping.PNG)

<br />

#### Data Snooping by Mere Shifting-Scaling

<br />

![shifting-scaling](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/shifting-scaling.PNG)

<br />

#### Data Snooping by Data Reusing

<br />

```
拷問資料夠久, 它就會招供(給你一個很好的Hypothesis)
```

<br />

![data reusing](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/data%20reusing.PNG)

<br />

#### Dealing with Data Snooping

<br />

```
先保留好一筆做Validation的資料
做決定(選特徵)前先不要看資料, 先將專業知識放進去, 不要看完資料才說資料有什麼特性
```

<br />

![dealing with data snooping](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/dealing%20with%20data%20snooping.PNG)

<br />

***

### Power of Three

#### Three Related Fields

1. Data Mining
2. Artificial Intelligence
3. Statistics

<br />

![related fields](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/related%20fields.PNG)

<br />

#### Three Theoretical Bounds

1. Hoeffding
2. Multi-Bin Hoeffding
3. VC

<br />

![bounds](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/bounds.PNG)

<br />

#### Three Linear Models

1. PLA/pocket
2. Linear regression
3. Logistic regression

<br />

![models](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/models.PNG)

<br />

#### Three Key Tools

1. Feature Transform
2. Regularization
3. Validation

<br />

![tools](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/tools.PNG)

<br />

#### Three Learning Principles

1. Occam's Razer: simple is good.
2. Sampling Bias: class matches exam.
3. Data Snooping: honesty is best policy.

<br />

#### Three Future Directions

1. More Transform
2. More Regularization
3. Less Label

<br />

![directions](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/directions.PNG)

<br />

***

### Summary

<br />

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2016/summary.PNG)

<br />

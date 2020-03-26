# Why Can Machines Learn

<br />

## Noise and Error

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/roadmap.PNG)

```
VC Dimension在推導過程中有一些假設，藉由放寬這些假設，
讓我們對VC Dimension的瞭解可以放寬到更多不同的問題上
```

<br />

***

### Noise and Probabilistic Target

* Good hypothesis set: **finite** DC Dimension
* Good hypothesis: **low** Ein

<br />

![recap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/recap.PNG)

<br />

#### Noise

<br />

Noise can happen in x or y.

<br />

![noise](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/noise.PNG)

<br />

#### Probabilistic Marbles

<br />

![probabilistic marbles](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/probabilistic%20marbles.PNG)

<br />

```
每一顆彈珠代表一個個x，然後從某個機率分布P把彈珠抽出來
當hypothesis的預測與目標函數f的預測相同時,漆成綠色彈珠
不同時(表示犯錯誤的地方)漆成橘色彈珠

有雜訊的意思是拿到的y可能與f(x)不同，
原本是錯誤的，結果變成綠色，
可以想像成是會變色的彈珠(probabilistic marbles)，
每個時間點可能從綠色變橘色，或從橘色變綠色(顏色不固定)
然而，整個罐子看，還是有一個大概的橘色比例(切在一個時間點上)

雖然彈珠顏色變來變去，但只要在抽出來的過程[x~P(x) iid]，
還有這些變來變去的過程[y~P(y|x) iid]，符合某些機率分布等等，
那麼就可以用抽樣的方式來估算罐子裡在同一時間有多少比例的橘色
```

<br />

#### Target Distribution P(y|x)

<br />

```
Mini-target: 對x(一顆彈珠)做一個預測，最理想的(顏色)預測是?
```

<br />

![target distribution](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/target%20distribution.PNG)

<br />

#### The New Learning Flow

<br />

![new learning flow](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/new%20learning%20flow.PNG)

<br />

```
PLA 在想盡辦法去讓Ein越小越好時，會不會真的變成Eout越小越好?
會~ 因為在有noise的情況下，只要我們想像noise是用Target Distribution來描述的話，
還是可以把事情學得很好:)
```

<br />

***

### Error Measure

<br />

```
先前用來衡量g跟f到底有多接近的方法
三種特性: 
1. out-of-sample
2. pointwise
3. classification
```

<br />

![error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/error%20measure.PNG)

<br />

#### Pointwise Error Measure

<br />

```
考慮每個點上到底有多少錯誤，再把他們平均
=> pointwise error measure (記做err)
```

<br />

![pointwise error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/pointwise%20error%20measure.PNG)

<br >

```
目前主要使用pointwise的方式來衡量錯誤，因為比較簡單
還有很多其他的錯誤衡量方式比較複雜，需要從pointwise方式出發，未來會再介紹
```

<br />

#### Two Important Pointwise Error Measures

<br />

```
有哪些pointwise的方式?
Examples:
1. 0/1 error
2. squared error
...
```

<br />

![two important pointwise error measures](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/two%20important%20pointwise%20error%20measures.PNG)

<br />

#### Ideal Mini-Target

<br />

**P(y|x)** and **err** define *ideal mini-target f(x)*

<br />

![ideal mini-target](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/ideal%20mini-target.PNG)

<br />

#### Learning Flow with Error Measure

<br />

![learning flow with error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/learning%20flow%20with%20error%20measure.PNG)

<br />

```
VC Dimension的整個推導與精神對很多不同的Hypothesis Set還有不同的錯誤衡量都會成立
例如: 今天不做classification分類，而是做回歸分析
則只需要將VC Dimension的推導做一些修改，定義今天一個實數輸出函數的VC Dimension是怎麼算的
```

<br />

***

### Algorithmic Error Measure

<br />

#### Choice of Error Measure

0/1 error penalizes both types equally.

<br />

![choice of error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/choice%20of%20error%20measure.PNG)

<br />

#### Fingerprint Verification for Supermarket

An example of err penalizes heavier on **false reject**.

<br />

![fingerprint verification for supermarket](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/fingerprint%20verification%20for%20supermarket.PNG)

<br />

#### Fingerprint Verification for CIA

An example of err penalizes heavier on **false accept**.

<br />

![fingerprint verification for cia](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/fingerprint%20verification%20for%20cia.PNG)

<br />

#### Take-home Message for Now

err is **application/user-dependent**.

```
然而, 使用者很難將錯誤(err)衡量數字化...
因此, 我們使用err hat來替代

可產生err hat的方式:
plausible => 能夠說服我們的方式(合理的衡量方式)
friendly => 對我們演算法設計更容易一點的方式(比較容易求到最佳解)
```

<br />

![take-home message for now](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/take-home%20message%20for%20now.PNG)

<br />

#### Learning Flow with Algorithmic Error Measure

<br />

![learning flow with algorithmic error measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%208/learning%20flow%20with%20algorithmic%20error%20measure.PNG)

<br />

***









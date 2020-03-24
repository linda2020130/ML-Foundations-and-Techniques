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






# How Can Machines Learn Better?

## Hazard of Overfitting

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/roadmap.PNG)

<br />

```
上週講到linear model配上nonlinear transform可以很快的產生出非線性model, 代價是必須付出額外的model complexity,
而這個額外的model complexity會造成機器學習裡面很大的困難-Overfitting,
因此這週要討論的就是到底這個困難是如何產生以及如何該如何解決它
```

<br />

***

### What is Overfitting?

#### Bad Generalization

<br />

```
VC Bound告訴我們...當VC Dimension太大的時候, 容易出現Ein低, 但Eout卻很高的情況, 稱之為Bad Generalization
(無法舉一反三, 只能將看過的點做得很好)
```

<br />

![bad generalization](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/bad%20generalization.PNG)

<br />

#### Bad Generalization and Overfitting

<br />

![bad generalization and overfitting](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/bad%20generalization%20and%20overfitting.PNG)

<br />

#### Cause of Overfitting: A Driving Analogy

<br />

1. Use Excessive d_vc
2. Noise
3. Limited Data Size N

<br />

![cause of overfitting](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/cause%20of%20overfitting.PNG)

<br />

***

### The Role of Noise and Data Size

#### Case Study

<br />

```
測試實驗 :
1. 分別用二次多項式和十次多項式來預估一條有Noise的10次多項式
2. 分別用二次多項式和十次多項式來預估一條沒有Noise的50次多項式
```

<br />

![case study](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/case%20study.PNG)

<br />

#### Irony of Two Learners

<br />

```
能力比較差的反而以退為進?
```

<br />

![irony of two learners](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/irony%20of%20two%20learners.PNG)

<br />

#### Learning Curves Revisited

Limited Data Size N

<br />

![learning curves revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/learning%20curve%20revisited.PNG)

<br />

```
Learning Curve: Expected Error v.s. Number of Data Points, N

右圖的H10, 用linear model+nonlinear transform產生出nonlinear model, 使得VC Dimension變大, 
因此付出model complexity的代價 -> Ein與Eou距離拉大(由Bad Generalization造成)
-> H10在灰色區塊時(limited data size N)Ein較低 然而Eout較高
-> 用二次多項式的Eout反而比十次多項式的還小
```

<br />

#### The 'No Noise' Case

<br />

![the no noise case](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/the%20no%20noise%20case.PNG)

<br />

```
如果Target Function很複雜, 實際上這個複雜度也造成了類似noise的影響...
```

<br />

***

### Deterministic Noise

#### A Detailed Experiment

<br />

```
透過y = target function + noise來實驗變數變換時對overfit有什麼影響
三個變數: 
1. Gaussian iid noise
2. Qf : Q次多項式, 在產生多項式的隨機過程需要正規化(不然可能某些項的係數過小而整個項消失掉), 才能確保真的是Q次
3. data size N
```

<br />

![detailed experiment](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/detailed%20experiment.PNG)

<br />

#### The Overfit Measure

<br />

```
Eout(g10)和Eout(g2)差很遠 -> Overfit很嚴重
```
<br />

![overfit measure](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/overfit%20measure.PNG)

<br />

#### The Results

<br />

```
左圖的Qf固定在20 -> Stochastic noise
右圖的σ^2固定在0.1 -> Deterministic noise
```

<br />

![results](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/results.PNG)

#### Impact of Noise and Data Size

<br />

When does overfit happen?
1. Small Data Size N
2. Large Stochastic Noise
3. Large Deterministic Noise
4. Excessive Power

<br />

![impact of noise and data size](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/impact%20of%20noise%20and%20data%20size.PNG)

<br />

#### Deterministic Noise

<br />

```
在教一個簡單的hypothesis set的時候, 不要舉太複雜的例子可以得到較小的deterministic noise
```

<br />

![deterministic noise](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2013/deterministic%20noise.PNG)

<br />

***





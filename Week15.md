# How Can Machines Learn Better?

## Validation

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/roadmap.PNG)

```
使用驗證方法來幫助我們做出合理正確的選擇(Model Selection)
```

<br />

***

### Model Selection Problem

<br />

![model selection problem](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/model%20selection%20problem.PNG)

<br />

#### Model Selection by Best Ein

<br />

```
Select the one with min Ein => Always select the most complicated one => Overfitting!!!

在所有Hypothesis Set中找最小 => VC Dimension變大
因為Hypothesis Set越大 => 付出越大Model Complexity的代價
```

<br />

![model selection by best ein](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/model%20selection%20by%20test%20ein.PNG)

<br />

#### Model Selection by Best Etest

<br />

```
用測試資料來測試每個Model 選Etest最小的
然而測試資料哪裡來?? => 實務上難以取得
```

<br />

![model selection by best etest](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/model%20selection%20by%20best%20etest.PNG)

<br />

#### Comparison between Ein and Etest

<br />

```
先將一筆資料預留下來當Eval, 等model訓練好後, 拿來驗證model
```

<br />

![comparison](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/comparison.PNG)

<br />

***

### Validation

#### Validation Set Dval

<br />

```
將D拆分成D_train和D_val

Hoeffding's Inequality保證Eout() <= Eval() + O(((log M)/K)^(1/2))
finite-bin, M種選擇, K代表validation set大小
```

<br />

![validation set dval](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/validation%20set%20dval.PNG)

<br />

#### Model Selection by Best Eval

<br />

```
通過training得到每個H最好的g-後, 用驗證資料Dval算出每個g-對應的E, 選出最低的E和對應的H
最後將所有資料(training + validation)丟進去選出的模型(A+H)內並重做一次得到最後的g

實務上來說: 使用越多資料 => Eout會越低 (by learning curve)
```

<br />

![model selection by best eval](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/model%20selection%20by%20best%20eval.PNG)

<br />

#### Validation in Practice

<br />

![validation in practice](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/validation%20in%20practice.PNG)

<br />

```
實務上來說用所有資料的Eout(g)會比只用training資料的Eout(g-)來得小
```

<br />

#### The Dilemma about K

<br />

![dilemma about k](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/dilemma%20about%20k.PNG)

<br />

```
K = Validation Set Size
Large K => 每個Eval約等於Eout
Small K => 用所有資料N訓練出來的g與只用N-K資料訓練出來的g- 兩者會很相近
實務上來說會取驗證資料K = N/5
```

<br />

***

### Leave-One-Out Cross Validation

#### Extreme Case: K = 1

<br />

```
只保留一筆資料(xn,yn)當作驗證用 => small K => Eval與Eout差很多
如何讓Eval(單筆資料的誤差en)與Eout相近?
=> 所有資料N裡面每一筆資料輪流當作驗證用的(xn,yn) 得到N個en(Eval)後取平均
=> 記作E_loocv(H,A) = (e1+e2+...+eN)/N
希望: E_loocv(H,A)約等於Eout(g)
```

<br />

![extreme case k1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/extreme%20case%20k1.PNG)

<br />

#### Illustration of Leave-One-Out

<br />

```
原本用Eval來選擇讓error最小的model
現在改用E_loocv來選擇讓error最小的model (e.g. linear model, constant model, ...)
然後再用選出來的model算出最理想的g
```

<br />

![illustration of leave-one-out](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/illustration%20of%20loo.PNG)

<br />

#### Theoretical Guarantee of Leave-One-Out Estimate

<br />

```
E_loocv(H, A)會是Eout在N-1資料上的平均
```

<br />

![theoretical guarantee of loo](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/theoretical%20guarantee%20of%20loo.PNG)

<br />

#### Leave-One-Out in Practice

<br />

```
E_loocv實務上效果比Ein還要好(效果好=Eout低)
```

<br />

![loo in practice](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/loo%20in%20practice.PNG)


<br/>

***

### V-Fold Cross Validation

#### Disadvantages of Leave-One-Out Estimate

1. **Computation**: N 'additional' training per model (not easy to calculate E_loocv except linear regression)
2. **Stability**: variance of single-point estimates

<br />

![disadvantages of loo](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/disadvantages%20of%20loo.PNG)

<br />

#### V-fold Cross Validation

<br />

```
如何降低計算時間?
=> Take 1 for validation 改成 Take '1 part' for validation
將N分成V等份, 每次取一等份來當驗證資料
經驗法則: V=10
```

![v-fold cross validation](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/v-fold%20cross%20validation.PNG)

<br />

#### Final Words on Validation

<br />

```
通常用5-fold或10-fold效果都不錯
然而要注意的是Eval相較於Eout仍是較樂觀(Eval比較低)
```

<br />

![final words](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/final%20words.PNG)

<br />

***

### Summary

<br />

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2015/summary.PNG)



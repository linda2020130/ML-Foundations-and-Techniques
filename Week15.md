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
實務上來說會取驗證資料K= N/5
```

<br />

***



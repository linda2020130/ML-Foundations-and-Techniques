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






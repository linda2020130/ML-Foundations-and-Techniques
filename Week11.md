# How Can Machines Learn?

## Linear Models for Classification

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/roadmap.PNG)

<br />

```
整合之前看過的Linear Model, 在把它們延伸至更多更複雜的Classification問題上面
```

<br />

***

### Linear Models for Binary Classification

<br />

```
共通點: 都會先算出一個分數s= w^T * x
```

<br />

![linear models revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/linear%20models%20revisited.PNG)

<br />

```
Linear Classification是NP-Hard的問題...
能否借用Linear Regression或Logistic Regression來作為Linear Classification的一個替代工具?
```

<br />

#### Error Functions Revisited

<br />

```
將error function改寫成有y和s相乘
=> y代表correctness, s代表score
=> 希望Correctness Score越大越好, 越大代表y和s同號
```

<br />

![error function revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/error%20functions%20revisited.PNG)

<br />

#### Visualizing Error Functions

<br />

```
橫軸: y*s
縱軸: error function

0/1: ys<=0時(y和s異號) => error=1
sqr: error function= (ys-1)^2 => 以1為頂點的向上拋物線 
      當ys超過1時error會越來越大=>拿來估算err_0/1會有誤差
      但是當一個hypothesis的err_sqr很小時, 可以推得err_0/1也很小
ce: 一平滑的遞減函數 => 小err_ce <=> 小err_0/1
scaled ce: 將err_ce的ln改取log2, 使得ys=0時err轉化為1, 與err_0/1切齊
```

<br />

With err_ce

![visualizing error functions1](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/visualizing%20error%20function1.PNG)

<br />

With err_sce

![visualizing error function2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/visualizing%20error%20function2.PNG)

<br />

#### Theoretical Implication of Upper Bound

<br />

```
換底公式: loga b= logc b/ logc a where c>0 and c=/=1
=> ln x/ ln 2 = log2 x
=> err_sce = (1/ln 2)*err_ce
```

<br />

![theoretical implication of upper bound](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/theoretical%20implication%20of%20upper%20bound.PNG)

<br />

#### Regression for Classification

<br />

```
實務上常拿Linear regression來算出一個比較好的初始w0, 來加速後面的optimization
另一個實務上常用的方式是用logistic regression而不用pocket, 
因為logistic regression在optimization上比較容易, 因此比較常拿來做binary classification的工作
```

<br />

![regression for classification](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/regression%20for%20classification.PNG)

<br />

***












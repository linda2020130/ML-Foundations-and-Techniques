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

### Stochastic Gradient Descent

#### Two Iterative Optimization Schemes

* PLA: O(1)
* Logistic Regression: O(N)

<br />

![two iterative optimization schemes](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/two%20iterative%20optimization%20schemes.PNG)

<br />

#### Logistic Regression Revisited

<br />

```
Ein(wt+ηv)約等於Ein(wt)+η*(v^T)*∇Ein(wt)
其中v為更新方向, v與∇Ein(wt)方向相反時, 內積最小 => Ein會最小

目標: 不希望花O(N)的力氣去把梯度算出來
=> 想像成是一個隨機過程的平均
=> 隨機抽一個當作是整體的平均(極端case)
```

<br />

![logistic regression revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/logistic%20regression%20revisited.PNG)

<br />

#### Stochastic Gradient Descent (SGD)

<br />

![sgd](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/sgd.PNG)

<br />

#### PLA Revisited

<br />

```
soft PLA: 不是看有沒有錯來更新, 而是看錯多少, 錯多一點就多更新一點, 錯少一點就少更新一點
score(w*x)很大時, θ不是接近0就是接近1 => PLA時, yn=sign(wx)得0, 不相等時得1

實務上如何使用SGD來替代PLA?
1. 何時該停 => 跑夠多次
2. η? => 0.1126(或0.1)
```

<br />

![pla revisited](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/pla%20revisited.PNG)

<br />

***

### Multiclass via Logistic Regression

#### Multiclass Classification

<br />

```
Multiclass Classification常用於影像辨識, 聲音辨識等,
如何將已經學會的binary classification或者logistic regression延伸來到這個多類別分類的問題上?
```

<br />

![multiclass classification](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/multiclass%20classification.PNG)

<br />

#### One Class at a Time

<br />

```
將其中一個類別用binary classification和其他類別分開
```

<br />

![one class at a time](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/one%20class%20at%20a%20time.PNG)

<br />

#### Multiclass Prediction: Combine Binary Classifiers

<br />

```
會出現三種狀況:
1. 有其中一個分類器說圈圈(表示是屬於他的類別), 其他說叉叉 (可以確定分類)
2. 有多個分類器說圈圈, 剩下說叉叉 (無法確定分類)
3. 全部分類器都說叉叉 (無法確定分類)
```
<br />

![combine binary classifiers](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/combine%20binary%20classifiers.PNG)

<br />

#### One Class at a Time Softly

<br />

```
從回答是不是該分類轉變為是該分類的可能性有多少(soft),
用顏色深淺來決定可能性高低,
```

<br />

![one class at a time softly](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/one%20class%20at%20a%20time%20softly.PNG)

<br />

#### Multiclass Prediction: Combine Soft Classifiers

<br />

```
比較每個分類器的機率, 將點劃分到得到最大機率的分類
由於θ是單調(monotonic)遞增函數, 我們只需要找出最大的, 並不需要知道實際值,
因此, 可以不需要考慮logistic function
```

<br />

![combine soft classifiers](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/combine%20soft%20classifiers.PNG)

<br />

#### One-Versus-All (OVA) Decomposition

<br />

```
OVA Decomposition: 將一個multiclass問題拆成多個binary classification的問題 (非常常用的方法)
k個分類 => 跑k次logistic regression

Pros: efficient, 可以平行處理(同時在不同機器跑logistic regression), 
且此方法可套用到任何像logistic regression一樣會輸出一個可以比大小數值的函數上

Cons: 如果類別比重不均時(e.g. 100個類別裡只有一個是圈圈), 
logistic regression會有一個很輕易就做得很好的solution(e.g. 全部猜叉叉), 
到最後會得到一堆喜歡猜叉叉的logistic regression hypotheses, 要從裡面選最大的一個,
有時候效果會不是很好

統計學上有將logistic regression延伸到多類別的分類問題上 => Multinomial Logistic Regression
有將機率加起來要等於1這件事情放進去, 來得到更好的估計
```

<br />

![ova decomposition](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2011/ova%20decomposition.PNG)

<br />

***








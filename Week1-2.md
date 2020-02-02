# When can Machines learn?

<br />
<br />

## _The Learning Problem_

#### Key Essence of Machine Learning
* exists some **underlying patterns** to be learned
* **no** programmable (easy) **definition**
* exists **data** about the pattern

<br />

### What is Machine Learning?
use **data** to compute `hypothesis g` that approximates `target f`

![ML Components](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/components%20of%20ml.PNG)

<br />

### Components of Machine Learning
* Unknown Target Function
`f: X -> Y`
* Training Data
`D: (x1, y1), ... ,(xn, yn)`
* Learning Model
  * Learning Algorithms `A` (to choose the best g)
  * Hypothesis Set `H` (set of candidate formula)
* Final Hypothesis
`g `


<br />
<br />

## _Learning to Answer Yes/No_

<br />

### Perceptron Hypothesis Set
* For **x=(x1, ..., xd)**, `d features`, compute a weighted **score** `w`
* **y={+1, -1}**, positive for good, negative for bad

![Perceptron Hypothesis Formula](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/vector%20form%20of%20perceptron%20hypothesis.PNG)

<br />

#### Example of h(x) in R^2 (2 features)

![Perceptrons in R^2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/perceptron%20in%20R%5E2.PNG)

<br />

### Perceptron Learning Algorithm (PLA)
**Algorithm** is to select `g` from `H` (all possible perceptrons) that approximates target `f` (ideally `g(xn)=f(xn)=yn`).

**Difficulty** : H is of *infinite* size

**Idea** of PLA : start from some g0, and *correct* its mistakes on D (represent g0 by its weighted vector w0)

```
PLA概念
1. yn=+1, 但 sign(wt*xnt)=-1  =>  代表wt(直線的法向量) 和 xnt 間的角度太大 
修正wt -> wt+1 = wt + ynt*xnt  =>  讓wt+1 和 xnt 間的角度縮小, 使得sign(wt+1*xnt)更接近yn
2. yn=-1, 但 sign(wt*xnt)=+1  =>  代表wt 和 xnt 間的角度太小
修正wt -> wt+1 = wt + ynt*xnt  =>  讓wt+1 和 xnt 間的角度放大, 使得sign(wt+1*xnt)更接近yn
```
<br />

![PLA](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/PLA.PNG)

<br />

#### Practical Implementation of PLA
**Cyclic PLA** will stop when not encounting mistakes after **a cycle of point visit** (visit order can follow *data source* or be *randomly* generated before algorithm starts).

![cyclic PLA](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/cyclic%20PLA.PNG)

<br />

### Linear Separability
**Linear Separability** : if PLA halts, then D allows some `w` to make no mistake. D is **linear separable**.

![Linear Separable](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/linear%20separable.PNG)

<br />

#### PLA Fact : wt Gets More Aligned with wf

```
D線性可分,代表存在一條線[target function f]能夠將y=+1和-1分隔開來 
<=> 存在wf[f的法向量] s.t. yn=f(xn)=sign(wfT*xn) 對於D內任意點xn

所以, yn和wfT*xn 一定會同號    
=> yn*(wfT*xn) > 0 對於任意一點xn    
=> ynt*(wfT*xnt) [第t次修正後,出現錯誤的點xn]  >=  min yn*(wfT*xn) [距離f最近的點xn]  > 0

希望wt藉由每一次的修正, 可以更接近wf    
=> wf與wt角度越小     
=> 內積[兩向量長度相乘,再乘上cos]會越大
```

![PLA Align](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/PLA%20align.PNG)

<br />

```
證明了 wf與wt+1的內積 比 wf與wt的內積 還大,
但 內積變大 可能是由 長度變長 或 角度變小 所造成,
因此, 還需要證明修正後的wt+1長度並沒有太大變化
```

<br />

#### PLA Fact : wt Does Not Grow Too Fast

```
再來看看 wt+1的長度 和 wt的長度 之間有什麼關係...

wt+1 = wt + ynt*xnt
取長度平方後, 後者的中間項為 2*ynt*(wtT*xnt)

PLA的一個特性: 
wt只有在遇到錯誤時才會進行修正   
<=>   發生錯誤的點xn: sign(wt*xnt) =\= ynt   
<=>   ynt和wtT*xnt 一定會異號: ynt*(wtT*xnt) <= 0

由於中間項 2*ynt*(wtT*xnt) < 0, 
wt+1的長度如果要變大, 必須由 ynt*xnt 來提供
出錯點長度 一定會比 最遠點長度 還小  
=>   ynt*xnt <= max_n ||yn*xn||^2  =  max_n ||xn||^2  [因為yn長度為1]
因此, wt+1的長度增長會受到限制
```

![PLA Grow](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/PLA%20grow.PNG)

<br />

```
正規化後的wf與wt之內積變大 => 兩向量之角度變小
```




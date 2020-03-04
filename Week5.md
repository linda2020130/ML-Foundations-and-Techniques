# Why Can Machines Learn?

<br />

## Training versus Testing

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/roadmap%20w5.PNG)

<br />

***

### Recap and Preview

#### the 'Statistical' Learning Flow

```
learning is PAC-possible if enough statistical data[N夠大的情況下,Ein(g)近似於Eout(g)] and finite |H|

若演算法找到一個g,使得Ein(g)趨近於0
=> PAC(Probably Approximately Correct) guarantee for Eout(g)趨近於0
因此, learning is possible
```

<br />

![statistical learning flow](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/stat%20learning%20flow.PNG)

<br />

#### Two Central Questions

1. Make Eout(g) close to Ein(g)?
2. Make Ein(g) small enough?

![two central questions](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/two%20central%20questions.PNG)

<br />

#### Trade-off on M

* **Small M**: lower probability to encounter BAD Data, but too *few choices* for Algorithm to choose from
* **Large M**: higher probability to encounter BAD Data, but *many choices* for Algorithm

<br />

#### Preview

```
M的大小(Hypothesis set)要多少才比較洽當?
```

<br />

![preview](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/preview.PNG)

<br />

***

### Effective Number of Lines

#### Where Did M Come From?

```
M個h遇到BAD Data
= h1遇到BAD Data or h2遇到BAD Data or ... or hM遇到BAD Data

當h遇到BAD Data的時機都沒有重疊時, M個h遇到BAD Data的機率 = 個別h遇到BAD Data的機率相加
但如果有重疊, 相加的機率結果會比實際上遇到的機率來得高估(upper bound會失真)
```

<br />

![where did m come from](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/where%20did%20m%20come%20from.PNG)

<br />

#### Where Did Uniform Bound Fail?

> BAD events Bm **overlapping** => Union bound **Over-estimating**

![over-estimating](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/over-estimating.PNG)

<br />

#### How Many Lines Are There?

```
若把相似的hypothesis(得到相同output的h)群聚在一起,視為一種的話, 
是否會變有限個h?
```

<br />

> One Inout

![one input](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/one%20input.PNG)

<br />

> Four Input => At most 14

![four input](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/four%20input.PNG)

<br />

#### Effective Number of Lines

```
相似的h群聚在一類後, 最多會有幾類? => effective number of lines [ 記作effective(N) ]
假如effective(N)
1. 可以取代M
2. 遠小於2^N
則learning possible with infinite lines!
```

<br />

![effective number of lines](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/effective%20number%20of%20lines.PNG)

<br />

***

### Effective Number of Hypotheses

#### Dichotomies: Mini-hypotheses
```
Dichotomy代表二分的意思
將得到相同output的h群聚在一起, 形成一個dichotomy
總共有?個不同的dichotomy => "?"可能可以用來替換掉Hoeffding裡的無限大M
```
<br />

![dichotomies](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/dichotomies.PNG)

<br />

#### Growth Function
```
然而dichotomy set其實會取決於我們先選好的x1, x2..., xN, 
因為點位置不同會導致不同個不同的dichotomy(dichotomy set的大小不同)
```

<br />

![growth function](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/growth%20function.PNG)

<br />

```
多次隨機抓取(x1, x2, ..., xN), 並記錄每一次的dichotomy set的大小
最後取最大的[記作mH(N): Growth Function]就可以排除掉因選點所造成的誤差
```
<br />

#### Examples of Growth Function

> Positive Rays

![positive rays](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/positive%20rays.PNG)

```
分隔線a可放進任一個間隔中, 共N+1個間隔
```

<br />

> Positive Intervals

![positive intervals](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/positive%20intervals.PNG)

```
N+1個間隔中取兩個當上下分隔線,
+1代表兩分隔線在同一隔(output全是X)
```

<br />

> Convex Sets

![convex sets](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%205/convex%20sets.PNG)

```
不管要幾個正的, 都可以被Convex Set做出來
=> mH(N) = 2^N

如果可以找到(特別的)N個點, 可以做出2^N個不同的dichotomy, 使得成長函數為2^N
=> N inputs "shattered" by H
```

<br />









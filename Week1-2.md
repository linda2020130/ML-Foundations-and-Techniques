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






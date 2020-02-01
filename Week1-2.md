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
  * Learning Algorithms `A`
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

* Example of h(x) in R^2 (2 features)

![Perceptrons in R^2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/perceptron%20in%20R%5E2.PNG)

<br />

### Perceptron Learning Algorithm (PLA)



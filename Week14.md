# How Can Machines Learn Better?

## Regularization

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/roadmap.PNG)

<br />

```
上次提到Overfitting在什麼情況下很可能會發生?
1. 太多的power
2. 資料量不夠多
3. 有stochastic或是deterministic noise

這週要講的regularization是可以用來對付overfitting的一種方法
```

<br />

***

### Regularized Hypothesis Set

#### Regularization: The Magic

<br />

![regularization the magic](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/regularization%20the%20magic.PNG)

<br />

```
從高次多項式的Hypothesis Set走回低次多項式的Hypothesis Set (高次會包含低次的Hypothesis Set)
=> How?
```

<br />

#### Stepping Back as Constraint

step back = **constraint**

<br />

![stepping back](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/stepping%20back.PNG)

<br />

#### Regression with Constraint

step back = **constrained optimization** of Ein

<br />

![regression with constraint](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/regression%20with%20constraint.PNG)

<br />

#### Regression with Looser Constraint

<br />

![regression with looser constraint](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/regression%20with%20looser%20constraint.PNG)

<br />

```
特定8個w是0 => 任意8個以上的w是0 
因為不是很多次的多項式, 且只有少少的係數, 所以Hypothesis set看起來會跟二次多項式類似
=> H2 ⊂ H'2 ⊂ H10
However, H'2 contains Boolean operation...is NP-Hard to solve...
```

<br />

#### Regression with Softer Constraint

**Regularized Hypothesis W_REG**: optimal solution from regularized hypothesis set `H(C)`

<br />

![regression with softer constraint](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/regression%20with%20softer%20constraint.PNG)

<br />

```
將限制式改寫成w的平方不超過一個上限C (able to solve)
H(0) ⊂ H(1.126) ⊂ ... ⊂ H(1126) ⊂ ... ⊂ H(∞) = H10
```

<br />

***

### Weight Decay Regularization

#### Matrix Form of Regularized Regression Problem

<br />

```
將sigma連加改寫成矩陣運算式,
w必須落在半徑為根號C的球內
```

<br />

![matrix form](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/matrix%20form.PNG)

<br />

#### The Lagrange Multiplier

<br />

```
w_lin => 山谷 (Ein最低點)
紅色圓圈 => 半徑為根號C的球
=> 限制式使得w只能在球內或線上滾
最好的解 = 符合條件又不能再往下滾 = -∇Ein(w)(藍色)與w_REG(紅色法向量)平行
```

<br />

![lagrange multiplier](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/lagrange%20multiplier.PNG)

<br />

#### Augmented Error

<br />

```
若已知 λ , 則變成是由w_REG組成的線性方程式
正定矩陣是可逆 => 存在唯一解 (Ridge Regression)
```

<br />

![augmented error](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/augmented%20error.PNG)

<br />

```
解有限制式C的Ein最佳化問題 = 解沒有限制式的E_aug最佳化問題
```

<br />

![augmented error2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/augmented%20error2.PNG)

<br />

#### The Results

<br />

```
λ=0 => 等於沒有限制式 => Overfitting
λ=1 => 模型複雜度太低 => Underfitting
λ只要一點點就可以讓w變小 (weight-decay regularization)
```

<br />

![results](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/results.PNG)

<br />

#### Some Detail: Legendre Polynomials

<br />

```
Polynomial regression要做regularization時, 用Legendre Polynomial效果會比較好
=> 加了一些係數讓多項式彼此之間是垂直的
```

<br />

![legendre polynomials](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%2014/legendre%20polynomials.PNG)

<br />

***




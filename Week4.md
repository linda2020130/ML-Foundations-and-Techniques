# When Can Machines Learn?

<br />

## Feasibility of Learning

<br />

![roadmap](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/roadmap%20w4.PNG)

<br />

***

### Learning is Impossible?

> Learning is impossible if any **unknown** f can happen.

![learning is impossible](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/learning%20is%20impossible.PNG)

<br />

***

### Probability to the Rescue

<br />

```
嘗試使用一些方法來推論未知的f
```

<br />

> How do we know the orange probability in the bin?

![infer orange probability](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/infer%20orange%20probability.PNG
)

<br />

> Hoeffding's Inequality

![hoeffding's inequality](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/hoeffding's%20inequality.PNG)

```
在N很大的情況下, v和u相差很遠的機率很小
```

<br />

![hoeffding's inequality-2](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/hoeffding's%20inequality-2.PNG)

```
在N夠大的情況下, 我們可以用v推論未知的u
```

<br />

***

### Connection to Learning

<br />

```
在N個sample下, 用v推測未知的u 
=> D={(xn, yn)}, 用[fraction of h(xn)=/=yn]推測未知的[probability of h(x)=/=f(x)]
```

![connection learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/connection%20to%20learning.PNG)

<br />

```
在固定任一h的情況下, 可以用已知的Ein(h)推測未知的Eout(h)
```

![added components](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/added%20components.PNG)

<br />

#### The Formal Guarantee

```
在固定任一h和N夠大的情況下
=> Ein(h)和Eout(h)之間的距離 大於 Epsilon 的機率 有上界
=> Ein(h)近似於Eout(h)的機率很大
所以 若同時Ein(h)很小
=> Eout(h)也會很小
=> h(x)=/=f(x)的機率很小
=> h近似於f
```

![formal guarantee](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/formal%20guarantee.PNG)

<br />

#### Verification of One h

> Can we claim good learning?

![verification of one h](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/verification%20of%20one%20h.PNG)

```
不論什麼題目下, A都被強制選出同一個h as g =>通常這個Ein(h)會很大...
必須靠演算法"自己選出"h as g才是真正的learning (演算法必須有選擇性)
```

<br />

#### The Verification Flow

![verification flow](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/verification%20flow.PNG)

<br />

```
可以透過N筆資料來驗證h=g是不是近似於f
```

<br />

***

### Connection to Real Learning

<br />

#### BAD Sample and BAD Data

**Bad** : `|Ein(h)-Eout(h)| > Epsilon`
<br />
Example: Eout(h) big, but Ein(h) small

![Bad Sample](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/bad%20sample.PNG)

<br />

```
根據Hoeffding不等式
=> 出現不好的機率非常小
```

<br />

#### Bad Data for Many h

```
很多個h <=> 演算法可以自由做選擇
然而每個h都會在某幾次Sample抓取時,出現BAD Data的情況...
BAD Data的存在容易導致演算法誤選到讓Eout(h)和Ein(h)差很多的h
```

<br />

![Bad Data for Many h](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/bad%20data%20for%20many%20h.PNG)

<br />

#### Bound of BAD Data

```
M個h遇到BAD Data的機率
=
h1遇到BAD Data的機率 or h2遇到BAD Data的機率 or hM遇到BAD Data的機率
```

<br />

![Bound of Bad Data](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/bound%20of%20bad%20data.PNG)

> PD[BAD D] <= 2M*exp(-2(epsilon^2)N)

<br />

#### The 'Statistical' Learning Flow

```
假如有M個(有限個)hypothesis, 且N夠大
若演算法A任意挑選一個h as g,
=> Eout(g)近似於Ein(g)
若A找到一個Ein(g)接近0的g
=> PAC guarantee for Eout(g)近似於0
```

<br />

![Statistical Learning Flow](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/statistical%20learning%20flow.PNG
)

```
比原本ML Flow多了一個未知的機率函數P, 控制Eout(g)和Ein(g)
```

<br />

***

#### Summary

![Summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%204/summary.PNG)


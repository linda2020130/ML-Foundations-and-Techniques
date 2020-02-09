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

```
在N個sample下, 用v推測未知的u 
=> D={(xn, yn)}, 用[fraction of h(xn)=/=yn]推測未知的[probability of h(x)=/=f(x)]
```

![connection learning]()

<br />

```
在固定任一h的情況下, 可以用已知的Ein(h)推測未知的Eout(h)
```

![added components]()

<br />

#### The Formal Guarantee

```
在固定任一h和N夠大的情況下
=> Ein(h)近似於Eout(h)
若同時Ein(h)很小
=> Eout(h)也會很小
=> h(x)=/=f(x)的機率很小
=> h近似於f
```

![formal guarantee]()

<br />

#### Verification of One h

> Can we claim good learning?

![verification of one h]()

```
不論什麼題目下, A都被強制選出同一個h as g =>通常這個Ein(h)會很大...
必須靠演算法"自己選出"h as g才是真正的learning (演算法必須有選擇性)
```

<br />

#### The Verification Flow

![verification flow]()

<br />

```
可以透過N筆資料來驗證h=g是不是近似於f
```





<br />

***

### Connection to Real Learning

<br />









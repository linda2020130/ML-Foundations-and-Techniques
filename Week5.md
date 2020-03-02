# Why Can Machines Learn?

<br />

## Training versus Testing

<br />

![roadmap]()

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

![statistical learning flow]()

<br />

#### Two Central Questions

1. Make Eout(g) close to Ein(g)?
2. Make Ein(g) small enough?

![two central questions]()

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

![preview]()

<br />




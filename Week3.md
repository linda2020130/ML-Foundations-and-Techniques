# When Can Machines Learns?

<br />

## _Types of Learning_

<br />

![Roadmap Week3](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/roadmap%20w3.PNG)

<br />

***

### Learning with Different Output Space y

* **Binary Classification**: `y={+1, -1}`
> Examples: Credit Card Approve/Disapprove; Email Spam/Non-spam
* **Multiclass Classification**: `y={1, 2, ..., K}`
> Examples: Coin Recognition; Written Digits(0, 1, ..., 9); Pictures(Cats, Dogs, ...); Emails(Spam, Primary, Promotion...)[Gmail]
* **Regression**: `y={R}` or `y=[lower, upper]C R` (Bounded Regression)
> Examples: Company Data (Stock Price); Climate Data (Temperature)
* **Structured Learning**: `y={PVN, PVP, ...}`; Huge multiclass classification problem **without *explicit* class definition**
> Examples: Sequence Tagging(詞性標記 Sentence=>structure); Speech Data=> Speech Parse Tree

<br />

![Different Output Space](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/different%20output%20space.PNG)

<br />

***

### Learning with Different Data Label yn

* **Supervised** Learning: **every** yn
* **Unsupervised** Learning: **no** yn
> Unsupervised Multiclass Classification <=> Clustering
* **Semi-supervised** Learning: **some** yn
* **Reinforcement** Learning: **implicit yn** by goodness (~yn)
* ...and more

![Different Data Label](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/different%20data%20label.PNG)

<br />

Example of **Unsupervised** Learning

![Unsupervised Learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/unsupervised%20learning.PNG)

<br />

Examples of **Semi-supervised** Learning

![Semi-supervised](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/semi-supervised.PNG)

<br />

Examples of **Reinforcement** Learning

![Reinforcement Learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/reinforcement%20learning.PNG)

<br />

***

### Learning with Different Protocol f => (xn, yn)

1. **Batch** Learning: learn from ***all known*** data
    * a very *common* protocol (人與機器溝通的方式)
    * can be adapted to supervised or unsupervised learning
2. **Online** Learning: hypothesis improves through receiving data ***sequentially***
    * *reinforcement* learning is often done online
    * PLA can be adapted to online protocol
3. **Active** Learning: improve hypothesis with fewer labels by asking questions ***strategically***
    * usually be adapted due to the *difficulty(cost) of labelling all data*

<br/>

![Different Protocol](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/different%20protocol.PNG)

<br />

> Batch Learning (Duck Feeding)

![Batch Learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/batch%20learning.PNG)

<br />

> Online Learning (Passive Sequentially)

![Online Learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/online%20learning.PNG)

<br />

> Active Learning (Question Asking)

![Active Learning](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/active%20learning.PNG)

<br />

***

### Learning with Different Input Space X

1. **Concrete** Features: **sophisticated** physical meaning
    * the easy ones for ML
2. **Raw** Features: **simple** physical meaning
    * more difficult for ML
    * Often need human(`Feature Engineering`) or machines(`Deep Learning`) to *convert to concrete ones*
3. **Abstract** Features: **no** physical meaning
    * even more difficult for ML
    * need *feature conversion/extraction/construction*

<br />

![Different Input Space](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/different%20input%20space.PNG)

<br >

> Example of Concrete Features

![concrete features](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/concrete%20features.PNG)

<br />

> Example of Raw Features

![raw features](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/raw%20features.PNG)

<br />

> Example of Abstract Features

![abstract features](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/abstract%20features.PNG)

<br />

***

### Summary

![summary](https://github.com/linda2020130/Notes_ML-Foundations/blob/master/Pictures/Week%203/summary.PNG)


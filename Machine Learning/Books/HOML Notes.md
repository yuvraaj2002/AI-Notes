> [!PDF|note] [[Hands on Machine Learning.pdf#page=177&selection=116,0,122,1&color=note|Hands on Machine Learning, p.149]]
> > What if your data is more complex than a straight line? Surprisingly, you can use a linear model to fit nonlinear data. A simple way to do this is to add powers of each feature as new features, then train a linear model on this extended set of features. This technique is called polynomial regression.

> [!PDF|note] [[Hands on Machine Learning.pdf#page=179&selection=30,0,82,1&color=note|Hands on Machine Learning, p.151]]
> > Note that when there are multiple features, polynomial regression is capable of finding relationships between features, which is something a plain linear regression model cannot do. This is made possible by the fact that PolynomialFeatures also adds all combinations of features up to the given degree. For example, if there were two features a and b, PolynomialFeatures with degree=3 would not only add the features a2, a3, b2, and b3, but also the combinations ab, a2b, and ab2.
> 
>

> [!PDF|note] [[Hands on Machine Learning.pdf#page=192&selection=4,1,21,50&color=note|Hands on Machine Learning, p.164]]
> > Logistic regression (also called logit regression) is commonly used to estimate the probability that an instance belongs to a particular class (e.g., what is the probability that this email is spam?). If the estimated probability is greater than a given threshold (typically 50%), then the model predicts that the instance belongs to that class (called the positive class, labeled “1”), and otherwise it predicts that it does not (i.e., it belongs to the negative class, labeled “0”). This makes it a binary classifier.

> [!PDF|note] [[Hands on Machine Learning.pdf#page=193&selection=40,0,99,48&color=note|Hands on Machine Learning, p.165]]
> > Notice that σ(t) < 0.5 when t < 0, and σ(t) ≥ 0.5 when t ≥ 0, so a logistic regression model using the default threshold of 50% probability predicts 1 if θ⊺ x is positive and 0 if it is negative. The score t is often called the logit. The name comes from the fact that the logit function, defined as logit(p) = log(p / (1 – p)), is the inverse of the logistic function. Indeed, if you compute the logit of the estimated probability p, you will find that the result is t. The logit is also called the log-odds, since it is the log of the ratio between the estimated probability for the positive class and the estimated probability for the negative class
> 
> 
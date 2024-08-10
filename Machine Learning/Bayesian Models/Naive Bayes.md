This page is dedicated towards understanding the concept of naive bayes theorem. The resources used for this topic are basically the videos of CampusX.

Here is the google drive link of the [Notebook](https://drive.google.com/file/d/1ocyl8UZi3qS-ARaw7_Ot9qUGLhA20f9n/view)

- [ ] Lidstone smoothing
- [ ] Complementing Smoothing
### [What is bayes theorem and how it is different from conditional probability ?](#) 

Bayes theorem is an important theorem in the field of statistics and it provides us the mechanism to relate 2 conditional probabilities, It is represented as $P(A|B) = (P(B|A)*P(A))/P(B)$

Note we can actually derive this by equating the conditional probabilities as $P(A|B)$ , $P(B|A)$

On the other hand the conditional probability is simply a measure of calculating the probability of an event occurring given an event have already occurred.

### [What is naive bayes algorithm and is it parametric or non parametric ?](#)

Naive bayes is a supervised machine learning algorithm which is used to solve the classification problems and it is based on bayes theorem with a naive assumption that all the features are independent from each other.

Also this algorithm is parametric in nature because it makes an assumption about the underlying data and this assumption is that all the features are independent from each other. 
### [Why do we make naive assumption and what would happen if we will not do so ?](#)

There are 2 main reasons behind why it is important to make a naive assumption that all the features are independent from each other

1. **To reduce the overall computational complexity of the model**: Without the naive assumption, our model would need to compute the joint conditional probability of every possible combination of feature values. If we have n features, each with k possible values, the total number of joint conditional probabilities to be calculated would be $k^n$. However, with the naive assumption that all features are independent of each other, we only need to compute $n⋅k$ conditional probabilities. This significantly reduces the computational complexity.

2. **To deal with overfitting**: In the absence of naive assumption the probabilistic conditions will become very much strict and specific because of which with the small change in the value we might get different results which means our model will be having low bias and high variance, so by making an assumption we prevent the model from overfitting.

### [How does this algorithm works and what are its learning parameters ?](#)

The way naive bayes work is that during the training phase, after making a naive assumption that all the features are independent from each other, it calculates conditional probabilities, prior probabilities (Model parameters) and store them. Then during the prediction phase it utilized these calculated probabilities to derive the final output.

1. $P(Yes|F_n) = P(F_n|Yes) * P(Yes)$
2. $P(F_n|Yes)  =  P(F_1|Yes) * P(F_2|Yes) * P(F_3|Yes) * P(Yes)$
3. $P(No|F_n) = P(F_n|No) * P(No)$
4. $P(F_n|No)  =  P(F_1|No) * P(F_2|No) * P(F_3|No) * P(No)$

Finally the $Max(P(Yes|F_n),P(No,F_n))$ is considered for the final output 
### [What is the issue of underflow, why it happens in NB and how to solve this ?](#) 

Underflow is basically a situation where when the number becomes very small then the computer finds it difficult to actually store this value accurately and precisely using bits representation. And this lead to numerical unstability.

Now this is a common issue which is faced incase of naive bayes specifically working with high dimensional data because in the high dimensional data, the number of conditional probabilities in the joint conditional probabilities will increase and with this the overall product of such values lying between 0 and 1 will become very small leading to underflow. So the only way to dealing with this is to consider the log conditional probabilities. But since the log of values between 0 and 1 will be negative thus the class having least negative value will be chosen. Example :
- $Log_P(yes)$ = -145
- $Log_P(no)$ = -130
Then out of yes and no the no will be chosen as class for the query data point.


### [How to deal with 0 Probability value in Naive bayes ?](#) 

Let say either due to underflow or due to usage of some feature value which was not using during training we got the 0 conditional probability, in such a scenario log cannot be used and the only way to deal with this issue is to use a technique called smoothing. Where in smoothing we add a small value to the conditional probability to prevent it from becoming 0. The smoothing technique which we use is called laplace additive smoothing.


### [Other than doing laplace additive smoothing what else can we do which is more efficient than it ?](#)

The drawback of adding a small constant value in each of the conditional probability is that it might give us over optimistic results in case we are not careful, so rather than simply adding a constant value we add a hyper parameter alpha / (n *  alpha), which not only helps us to deal with 0 probability but at the same time also provides us a tuning nob for handling the bias and variance of the model.

### [Talk about the bias variance](#) 

- With **high value** of alpha the conditional probabilities of feature given class approaches towards 0.5 and for very high value it becomes 0.5. Now due to this for all the classes their prior probability becomes the deciding factor for which class label will be provided. And in case the prior probability particular will be high then for every data point we will get that class only and this is sign of underfitting means high bias and low variance
- With smaller value of alpha the conditional probabilities will become very much sensitive to change in data and this is clear sign of overfitting and low bias- high variance


### [What type of Naive bayes to use when all feature are numerical and why do we not need to do smoothing in this type ?](#) 

Gaussian naive bayes is basically a specific variant of naive bayes which is used in those kind of scenarios where all the features are numerical in nature and follow gaussian distribution.

Now if we will be given query point information like the given CGPA = 3.6 and IQ = 100 will the student get placed or not. We will actually calculate the the things like

- P(Yes | CGPA = 3.6 and IQ = 100) = P(Yes) * P(CGPA = 3.6 | Yes) * P(IQ = 100 | Yes)
- P(No | CGPA = 3.6 and IQ = 100) = P(No) * P(CGPA = 3.6 | No) * P(IQ = 100 | No)

After this we will be using the gaussian distribution to find the conditional probabilities. Also in case the features are not following a gaussian distribution we can use [[Transformations]] in that case to transform them to follow a gaussian distribution. 

Gaussian distributions, being continuous probability distributions, do not assign zero probability density to any specific value, thus there is no need for doing smoothing.
### [Talk about bernoulli, categorical, Multinomial naive bayes](#)

- Bernoulli naive bayes is basically a specific variant of naive bayes which is used in those kind of scenarios where all the features are categorical and have only 2 categories which means they follow bernoulli distribution.

- Categorical naive bayes is a specific variant of naive bayes which is used in those kind of scenarios where the feature is categorical in nature with more than 2 categories. Example : Consider a dataset with features such as color (Red, Green, Blue) and shape (Square, Circle, Triangle) to classify objects into categories (e.g., Toys, Tools). In this case categorical naive bayes can be used

- Multinomial Naive Bayes is a variant of the Naive Bayes classifier tailored for discrete data (means the data having finite number of distinct values), especially useful for count data. It is commonly applied in text classification problems where features represent the frequency of words or terms in a document.

### [What is the use of Out of Core Naive bayes](#) 

Out of core naive bayes is basically a variant of naive bayes which is used in those kind of scenarios where our data is very large in size and it becomes difficult to process it once in single go due to memory issues.

So rather loading the complete dataset into the memory we load the dataset in term of batches and then do the partial fitting of the batches.

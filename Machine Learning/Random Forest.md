This page is actually dedicated towards understanding the concept of random forest in machine learning. The main resource used for this topic are the course videos of CampusX. 

- [Session 1 (Introduction to Random Forest](https://drive.google.com/file/d/1EK3u-hyEiK0wMMsy07fI0Dn-jwOicbEU/view)
- [Session 2 (Hyper parameters of Random forest, OOB score and ERT)](https://drive.google.com/file/d/1sV_PG8PNCzXNvN73cvSxw3NDiwh1Y7bc/view)

Now we will take a look at all the possible interview questions which can come in the interview also we will take a look at the practical code of random forest classifier and regressor.

- What do you mean by random forest ? 

	Random forest is basically a machine learning technique which is build on top of bagging and in order to truly understand what is Random forest we can simply focus on the terms Random and Forest.
	
	- Forest comes form the fact that only decision trees will be used as base models in bagging architecture, where decision tree by nature are low bias and high variance models.
	- Random comes form the fact that the complete dataset is not used for training the decision trees, instead bootstrap sampling technique [[Types of Sampling]] is used where we random take subset of data points from the dataset for training the algorithm, in addition to this in random forest during the construction of decision tree there is node level column sampling so because of this fact as well term random term is used in random forest.

	![[Pasted image 20240703123151.png|450]]

- What is the difference between bagging and random forest ? 

	- Base models: In case of bagging we can use any machine learning algorithms as the base models but we need to make sure all the base models are of same type, whereas in case of Random forest all the base models needs to be decision trees only.
	-  In bagging if we will use Decision tree as base models then during the construction of tree, tree level column sampling will be done whereas in case of random forest node level column sampling is done.

- Why do we use forest rather than using single tree or why random forest is very robust to outliers ? 

	Forest is always preferred over the decision tree because with Random forest it is easy to attain low bias and low variance configuration which helps to deal with the problem of overfitting.
	 
	Single tree means single decision tree and by default due to their stopping criterion decision tree is a low bias and high variance model, which means that with the small change in the data we will observer high variability in terms of model performance.

	On the other hand if we will use group of decision trees in that case the variance of the overall system will decrease, because of Bootstrap sampling and node level column sampling during construction of decision tree. Also it is very much intuitive as let say we have the new data and if we will use this new data with single decision tree then we will observe high variance whereas if we will use this new data with random forest then due to bootstrap sampling and node level column sampling, the effect of new data on individual tree will be reduced leading to decrease in variance.

- How random forest can be used as feature selection technique ? 

	Random forest itself can't calculate the feature importance scores, instead the individual [[Decision Tree]] are used for calculating the feature importance score and we finally just average all the scores to get final feature importance scores.

- What do you mean by OOB score and OOB error in random forest ? 
	In order to truly understand what is OOB score and OOB error we first needs to be aware about what does OOB samples means.

	OOB stands for Out of Bag samples, which are basically those samples which remained unutilized due to bootstrap sampling and since these samples are unseen thus they are perfect for testing the performance of the algorithm. On average, about 63% of the original data points are included in each bootstrap sample, leaving about 37% as OOB samples.


	-  The OOB score is a measure of overall accuracy of the random forest and it is calculated by passing OOB samples to each of the DT, calculating the accuracies and then finally averaging them to get final accuracy. 
	- OOB error is basically complement of the OOB score and it is a numerical value which tell use the error which our ensemble model is making on the OOB samples. OOB Error=1−OOB Score

- What are the various hyper parameters associated with random forest ? 

	![[Pasted image 20240702071859.png|550]]

- What do you mean by extreme randomized tree ? 



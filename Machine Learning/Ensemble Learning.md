This page is dedicated towards understand the concept of ensemble learning and the resource used for this are the videos of CampusX course videos.

- Wisdom of crowd ? 

	Wisdom of the crowd is a concept which states that collectively crowd will always have the correct answer and there are couple of real world examples of this concept as well 
	
	- In KBC during the audience poll we will always observe that the collectively group of individuals will always know the correct answer.
	- In ecommerce websites the reviews of group of customers collectively will always give us information about the overall performance of the product.

- What is ensemble learning and what are its types ? 

	Ensemble learning is a technique where we group together multiple machine learning models to solve a complex problem with best performance possible and there are 4 different types of ensemble learning
	
	- Voting
	- Stacking
	- Bagging 
	- Boosting

-  Why we focus on making ML models different from each other ?

	In ensemble learning we always make sure that the base machine learning algorithms are different form each other so that the problem could be solved effectively by approached it from different perspectives, ensuring the elimination of any kind of biasness. Every different or decoupled ML model will have its own understanding of the data and collectively the output from all the models will eventually give us correct results.

-  Ways to ensure the base models are different from each other ?

	There are 3 ways using which we can make sure that the base models are different from each other and these 3 ways are ⬇️
	
	1. By using different types of models ( Like logistic regression, Decision tree and KNN)
	2. By using different dataset for the same models we can also make sure that the base models are different because with the change in the data, the model parameters will differ leading to different base models.
	3. By using different model and different subset of data

-  How do we get low bias and low variance model

	First of all we need to be aware about what does bias and variance actually means
	
	- Bias → Inability of model to understand the true relationship between the data
	-  Variance → Variability in model performance with change in the data
	
	In ensemble learning we get low bias and low variance model pretty easily. To better understand this let say we have chosen low bias and high variance model (Decision tree) but we have created an ensemble architecture. Now due to this whenever we will get some new data then rather than providing the new data to any single model (which is having high variance) we will actually divide the data and distribute the subsets to all the base models. By doing so sensitivity of every individual model to change in the data decreases and in short we can say the overall variance of the combined model decreases

- What is the major drawback of ensemble learning

	The major drawback of ensemble learning is that it can become computationally expensive in case our base models are complex in nature

-  What are the various resampling techniques used in the context of ensemble learning ?  

	While bagging primarily uses bootstrap sampling, there are other resampling techniques that can be used in ensemble learning. Some alternatives include:
	
	1. **Pasting**: Similar to bagging, but instead of sampling with replacement, each subset of data is sampled without replacement. This means that each observation is used only once in the creation of a subset.
	2. **Random Subspace Method**: In this method, instead of resampling the data, different subsets of features are selected randomly for each model. This is useful when dealing with high-dimensional data where the number of features is large.
	3. **Random Patching**: This technique is a combination of bagging and random subspace method, where both samples of data and subsets of features are used to train individual models.
	4. **Rotation Forest**: In rotation forest, principal component analysis (PCA) is applied to random subsets of features, and then decision trees are trained on the transformed data. This technique aims to improve diversity among base learners.

Now since we are aware about the basics of ensemble learning so now let us try to understand the different types of ensemble learning.

- [[Bagging-Boosting]]
- [[Voting-Stacking]]
- [[Random Forest]]
- [[Gradient Boosting]]



First model ke prediction ko subtract kr diya acutal value to find the pseudo residual for each row
- After that next model is trained on the galtiyaan of the pichla model ( that is trained on the pseudo residuals) and after that we get the terminal regions which are the regions represented by the terminal regions.
- Then find the output for each terminal region, means if the query point lie in one of region then what would be the output but to calculate that we will only consider those X values which lies in that region
- https://drive.google.com/file/d/1-MO6IasyTlk2jWX61SPuQ_4I1MsLJ0-a/view
- https://colab.research.google.com/github/campusx-official/100-days-of-machine-learning/blob/main/gradient-boosting/gradient_boost_step_by_step.ipynb




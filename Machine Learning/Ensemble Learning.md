This page is dedicated towards understand the concept of ensemble learning and the resource used for this are the videos of CampusX course videos and also the book called Hands on Machine Learning.

##### What is the concept of wisdom of crowd ? 

Wisdom of crowd is basically a concept which states that when we aggregate the answers of the crowd then that answer will either be close or better than some expert answer. And there are a lot of real world scenarios where we can see this concept

1. In KBC during the audience poll we will always observe that the collectively group of individuals will always know the correct answer.
2. In ecommerce websites the reviews of group of customers collectively will always give us information about the overall performance of the product.

##### What do you mean by ensemble learning and what are its types and its drawback? 

Ensemble learning is a machine learning technique where we group together multiple machine learning models to solve a complex problem. In ensemble learning there are 4 different types of architectures which we use

1. [[Voting]]
2. [[Stacking]]
3. [[Bagging]]
4. Boosting

Even though ensemble learning will give us very good results but the only drawback is the computational complexity of the overall architecture. Basically if we will be dealing with huge data and complex base models then we will experience high computation requirements.

##### Why we generally focus on using different ML algorithms in Ensemble learning  and the ways to ensure different models? 

By using different ML algorithms in ensemble we can solve the problem more effectively and the reason is that, every different machine learning model will approach the problem differently and with this we will be able to eliminate the biasness of individual model thus giving us a good overall result.

There are 3 ways using which we can actually create different machine learning models and these are : 

1. Using different algorithms
2. By giving different data to same algorithms
3. By giving different data to different algorithms


##### Does ensemble learning gives low bias and low variance, if so then how ? 

Yes ensemble learning architecture have the capability to give us low bias and low variance model but the way we can get that is by first using multiple base models having low bias - high variance such as decision tree and after that, since the new data will be spread across multiple decision trees thus the affect on individual decision tree will be reduced which will eventually give us low bias and low variance model as a whole. 

##### What are the various resampling techniques used in context of ensemble learning ? 



-  What are the various resampling techniques used in the context of ensemble learning ?  

	While bagging primarily uses bootstrap sampling, there are other resampling techniques that can be used in ensemble learning. Some alternatives include:
	
	1. **Pasting**: Similar to bagging, but instead of sampling with replacement, each subset of data is sampled without replacement. This means that each observation is used only once in the creation of a subset.
	2. **Random Subspace Method**: In this method, instead of resampling the data, different subsets of features are selected randomly for each model. This is useful when dealing with high-dimensional data where the number of features is large.
	3. **Random Patching**: This technique is a combination of bagging and random subspace method, where both samples of data and subsets of features are used to train individual models.
	4. **Rotation Forest**: In rotation forest, principal component analysis (PCA) is applied to random subsets of features, and then decision trees are trained on the transformed data. This technique aims to improve diversity among base learners.



- [[Bagging-Boosting]]
- [[Voting-Stacking]]
- [[Random Forest]]
- [[Gradient Boosting]]



First model ke prediction ko subtract kr diya acutal value to find the pseudo residual for each row
- After that next model is trained on the galtiyaan of the pichla model ( that is trained on the pseudo residuals) and after that we get the terminal regions which are the regions represented by the terminal regions.
- Then find the output for each terminal region, means if the query point lie in one of region then what would be the output but to calculate that we will only consider those X values which lies in that region
- https://drive.google.com/file/d/1-MO6IasyTlk2jWX61SPuQ_4I1MsLJ0-a/view
- https://colab.research.google.com/github/campusx-official/100-days-of-machine-learning/blob/main/gradient-boosting/gradient_boost_step_by_step.ipynb




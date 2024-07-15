This page is actually dedicated towards understanding the concept of gradient boosting in machine learning and the resources used for this topic are the course videos of CampusX and the links to the notebook PDFs are mentioned

- [Introduction to Gradient Boosting](https://drive.google.com/file/d/1-MO6IasyTlk2jWX61SPuQ_4I1MsLJ0-a/view)
- [Mathematical Intuition behind Gradient Boosting](https://drive.google.com/file/d/1wIBrSzZhbf1DSkqlzXHtBXBt-Oc1YmhC/view)


### What is Boosting ? 

Boosting is basically a ensemble learning technique where we group together multiple weak learners (machine learning algorithms) and these models are trained sequentially, where every model try to correct the mistakes made by the previous model and by this we actually end up creating a very strong big model. 

In the boosting high bias and low variance models, and we specifically chose weak models to avoid overfitting and for fast and easy training.

Now there are actually 3 main algorithms which are based on top of boosting and these are 
1. Gradient Boosting
2. Xgboost
3. CatBoost

### What is gradient boosting and Additive modeling?

Gradient boosting is basically a machine learning technique which is built on top of boosting and this technique can be used to solve both complex regression and classification problems.

Basically in order to solve the complex problems gradient boosting uses the concept of additive modelling, whereas in order to estimate the complex relationship between dependent and independent variables the predictive models are added iteratively in the ensemble, where every new predictive model is constructed to reduce the residual error of the entire ensemble.

### What is the difference between function space and parameter space

- Function space refers to set of all possible functions that can be considered as solution to a given problem.
- Parameter space refers to set of all the possible parameter values associated with some mathematical function.

To mention in short gradient boosting algorithms first operates in the function space and after discovering the final function using additive smoothing, it then move on to the parameter space to find the best set of hyper parameters.

### Explanation of working of the algorithm of the gradient boosting for regression

Since gradient boosting algorithm operates in the function space so the best part is that we can start with any of the regression loss function. Here's a step-by-step explanation of how it works:

1. **Initialization**: Begin with an initial model, $F_0(x)$, and this initial model could be as simple as predicting the mean of the target values for all inputs.
2. Iterative Process: After finding the initial model we start an iterative process which will run for the number of predictive models we want in the ensemble and with every iteration couple of steps will be performed which are
	1. Calculation of pseudo residuals which are the gradients of the loss function with respect to the current model's predictions. These residuals indicate how much and in which direction each prediction needs to be adjusted.
	2. Train a weak learner (e.g., a decision tree) $h_m(x)$ to predict these residuals.
	3. Update the current model by adding the predictions of the weak learner, scaled by a learning rate ν. ( This is basically finding the new function which minimize the overall error in the ensemble)
		$F_m(x) = F_(m-1)(x) + ν*h_m$
    


### What is the difference between gradient descent and Gradient boosting ? 
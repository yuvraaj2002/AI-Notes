Tags : [[Data Processing]]

This  page is dedicated towards understanding the concept of hyper parameter optimization and the resources used for this video are simply the videos of CampusX.

[Bayesian Optimization Concept Explained in Layman Terms](https://towardsdatascience.com/bayesian-optimization-concept-explained-in-layman-terms-1d2bcdeaf12f)
[Keras documentation: Keras Tuner](https://keras.io/keras_tuner/)


### Questions about introduction and techniques

- What is the difference between model parameter and hyper-parameter ?
    
    - Parameters also called model parameters are the type of variables which gets their value during the training of the model. Example : Coefficients of linear regression or weights of neural network.
    - Hyper-parameters are the parameters which influence the training of the model. Example: Value of K in KNN, max_depth in decision tree

- What do you mean by hyper-parameter tuning ?
    
    Hyper parameter tuning is the process of finding the best set of hyper-parameter which maximize the performance of the algorithm.

- What are the various approaches we can use ?
    
    There are 3 different ways using which we can find the optimal values of hyper-parameters ⬇️
    
    1. Grid search cv
    2. Randomized search cv
    3. Advance technqiues ( Bayesian optimization )

- Explain grid search cv ?
    
    Grid search is basically brute force approach of doing hyper-parameter tuning in which we exhaustively go over each and every combination of hyper-parameter on the parameter grid and find the best set of values using cross validation.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/616851a2-2502-4ede-8bac-1dd2af604d5f/Untitled.png)

- What are the major drawbacks of using grid search ?
    
    It is computationally very much expensive especially in case of large datasets and large number of hyper-parameters. To better understand this let us assume that there are 2 hyper-parameters both have 5 possible values.
    
    So for this configuration we will be having total 25 combination of hyper-parameters and for every combination if we are using 5 fold cross validation then we will have to train total 125 models.

- What do you mean by randomized search cv and drawback of this ?
    
    Randomized search cv stands for randomized search cross validation and it is comparatively less computationally expensive than grid search because in this instead of exhaustively going over each and every combination on the parameter grid we random look for some k random combinations.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc979be3-c712-4794-98a8-e832ab76ab34/Untitled.png)
    
    ### Drawback of Randomized search
    
    Since this approach is completely random thus there are high changes we might not get the most optimal values of hyper-parameters.

- Is there any technique which we can use that is not very computationally expensive and also give us best set of hyper-parameters?
    
    Yes by using Bayesian optimization we can actually do hyper-parameter tuning efficiently.
    
    In essence, Bayesian optimization uses past evaluations to strategically choose the next hyperparameter combinations to explore, leading to optimal hyperparameters faster.

- Which libraries can be used for doing Bayesian search
    
    - Hyperopt
    - Optuna

- While doing hyper parameter tuning why we use validation data rather than using test data
    
    In machine learning or deep learning we have concept of data leakage where we make sure that there is proper isolation between training and test data. So that we could get true model performance rather than biases optimistic results.
    
    Now the thing is that during hyper parameter optimization we always have an objective function at hand which we need to maximize or minimize. Now if we will use test data for it then somehow we will passing the information about out test data to algorithm and this violates data leakage condition, so to prevent this we create a proper isolation by using validation data.


### Hyper parameter tuning in deep learning

- What are the various hyper parameters by tuning which we would be able to increase the accuracy of Neural network
    
    There are around 7 hypter parameters by tuning which we would be able to increase the accuracy of the neural network ⬇️
    
    1. Number of Hidden layers
    2. Neurons per layer
    3. learning Rate
    4. Optimizers
    5. Choosing correct batch size
    6. Use appropriate activation function
    7. Choosing accurate number of epochs

- How can we increase the accuracy of the neural network by selecting correct number of hidden layers ?
    
    The thing is that it is always advised to use multiple hidden layers with less number of neurons that one hidden layers with a lot of neurons , and there are 2 reasons for this ⬇️
    
    1. Deep learning use a techinque called REPRESENTATION LEARNING and according to this technique the initial layers of the neural network captures the primitive features such as lines , and edges etec whereas the deep hidden layers captures more complex features as a result if there are multiple hidden layers then the neural network captures the minute details in the data and give more accurate results.
        
        <aside> 📣 Now the thing to keep in mind is that to get correct number of hidden layers in the neural network , just keep increasing the number of hidden layers till overfitting doesn’t happen
        
        </aside>
        
    2. Transfer learning : Let us assume that we made a CNN that detects human face and if we would be asked to make a DL model that could detect monkey face , then in that case since we know that the primitive features of both the human and monkeys are similar thus we will use the initial hidden layers of our previous CNN to build our new CNN , so if there would be multiple hidden layers then only we would be able to implement the concept of transfer learning and if we will use only single layer then transfer learning will not be possible



##### What is a uniform distribution and its types with examples ?

Uniform distribution is a type of probability distribution where all the outcomes are equally likely to occur within a given range and based on type of random variable there are 2 different variants of uniform distribution.

- Discrete uniform distribution : In this the probability associated with every discrete value within  a given range will be same. Example: While Rolling a dice the probability of all outcomes will be same and that is 1/6
- Continuous uniform distribution : In this , the probability of associated with all the possible values of random variable withing the range [a, b] will be same.

##### Can you describe the probability density function (PDF) of a continuous uniform distribution?

##### How do you calculate the mean and variance of a continuous uniform distribution?

##### Give an example of a real-world scenario that can be modeled using a uniform distribution.

##### Explain the concept of the cumulative distribution function (CDF) for a uniform distribution.

##### How would you test if a given dataset follows a uniform distribution?

##### What are the assumptions underlying the use of a uniform distribution?

##### How would you estimate the parameters \(a\) and \(b\) of a continuous uniform distribution from sample data?

##### How does the uniform distribution relate to other distributions, such as the normal distribution or the exponential distribution?

##### What is the entropy of a uniform distribution, and how is it interpreted?

##### How would you apply the uniform distribution in Monte Carlo simulations?

##### Can a uniform distribution be used to model real-world data effectively? Under what circumstances might this be true or not true?

##### How does the uniform distribution fit into the broader context of probability and statistics?



- What do you mean by uniform distribution and what are its types?
    
    Uniform distribution is a type of probability distribution where all the outcomes are equally likely to occur within a given range. There are 2 types of uniform distribution based on the nature of random variable ⬇️
    
    1. **Discrete uniform distribution** : In discrete uniform distribution the random variable is discrete in nature
    2. **Continuous uniform distribution** : In discrete uniform distribution the random variable is continuous in nature
- How many parameters are there in uniform distribution ?
    
    2 parameters namely b and a, upper and lower value (Specifying the range)
    
- What is the Probability density function and CDF for uniform distribution
    
    - Probability density function
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/b7de8798-584c-44a1-9a87-7260cc27d429/Untitled.png)
        
    - Cumulative distribution function
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/9a0332f8-28be-48c0-be88-8d4a38a37a99/Untitled.png)
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/831cefa8-76d5-46d1-902c-e749a46ed1a7/Untitled.png)
        
- How do you compute the mean and variance of a uniform distribution?
    
    - Mean → $(b+a)/2$
    - Variance → $(b-a)^2/12$
- Given a random variable X following a uniform distribution on the interval [a, b], what is the probability P(X < c), where c is a value within the interval [a, b]?
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/31d417b5-456d-4814-a565-19bd1afd5a02/Untitled.png)
    
- Give general examples of Uniform distribution
    
    - Rolling a die and getting a number between 1 to 6 will actually follow a discrete uniform distribution
    - The height of a person randomly selected from a group of individuals whose heights range from 5'0" to 6'0" would follow a continuous uniform distribution.
    - The weight of a randomly selected apple from a basket of apples that weighs between 100 and 200 grams, would follow a continuous uniform distribution.
- Give examples of where uniform distribution is used in machine learning?
    
    Uniform distribution is used in machine learning or deep learning while doing random initialization of some value.
    
    ### In machine learning context
    
    - Example : Randomly initializing the weights of the neural network with the range between 0 and 1 will follow continuous uniform distribution.
    - Example : Selecting the value of K in K means algorithm within specific range would follow discrete uniform distribution.
    
    ### In deep learning context
    
    In deep learning uniform distribution can be seen while performing data augmentation. Basically to generate some artificial data let say image data, we basically perform some mathematical operation on the channel of the image. So let say we want to multiply the red channel value of RGB image with some scaler value so for choosing this value from the range will follow continuous uniform distribution.
    
- What will be the skewness of uniform distribution
    
    The skewness of a uniform distribution is zero. Skewness is a measure of the asymmetry of the probability distribution of a random variable about its mean. In a uniform distribution, all values within the range have the same probability of occurring, and the distribution is symmetric around its mean.
    


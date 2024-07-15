This notion page is dedicated towards understanding the concept of multicollinearity in machine learning and the main resource used for this topic is basically the course video of CampusX.
[Notebook](https://drive.google.com/file/d/131sJUu335FSldQmdP4qTbp4qdSG4jYN8/view) Pdf of this topic.

Tags : [[Data Processing]]


- What do you mean by multicollinearity?
    
    Multicollinearity is basically a situation where 2 or more independent variables are high correlated with each other and this high correlation actually introduces of lot of problems ranging from unreliable estimation of coefficients to difficulty in analyzing the individual effect of independent variable on dependent variable.
    
    ### Example
    
    One common example in which we can see high multicollinearity would be the one, like let say we have the dataset about the college going students in the dataset we have features like CGPA and IQ, now in this case the CGPA and IQ will be highly correlated with each other as normally student with high CGPA tends to have high IQ as well.
    
- When the multicollinearity is considered to be bad ?
    
    Multicollinearity will be considered bad when we want to do inference whereas in case of prediction the multicollinearity will not affect predictive power.
    
    The reason behind this is that in case of inference we try to study the relationship between the independent features and the dependent feature but since due to multicollinearity the independent features are highly correlated with each other thus it becomes difficult to study the individual relationship of independent feature with dependent feature in isolation thus the inference gets hampered.
    
    <aside> 💡 Down below we can actually see that the modified equation looks like the linear regression only so the overall predictive power will not be hampered
    
    </aside>
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/6038e626-14d3-40bc-a270-d5da4c2e0524/Untitled.png)
    
- In the regression Analysis what happens mathematically due to multicollinearity ?
    
    Due to multicollinearity the model coefficients actually become unreliable and the overall standard error increases, further affecting the t test value and the confidence interval of the coefficients.
    
- What do you mean by perfect multicollinearity and what happens due to this ?
    
    Perfect multicollinearity is basically a situation where independent feature is basically the linear function of one or more independent feature.
    
    ### Example
    
    Let say we have dataset regarding the college going students in that feature if we have features like CGPA and Marks in percentage then these 2 features will show perfect multicollinearity. **`Percentage = CGPA * 100`**
    
    |CGPA|Percentage|Placement|
    |---|---|---|
    |8|80|1|
    |7.5|75|0|
    
    ### Problem because of perfect multicollinearity
    
    Due to perfect multicollinearity we will actually not be able to find the value of model coefficients of linear regression using OLS technique.
    
    The reason is that in case of OLS technique we need to find the matrix inverse and in order to find the matrix inverse we need to first calculate 2 things → determinant and Adjoint.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/8a93be5b-3f05-487e-90f2-5780204e62d2/Untitled.png)
    
    Now since there is perfect multicollinearity in our data thus the determinant will actually become 0 and due to this 1/0 will be undefined and we will not get the value of model coefficients
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/633cad05-2c47-4a3c-8bd9-6d4462c8d7f0/Untitled.png)
    
- When do we get perfect multicollinearity ?
    
    One hot encoding is the most common example where we can see perfect multicollinearity (Dummy variable trap)
    
- What do you mean by standard error ?
    
    Standard error is basically the standard deviation of the sampling distribution of a statistic.
    
    <aside> 💡 From population → Multiple samples are derived and summarized via mean as a statistic → The standard deviation of such values will be called the standard error
    
    </aside>
    
- Why happens to standard error due to high multicollinearity ?
    
    Basically for all the variants of the linear regression one common assumption out of many assumption is that there should be no or low multicollinearity but due to high multicollinearity majorly the standard error increase and regression coefficients becomes unreliable
    
    ![1000009692.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/c3a7932d-ea44-4979-97ec-3013b2db28d2/1000009692.jpg)
    
- What things happens due high standard error ?
    
    - Due to increase in standard error the t statistic value decreases and the p value increases, because of which the chances of rejecting the null hypothesis decreases (Where the null hypothesis is that _all regression coefficients accept intercept are 0. And failing to reject null hypothesis actually masks the importance of features for predicting the output_
    - Also due to increase in the standard error the confidence interval also increase and due to increase in confidence interval we actually loose precision.

- What are the types of multicollinearity ?
    
    - **Perfect Multicollinearity**: One predictor is an exact linear combination of others. This makes the model unsolvable using OLS regression as it leads to singularity.
    - **Imperfect Multicollinearity**: Predictors are highly correlated but not perfectly. This leads to instability in coefficient estimates and inflated standard errors, complicating the interpretation of the model.

- What are the ways using which we can detect multicollinearity
    
    There are actually couple of ways through which we can detect the multicollinearity some of which are ⬇️
    
    1. Correlation analysis → Variables having high correlation show high multicollinearity between them
    2. Very small determinant
    3. Variance inflation factor and tolerance

- What is VIF
    
    VIF which stands for Variance inflation factor actually quantifies how much the variance of a regression coefficient is increased due to collinearity.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/8467b3ec-decb-4e06-94d8-62ee2349e981/Untitled.png)
    
    ### Understanding
    
    Suppose you have three predictors in a model: 𝑋1_X_1, 𝑋2_X_2, and 𝑋3_X_3.
    
    1. Calculate VIF for 𝑋1_X_1:
        - Regress _X_1 on _X_2 and _X_3.
        - Obtain $_R^2_$ from this regression and calculate VIF
    2. Repeat the process for 𝑋2 and 𝑋3.
    
    If $𝑉𝐼𝐹_1$ is high, it indicates that 𝑋1 is highly collinear with 𝑋2 and/or 𝑋3, even though we are calculating the VIF for 𝑋1_X_1 alone. The process inherently involves the relationship between 𝑋1_X_1 and the other predictors, thus capturing the multicollinearity.
    
    In summary, VIF is a univariate calculation in the sense that it is computed for individual predictors, but it effectively measures multicollinearity by considering the linear relationships between each predictor and all other predictors in the model.
    
- Explain Tolerance
    
    Tolerance is actually used to measure the proportion of unexplained variance by the predictor and the predictor having high Tolerance means it is largely independent of other features.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/d215e1a6-79d3-4736-b7f1-79addc5b7a82/Untitled.png)
    
    - A tolerance close to 1 means that the predictor is largely independent of the other predictors.
    - A low tolerance value (close to 0) indicates that a large proportion of the predictor's variability is explained by the other predictors, suggesting high multicollinearity.

- How can we remove multicollinearity from our data?
    
    - Collect more data
    - Remove highly correlated variable
    - Combine correlated variable : If correlated independent variables represent similar information, consider combining them into a single variable.
    - Partial least square which is a statistical technique which first perform PCA and then linear regression on newly formed principal components.
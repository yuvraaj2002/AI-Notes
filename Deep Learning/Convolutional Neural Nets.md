QASC This page is dedicated to everything related to convolutional neural network. The notes written in this page are from the Andrew Ng CNN course on Coursera and CampusX video on Youtube. The list of resources that can be useful are mentioned below.
[Andrew Ng Course](https://www.coursera.org/learn/convolutional-neural-networks/home/week/1)

Tags : [[Deep Learning]]


- What is the difference between RGB image and Gray Scale image ?
	- RGB image is a type of image where every pixel is simply a combination of values of 3 different channels that is red, blue and green
	- Gray scale image is a type of image which have only 1 channel. High value represent white color and smaller value represent the black color
    
		![[Pasted image 20240629164024.png|400]]

- What do you mean by Convolutional neural network ?
    
    CNN which stands for Convolutional neural network and they are simply a type of neural network which are designed to work with image data or any matrix like structured data.

    ![[Pasted image 20240629164220.png|500]]
    
- From where the convolutional neural nets are inspired from ?
    From the visual cortex of the human brain.
    
- Why can’t we use ANN for working with Images
    
    ### Why ANN can’t be used
    
    There are 2 major reasons behind why ANN can’t be used for image or any other grid like data structure.
    
    1. **High computation of ANN** : In case we want to use ANN for image or grid like structured data then we need to make sure that the 2d shape is first flattened to 1d because the input layer of ANN only accepts 1d data. Now the problem is that when we flatten the data then the number of neurons on the input layer becomes very large in number and due to this the total number of trainable parameters also increase leading to increase in the computational complexity of the ANN
        
    2. **Loss of spatial information**: ANN by architecture are not capable of capturing the spatial information which could be important features.
        
        <aside> 🚊 Spatial information between pixels is the relationship between the pixel values in the space used to represent the texture, shape, and structure of objects in an image.
        
        </aside>
        
- Why can’t we use RNN for working with image
    
    The thing is that RNN independently can’t be used to work with image data because of high computational complexity and inability to capture spatial information.
    
    But RNN + CNN is used to work with videos where CNN extract features from the video frames and RNN take care of sequential data processing. Common example where both CNN and RNN used are Object activity detection.
    
- Explain why capturing spatial information could be important
    
    Let say we are trying to solve a multi-class classification problem of predicting whether a particular image is of human or dog. In this case we know that in most of dogs face the nose is of dark color and as we move towards the facial features the we see light color skin, so this kind of spatial information (relationship between pixel values) can be an important feature.
    
- What are the various layers present in CNN ?
    
    - Convolutional layer → To extract features from the image or grid
    - Pooling layer → To downsample the feature map to for memory management and making feature map translation invariant
    - Artificial neural network layer → Used as classification head

- Explain Convolutional layer, its operation?
    
    Convolution layer is the very firsts layer with which the image interact and this layer is responsible for extracting the features from the image matrix or grid like data.
    
    - Initial `Conv2D` layers extract abstract features such as vertical or horizontal edges
        
    - The `Conv2D` layers which are present deep inside the layer extract more refined or precise features such as shapes.
        ![[Pasted image 20240629170111.png]]
        
    
    ### Convolution operation
    
    In convolution layer the convolution operation is used to extract features from the image by  performing a element wise multiplication between kernel/filter and the image matrix.
    ![[Pasted image 20240629170050.png]]
    
    The matrix we get after convolution operation will be called feature map and the dimension  of the feature map will be given by the below formula $(N−F+2P)/S​+1$
    
- How Convolution operation works for the RGB image?
    
    In case of RGB image separate filters will be there for individual channel and the final feature map will be the combination of values from the individual filter.
    ![[Pasted image 20240629170700.png]]
    
- What are the various hyper-parameters in Convolutional layer, Explain them
    
    - Filter / Kernel size: Filter is simply a matrix of n*n size which is used to perform convolution operation on the image. **Filter is also known as kernel.**. As Filter size ⬆️ the size of feature map ⬇️
    
    - Stride : Stride is a hyper-parameter using which we can define that how far the filter will move horizontally or vertically after performing single convolution operation. As Filter size ⬆️ the size of feature map ⬇️
        
        ![[Pasted image 20240629171713.png|400]]
        
    - Padding : Padding is a technique of adding a cushioning of 0s around the image matrix to prevent ⬇️
        1. Loss of information after convolution operation
        2. To increase the contribution of border pixels in feature map
        
- What is a feature map and what is the formula to calculate ?
    
    Feature map is simply a matrix which we receive after the convolution or pooling operation and this matrix is used to represent the features which are extracted from the image matrix.
    
    $$ (n-f+2P+1)/S*(n-f+2P+1)/S $$
    
- What are 2 common types of filters used?
    
    - Sobel filter for detecting vertical edges : Left column values **`+ve`** and right column values **`-ve`**
    - Scharr filter for detecting horizontal edges : Upper row values **`+ve`** and bottom row values **`-ve`**
    
	 ![[Pasted image 20240629172141.png|400]]
    
    ### For Making the filter robust
    
    In case we want to detect more robustly (Like edges at 45 or 75 ) then instead of hard coding the filter values we must consider each value to be a parameter and by doing so these parameters will also be learned during the model training.
    
- What are the types of padding ?
    
    - In Valid padding no padding is added to image. This means that the output of the convolution operation will be smaller than the input image.
    - Same padding adds padding to the image so that the output of the convolution operation is the same size as the input image.|
    
- Before passing the feature map to the layer present next to the convolution layer what is prerequisite?
    
    As per recommendation before performing the pooling operation on the feature map first we need to add some non linearity to the feature map and for doing so we can use Nonlinear activation functions such as ReLU, sigmoid or tanh
    
- Which layer comes after convolutional layer and what is the purpose of this layer ?
    
    After the convolutional layer, there typically comes a pooling layer. The pooling layer is used to downsample the feature map, which helps with memory management by reducing the number of parameters and computations in the network. Additionally, pooling helps make the feature map more translation invariant, meaning the output becomes less sensitive to the exact location of features within the input image.
    
- What are the various types of pooling ?
    
    Pooling is an important operation in convolutional neural networks (CNNs) used to reduce the spatial dimensions of the input. The primary types of pooling are:
    
    1. **Max Pooling**: - **Operation**: Takes the maximum value from each patch of the feature map. - **Purpose**: Captures the most prominent features within a region, making it effective for preserving the most significant information while reducing dimensionality.
    2. **Average Pooling**: - **Operation**: Takes the average value from each patch of the feature map. - **Purpose**: Computes the average presence of features, providing a more generalized view compared to max pooling. 
    3. **Global Pooling**: - **Types**: Global Max Pooling and Global Average Pooling. - **Operation**: Applies pooling over the entire feature map rather than patches. - **Purpose**: Reduces each feature map to a single value, commonly used in the final layers of CNNs before fully connected layers. - **Example**: For a feature map of size 4x4, global max pooling will take the maximum value of all 16 elements, while global average pooling will take the average of all 16 elements.
    4. **Fractional Pooling**: - **Operation**: Pools the input with a non-integer down-sampling ratio. - **Purpose**: Offers more flexibility in the pooling size, useful when specific dimensionality reduction is required that doesn't fit into standard integer pooling sizes. - **Example**: Instead of pooling with a fixed size (e.g., 2x2), fractional pooling might pool a 4x4 region into a 2.5x2.5 region.
    5. **Strided Pooling**: - **Operation**: Uses strides to slide the pooling window across the input with steps larger than 1, effectively combining pooling and down-sampling. - **Purpose**: Controls the degree of down-sampling by adjusting the stride length. - **Example**: A 2x2 pooling window with a stride of 2 will move 2 steps horizontally and vertically, reducing the spatial dimensions by half.
    
    ### Differences Between Pooling Types
    
    - **Max Pooling vs. Average Pooling**: - Max pooling focuses on the most prominent features within a region, often leading to sparse representations and better performance in tasks where the presence of certain features is crucial. - Average pooling provides a more holistic view by considering all values in a region, which might be useful for tasks requiring a smoother representation of features.
    - **Local vs. Global Pooling**: - Local pooling (e.g., max or average pooling) reduces spatial dimensions incrementally by applying the operation to patches of the feature map. - Global pooling compresses the entire feature map into a single value per feature map, often used at the end of CNNs to create a fixed-size representation irrespective of the input size.
    - **Fixed vs. Fractional Pooling**: - Fixed pooling (max or average pooling) uses standard integer pooling sizes (e.g., 2x2, 3x3). - Fractional pooling allows for non-integer pooling sizes, providing more flexibility in how the dimensions are reduced. Each type of pooling has its unique benefits and can be chosen based on the specific requirements of the neural network architecture and the problem at hand.
    
    |Max Pooling|Average Pooling|
    |---|---|
    |In this type of pooling for the given filter size window we select the maximum value|In this type of pooling for the given filter size window we calculate the average of pixel values.|
    
    ![This is example of max pooling where the high level features are considered as we have somewhat ignored the low level features.](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/b7200c39-b59c-4d06-8446-3651590866c5/Untitled.png)
    
    This is example of max pooling where the high level features are considered as we have somewhat ignored the low level features.
    
- Out of pooling layer and convolutional layer which one is parametric and which one is non parametric ?
    
    In the context of neural networks, especially convolutional neural networks (CNNs), the terms "parametric" and "non-parametric" relate to whether the layers have learnable parameters or not:
    
    - Convolutional Layer: This is a _**parametric layer**_. It contains learnable parameters, which are the weights (filters or kernels) that are optimized during the training process. These parameters are adjusted through backpropagation to minimize the loss function and improve the model's performance.
    - Pooling Layer: This is a _**non**_-_**parametric**_ layer. Pooling layers, such as max pooling or average pooling, do not have learnable parameters. They perform a fixed operation (e.g., taking the maximum or average of a set of values) that reduces the spatial dimensions of the input, thus helping to down-sample the feature maps and making the network more efficient while maintaining important information.
    
    In summary, convolutional layers are parametric because they involve learnable parameters (filters), whereas pooling layers are non-parametric because they involve fixed operations without any learnable parameters.
    
- What are the drawbacks of Pooling layer ?
    
    1. The use of pooling layer makes our model [translation invariant](https://www.baeldung.com/cs/translation-invariance-equivariance#:~:text=CNNs) but in case of image segmentation use cases where the positioning of the objects matters a lot, in these cases pooling layer makes things worse so it is not applied
    2. It leads to loss of a lot of information even if padding is used.

- What comes after the Pooling layer ?
    
    Once the feature map passes through the pooling layer then its is first flatten using the flatten layer so that it could be passed as an input to the Fully connected neural network layer.
    
    - Convolutional + Pooling layer → Feature extractor
    - Fully connected layer → Classification head

	After using the pooling layer in a CNN, you can either flatten the data or use a global pooling layer. The resulting data can then be passed to a fully connected layer or used as input to some traditional machine learning algorithm for classification.
    
    

![[Pasted image 20240629180556.png]]
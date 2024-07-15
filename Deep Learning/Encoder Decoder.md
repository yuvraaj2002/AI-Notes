This notion page is dedicated towards the notes related to the topic of sequence to sequence model in deep learning. The resources used for understanding are mentioned below. Resources used 📚

- [Encoder-Decoder Seq2Seq Models, Clearly Explained!!](https://medium.com/analytics-vidhya/encoder-decoder-seq2seq-models-clearly-explained-c34186fbf49b)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
- [Deep Visual-Semantic Alignments for Generating Image Descriptions](https://arxiv.org/abs/1412.2306)
- [NIPS: Oral Session 4 - Ilya Sutskever](https://youtu.be/-uyXE7dY5H0)

    # **Further Reading**
    
  If you’ve found your way here, then congratulations!! I hope you’ve found this useful. Since this is my first attempt at blogging, I hope that the readers will be forgiving and overlook any slight errors I may have made. I am mentioning more resources on the topic if you are looking to go deeper.
    
    1. I would suggest you to go through the paper we have discussed [**Sequence to Sequence Learning with Neural Networks by Ilya Sutskever, et al](https://arxiv.org/abs/1409.3215)** by yourself once.
    2. Nothing helps you understand a concept better than implementing it yourself. I found this amazing blog [**Neural Machine Translation with Keras](https://towardsdatascience.com/neural-machine-translation-using-seq2seq-with-keras-c23540453c74)** where an Encoder-Decoder model is trained from scratch for English to French translation.
    3. As mentioned before, there are a lot of advanced techniques which have been developed over encoder-decoder models for Seq2Seq modelling. For them I strongly suggest you to refer to the following in order
    
    - Attention Mechanism → _Jay Alammar,_ [**Visualizing A Neural Machine Translation Model](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)** blog post, 2018.
    - Transformer → _Jay Alammar,_ [**The Illustrated Transformer**](https://jalammar.github.io/illustrated-transformer/) blog post*,* 2018.
    - BERT → Jay Alammar, [**The Illustrated BERT](http://jalammar.github.io/illustrated-bert/)** blog post, 2018.
- Difference between seq2seq and encoder decoder model
    
    1. **Sequence-to-Sequence (Seq2Seq):**
        - Seq2Seq refers to a type of model architecture designed for tasks where the input and output are both sequential data of potentially different lengths.
        - The architecture consists of two main components: an encoder and a decoder.
        - The encoder processes the input sequence and transforms it into a fixed-size context or representation (often a vector) called the "thought vector" or "context vector."
        - The decoder takes this context vector and generates the output sequence step by step.
    2. **Encoder-Decoder:**
        - An encoder-decoder architecture is a more general framework that can be applied to various tasks, not just those involving sequences.
        - In the context of sequences, it typically involves an encoder that processes the input and produces a representation, and a decoder that takes this representation and generates the output.
        - The term "encoder-decoder" is broad and can encompass different types of architectures beyond just sequences.
    
    In summary, sequence-to-sequence specifically emphasizes the nature of tasks where sequences are input and output. An encoder-decoder, on the other hand, is a more general term that can be applied to a broader range of tasks, including but not limited to sequences. A Seq2Seq model is a specific instance of an encoder-decoder architecture tailored for sequential data.
    
- Content
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/bfad22c2-e3a3-4676-97d0-58ffa6a493db/Untitled.png)
    
    # Sequence to sequence model ⛓️
    
    Sequence to sequence model is a **deep learning model** which takes sequence of items as an input and return sequence of items as an output. In this model under the hood there are 2 recurrent neural networks which works and these are **`encoder`** and **`decoder`.**
    
    <aside> ♻️ An important thing is that in the Sequence to sequence model the length of input and output sequence may or may not be same. For example Seq2Seq are widely used in **machine/language translation** and **text summarization**.
    
    </aside>
    
    ### Encoder in Seq2Seq Model
    
    The **`encoder`** basically _process each item in the sequence_ , **compile the information into a vector called context vector** and then pass this context vector to the decoder RNN. _Context vector is simply the output which is received after processing last item in the input sequence._
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/18687c81-b85e-4acc-bf28-88bee4038d8a/Untitled.png)
    
    - We can set the size of the context vector, and **size of the context vector = number of neurons in the encoder RNN**. In real world the size of context vector could be of size like 256, 512, or 1024.
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/69fabea3-f77c-43b7-b6b6-aaf4fd43b11f/Untitled.png)
        
    
    ⚠️ An important thing to keep in mind is that we don’t pass the input words directly into the encoder RNN, instead we first give a numerical representation to that word using some word embedding algorithm for example Word2Vec which is a neural network based word embedding technique.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/80cf6d14-1c06-49b3-8729-fba5baa22663/Untitled.png)
    
    After giving a numerical representation to the word at each time step the RNN gets 2 things as an input and these are “word vector” and “hidden state”.
    
    - Mathematical flow (Vector representation)
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/faaa2b72-b088-46d6-890b-76f75acb514c/Untitled.png)
        
    
    [The decoder also maintains a hidden state that it passes from one time step to the next. We just didn’t visualise it in this graphic because we’re concerned with the major parts of the model for now.](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/e4f4329e-f229-4cf3-8c72-91b29f241491/seq2seq_5.mp4)
    
    The decoder also maintains a hidden state that it passes from one time step to the next. We just didn’t visualise it in this graphic because we’re concerned with the major parts of the model for now.
    
    - Unrolled view of the above flow
        
        [https://jalammar.github.io/images/seq2seq_6.mp4](https://jalammar.github.io/images/seq2seq_6.mp4)
        
    
    ### Context vector : Bottle neck for Seq2Seq model 💔
    
    In sequence to sequence model the **`context vector`** became a bottle neck, because for the long input sentences the context vector had to capture the complete information about that sentence including the order of the words and the relationships between them and this approach didn’t gave good results for the long sentences, thus to solve this issue 2 things came into existence 👇🏾
    
    1. **Attention mechanism** allows the decoder to focus on different parts of the input sequence at different times. This allows the decoder to access more information about the input sequence, even if it is very long.
    2. **Bidirectional encoder** processes the input sequence in both the forward and backward directions. This allows the encoder to learn more complex representations of the input sequence, which can be helpful for tasks such as machine translation and text summarization.
    
    ### Attention model 🧠 and how is it different from traditional Seq2Seq models ?
    
    The attention model differ from the traditional sequence to sequence model in 2 ways and these are ⬇️
    
    1. In attention model the attention encoder instead of passing only the last hidden state “context vector” to the decoder passes all the hidden states generated at each time step.
        
        [seq2seq_7.mp4](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/1c995188-7e30-403e-b2a7-1e1fb77e4c13/seq2seq_7.mp4)
        
    2. The attention decoder perform some additional steps before producing output for the current time step so that it could focus on the relavent parts at that time step and these steps are :
        
        1. It considers all the encoder hidden states and score each hidden state
        2. After scoring each encoder hidden state it calculate the soft max score for each hidden state and then multiply the resultant soft max scores with each vector.
        3. Finally the resultant vectors are added to create a final decoder hidden state for the current time step
        
        [This scoring exercise is done at each time step on the decoder side.](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/782da3a1-57b4-4ba3-845f-7b6bfd2f43df/attention_process.mp4)
        
        This scoring exercise is done at each time step on the decoder side.
        



- What do you mean by sequence modeling problems, and how do sequence-to-sequence problems differ from other types of sequence modeling challenges?
    
    Sequence modeling problems are type of problems where the input is sequence of data whereas the output may or may not be sequence of data. Example : Movie review.
    
    Sequence to sequence are type of sequence modeling problems where both the input and output is sequence of data. Example: Machine translation
    
    <aside> 🚊 Sequence modeling problems may be **`(1-M)`** or **`(M-M)`** but sequence to sequence problems will always be **`(M-M)`**
    
    </aside>
    
    [This is an illustration of the sequence to sequence model](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/6f27ba6c-4649-4d3c-a917-35a7822d90e4/seq2seq_3.mp4)
    
    This is an illustration of the sequence to sequence model
    
- Can you provide an overview of the general architecture of a sequence-to-sequence model and elaborate on its key components?
    
    To solve sequence to sequence modelling problems encoder decoder architecture is being used and this architecture have 3 main components ⬇️
    
    1. Encoder block → This module process the sequence of data as input and then generate a context vector.
    2. Context vector → A vector encapsulating all the information about the input sequential data
    3. Decoder block → Generate output data by utilizing the context vector generated by the encoder block
    
    ### High level Diagram
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/5b60bcec-4782-4ea4-8553-d01635ed6bfd/Untitled.png)
    
    ### Inside of the encoder and decoder module
    
    - Encoder module
        
        The encoder block of the encoder-decoder model contains a LSTM cell or GRU cell. The internal LSTM cell takes the input vector (word embedding) at every time step and generates 2 states called cell state and hidden state.
        
        - Cell state maintains the long term context of the input data
        - Hidden state maintains the short term context of the input data
        
        > At the last time step both the states are sent as input to the decoder inform of context vector.
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/ba54ccf9-48a5-45a1-85bf-9731f083950f/Untitled.png)
        
    - Decoder module
        
        Just like the encoder module the decoder module also has LSTM and GRU cells but the main working of the decoder module is to generate sequence of output by utilizing the context vector generated by the encoder module.
        
    
    ![Context vector is basically derived from the hidden state of the last time step and its dimensionality = Number of neurons present in the sigmoid or tanh neural net layer of LSTM Cell](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/ea053cdc-13af-486f-9cb7-9c0c12e690b4/Untitled.png)
    
    Context vector is basically derived from the hidden state of the last time step and its dimensionality = Number of neurons present in the sigmoid or tanh neural net layer of LSTM Cell
    
- Likewise, could you elaborate on the decoder component of a sequence-to-sequence model and shed light on its function within the model?
    
    Just like encoder block, the decoder block also contains either LSTM cell or GRU cell, but the main working of the decoder block is to simply utilize the context vector as input and generate the output sequence data.
    
    - The working of decoder is different for the training and testing phase
    
    ![https://miro.medium.com/v2/resize:fit:875/1*yYL1eM6UWbBZa9N975ShpA.png](https://miro.medium.com/v2/resize:fit:875/1*yYL1eM6UWbBZa9N975ShpA.png)
    
- For an encoder-decoder model, how does training works?
    
    ### Training and testing phase : Encoder
    
    The encoder works same for both the training and testing phase, basically the encoder takes the word embedding of word at the current time step and then process it to give 2 vectors or states called cell state and hidden state, which are sent as input for the next time step. Finally for the last word or last time step a final vector is sent as output called the context vector.
    
    ### Training and testing phase : Decoder
    
    **`Note`**: The working of the decoder module is different for the training and testing phase, During the training phase for the decoder model 2 words are added to the output sequence. Commonly the words are <START> and <END>. Representing the start and the end of the sequence.
    
    After the addition of these 2 words in the output sequence, for every time step the decoder model utilize the context vector and generate a vector having probability values and the token with the maximum value will be considered as the output for that time step.
    
    Other than this the actual binary output vector is also provided so that decoder model could actually learn the real output.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/96e5a50f-3b88-4011-8047-0dc797852d83/Untitled.png)
    
    Referring to the above diagram, `y1_pred` = [0.02 0.12 0.36 0.1 0.3 0.1] tells us that our model thinks that the probability of 1st token in the output-sequence being ‘<START>’ is 0.02, ‘ravi’ is 0.12, ‘de’ is 0.36 and so on. We take the predicted word to be the one with the highest probability. Hence here the predicted word/token is **‘de’** with a probability of 0.36
    
- When it comes to testing a sequence-to-sequence model, what steps are involved, and how is the model evaluated for its effectiveness?
    
    ### Testing phase of decoder model
    
    - During the testing phase once the context vector is generated by the encoder block. For first time step <START> key word is sent as an input and this time for the next time step since the model is already trained so copy of the current time step is sent as an input for the next time step.
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/9256508f-0c62-4e94-b02c-43429de1e57b/Untitled.png)
        
    - The correctness of the model depends on the amount of data available and how well it has been trained. The model may predict a wrong output but nevertheless, the same output is only fed to the next time-step in the test phase.
        
- Final representation of the encoder decoder model
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/4b8bca5a-93d7-4a87-a5af-d7f002a94ae9/Untitled.png)
    
- In your view, what are the limitations associated with encoder-decoder models, and what have been done to deal with this issue?
    
    The major drawback of sequence to sequence model is too much dependency on context vector to store the information about the entire input sequence. Basically context vector is fixed size vector and for the very long sentences the context vectors fails to capture the entire information.
    
    - To deal with this issue the concept of attention came into existence
- Advance questions
    
    1. Can you explain the concept of attention mechanisms in the context of sequence-to-sequence models and how they address certain limitations in traditional encoder-decoder architectures?
    2. What are some common challenges faced during the training of sequence-to-sequence models, and how can these challenges be mitigated?
    3. How does the choice of the neural network architecture for the encoder and decoder impact the performance of a sequence-to-sequence model?
    4. Are there any real-world applications where sequence-to-sequence models have demonstrated significant success, and what makes them particularly suitable for those applications?
    5. In terms of computational efficiency, what are some strategies or advancements that have been introduced to enhance the training and inference speed of sequence-to-sequence models?
    6. Could you discuss any advancements or variations of sequence-to-sequence models, such as transformer-based architectures, and how they compare to the traditional encoder-decoder models?
    7. When dealing with variable-length input sequences, how does padding affect the performance of a sequence-to-sequence model, and are there alternative approaches to handling variable-length inputs?
    8. In the context of transfer learning, how can pre-trained embeddings or models be leveraged to improve the performance of sequence-to-sequence tasks?
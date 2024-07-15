This is the place for all the notes related to Object detection and the architectures related to the object detection. Basically we will talk about couple of architectures and understand the drawback of each of the architecture. The list of architectures we will be looking at are 
1. CNN
2. RCNN
3. Fast RCNN
4. Faster RCNN
5. YOLO
6. Short Overview of variations made from V1 to V8

#### ▶️ What is object detection and how is it different from classification

From the birds eye view both object detection and classification are basically computer vision problems but the fundamental difference between the 2 is that in case of classification we are only focused towards assigning a predefined class label to the image whereas in case of object detection we first of all we try to find out the exact positioning of object in the image (Object localization) and then assigning a predefined class to that object in image.

![[Pasted image 20240627050500.png|350]]
#### ▶️ Why plain CNN is not used for object detection

As a matter of fact the CNN can be used for doing object detection but the thing is that they can only be used to detect single object only. In very very simple terms we simply need to pass the image having an object in it through the Conv and Pooling layers of CNN to extract features from it, and after that we need to adjust the overall architecture in such a way that it not only predicts the bounding box coordinates of the object, but also gives us the class probability.

![[Pasted image 20240627051148.png|450]]


Now in order to make CNN detect more than 1 object in the image we need to use sliding window approach, where we will define a window of size w * h and we will move that window over the entire image and pass every window patch to the CNN for detection of bounding box and class probability. The 2 major drawback of this approach 
1. It is computationally very much expensive
2. There is a tradeoff between accuracy/speed and the size of the sliding window

#### ▶️ Alternative Approaches for Efficient Object Detection:

- **Region Proposal Networks (RPNs):** There are architectures like R-CNN, Fast RCNN and Faster RCNN. RPNs are smaller networks that efficiently propose candidate regions likely to contain objects. The CNN then focuses its processing power on these promising regions instead of every possible window.
- **Single Shot Detectors (SSD) & You Only Look Once (YOLO):** These architectures aim to directly predict bounding boxes and class probabilities from a single image pass through the CNN. They achieve this through various techniques like feature pyramids and anchor boxes, avoiding the need for exhaustive sliding windows.


### ▶️ Region Proposal networks

Out of all region proposal networks R-CNN was the very first architecture which was built on top of CNN for doing object detection. The way this network works is that rather that doing exhaustive search over the entire image for doing object detection it uses a Selective Search algorithm on top of CNN to first propose some possible regions in the overall frame which have high probability of having some object. And then only the CNN is applied for these selected regions. 

![[Pasted image 20240627053218.png|550]]


#### ▶️ Understanding the selective search algorithm for region proposal

Selective search algorithm basically propose 2000 region proposals, let us take a look at the steps which are being followed for proposing the regions ⬇️

1. `Step 1 (Over segmentation)` → Performing over segmentation on the given image, where the segmented regions will actually hold low level features like color similarity.
    
    ![[Pasted image 20240627054603.png|500]]
    
2. `Step 2 (Similarity-based Merging)` → After the over segmentation the merging of these regions is performed based on similarity like Color similarity, texture similarity and size similarity
    
3. `Step 3 (Hierarchical merging strategy)` → Selective Search doesn't simply merge all similar regions at once. Instead, it follows a hierarchical strategy.
    
    - It calculates the similarity between all pairs of adjacent regions.
    - The most similar pair of regions is then merged into a single larger region.
    - This process continues iteratively, merging the most similar regions based on the updated similarities after each merge.
        
        ![[Pasted image 20240627054439.png|500]]
        
4. `Step 4 (Stopping criteria)` → The merging process stops when a certain stopping criterion is met. This criterion can be based on factors like:
    
    - Reaching a predefined number of regions.
    - Reaching a minimum region size (avoiding merging very small regions).

Also point to be noted is that since the CNN expect the input to be of specific size and dimension so the regions are also scaled before passing them to the CNN.

![[Pasted image 20240627055348.png|450]]

#### ▶️ Issues with Simple RCNN architecture

- RCNN normally proposes 2000 candidate regions in couple of seconds which is better than exhaustive search, but still this process is computationally expensive due to processing each proposed region separately through the CNN.

- Perform a bitwise AND operation between the original image and the mask image. This operation retains pixel values only where both images have non-zero values, effectively masking out the bounding box area in the original image with black.
- **Pixelation:** Replace the number plate area with randomly colored squares, making the details indistinguishable.
- **Gaussian Blur:** Apply a blur filter to the plate, obfuscating the characters while preserving some background context.
- **Mosaic Blur:** Divide the plate area into smaller tiles and shuffle them, creating a distorted view.
- **Dithering:** Convert the plate area to a pattern of dots with varying density, obscuring the characters.
- **Watermarking:** Embed a transparent, non-invasive watermark over the plate, indicating the masking without completely hiding it.
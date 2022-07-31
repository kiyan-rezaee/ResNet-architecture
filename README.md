## Introduction : 
>> In this novel architecture, the input of each layer consists of the feature maps of all earlier layer, and its output is passed to each subsequent layer. to get more information you can click [here](https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035)

## model : 
> I use pretrained model ( Res-net 152 ) from [Imagenet](https://www.image-net.org/)

> here is a list of labels that Imagenet classified. [link](https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a)

 <hr>

### model summary :
 ```
Model: "resnet152"
_______________________________________________________
Total params: 60,419,944
Trainable params: 60,268,520
Non-trainable params: 151,424
 ```

## Result :
>> I give three random images to model to predict the label. 

### Image one : 
![Dog image](/1.jpg)

### model predictions (top 3) : 

| **prediction** 	| **probability** 	|
|----------------	|-----------------	|
| Samoyed        	| 0.99634475      	|
| kuvasz         	| 0.0021851999    	|
| Eskimo_dog     	| 0.00034048688   	|

<hr>

### Image two : 
![cup](/2.jpg)

### model predictions (top 3) : 

| **prediction** 	| **probability** 	|
|----------------	|-----------------	|
| cup        	    | 0.70212674      	|
| coffee_mug        | 0.2844404       	|
| pitcher     	    | 0.007878293   	|

<hr>

### Image one : 
![cat image](/3.jpeg)

### model predictions (top 3) : 

| **prediction** 	| **probability** 	|
|----------------	|-----------------	|
| Egyptian_cat      | 0.864664      	|
| tabby         	| 0.061028093    	|
| lynx     	        | 0.02759154   	    |   

<hr>
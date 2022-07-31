## Introduction : 
>> In this novel architecture, the input of each layer consists of the feature maps of all earlier layer, and its output is passed to each subsequent layer. to get more information you can click [here](https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035)

## model : 
> I use pretrained model ( Res-net 152 ) from [Imagenet](https://www.image-net.org/)

 <hr>

> here is a list of labels that Imagenet classified. [link](https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a)

 <hr>

 ```
Model: "resnet152"
__________________________________________________________________________________________________
 Layer (type)                   Output Shape         Param #     Connected to
==================================================================================================
 input_1 (InputLayer)           [(None, 224, 224, 3  0           []
                                )]

 conv1_pad (ZeroPadding2D)      (None, 230, 230, 3)  0           ['input_1[0][0]']

 conv1_conv (Conv2D)            (None, 112, 112, 64  9472        ['conv1_pad[0][0]']
                                )

 conv1_bn (BatchNormalization)  (None, 112, 112, 64  256         ['conv1_conv[0][0]']
                                )

 conv1_relu (Activation)        (None, 112, 112, 64  0           ['conv1_bn[0][0]']
                                )

 pool1_pad (ZeroPadding2D)      (None, 114, 114, 64  0           ['conv1_relu[0][0]']
                                )

 pool1_pool (MaxPooling2D)      (None, 56, 56, 64)   0           ['pool1_pad[0][0]']

 conv2_block1_1_conv (Conv2D)   (None, 56, 56, 64)   4160        ['pool1_pool[0][0]']

 conv2_block1_1_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block1_1_conv[0][0]']
 ization)

 conv2_block1_1_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block1_1_bn[0][0]']
 n)

 conv2_block1_2_conv (Conv2D)   (None, 56, 56, 64)   36928       ['conv2_block1_1_relu[0][0]']

 conv2_block1_2_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block1_2_conv[0][0]']
 ization)

 conv2_block1_2_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block1_2_bn[0][0]']
 n)

 conv2_block1_0_conv (Conv2D)   (None, 56, 56, 256)  16640       ['pool1_pool[0][0]']

 conv2_block1_3_conv (Conv2D)   (None, 56, 56, 256)  16640       ['conv2_block1_2_relu[0][0]']

 conv2_block1_0_bn (BatchNormal  (None, 56, 56, 256)  1024       ['conv2_block1_0_conv[0][0]']
 ization)

 conv2_block1_3_bn (BatchNormal  (None, 56, 56, 256)  1024       ['conv2_block1_3_conv[0][0]']
 ization)

 conv2_block1_add (Add)         (None, 56, 56, 256)  0           ['conv2_block1_0_bn[0][0]',
                                                                  'conv2_block1_3_bn[0][0]']

 conv2_block1_out (Activation)  (None, 56, 56, 256)  0           ['conv2_block1_add[0][0]']

 conv2_block2_1_conv (Conv2D)   (None, 56, 56, 64)   16448       ['conv2_block1_out[0][0]']

 conv2_block2_1_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block2_1_conv[0][0]']
 ization)

 conv2_block2_1_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block2_1_bn[0][0]']
 n)

 conv2_block2_2_conv (Conv2D)   (None, 56, 56, 64)   36928       ['conv2_block2_1_relu[0][0]']

 conv2_block2_2_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block2_2_conv[0][0]']
 ization)

 conv2_block2_2_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block2_2_bn[0][0]']
 n)

 conv2_block2_3_conv (Conv2D)   (None, 56, 56, 256)  16640       ['conv2_block2_2_relu[0][0]']

 conv2_block2_3_bn (BatchNormal  (None, 56, 56, 256)  1024       ['conv2_block2_3_conv[0][0]']
 ization)

 conv2_block2_add (Add)         (None, 56, 56, 256)  0           ['conv2_block1_out[0][0]',
                                                                  'conv2_block2_3_bn[0][0]']

 conv2_block2_out (Activation)  (None, 56, 56, 256)  0           ['conv2_block2_add[0][0]']

 conv2_block3_1_conv (Conv2D)   (None, 56, 56, 64)   16448       ['conv2_block2_out[0][0]']

 conv2_block3_1_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block3_1_conv[0][0]']
 ization)

 conv2_block3_1_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block3_1_bn[0][0]']
 n)

 conv2_block3_2_conv (Conv2D)   (None, 56, 56, 64)   36928       ['conv2_block3_1_relu[0][0]']

 conv2_block3_2_bn (BatchNormal  (None, 56, 56, 64)  256         ['conv2_block3_2_conv[0][0]']
 ization)

 conv2_block3_2_relu (Activatio  (None, 56, 56, 64)  0           ['conv2_block3_2_bn[0][0]']
 n)

 conv2_block3_3_conv (Conv2D)   (None, 56, 56, 256)  16640       ['conv2_block3_2_relu[0][0]']

 conv2_block3_3_bn (BatchNormal  (None, 56, 56, 256)  1024       ['conv2_block3_3_conv[0][0]']
 ization)

 conv2_block3_add (Add)         (None, 56, 56, 256)  0           ['conv2_block2_out[0][0]',
                                                                  'conv2_block3_3_bn[0][0]']

 conv2_block3_out (Activation)  (None, 56, 56, 256)  0           ['conv2_block3_add[0][0]']

 conv3_block1_1_conv (Conv2D)   (None, 28, 28, 128)  32896       ['conv2_block3_out[0][0]']

 conv3_block1_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block1_1_conv[0][0]']
 ization)

 conv3_block1_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block1_1_bn[0][0]']
 n)

 conv3_block1_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block1_1_relu[0][0]']

 conv3_block1_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block1_2_conv[0][0]']
 ization)

 conv3_block1_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block1_2_bn[0][0]']
 n)

 conv3_block1_0_conv (Conv2D)   (None, 28, 28, 512)  131584      ['conv2_block3_out[0][0]']

 conv3_block1_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block1_2_relu[0][0]']

 conv3_block1_0_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block1_0_conv[0][0]']
 ization)

 conv3_block1_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block1_3_conv[0][0]']
 ization)

 conv3_block1_add (Add)         (None, 28, 28, 512)  0           ['conv3_block1_0_bn[0][0]',
                                                                  'conv3_block1_3_bn[0][0]']

 conv3_block1_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block1_add[0][0]']

 conv3_block2_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block1_out[0][0]']

 conv3_block2_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block2_1_conv[0][0]']
 ization)

 conv3_block2_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block2_1_bn[0][0]']
 n)

 conv3_block2_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block2_1_relu[0][0]']

 conv3_block2_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block2_2_conv[0][0]']
 ization)

 conv3_block2_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block2_2_bn[0][0]']
 n)

 conv3_block2_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block2_2_relu[0][0]']

 conv3_block2_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block2_3_conv[0][0]']
 ization)

 conv3_block2_add (Add)         (None, 28, 28, 512)  0           ['conv3_block1_out[0][0]',
                                                                  'conv3_block2_3_bn[0][0]']

 conv3_block2_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block2_add[0][0]']

 conv3_block3_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block2_out[0][0]']

 conv3_block3_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block3_1_conv[0][0]']
 ization)

 conv3_block3_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block3_1_bn[0][0]']
 n)

 conv3_block3_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block3_1_relu[0][0]']

 conv3_block3_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block3_2_conv[0][0]']
 ization)

 conv3_block3_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block3_2_bn[0][0]']
 n)

 conv3_block3_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block3_2_relu[0][0]']

 conv3_block3_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block3_3_conv[0][0]']
 ization)

 conv3_block3_add (Add)         (None, 28, 28, 512)  0           ['conv3_block2_out[0][0]',
                                                                  'conv3_block3_3_bn[0][0]']

 conv3_block3_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block3_add[0][0]']

 conv3_block4_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block3_out[0][0]']

 conv3_block4_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block4_1_conv[0][0]']
 ization)

 conv3_block4_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block4_1_bn[0][0]']
 n)

 conv3_block4_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block4_1_relu[0][0]']

 conv3_block4_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block4_2_conv[0][0]']
 ization)

 conv3_block4_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block4_2_bn[0][0]']
 n)

 conv3_block4_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block4_2_relu[0][0]']

 conv3_block4_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block4_3_conv[0][0]']
 ization)

 conv3_block4_add (Add)         (None, 28, 28, 512)  0           ['conv3_block3_out[0][0]',
                                                                  'conv3_block4_3_bn[0][0]']

 conv3_block4_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block4_add[0][0]']

 conv3_block5_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block4_out[0][0]']

 conv3_block5_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block5_1_conv[0][0]']
 ization)

 conv3_block5_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block5_1_bn[0][0]']
 n)

 conv3_block5_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block5_1_relu[0][0]']

 conv3_block5_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block5_2_conv[0][0]']
 ization)

 conv3_block5_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block5_2_bn[0][0]']
 n)

 conv3_block5_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block5_2_relu[0][0]']

 conv3_block5_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block5_3_conv[0][0]']
 ization)

 conv3_block5_add (Add)         (None, 28, 28, 512)  0           ['conv3_block4_out[0][0]',
                                                                  'conv3_block5_3_bn[0][0]']

 conv3_block5_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block5_add[0][0]']

 conv3_block6_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block5_out[0][0]']

 conv3_block6_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block6_1_conv[0][0]']
 ization)

 conv3_block6_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block6_1_bn[0][0]']
 n)

 conv3_block6_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block6_1_relu[0][0]']

 conv3_block6_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block6_2_conv[0][0]']
 ization)

 conv3_block6_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block6_2_bn[0][0]']
 n)

 conv3_block6_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block6_2_relu[0][0]']

 conv3_block6_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block6_3_conv[0][0]']
 ization)

 conv3_block6_add (Add)         (None, 28, 28, 512)  0           ['conv3_block5_out[0][0]',
                                                                  'conv3_block6_3_bn[0][0]']

 conv3_block6_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block6_add[0][0]']

 conv3_block7_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block6_out[0][0]']

 conv3_block7_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block7_1_conv[0][0]']
 ization)

 conv3_block7_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block7_1_bn[0][0]']
 n)

 conv3_block7_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block7_1_relu[0][0]']

 conv3_block7_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block7_2_conv[0][0]']
 ization)

 conv3_block7_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block7_2_bn[0][0]']
 n)

 conv3_block7_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block7_2_relu[0][0]']

 conv3_block7_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block7_3_conv[0][0]']
 ization)

 conv3_block7_add (Add)         (None, 28, 28, 512)  0           ['conv3_block6_out[0][0]',
                                                                  'conv3_block7_3_bn[0][0]']

 conv3_block7_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block7_add[0][0]']

 conv3_block8_1_conv (Conv2D)   (None, 28, 28, 128)  65664       ['conv3_block7_out[0][0]']

 conv3_block8_1_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block8_1_conv[0][0]']
 ization)

 conv3_block8_1_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block8_1_bn[0][0]']
 n)

 conv3_block8_2_conv (Conv2D)   (None, 28, 28, 128)  147584      ['conv3_block8_1_relu[0][0]']

 conv3_block8_2_bn (BatchNormal  (None, 28, 28, 128)  512        ['conv3_block8_2_conv[0][0]']
 ization)

 conv3_block8_2_relu (Activatio  (None, 28, 28, 128)  0          ['conv3_block8_2_bn[0][0]']
 n)

 conv3_block8_3_conv (Conv2D)   (None, 28, 28, 512)  66048       ['conv3_block8_2_relu[0][0]']

 conv3_block8_3_bn (BatchNormal  (None, 28, 28, 512)  2048       ['conv3_block8_3_conv[0][0]']
 ization)

 conv3_block8_add (Add)         (None, 28, 28, 512)  0           ['conv3_block7_out[0][0]',
                                                                  'conv3_block8_3_bn[0][0]']

 conv3_block8_out (Activation)  (None, 28, 28, 512)  0           ['conv3_block8_add[0][0]']

 conv4_block1_1_conv (Conv2D)   (None, 14, 14, 256)  131328      ['conv3_block8_out[0][0]']

 conv4_block1_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block1_1_conv[0][0]']
 ization)

 conv4_block1_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block1_1_bn[0][0]']
 n)

 conv4_block1_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block1_1_relu[0][0]']

 conv4_block1_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block1_2_conv[0][0]']
 ization)

 conv4_block1_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block1_2_bn[0][0]']
 n)

 conv4_block1_0_conv (Conv2D)   (None, 14, 14, 1024  525312      ['conv3_block8_out[0][0]']
                                )

 conv4_block1_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block1_2_relu[0][0]']
                                )

 conv4_block1_0_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block1_0_conv[0][0]']
 ization)                       )

 conv4_block1_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block1_3_conv[0][0]']
 ization)                       )

 conv4_block1_add (Add)         (None, 14, 14, 1024  0           ['conv4_block1_0_bn[0][0]',
                                )                                 'conv4_block1_3_bn[0][0]']

 conv4_block1_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block1_add[0][0]']
                                )

 conv4_block2_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block1_out[0][0]']

 conv4_block2_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block2_1_conv[0][0]']
 ization)

 conv4_block2_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block2_1_bn[0][0]']
 n)

 conv4_block2_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block2_1_relu[0][0]']

 conv4_block2_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block2_2_conv[0][0]']
 ization)

 conv4_block2_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block2_2_bn[0][0]']
 n)

 conv4_block2_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block2_2_relu[0][0]']
                                )

 conv4_block2_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block2_3_conv[0][0]']
 ization)                       )

 conv4_block2_add (Add)         (None, 14, 14, 1024  0           ['conv4_block1_out[0][0]',
                                )                                 'conv4_block2_3_bn[0][0]']

 conv4_block2_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block2_add[0][0]']
                                )

 conv4_block3_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block2_out[0][0]']

 conv4_block3_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block3_1_conv[0][0]']
 ization)

 conv4_block3_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block3_1_bn[0][0]']
 n)

 conv4_block3_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block3_1_relu[0][0]']

 conv4_block3_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block3_2_conv[0][0]']
 ization)

 conv4_block3_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block3_2_bn[0][0]']
 n)

 conv4_block3_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block3_2_relu[0][0]']
                                )

 conv4_block3_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block3_3_conv[0][0]']
 ization)                       )

 conv4_block3_add (Add)         (None, 14, 14, 1024  0           ['conv4_block2_out[0][0]',
                                )                                 'conv4_block3_3_bn[0][0]']

 conv4_block3_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block3_add[0][0]']
                                )

 conv4_block4_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block3_out[0][0]']

 conv4_block4_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block4_1_conv[0][0]']
 ization)

 conv4_block4_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block4_1_bn[0][0]']
 n)

 conv4_block4_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block4_1_relu[0][0]']

 conv4_block4_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block4_2_conv[0][0]']
 ization)

 conv4_block4_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block4_2_bn[0][0]']
 n)

 conv4_block4_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block4_2_relu[0][0]']
                                )

 conv4_block4_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block4_3_conv[0][0]']
 ization)                       )

 conv4_block4_add (Add)         (None, 14, 14, 1024  0           ['conv4_block3_out[0][0]',
                                )                                 'conv4_block4_3_bn[0][0]']

 conv4_block4_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block4_add[0][0]']
                                )

 conv4_block5_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block4_out[0][0]']

 conv4_block5_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block5_1_conv[0][0]']
 ization)

 conv4_block5_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block5_1_bn[0][0]']
 n)

 conv4_block5_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block5_1_relu[0][0]']

 conv4_block5_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block5_2_conv[0][0]']
 ization)

 conv4_block5_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block5_2_bn[0][0]']
 n)

 conv4_block5_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block5_2_relu[0][0]']
                                )

 conv4_block5_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block5_3_conv[0][0]']
 ization)                       )

 conv4_block5_add (Add)         (None, 14, 14, 1024  0           ['conv4_block4_out[0][0]',
                                )                                 'conv4_block5_3_bn[0][0]']

 conv4_block5_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block5_add[0][0]']
                                )

 conv4_block6_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block5_out[0][0]']

 conv4_block6_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block6_1_conv[0][0]']
 ization)

 conv4_block6_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block6_1_bn[0][0]']
 n)

 conv4_block6_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block6_1_relu[0][0]']

 conv4_block6_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block6_2_conv[0][0]']
 ization)

 conv4_block6_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block6_2_bn[0][0]']
 n)

 conv4_block6_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block6_2_relu[0][0]']
                                )

 conv4_block6_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block6_3_conv[0][0]']
 ization)                       )

 conv4_block6_add (Add)         (None, 14, 14, 1024  0           ['conv4_block5_out[0][0]',
                                )                                 'conv4_block6_3_bn[0][0]']

 conv4_block6_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block6_add[0][0]']
                                )

 conv4_block7_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block6_out[0][0]']

 conv4_block7_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block7_1_conv[0][0]']
 ization)

 conv4_block7_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block7_1_bn[0][0]']
 n)

 conv4_block7_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block7_1_relu[0][0]']

 conv4_block7_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block7_2_conv[0][0]']
 ization)

 conv4_block7_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block7_2_bn[0][0]']
 n)

 conv4_block7_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block7_2_relu[0][0]']
                                )

 conv4_block7_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block7_3_conv[0][0]']
 ization)                       )

 conv4_block7_add (Add)         (None, 14, 14, 1024  0           ['conv4_block6_out[0][0]',
                                )                                 'conv4_block7_3_bn[0][0]']

 conv4_block7_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block7_add[0][0]']
                                )

 conv4_block8_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block7_out[0][0]']

 conv4_block8_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block8_1_conv[0][0]']
 ization)

 conv4_block8_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block8_1_bn[0][0]']
 n)

 conv4_block8_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block8_1_relu[0][0]']

 conv4_block8_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block8_2_conv[0][0]']
 ization)

 conv4_block8_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block8_2_bn[0][0]']
 n)

 conv4_block8_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block8_2_relu[0][0]']
                                )

 conv4_block8_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block8_3_conv[0][0]']
 ization)                       )

 conv4_block8_add (Add)         (None, 14, 14, 1024  0           ['conv4_block7_out[0][0]',
                                )                                 'conv4_block8_3_bn[0][0]']

 conv4_block8_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block8_add[0][0]']
                                )

 conv4_block9_1_conv (Conv2D)   (None, 14, 14, 256)  262400      ['conv4_block8_out[0][0]']

 conv4_block9_1_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block9_1_conv[0][0]']
 ization)

 conv4_block9_1_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block9_1_bn[0][0]']
 n)

 conv4_block9_2_conv (Conv2D)   (None, 14, 14, 256)  590080      ['conv4_block9_1_relu[0][0]']

 conv4_block9_2_bn (BatchNormal  (None, 14, 14, 256)  1024       ['conv4_block9_2_conv[0][0]']
 ization)

 conv4_block9_2_relu (Activatio  (None, 14, 14, 256)  0          ['conv4_block9_2_bn[0][0]']
 n)

 conv4_block9_3_conv (Conv2D)   (None, 14, 14, 1024  263168      ['conv4_block9_2_relu[0][0]']
                                )

 conv4_block9_3_bn (BatchNormal  (None, 14, 14, 1024  4096       ['conv4_block9_3_conv[0][0]']
 ization)                       )

 conv4_block9_add (Add)         (None, 14, 14, 1024  0           ['conv4_block8_out[0][0]',
                                )                                 'conv4_block9_3_bn[0][0]']

 conv4_block9_out (Activation)  (None, 14, 14, 1024  0           ['conv4_block9_add[0][0]']
                                )

 conv4_block10_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block9_out[0][0]']

 conv4_block10_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block10_1_conv[0][0]']
 lization)

 conv4_block10_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block10_1_bn[0][0]']
 on)

 conv4_block10_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block10_1_relu[0][0]']

 conv4_block10_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block10_2_conv[0][0]']
 lization)

 conv4_block10_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block10_2_bn[0][0]']
 on)

 conv4_block10_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block10_2_relu[0][0]']
                                )

 conv4_block10_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block10_3_conv[0][0]']
 lization)                      )

 conv4_block10_add (Add)        (None, 14, 14, 1024  0           ['conv4_block9_out[0][0]',
                                )                                 'conv4_block10_3_bn[0][0]']

 conv4_block10_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block10_add[0][0]']
                                )

 conv4_block11_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block10_out[0][0]']

 conv4_block11_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block11_1_conv[0][0]']
 lization)

 conv4_block11_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block11_1_bn[0][0]']
 on)

 conv4_block11_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block11_1_relu[0][0]']

 conv4_block11_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block11_2_conv[0][0]']
 lization)

 conv4_block11_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block11_2_bn[0][0]']
 on)

 conv4_block11_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block11_2_relu[0][0]']
                                )

 conv4_block11_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block11_3_conv[0][0]']
 lization)                      )

 conv4_block11_add (Add)        (None, 14, 14, 1024  0           ['conv4_block10_out[0][0]',
                                )                                 'conv4_block11_3_bn[0][0]']

 conv4_block11_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block11_add[0][0]']
                                )

 conv4_block12_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block11_out[0][0]']

 conv4_block12_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block12_1_conv[0][0]']
 lization)

 conv4_block12_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block12_1_bn[0][0]']
 on)

 conv4_block12_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block12_1_relu[0][0]']

 conv4_block12_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block12_2_conv[0][0]']
 lization)

 conv4_block12_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block12_2_bn[0][0]']
 on)

 conv4_block12_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block12_2_relu[0][0]']
                                )

 conv4_block12_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block12_3_conv[0][0]']
 lization)                      )

 conv4_block12_add (Add)        (None, 14, 14, 1024  0           ['conv4_block11_out[0][0]',
                                )                                 'conv4_block12_3_bn[0][0]']

 conv4_block12_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block12_add[0][0]']
                                )

 conv4_block13_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block12_out[0][0]']

 conv4_block13_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block13_1_conv[0][0]']
 lization)

 conv4_block13_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block13_1_bn[0][0]']
 on)

 conv4_block13_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block13_1_relu[0][0]']

 conv4_block13_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block13_2_conv[0][0]']
 lization)

 conv4_block13_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block13_2_bn[0][0]']
 on)

 conv4_block13_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block13_2_relu[0][0]']
                                )

 conv4_block13_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block13_3_conv[0][0]']
 lization)                      )

 conv4_block13_add (Add)        (None, 14, 14, 1024  0           ['conv4_block12_out[0][0]',
                                )                                 'conv4_block13_3_bn[0][0]']

 conv4_block13_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block13_add[0][0]']
                                )

 conv4_block14_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block13_out[0][0]']

 conv4_block14_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block14_1_conv[0][0]']
 lization)

 conv4_block14_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block14_1_bn[0][0]']
 on)

 conv4_block14_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block14_1_relu[0][0]']

 conv4_block14_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block14_2_conv[0][0]']
 lization)

 conv4_block14_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block14_2_bn[0][0]']
 on)

 conv4_block14_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block14_2_relu[0][0]']
                                )

 conv4_block14_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block14_3_conv[0][0]']
 lization)                      )

 conv4_block14_add (Add)        (None, 14, 14, 1024  0           ['conv4_block13_out[0][0]',
                                )                                 'conv4_block14_3_bn[0][0]']

 conv4_block14_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block14_add[0][0]']
                                )

 conv4_block15_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block14_out[0][0]']

 conv4_block15_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block15_1_conv[0][0]']
 lization)

 conv4_block15_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block15_1_bn[0][0]']
 on)

 conv4_block15_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block15_1_relu[0][0]']

 conv4_block15_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block15_2_conv[0][0]']
 lization)

 conv4_block15_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block15_2_bn[0][0]']
 on)

 conv4_block15_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block15_2_relu[0][0]']
                                )

 conv4_block15_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block15_3_conv[0][0]']
 lization)                      )

 conv4_block15_add (Add)        (None, 14, 14, 1024  0           ['conv4_block14_out[0][0]',
                                )                                 'conv4_block15_3_bn[0][0]']

 conv4_block15_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block15_add[0][0]']
                                )

 conv4_block16_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block15_out[0][0]']

 conv4_block16_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block16_1_conv[0][0]']
 lization)

 conv4_block16_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block16_1_bn[0][0]']
 on)

 conv4_block16_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block16_1_relu[0][0]']

 conv4_block16_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block16_2_conv[0][0]']
 lization)

 conv4_block16_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block16_2_bn[0][0]']
 on)

 conv4_block16_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block16_2_relu[0][0]']
                                )

 conv4_block16_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block16_3_conv[0][0]']
 lization)                      )

 conv4_block16_add (Add)        (None, 14, 14, 1024  0           ['conv4_block15_out[0][0]',
                                )                                 'conv4_block16_3_bn[0][0]']

 conv4_block16_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block16_add[0][0]']
                                )

 conv4_block17_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block16_out[0][0]']

 conv4_block17_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block17_1_conv[0][0]']
 lization)

 conv4_block17_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block17_1_bn[0][0]']
 on)

 conv4_block17_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block17_1_relu[0][0]']

 conv4_block17_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block17_2_conv[0][0]']
 lization)

 conv4_block17_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block17_2_bn[0][0]']
 on)

 conv4_block17_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block17_2_relu[0][0]']
                                )

 conv4_block17_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block17_3_conv[0][0]']
 lization)                      )

 conv4_block17_add (Add)        (None, 14, 14, 1024  0           ['conv4_block16_out[0][0]',
                                )                                 'conv4_block17_3_bn[0][0]']

 conv4_block17_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block17_add[0][0]']
                                )

 conv4_block18_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block17_out[0][0]']

 conv4_block18_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block18_1_conv[0][0]']
 lization)

 conv4_block18_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block18_1_bn[0][0]']
 on)

 conv4_block18_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block18_1_relu[0][0]']

 conv4_block18_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block18_2_conv[0][0]']
 lization)

 conv4_block18_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block18_2_bn[0][0]']
 on)

 conv4_block18_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block18_2_relu[0][0]']
                                )

 conv4_block18_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block18_3_conv[0][0]']
 lization)                      )

 conv4_block18_add (Add)        (None, 14, 14, 1024  0           ['conv4_block17_out[0][0]',
                                )                                 'conv4_block18_3_bn[0][0]']

 conv4_block18_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block18_add[0][0]']
                                )

 conv4_block19_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block18_out[0][0]']

 conv4_block19_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block19_1_conv[0][0]']
 lization)

 conv4_block19_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block19_1_bn[0][0]']
 on)

 conv4_block19_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block19_1_relu[0][0]']

 conv4_block19_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block19_2_conv[0][0]']
 lization)

 conv4_block19_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block19_2_bn[0][0]']
 on)

 conv4_block19_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block19_2_relu[0][0]']
                                )

 conv4_block19_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block19_3_conv[0][0]']
 lization)                      )

 conv4_block19_add (Add)        (None, 14, 14, 1024  0           ['conv4_block18_out[0][0]',
                                )                                 'conv4_block19_3_bn[0][0]']

 conv4_block19_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block19_add[0][0]']
                                )

 conv4_block20_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block19_out[0][0]']

 conv4_block20_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block20_1_conv[0][0]']
 lization)

 conv4_block20_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block20_1_bn[0][0]']
 on)

 conv4_block20_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block20_1_relu[0][0]']

 conv4_block20_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block20_2_conv[0][0]']
 lization)

 conv4_block20_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block20_2_bn[0][0]']
 on)

 conv4_block20_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block20_2_relu[0][0]']
                                )

 conv4_block20_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block20_3_conv[0][0]']
 lization)                      )

 conv4_block20_add (Add)        (None, 14, 14, 1024  0           ['conv4_block19_out[0][0]',
                                )                                 'conv4_block20_3_bn[0][0]']

 conv4_block20_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block20_add[0][0]']
                                )

 conv4_block21_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block20_out[0][0]']

 conv4_block21_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block21_1_conv[0][0]']
 lization)

 conv4_block21_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block21_1_bn[0][0]']
 on)

 conv4_block21_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block21_1_relu[0][0]']

 conv4_block21_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block21_2_conv[0][0]']
 lization)

 conv4_block21_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block21_2_bn[0][0]']
 on)

 conv4_block21_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block21_2_relu[0][0]']
                                )

 conv4_block21_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block21_3_conv[0][0]']
 lization)                      )

 conv4_block21_add (Add)        (None, 14, 14, 1024  0           ['conv4_block20_out[0][0]',
                                )                                 'conv4_block21_3_bn[0][0]']

 conv4_block21_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block21_add[0][0]']
                                )

 conv4_block22_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block21_out[0][0]']

 conv4_block22_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block22_1_conv[0][0]']
 lization)

 conv4_block22_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block22_1_bn[0][0]']
 on)

 conv4_block22_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block22_1_relu[0][0]']

 conv4_block22_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block22_2_conv[0][0]']
 lization)

 conv4_block22_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block22_2_bn[0][0]']
 on)

 conv4_block22_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block22_2_relu[0][0]']
                                )

 conv4_block22_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block22_3_conv[0][0]']
 lization)                      )

 conv4_block22_add (Add)        (None, 14, 14, 1024  0           ['conv4_block21_out[0][0]',
                                )                                 'conv4_block22_3_bn[0][0]']

 conv4_block22_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block22_add[0][0]']
                                )

 conv4_block23_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block22_out[0][0]']

 conv4_block23_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block23_1_conv[0][0]']
 lization)

 conv4_block23_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block23_1_bn[0][0]']
 on)

 conv4_block23_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block23_1_relu[0][0]']

 conv4_block23_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block23_2_conv[0][0]']
 lization)

 conv4_block23_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block23_2_bn[0][0]']
 on)

 conv4_block23_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block23_2_relu[0][0]']
                                )

 conv4_block23_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block23_3_conv[0][0]']
 lization)                      )

 conv4_block23_add (Add)        (None, 14, 14, 1024  0           ['conv4_block22_out[0][0]',
                                )                                 'conv4_block23_3_bn[0][0]']

 conv4_block23_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block23_add[0][0]']
                                )

 conv4_block24_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block23_out[0][0]']

 conv4_block24_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block24_1_conv[0][0]']
 lization)

 conv4_block24_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block24_1_bn[0][0]']
 on)

 conv4_block24_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block24_1_relu[0][0]']

 conv4_block24_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block24_2_conv[0][0]']
 lization)

 conv4_block24_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block24_2_bn[0][0]']
 on)

 conv4_block24_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block24_2_relu[0][0]']
                                )

 conv4_block24_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block24_3_conv[0][0]']
 lization)                      )

 conv4_block24_add (Add)        (None, 14, 14, 1024  0           ['conv4_block23_out[0][0]',
                                )                                 'conv4_block24_3_bn[0][0]']

 conv4_block24_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block24_add[0][0]']
                                )

 conv4_block25_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block24_out[0][0]']

 conv4_block25_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block25_1_conv[0][0]']
 lization)

 conv4_block25_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block25_1_bn[0][0]']
 on)

 conv4_block25_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block25_1_relu[0][0]']

 conv4_block25_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block25_2_conv[0][0]']
 lization)

 conv4_block25_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block25_2_bn[0][0]']
 on)

 conv4_block25_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block25_2_relu[0][0]']
                                )

 conv4_block25_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block25_3_conv[0][0]']
 lization)                      )

 conv4_block25_add (Add)        (None, 14, 14, 1024  0           ['conv4_block24_out[0][0]',
                                )                                 'conv4_block25_3_bn[0][0]']

 conv4_block25_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block25_add[0][0]']
                                )

 conv4_block26_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block25_out[0][0]']

 conv4_block26_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block26_1_conv[0][0]']
 lization)

 conv4_block26_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block26_1_bn[0][0]']
 on)

 conv4_block26_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block26_1_relu[0][0]']

 conv4_block26_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block26_2_conv[0][0]']
 lization)

 conv4_block26_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block26_2_bn[0][0]']
 on)

 conv4_block26_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block26_2_relu[0][0]']
                                )

 conv4_block26_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block26_3_conv[0][0]']
 lization)                      )

 conv4_block26_add (Add)        (None, 14, 14, 1024  0           ['conv4_block25_out[0][0]',
                                )                                 'conv4_block26_3_bn[0][0]']

 conv4_block26_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block26_add[0][0]']
                                )

 conv4_block27_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block26_out[0][0]']

 conv4_block27_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block27_1_conv[0][0]']
 lization)

 conv4_block27_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block27_1_bn[0][0]']
 on)

 conv4_block27_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block27_1_relu[0][0]']

 conv4_block27_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block27_2_conv[0][0]']
 lization)

 conv4_block27_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block27_2_bn[0][0]']
 on)

 conv4_block27_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block27_2_relu[0][0]']
                                )

 conv4_block27_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block27_3_conv[0][0]']
 lization)                      )

 conv4_block27_add (Add)        (None, 14, 14, 1024  0           ['conv4_block26_out[0][0]',
                                )                                 'conv4_block27_3_bn[0][0]']

 conv4_block27_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block27_add[0][0]']
                                )

 conv4_block28_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block27_out[0][0]']

 conv4_block28_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block28_1_conv[0][0]']
 lization)

 conv4_block28_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block28_1_bn[0][0]']
 on)

 conv4_block28_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block28_1_relu[0][0]']

 conv4_block28_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block28_2_conv[0][0]']
 lization)

 conv4_block28_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block28_2_bn[0][0]']
 on)

 conv4_block28_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block28_2_relu[0][0]']
                                )

 conv4_block28_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block28_3_conv[0][0]']
 lization)                      )

 conv4_block28_add (Add)        (None, 14, 14, 1024  0           ['conv4_block27_out[0][0]',
                                )                                 'conv4_block28_3_bn[0][0]']

 conv4_block28_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block28_add[0][0]']
                                )

 conv4_block29_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block28_out[0][0]']

 conv4_block29_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block29_1_conv[0][0]']
 lization)

 conv4_block29_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block29_1_bn[0][0]']
 on)

 conv4_block29_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block29_1_relu[0][0]']

 conv4_block29_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block29_2_conv[0][0]']
 lization)

 conv4_block29_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block29_2_bn[0][0]']
 on)

 conv4_block29_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block29_2_relu[0][0]']
                                )

 conv4_block29_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block29_3_conv[0][0]']
 lization)                      )

 conv4_block29_add (Add)        (None, 14, 14, 1024  0           ['conv4_block28_out[0][0]',
                                )                                 'conv4_block29_3_bn[0][0]']

 conv4_block29_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block29_add[0][0]']
                                )

 conv4_block30_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block29_out[0][0]']

 conv4_block30_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block30_1_conv[0][0]']
 lization)

 conv4_block30_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block30_1_bn[0][0]']
 on)

 conv4_block30_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block30_1_relu[0][0]']

 conv4_block30_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block30_2_conv[0][0]']
 lization)

 conv4_block30_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block30_2_bn[0][0]']
 on)

 conv4_block30_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block30_2_relu[0][0]']
                                )

 conv4_block30_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block30_3_conv[0][0]']
 lization)                      )

 conv4_block30_add (Add)        (None, 14, 14, 1024  0           ['conv4_block29_out[0][0]',
                                )                                 'conv4_block30_3_bn[0][0]']

 conv4_block30_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block30_add[0][0]']
                                )

 conv4_block31_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block30_out[0][0]']

 conv4_block31_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block31_1_conv[0][0]']
 lization)

 conv4_block31_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block31_1_bn[0][0]']
 on)

 conv4_block31_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block31_1_relu[0][0]']

 conv4_block31_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block31_2_conv[0][0]']
 lization)

 conv4_block31_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block31_2_bn[0][0]']
 on)

 conv4_block31_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block31_2_relu[0][0]']
                                )

 conv4_block31_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block31_3_conv[0][0]']
 lization)                      )

 conv4_block31_add (Add)        (None, 14, 14, 1024  0           ['conv4_block30_out[0][0]',
                                )                                 'conv4_block31_3_bn[0][0]']

 conv4_block31_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block31_add[0][0]']
                                )

 conv4_block32_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block31_out[0][0]']

 conv4_block32_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block32_1_conv[0][0]']
 lization)

 conv4_block32_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block32_1_bn[0][0]']
 on)

 conv4_block32_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block32_1_relu[0][0]']

 conv4_block32_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block32_2_conv[0][0]']
 lization)

 conv4_block32_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block32_2_bn[0][0]']
 on)

 conv4_block32_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block32_2_relu[0][0]']
                                )

 conv4_block32_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block32_3_conv[0][0]']
 lization)                      )

 conv4_block32_add (Add)        (None, 14, 14, 1024  0           ['conv4_block31_out[0][0]',
                                )                                 'conv4_block32_3_bn[0][0]']

 conv4_block32_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block32_add[0][0]']
                                )

 conv4_block33_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block32_out[0][0]']

 conv4_block33_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block33_1_conv[0][0]']
 lization)

 conv4_block33_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block33_1_bn[0][0]']
 on)

 conv4_block33_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block33_1_relu[0][0]']

 conv4_block33_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block33_2_conv[0][0]']
 lization)

 conv4_block33_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block33_2_bn[0][0]']
 on)

 conv4_block33_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block33_2_relu[0][0]']
                                )

 conv4_block33_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block33_3_conv[0][0]']
 lization)                      )

 conv4_block33_add (Add)        (None, 14, 14, 1024  0           ['conv4_block32_out[0][0]',
                                )                                 'conv4_block33_3_bn[0][0]']

 conv4_block33_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block33_add[0][0]']
                                )

 conv4_block34_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block33_out[0][0]']

 conv4_block34_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block34_1_conv[0][0]']
 lization)

 conv4_block34_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block34_1_bn[0][0]']
 on)

 conv4_block34_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block34_1_relu[0][0]']

 conv4_block34_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block34_2_conv[0][0]']
 lization)

 conv4_block34_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block34_2_bn[0][0]']
 on)

 conv4_block34_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block34_2_relu[0][0]']
                                )

 conv4_block34_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block34_3_conv[0][0]']
 lization)                      )

 conv4_block34_add (Add)        (None, 14, 14, 1024  0           ['conv4_block33_out[0][0]',
                                )                                 'conv4_block34_3_bn[0][0]']

 conv4_block34_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block34_add[0][0]']
                                )

 conv4_block35_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block34_out[0][0]']

 conv4_block35_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block35_1_conv[0][0]']
 lization)

 conv4_block35_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block35_1_bn[0][0]']
 on)

 conv4_block35_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block35_1_relu[0][0]']

 conv4_block35_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block35_2_conv[0][0]']
 lization)

 conv4_block35_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block35_2_bn[0][0]']
 on)

 conv4_block35_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block35_2_relu[0][0]']
                                )

 conv4_block35_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block35_3_conv[0][0]']
 lization)                      )

 conv4_block35_add (Add)        (None, 14, 14, 1024  0           ['conv4_block34_out[0][0]',
                                )                                 'conv4_block35_3_bn[0][0]']

 conv4_block35_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block35_add[0][0]']
                                )

 conv4_block36_1_conv (Conv2D)  (None, 14, 14, 256)  262400      ['conv4_block35_out[0][0]']

 conv4_block36_1_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block36_1_conv[0][0]']
 lization)

 conv4_block36_1_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block36_1_bn[0][0]']
 on)

 conv4_block36_2_conv (Conv2D)  (None, 14, 14, 256)  590080      ['conv4_block36_1_relu[0][0]']

 conv4_block36_2_bn (BatchNorma  (None, 14, 14, 256)  1024       ['conv4_block36_2_conv[0][0]']
 lization)

 conv4_block36_2_relu (Activati  (None, 14, 14, 256)  0          ['conv4_block36_2_bn[0][0]']
 on)

 conv4_block36_3_conv (Conv2D)  (None, 14, 14, 1024  263168      ['conv4_block36_2_relu[0][0]']
                                )

 conv4_block36_3_bn (BatchNorma  (None, 14, 14, 1024  4096       ['conv4_block36_3_conv[0][0]']
 lization)                      )

 conv4_block36_add (Add)        (None, 14, 14, 1024  0           ['conv4_block35_out[0][0]',
                                )                                 'conv4_block36_3_bn[0][0]']

 conv4_block36_out (Activation)  (None, 14, 14, 1024  0          ['conv4_block36_add[0][0]']
                                )

 conv5_block1_1_conv (Conv2D)   (None, 7, 7, 512)    524800      ['conv4_block36_out[0][0]']

 conv5_block1_1_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block1_1_conv[0][0]']
 ization)

 conv5_block1_1_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block1_1_bn[0][0]']
 n)

 conv5_block1_2_conv (Conv2D)   (None, 7, 7, 512)    2359808     ['conv5_block1_1_relu[0][0]']

 conv5_block1_2_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block1_2_conv[0][0]']
 ization)

 conv5_block1_2_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block1_2_bn[0][0]']
 n)

 conv5_block1_0_conv (Conv2D)   (None, 7, 7, 2048)   2099200     ['conv4_block36_out[0][0]']

 conv5_block1_3_conv (Conv2D)   (None, 7, 7, 2048)   1050624     ['conv5_block1_2_relu[0][0]']

 conv5_block1_0_bn (BatchNormal  (None, 7, 7, 2048)  8192        ['conv5_block1_0_conv[0][0]']
 ization)

 conv5_block1_3_bn (BatchNormal  (None, 7, 7, 2048)  8192        ['conv5_block1_3_conv[0][0]']
 ization)

 conv5_block1_add (Add)         (None, 7, 7, 2048)   0           ['conv5_block1_0_bn[0][0]',
                                                                  'conv5_block1_3_bn[0][0]']

 conv5_block1_out (Activation)  (None, 7, 7, 2048)   0           ['conv5_block1_add[0][0]']

 conv5_block2_1_conv (Conv2D)   (None, 7, 7, 512)    1049088     ['conv5_block1_out[0][0]']

 conv5_block2_1_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block2_1_conv[0][0]']
 ization)

 conv5_block2_1_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block2_1_bn[0][0]']
 n)

 conv5_block2_2_conv (Conv2D)   (None, 7, 7, 512)    2359808     ['conv5_block2_1_relu[0][0]']

 conv5_block2_2_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block2_2_conv[0][0]']
 ization)

 conv5_block2_2_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block2_2_bn[0][0]']
 n)

 conv5_block2_3_conv (Conv2D)   (None, 7, 7, 2048)   1050624     ['conv5_block2_2_relu[0][0]']

 conv5_block2_3_bn (BatchNormal  (None, 7, 7, 2048)  8192        ['conv5_block2_3_conv[0][0]']
 ization)

 conv5_block2_add (Add)         (None, 7, 7, 2048)   0           ['conv5_block1_out[0][0]',
                                                                  'conv5_block2_3_bn[0][0]']

 conv5_block2_out (Activation)  (None, 7, 7, 2048)   0           ['conv5_block2_add[0][0]']

 conv5_block3_1_conv (Conv2D)   (None, 7, 7, 512)    1049088     ['conv5_block2_out[0][0]']

 conv5_block3_1_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block3_1_conv[0][0]']
 ization)

 conv5_block3_1_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block3_1_bn[0][0]']
 n)

 conv5_block3_2_conv (Conv2D)   (None, 7, 7, 512)    2359808     ['conv5_block3_1_relu[0][0]']

 conv5_block3_2_bn (BatchNormal  (None, 7, 7, 512)   2048        ['conv5_block3_2_conv[0][0]']
 ization)

 conv5_block3_2_relu (Activatio  (None, 7, 7, 512)   0           ['conv5_block3_2_bn[0][0]']
 n)

 conv5_block3_3_conv (Conv2D)   (None, 7, 7, 2048)   1050624     ['conv5_block3_2_relu[0][0]']

 conv5_block3_3_bn (BatchNormal  (None, 7, 7, 2048)  8192        ['conv5_block3_3_conv[0][0]']
 ization)

 conv5_block3_add (Add)         (None, 7, 7, 2048)   0           ['conv5_block2_out[0][0]',
                                                                  'conv5_block3_3_bn[0][0]']

 conv5_block3_out (Activation)  (None, 7, 7, 2048)   0           ['conv5_block3_add[0][0]']

 avg_pool (GlobalAveragePooling  (None, 2048)        0           ['conv5_block3_out[0][0]']
 2D)

 predictions (Dense)            (None, 1000)         2049000     ['avg_pool[0][0]']

===============================================================================================
Total params: 60,419,944
Trainable params: 60,268,520
Non-trainable params: 151,424
 ```

## Result :
>> I give three random images to model to predict the label. 
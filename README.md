# Social-Distancing-Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This programme checks for social distancing between pedestrians in a COVID-ridden world.


Ackermann Steering

<p align="center">
  <img height="500" src="Images/social_distancing_gif.gif">
</p>

## Author

 - Govind Ajith Kumar

## Device and OS

 - The code was developed on a 2019 Razer Blade 15 .</br>
 - Windows 10

Please ensure the following packages are installed:
--

 - Tensorflow 2.3.1 (GPU Version for faster training)
 - CUDA 10.1
 - cudnn v7.6.5 for cuda 10.1
## For using your own Custom Dataset:


Clone [this repository](https://github.com/tzutalin/labelImg) to download the labelImg software which enables you to build custom dataset.

Prerequisites for this

    conda install pyqt=5
    pyrcc5 -o resources.py resources.qrc
    Transfer resources.py and resources.qrc into the resources folder

Execute using 

`python labelImg.py`

## For using the Caltech dataset:

Download dataset from : http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/

Create a directory structure in the format
--

    startdt_data
      caltech_pedestrian_dataset
        annotations
        set01
        .
        .
          <contains all the .vbb files>
      set01
      .
      .
      .
        <contains all the .seq files>

run `python vbb2voc.py`

The above code generated xml files in startdt_data\caltech_pedestrian_dataset\annotations\set01 and extracts the jpeg images from .seq and pastes them into /caltech_pedestrian_dataset/set01/frame

I've saved in XML filetype.

Switch to tools folder
--

Execute XML_to_YOLOv3.py
--

This Creates 3 text files under the Text_Files folder

Change necessary configurations by setting up configs.py

Run `train.py`

Visualize results on Video
--

Run on Custom video by inserting the video in path and run the detection file. Tested on [this video](https://www.youtube.com/watch?v=GJNjaRJWVP8).

Run `detection_custom.py`

Checking Tensorflow graphs
--

Check the graphs using : `tensorboard --logdir=log`


## Current status 

I am working on improving the training weights. The entire project will be linked here when the weights are retrained.</br>
For now, you can find the [download here](https://drive.google.com/file/d/1eMx6QdkupcESgp3kGyUqns2y0M5iAJev/view?usp=sharing).

Make sure the directory structure is as follows: 

    Social Distancing
    |_labelimg
    |_startdt_data (as explained above)
    |_Tensorflow_Folder_that_you_just_downloaded
    |_vbb2voc.py

## Credits

The YOLOV3 repository was inspried and drawn from the work done [here] (https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3).</br>
Thanks to [this](https://github.com/Ashwini-Analytics/Pedestrian-Detection-using-Darkflow) and [this](https://github.com/CasiaFan/Dataset_to_VOC_converter) repository for the vbb2voc file.

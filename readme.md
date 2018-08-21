# Tensorflow object detection - Custom object detector

Hi, This is about custom object detector using tensorflow object detection API. In this project trying to detect batman apperance. Please refer step by step.

![Result](/results/result1.png)

![Result](/results/result2.png)

## Preparing resources for tensorflow custom object detection.

1. Download the images of the object what you want to detect.
2. Download the [tensorflow models](https://github.com/tensorflow/models) repo and do installation steps in which is given at [object detection](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md).

## Labeling image and exporting csv

1. Labeling image is main the process of object detection. It is the process of adding bounding boxes to the objects in the images.

2. In this project [Colabeler](http://www.colabeler.com) used for image labeling.

3. After Labeled images the folder structure images have all the images. The subdirectory train and test have the xml files. The folder structure was given below. Create folder named data also in main folder.

	```
	Pre Processing
	|
	└───/images
	│   │   // All images present()
	│   │
	│   └───/train
	│   │   	// .xml files of train images 
	│   │
	│   └───/test 
	│		  	// .xml files of test images
	|
	└───/data
	│		// The exported data folder
	│   
	└─── xml_to_csv.py
	│   
	└─── generate_tfrecord.py
	```

4. Execute the xml\_to\_csv.py file. It will create the test.csv and train.csv inside the data folder.

## Create tf records

1. Before creating tf record change the lable row\_label to repected class at line 30 in generate_tfrecord.py. Here I have one object so I changed the label as 'batman'

2. After changing line execute generate_tfrecord.py. It will create the test.record and train.record inside the data folder.

## Create .pbtxt(label map) file

The label map file will contain the labels and ids of the object. In this case the object was only one. So the pbtxt file have label for only one object.

## Create .config file

1. The creation of .config file for explained in this [link](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/configuring_jobs.md).

2. To complete this process the .ckpt file also needed. In this case .ckpt inherited from [ssd\_mobilenet\_v1\_coco\_2017\_11\_17](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz). Download the model and move it to object\_detection folder
 
3. Please also refer batman.config file. Here paths need to be changed for "input\_path" and "label\_map\_path" for both test and train and "fine\_tune\_checkpoint" path to .ckpt file path".



## Final folder structure

1. Open tensorflow models directory and execute following commands.

	```
	# From tensorflow/models/research/
	protoc object_detection/protos/*.proto --python_out=.
	
	# From tensorflow/models/research/
	export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim 
	
	```

2. Now move the .pbtxt, .records and .csv files to /research/object_detection/data

3. split images as train and evol folder and move it to /research/object_detection/models/model folder. Also move .config file also to this folder.

4. The final folder structure as follows.

	```
	object_detection
	|
	└───/data
	│   │   
	│   └─── .pbtxt file
	│   └─── test.record 
	│   └─── train.record 
	│   └─── test.csv
	│   └─── train.csv 
	|
	└───/models
	│	│
	│	└───/model
	│	│	│
	│	│	└───/train
	│	│	│	// Trainning Images
	│	│	└───/eval
	│	│	│	// Test Images
	│	│	└─── .config file
	│	│
	│       └─── Other Files
	│
	└───/ssd_mobilenet_v1_coco_2017_11_17
	│	    │
	│	    └─── model.ckpt
	│	    │
	│	    └─── Other files
	│   
	└─── Other folders and files
	```


## Trainning a model

Move to object\_detection folder in terminal and execute following command in terminal.

```
python model_main.py --pipeline_config_path=models/model/{NAME_OF_CONFIG_FILE}.config --model_dir=models/model --num_train_steps={NUMBER_OF_TRAINNING_STEP} --num_eval_steps={NUMBER_OF_TEST_STEP} --alsologtostderr
```

Above command will train model locally. If want to train in cloud please refer [docs](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_cloud.md)

The trainned model will be available at "object\_detection/models/model" folder.

## Export Frozen Graph

To export frozen_inference\_graph.pb file execute following commad.

	python export_inference_graph.py --input_type image_tensor --pipeline_config_path models/model/{CONFIG_FILE_NAME}.config --trained_checkpoint_prefix models/model/model.ckpt-{NUMBER} --output_directory {EXPORT_DIRECTORY_PATH}
	
## Run and test model

1. Open jupyter notebook.

2. Open "object\_detection\_tutorial.ipynb".

3. Change MODEL\_NAME and PATH\_TO\_FROZEN\_GRAPH.
.
4. Remove download codes for DOWNLOAD\_BASE

5. Add images for test in the "test\_images" folder and chand TEST\_IMAGE\_PATHS

6. Run cells.

## Refences

1. [Tensorflow object detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)

	

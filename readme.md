# Average-food-calorie-estimation-using-YOLOv3

Project based on deep learning that can detect food items from the image and calculate average calorie from image or video and prints it on the console and image.

This model is trained on YOLOv3 object detection algorithm which is implimanted by ultralytics using pytorch. for more information about training your own model and requirements you can refer original repo. link to the repo is : https://github.com/ultralytics/yolov3 

Data directory contains images with labels in yolo format as shown in table
| Food Name|Number of images |
|:------|:----------------:|
|Apple|117|
|Banana|90|
|Carrot|55|
|Egg|108|
|Kiwi|76|
|Mango|60|
|Orange|84|
|Pomegranate|76|
|Tomato|79|
|Indian one rupee Coin|64|

This images are downloded either from goolge open image dataset or scraped from google or captured from mobile.

For simply detecting the calorie in image you can run with these line with the pretrained weights

### In Linux
python3 detect.py --cfg 'cfg/yolov3.cfg' --names 'cfg/food.names' --weights 'weights/last.pt' --source 'test/'

### In Windows
python detect.py --cfg 'cfg/yolov3.cfg' --names 'cfg/food.names' --weights 'weights/last.pt' --source 'test/'

where test directory contain the your source images or you can use **--source 0** which will use your camera in real time.
For more information about detect.py parameters you can refer to detect.py file which contains imformation about all parameters.

If you need weights file then open an issue then I will provide google drive link.
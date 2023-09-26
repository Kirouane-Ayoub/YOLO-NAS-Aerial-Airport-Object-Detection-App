# Project Title: YOLO-NAS Aerial Airport Object Detection App

## Description:
This project utilizes the **YOLO-NAS** (You Only Look Once - Neural Architecture Search) model to perform real-time object detection on aerial images from the **GDIT Aerial Airport** dataset. **YOLO-NAS** is a cutting-edge object detection model developed by **Deci-AI**, known for its remarkable trade-off between accuracy and latency.

## Model:

+ **Name**: YOLO-NAS
+ **Description**: YOLO-NAS is a novel object detection model based on the YOLO framework. It employs a proprietary neural architecture search algorithm, AutoNAC™, to automatically discover the most optimal architecture for object detection on the given dataset.
+ **Performance**: YOLO-NAS has demonstrated superior performance on various datasets, including COCO and ImageNet, making it a top choice for real-time object detection tasks.

## Dataset:

+ **Name**: GDIT Aerial Airport dataset
+ **Description**: This dataset consists of aerial images containing instances of parked airplanes at various airports. It is specifically curated for airplane detection tasks.
+ **Classes**: All airplane types have been grouped into a single classification named **airplane**.
+ **https://universe.roboflow.com/gdit/aerial-airport**

## Limitations:

+ **Limited to Airplane Detection**: YOLO-NAS is designed for detecting airplanes in aerial images and may not perform optimally on other object detection tasks.
+ **Hardware Requirements**: The model's real-time capabilities may require powerful hardware for efficient inference.
+ **Accuracy Trade-off**: While YOLO-NAS offers a balance between accuracy and latency, there may still be limitations in extremely high-precision scenarios.

## Use Cases:

+ **Airport Security**: Enhance airport security by automating the monitoring of parked airplanes.
+ **Aircraft Maintenance**: Assist in aircraft maintenance by identifying parked airplanes for inspection.
+ **Traffic Management**: Aid in efficient traffic management at airports.
+ **Research**: Support research in aviation and transportation.

## Ethical Considerations:

+ **Privacy**: Ensure that the app is used responsibly to respect privacy and not capture individuals or sensitive information in the images.
+ **Bias**: Be vigilant against bias in object detection results, which may have consequences in airport security.
+ **Data Security**: Protect the dataset and user data to prevent misuse or breaches.
+ **Transparency**: Clearly communicate the purpose and capabilities of the app to users and stakeholders.

## Usage : 
```
pip install -r requirements.txt
python download_weights.py 
python app.py
```
+ You can Check The Demo from here : **https://huggingface.co/spaces/ayoubkirouane/Aerial-Airport-YOLO-Nas_Object-Detection**

![Screenshot at 2023-09-26 17-18-10](https://github.com/Kirouane-Ayoub/YOLO-NAS-Aerial-Airport-Object-Detection-App/assets/99510125/f3b4d46d-422d-42ce-a99d-5a4fbd3b10b3)

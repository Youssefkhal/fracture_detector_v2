# Fracture Detector Dataset

This dataset is used to train and test the YOLOv5 model in the Fracture Detector v2 project.
It consists of medical images annotated for fracture detection.

🔗 Dataset Google Drive Link:
https://drive.google.com/drive/folders/15bUxugOmW3hWJ4QJ-Nosuh9UmPSaT8bm?usp=sharing
![image](https://github.com/user-attachments/assets/92869140-4ba9-4339-83ce-d8876cf74be0)
![image](https://github.com/user-attachments/assets/8ff0cbc0-f762-4582-a2b4-e0b30c0f65c7)
![image](https://github.com/user-attachments/assets/f43808c6-73ef-4238-840d-df6c5de15716)
![image](https://github.com/user-attachments/assets/0db774ba-b02c-4dbc-8a6a-72d636be5552)
![image](https://github.com/user-attachments/assets/830e66c3-4def-48fe-9d07-e979a8f0e140)


## 📁 Dataset Structure

The folder contains:

- `images/` – Original X-ray or medical images.
- `labels/` – YOLO-formatted annotation files for each image.
- `train/` and `val/` – Subfolders for training and validation splits.
- `data.yaml` – YOLOv5 data configuration file with class names and dataset paths.

## 🏷️ Label Format

The labels follow YOLOv5 format:
<class_id> <x_center> <y_center> <width> <height>
All coordinates are normalized between 0 and 1.

## 👨‍⚕️ Use Case

This dataset was curated to detect bone fractures from X-ray images using YOLOv5. Each image is annotated with bounding boxes around fracture regions.

## 📌 Note

- The dataset is intended for educational and research use only.

## 🧠 Related Project

GitHub Repository:  
https://github.com/Youssefkhal/fracture_detector_v2

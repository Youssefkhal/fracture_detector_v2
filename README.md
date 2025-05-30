# Fracture Detector Dataset

This dataset is used to train and test the YOLOv5 model in the Fracture Detector v2 project.
It consists of medical images annotated for fracture detection.

🔗 Dataset Google Drive Link:
https://drive.google.com/drive/folders/15bUxugOmW3hWJ4QJ-Nosuh9UmPSaT8bm?usp=sharing
![image](https://github.com/user-attachments/assets/1abe9a0e-b9ee-4c74-9801-d5fc4f16fd66)
![image](https://github.com/user-attachments/assets/51833051-f338-48b8-8bb0-1813479f39a0)
![image](https://github.com/user-attachments/assets/f45df798-ad53-45c4-998c-3e5b2af3992d)
![image](https://github.com/user-attachments/assets/a25facb6-8888-4d98-b2d0-7892004bc043)

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

from flask import Flask, request, render_template
import torch
import cv2
import os

app = Flask(__name__)
model = torch.hub.load('.', 'custom', path='runs/train/exp3/weights/best.pt', source='local')

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/uploads2'

@app.route('/', methods=['GET', 'POST'])
def index():
    result_image = None
    user_image = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            img = cv2.imread(filepath)
            results = model(img)

            annotated_img = results.render()[0]
            result_filename = 'result_' + filename
            result_path = os.path.join(RESULT_FOLDER, result_filename)
            cv2.imwrite(result_path, annotated_img)

            user_image = 'uploads/' + filename
            result_image = 'uploads2/' + result_filename

    return render_template('index.html', user_image=user_image, result_image=result_image)


if __name__ == '__main__':
    app.run(debug=True)

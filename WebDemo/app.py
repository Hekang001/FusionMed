from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = "请输入正确的文本和图像"
    image_url = None
    if request.method == 'POST':
        # 获取输入文本
        input_text = request.form.get('input_text', '')
        # 在这里改输出文本
        output_text = 'The chest X-ray shows clear lung fields, a normal cardiac silhouette, and no visible abnormalities in the bones or soft tissues. No signs of pneumothorax, consolidation, or pleural effusion are present. The image is consistent with no acute radiographic abnormalities, suggesting the patient\'s asthma exacerbation and symptoms may not be visible on X-ray.'

        # 文件上传
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_url = url_for('static', filename=f'uploads/{filename}')

    return render_template('index.html', input_text=input_text, output_text=output_text, image_url=image_url)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
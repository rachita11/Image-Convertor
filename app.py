from flask import Flask, render_template,request, url_for, redirect, flash
import os
import cv2
from werkzeug.utils import secure_filename
import numpy as np

upload_folder= os.path.join('static', 'uploads')

app = Flask('__name__')
app.config['UPLOAD_FOLDER']=upload_folder

def pencilsketch(new_img):
    image1 = cv2.imread(new_img)
    grey = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - grey
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(grey, inverted_blurred, scale=256.0)
    return pencil_sketch

def painting(new_img):
    image1 = cv2.imread(new_img)
    watercolor = cv2.stylization(image1,sigma_s=50,sigma_r=0.5)
    return watercolor

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

def vector(new_img):
    image1 = cv2.imread(new_img)
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    color = cv2.bilateralFilter(image1, 9, 250, 250)
    total_color = 12
    img2 = color_quantization(color, total_color)
    blurred = cv2.bilateralFilter(img2, d=7, sigmaColor=200,sigmaSpace=200)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    return cartoon

@app.route('/')
def page1():
     return render_template('index.html')

@app.route('/upload1',methods = ['GET','POST'])
def application1():
   if request.method == 'POST':
        file = request.files['file']
        if file.filename !='':
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            cv2.imwrite(os.path.join('C:/Users/HP/Desktop/MLprojects/pencilsketcher/static/uploads','new.png'),pencilsketch(path))
            pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'new.png')
            return render_template('index2.html',user_image=pic2)


@app.route('/upload2',methods = ['GET','POST'])
def application2():
   if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if file.filename !='':
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            cv2.imwrite(os.path.join('C:/Users/HP/Desktop/MLprojects/pencilsketcher/static/uploads','new.png'),painting(path))
            pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'new.png')
            return render_template('index2.html',user_image=pic2)


@app.route('/upload3',methods = ['GET','POST'])
def application3():
   if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if file.filename !='':
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            cv2.imwrite(os.path.join('C:/Users/HP/Desktop/MLprojects/pencilsketcher/static/uploads','new.png'),vector(path))
            pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'new.png')
            return render_template('index2.html',user_image=pic2)

@app.route('/back',methods = ['POST'])
def back_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

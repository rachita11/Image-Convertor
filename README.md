# Image-Convertor

How the website looks<br>
It gives you the option to select a file from your pc and gives you three options/filters to choose from<br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/1.png)<br>
Let this be the first image we feed in to conver into a <b>pencil sketch</b>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/deer.jpg)<br><br>
On clicking the pencil sketch button, this is the result that comes out. Again two options are provided one of which lets the user download this news image and the other redirect them to the home page.<br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/2.png)<br><br>
Let the next image be this one shown here, to test the <b>watercolor painting filter.</b><br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/flower.jpg)<br><br>
On clicking the required option, this results gets displayed.<br><br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/3.png)<br><br>
This is the image to test the final feature which is <b>vector art.</b><br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/landscape.jpg)<br><br>
 On clicking thr option this is the image formed.<br>
![image1](https://github.com/rachita11/Image-Convertor/blob/main/Images/4.png)<br><br>
In every case user can download the output to their pc.


This web application contains 3 main elements 2 being the folders of 'templates' and 'static' and 1 being the main app.py file.<br>
<br>
<b>Static</b> is serving as the folders that uploads the input images by user and saving the output of the defined functions within itself, along with the style.css file.
<b>Templates</b> folder has the two html files which we require for this application<br>
<br>
**app.py DESCRIPTION:-**
<br>
Let us divide the file into 3 different elements<br> 1.module imports<br>2.Defining functions<br>3.Creating the Flask api<br><br>
*Functions*<br>
the three tasks it is doing are<br> i)taking in a new image as parameter<br> ii)performing Opencv enabled calculations <br> iii)returning the final coverted image(mind that it hasn't been stored anywhere yet)<br><br>
*APIs'*<br>
the main function is being done by the app.route('/uploads') api which interfaces between the the form input to giving out the output and these are tasks it is doing along the way.<br>1.reading and securing filename from form<br>2.declaring the path to store input image and saving it there<br>3.providing this image to predefined function to convert into required forms.<br>4.returning the html file to display this image.

# This is a small project to borrow court from new NCHU Physical Education Center
Make sure you have a account in [NCHU Physical Education Center](https://rent.pe.nchu.edu.tw/nchugym/login.php)
## Here are some quick instructions to help you set up the environment. 
1. Install all the packages in requirements.txt
2. Install tesseract in [link](https://github.com/UB-Mannheim/tesseract/wiki) and remember the path of "pytesseract.exe" (e.g. C:\Program Files\Tesseract-OCR\tesseract.exe)
3. Set configurations in main.py
    - file_dir: Path to the whole project
    - account: Your account
    - passwd: Your password
    - OCR_path: Path of "pytesseract.exe"
    - target: You can borrow badminton, tennis, or table tennis court
4. Write a .bat file and schedule batch file with windows task scheduler
ˋˋˋ
@echo off
"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script name.py"
pause
ˋˋˋ

## Error
Solve the following error in https://blog.csdn.net/zhoukeguai/article/details/113247342.
>selenium.common.exceptions.WebDriverException: Message: Service C:\Program Files\Google\Chrome\Application\chrome.exe unexpectedly exited. Status code was: 0

## Demo
[![Alt text](https://img.youtube.com/vi/zcn6z-nweHo/0.jpg)](https://www.youtube.com/watch?v=zcn6z-nweHo)


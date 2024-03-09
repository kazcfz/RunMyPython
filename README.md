# RunMyPython
RunMyPython is a web-based Python execution module built using the Flask framework. It allows users to execute custom Python code snippets directly from their web browser and view the executed results. This project is designed to be Docker-based, ensuring secure execution of arbitrary Python code.
<br><br>

## Features
- User-friendly Web Interface
- Safe Arbitrary Code Execution
<br><br>

## Getting Started
1. Download [source code](https://github.com/kazcfz/RunMyPython/releases) / Clone repository
2. Navigate to project directory `cd RunMyPython`
3. Run `docker build -t runmypython .` to build the Docker image
4. Run `docker run -p 5000:5000 runmypython` to run the Docker container
5. Navigate to http://localhost:5000 on your browser to access the running Flask app
<br><br>

## Usage
1. Navigate to http://localhost:5000
2. Write your Python code in the editor
3. Click on the "Run" button to execute it
4. Output of your code execution will be displayed beside the code editor
<br><br>

## Screenshot Preview
![](https://i.imgur.com/gUru2ge.png)

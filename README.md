# zh-airline

## Requirements:
We are creating a new software for a airline company called “ZA”.
- The company is assessing 10 different airplanes.
- Each airplane has a fuel tank of (200 liters * id of the airplane) capacity. For example, if
the airplane id = 2, the fuel tank capacity is 2*200 = 400 liters.
- The airplane fuel consumption per minute is the logarithm of the airplane id multiplied by
0.80 liters.
- Each passenger will increase fuel consumption for additional 0.002 liters per minute.

**Write a RESTful API using Django Rest Framework to:**
+ Allow for input of 10 airplanes with user defined id and passenger assumptions
+ Print total airplane fuel consumption per minute and maximum minutes able to fly

**Implementation**
There will not be any database system since all we need is an I/O app

### Steps to reproduce
1. Clone the repo 
```
https://github.com/harryface/zh-airline.git
```
2. Set up a virtual environment and activate it
```
python3 -m venv c:\path\to\myenv
c:\path\to\myenv\Scripts\activate.bat
```

3. Install requirements.txt using the command below
```
pip install -r requirements.txt
```

4. cd into the repo folder and run
```
python manage.py runserver
```

**NB:** we do not need to run makemigrations or migrate for a database was not utilized.

### API endpoints
1. POST http://localhost:8000/api/v1/aeroplane HTTP/1.1

**For Live Testing**
If you are using vscode, you can install _REST client_ by Huachao Mao, and then run the attached rest.http file i have included

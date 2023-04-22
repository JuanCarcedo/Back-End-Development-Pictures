# IBM Back-End-Development-Capstone Pictures(Flask) final project
## Index
1) IBM Skills Network - Intro to the project
   1) Background
   2) Important Notes
2) Instructions
   1) How to install
   2) Version Updates
3) Author and Licence


## IBM Skills Network - Intro to the project
The starting point of this project can be found here [IBM Project](https://github.com/ibm-developer-skills-network/luggb-Back-End-Development-Pictures). This is a template (not a fork).  
I implemented the necessary code to make this project work (initial structure given, please check the repository).

Changes:
+ updated ```backend/data/routes.py```

### Background
Your client has asked you to build a website for a famous band. The backend developer on the project has recently left, and you need to finish the code so the website can go live. The application consists of some different microservices working together.  
You are asked in this lab to finish the Get Pictures microservice. This microservice stores URLs of pictures from past events. The previous developer started a Python Flask-based REST API and wrote some tests following the TDD or test driven development process. You will need to get the code from GitHub and fill in the missing pieces so that the code can pass all tests.

_This part relates to the Pictures' management._  
Linked parts of this project:
- [Back-End-Development-Songs](https://github.com/JuanCarcedo/Back-End-Development-Songs)
- [Back-End-Development-Django](https://github.com/JuanCarcedo/Back-end-Development-Capstone)

### Important Notes
You may need IBM Cloud account for some of the deployments.  
This project is made with:  
+ Flask
+ MongoDB
+ IBM Cloud

I use WSL for simple CURL test.

## Instructions
### How to install:  
- Fork the project.
- Configure git (I am using WSL):
  - `git config --global user.email "myemail@something.com"`
  - `git config --global user.name "MyUser"`
- Local clone `git clone <URL_PROJECT>` the project in your local machine.
- Open your favourite IDE (I use [PyCharm](https://www.jetbrains.com/pycharm/)).
- You can install the requirements manually:
   1) Create a virtual environment (I am using Python 3.11).
   2) Install required packages using `py -m pip install -U -r requirements.txt`  
- You can install them via bash: 
   1) `cd Back-end-Development-Pictures`  
   2) `bash ./bin/setup.sh`
- Remember to Commit and Push changes to your GitHub!

### Version Updates:  
+ v0 -- 2023/04 - Solution deployed.

## Author and Licence
This is a template from an IBM repository:  
**[IBM Project](https://github.com/ibm-developer-skills-network/luggb-Back-End-Development-Pictures)**  
2023 Copyright © - Licence [Apache](https://github.com/ibm-developer-skills-network/luggb-Back-End-Development-Pictures/blob/main/LICENSE)  

Enhancements and other modifications by:  
**[Juan Carcedo](https://github.com/JuanCarcedo)**      

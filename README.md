Automation REST API testing project on Python

[![API tests](https://github.com/ivanovajulika/Api_Petstore/actions/workflows/action.yml/badge.svg)](https://github.com/ivanovajulika/Api_Petstore/actions/workflows/action.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
---
#  Swagger Petstore

[Api documentation]👉
[<img src="https://github.com/ivanovajulika/Api_Petstore/raw/main/picture/Swagger.jpg" alt='Swagger' width="200" height="150">](https://petstore.swagger.io/)
[OUR]👉
[<img src="https://logosmarken.com/wp-content/uploads/2021/03/Trello-Logo-650x366.png" alt='Trello' width="115" height="70">](https://trello.com/b/6n6e0r1L/psevdokodapip)

## Table of contents
- [Pytest INFO](#some-pytest)
- [Allure](#some-allure)

___


## Pytest INFO:<a name="some-pytest"></a> [![pytest](https://img.shields.io/badge/pytest-website-brightgreen.svg?style=flat-square)](https://docs.pytest.org/en/7.2.x/)

> ***Do not forget check your tests with black and flake8 before pushing***

### **pytest flags**
    -s - prints desired output (pytest -s test_file_name)
    
    -v - shows test process' percentage (pytest -v test_file_name)
    
    -m - allows to run tests with specific marks (pytest -m mark_title test_file_name)

### **pytest-xdist**

##### *Runs multiple tests at the same time* 

    pytest -n auto OR pytest -n 5( any number)
 
___
## ALLURE <a name="some-allure"></a>
#### Website with more information &middot;[![WEB-SITE](https://img.shields.io/badge/allure-website-brightgreen.svg?style=flat-square)](https://docs.qameta.io/allure/#_pytest)

### ***Installation:***
    pip install allure-pytest
    pip install allure-python-commons
  
### ***1. Create allure:***
  
###### Collect reports for all tests:
  
    pytest alluredir=allure-results
  
###### Generates a report for the specified test:
  
    pytest test_name alluredir=allure-results
  
### ***2. Generates a report and opens it in a browser::***
     
    allure serve allure-results
      
### ***3. Report generated for allure-report:***
  
    allure generate <allure-results>
  
### ***4. Create single HTML report:***<a name="some-allure-html-file"></a>
-creates a report file`complete.html`(can be shared with others) 
  
    allure-combine ./allure-report
  
-delete  `sinon.js` и `server.js`
  
### ***Open allure report:***
  
    allure open <directory>  

### ***Clean allure report:***
  
    allure report clean 

### ***Change directory:***

    allure generate old directory-o new directory
___
## Useful links <a name="some-links"></a>

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/7.1.x/contents.html)
[![Allure](https://img.shields.io/badge/-Allure-464646?style=flat-square&logo=Allure)](http://allure.qatools.ru/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions/)
[![GitHub%20Pages](https://img.shields.io/badge/-GitHub%20Pages-464646?style=flat-square&logo=GitHub%20Pages)](https://pages.github.com/)

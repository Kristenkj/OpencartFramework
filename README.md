### 🚀 Custom QA Automation Framework for Opencart E-commerce Site


## Project Description
Hello, I am Kristen!

For this project, I created a hybrid web automation framework utilizing the page object model (POM) design pattern in Selenium 
In addition, I validated the functionality and user interactions of the e-commerce-based site using automated tests with Selenium Webdriver.
The site that was used: [Opencart E-commerce site](https://awesomeqa.com/ui/)

## Table of Contents

- [Test Cases](#test-cases)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Test Cases

The automated test cases cover the following functionalities:

- User Registration: Validates the user registration form with various input scenarios.
* Login Functionality: Ensures users can log in with valid credentials and are prevented from logging in with invalid ones.
* Product Listing and Purchase: Tests the process of browsing products and completing a purchase.
* Form Validations: Checks form validations and error messages.
* 
## Technologies Used

- Python 3.12: Programming Language
- Pytest: Framework for writing and running tests
- Selenium Webdriver: For browser Automation
- Openpyxl: For handling Excel files
- Logger: For logging test execution details
- Jenkins: For CI/CD
- Faker: For generating fake data for testing

## Project Structure


```
Opencart Framework/
├── configs               # Configuration files
├── Logs/                 # Log files
│   ├── logfile.log
├── reports/              # Test reports
│   └── allure-results    # Allure results directory
├── pageObjects/          # Page Object Models - Represents different pages/screens of the application.
│   ├── basePage.py
│   ├── desktopsPage.py
│   ├── camerasPage.py
│   ├── my_accountPage.py
|   ├── my_accountPage.py
├── screenshots/          # Screenshots of test execution
│   ├── CheckoutPage.py
│   ├── ConfirmPage.py
│   ├── HomePage.py
│   ├── ShopPage.py
├── testCases/            # Test files
│   ├── test_ui_elements.py
│   ├── test_login.py
│   ├── test_purchase.py
│   └── test_form_validations.py
├── testData/             # Test data files
│   └── test_form_validations.py
├── utils/                # Utility functions
│   ├── helpers.py        # Helper functions to assist in test execution and setup.
│   ├── BaseClass.py
│   └── excel_utils.py    # Excel handling functions using openpyxl
├── conftest.py           # Configuration for pytest
├── requirements.txt      # File listing Python dependencies required for running the project.
└── README.md             # Documentation file providing an overview of the project, structure, and other relevant information. 
```

## Contact
For any questions, feedback, or collaboration opportunities, feel free to reach out to me:
- Email: jonesbkristen@gmail.com
- Github: [Kristen's GitHub Profile](https://github.com/Kristenkj)



  

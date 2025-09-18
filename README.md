# 🐼 PandaDoc Web Autotests

Automation testing for **PandaDoc website** using Python, Pytest, Selene, Allure, Jenkins 

---

## 📖 About the project

UI test framework for PandaDoc.  
Covers **smoke** and **regression** scenarios for:

- **Homepage** — header & footer checks  
- **Pricing** — plans presence, CTA buttons, price toggle  
- **Templates** — template search and filtering  
- **Forms** — validation of *Request a Demo* and *Contact Sales* forms  
- **Navigation** — correctness of main menu links  

Page Object Model (POM) is implemented for structured page logic.

---

## 🛠️ Technologies & Tools

<p align="center">
  <img width="10%" title="Python" src="./resources/images/logo/python.png" alt="python">
  <img width="10%" title="Pytest" src="./resources/images/logo/pytest.png" alt="pytest">
  <img width="10%" title="Selene" src="./resources/images/logo/selene.png" alt="selene">
  <img width="10%" title="Selenium" src="./resources/images/logo/selenium.png" alt="selenium">
  <img width="10%" title="Allure Report" src="./resources/images/logo/allure_report.png" alt="areport">
  <img width="10%" title="Allure TestOps" src="./resources/images/logo/allure_testops.png" alt="testops">
  <img width="10%" title="Jenkins" src="./resources/images/logo/jenkins.png" alt="jenkins">
  <img width="10%" title="Telegram" src="./resources/images/logo/tg.png" alt="tg">
  <img width="10%" title="GitHub" src="./resources/images/logo/github.png" alt="github">
</p>

---

## ▶️ Run tests locally

Clone the repository:

```bash
git clone https://github.com/username/pd_web_tests_selene.git
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run tests with Allure report generation:
```bash
pytest --alluredir=allure-results
```
View Allure report:
```bash
allure serve allure-results
```

---

## ⚙️ Run tests in Jenkins

1. Log in to **Jenkins**  
2. Select the job **`hw_14_pd_web_test_ihar_t`**  
3. Click **Build Now**  
4. After the run finishes, open the **Allure Report** or **Allure TestOps**  icon on the build page

![Jenkins_build_page](./resources/images/screenshots/jenkins_build.png)

---

## 📊 Reports

### Allure Report
![Allure Report](./resources/images/screenshots/allure_example.png)

### Allure TestOps
![Allure TestOps](./resources/images/screenshots/allure_testops.png)

### Telegram Notifications
![Telegram report](./resources/images/screenshots/telegram_example.png)

---


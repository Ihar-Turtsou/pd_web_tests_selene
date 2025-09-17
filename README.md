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
  <code><img width="8%" title="Python" src="resources/images/logo/python.png"></code>
  <code><img width="8%" title="Pytest" src="resources/images/logo/pytest.png"></code>
  <code><img width="8%" title="Selene" src="resources/images/logo/selene.png"></code>
  <code><img width="8%" title="Selenium" src="resources/images/logo/selenium.png"></code>
  <code><img width="8%" title="Allure Report" src="resources/images/logo/allure_report.png"></code>
  <code><img width="8%" title="Allure TestOps" src="resources/images/logo/allure_testops.png"></code>
  <code><img width="8%" title="Jenkins" src="resources/images/logo/jenkins.png"></code>
  <code><img width="8%" title="Telegram" src="resources/images/logo/tg.png"></code>
  <code><img width="8%" title="GitHub" src="resources/images/logo/github.png"></code>
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
2. Select the job **`hw_pd_web_tests`**  
3. Click **Build with parameters**  
4. After the run finishes, open the **Allure Report** icon on the build page

<p align="center">
  <img title="Jenkins build" src="resources/images/screenshot/jenkins_build.png">
</p>

---

## 📊 Reports

### Allure Report
<p align="center">
  <img title="Allure Report" src="resources/images/screenshot/allure_example.png">
</p>

### Allure TestOps
<p align="center">
  <img title="Allure TestOps" src="resources/images/screenshot/allure_testops.png">
</p>

### Telegram Notifications
<p align="center">
  <img title="Telegram report" src="resources/images/screenshot/telegram_example.png">
</p>

---

## ✅ Test coverage

- **Homepage** — Header & Footer  
- **Pricing** — Plans & CTA, Price toggle  
- **Templates** — Search  
- **Forms** — Request a Demo, Contact Sales  
- **Navigation** — Main menu links


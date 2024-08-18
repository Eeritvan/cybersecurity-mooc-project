# cybersecurity-project
This repository is for a project made for a University of Helsinki [course](https://cybersecuritybase.mooc.fi/)

## Getting the app and running
1. clone this repository to your system and navigate to the root
2. run `cd application`
3. run `python3 manage.py migrate`
4. run `python3 manage.py runserver`
5. locate to url `http://127.0.0.1:8000/`

## resetting application
1. shut down the application `(ctrl+c)`
2. delete db.sqlite3
3. run `python3 manage.py migrate`
4. run `python3 manage.py runserver`
5. locate to url `http://127.0.0.1:8000/`

## pre-made users for testing
| username | password    |
| -------- | ----------- |
| alice    | redqueen    |
| bob      | squarepants |

## security vulnerabilities
These flaws were selected from [OWASP's 2017 Top 10 security risks list](https://owasp.org/www-project-top-ten/2017/Top_10)

1. [Injection](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection)
2. [Broken Authentication](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)
3. [Broken Access Control](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control)
4. [Security Misconfiguration](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration)
5. [Cross-Site Scripting (XSS)](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS))
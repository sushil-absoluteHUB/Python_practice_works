# Python Practice Works - Learning Guide

## Workspace Overview

This workspace contains a Django project environment with various Python learning modules and practice exercises.

### Workspace Structure
```
myproject/
├── dj1/                          # Django project
│   ├── manage.py                # Django management script
│   ├── db.sqlite3               # SQLite database
│   ├── blog/                    # Django app
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View logic
│   │   ├── urls.py              # URL routing
│   │   ├── admin.py             # Django admin
│   │   └── migrations/          # Database migrations
│   └── dj1/                     # Project settings
│       ├── settings.py          # Django configuration
│       ├── urls.py              # Main URL routing
│       ├── wsgi.py              # WSGI application
│       └── asgi.py              # ASGI application
│
├── API_test/                     # API testing
│   ├── main.py                  # API implementation
│   └── test_main.py             # API tests
│
├── pytest1/                      # Pytest examples
│   ├── test_example.py          # Example tests
│   └── test_login.py            # Login test cases
│
├── Python_practice_works/        # Python learning exercises
│   ├── day1.py to day4.py       # Daily practice files
│   ├── oops.py                  # Object-Oriented Programming
│   ├── parent.py & child.py     # Inheritance examples
│   ├── exceptionH.py            # Exception handling
│   ├── fileH.py                 # File handling
│   ├── clock.py                 # Clock program
│   └── xel.py                   # XEL practice
│
└── selenium/                     # Selenium automation
    └── selm1.py                 # Web automation script
```

---

## Python Basic Coding Steps

### 1. Setting Up Python Environment

#### Prerequisites
- Python 3.8+ installed on your system
- VS Code with Python extension installed
- Virtual environment setup

#### Create a Virtual Environment
```bash
# Windows PowerShell
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

#### Install Dependencies
```bash
pip install django
pip install pytest
pip install selenium
pip install requests
```

---

### 2. Python Fundamentals

#### Variables and Data Types
```python
# String
name = "Python"

# Integer
age = 25

# Float
height = 5.9

# Boolean
is_student = True

# List
numbers = [1, 2, 3, 4, 5]

# Dictionary
person = {"name": "John", "age": 30}

# Tuple (immutable)
coordinates = (10, 20)
```

#### Control Flow
```python
# If-Else Statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Loops
for i in range(5):
    print(i)

while count < 10:
    count += 1
```

#### Functions
```python
def greet(name):
    """Function to greet someone"""
    return f"Hello, {name}!"

result = greet("Alice")
print(result)
```

---

### 3. Object-Oriented Programming (OOP)

#### Classes and Objects
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Creating instances
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks
```

#### Key OOP Concepts
- **Encapsulation**: Bundling data and methods together
- **Inheritance**: Deriving classes from parent classes
- **Polymorphism**: Objects can take multiple forms
- **Abstraction**: Hiding complex implementation details

---

### 4. File Handling

```python
# Writing to a file
with open("my.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("my.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("my.txt", "a") as file:
    file.write("\nNew line")
```

---

### 5. Exception Handling

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")
```

---

### 6. Working with Django

#### Create a Django Project
```bash
django-admin startproject dj1
cd dj1
python manage.py startapp blog
```

#### Define Models
```python
# In blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Create Views
```python
# In blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

---

### 7. Testing with Pytest

```python
# test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

#### Running Tests
```bash
pytest test_example.py
pytest -v  # Verbose output
pytest --cov  # Coverage report
```

---

### 8. Web Automation with Selenium

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to website
driver.get("https://example.com")

# Find elements
element = driver.find_element(By.ID, "element_id")

# Interact with elements
element.click()
element.send_keys("text to type")

# Wait for elements
time.sleep(2)

# Close browser
driver.quit()
```

---

### 9. Best Practices

#### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused

#### Documentation
```python
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    """
    return 3.14 * radius ** 2
```

#### Error Handling
- Always handle exceptions explicitly
- Use custom exceptions when needed
- Log errors for debugging

---

### 10. Common Commands

```bash
# Run Python file
python filename.py

# Interactive Python
python

# Install packages
pip install package_name

# List installed packages
pip list

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Django server
python manage.py runserver

# Django shell
python manage.py shell
```

---

## Learning Path

1. **Start with basics**: Variables, data types, and control flow
2. **Learn functions**: Create reusable code blocks
3. **Study OOP**: Understand classes and objects
4. **File operations**: Read/write data from files
5. **Error handling**: Deal with exceptions gracefully
6. **Testing**: Write and run tests
7. **Web frameworks**: Learn Django
8. **Automation**: Explore Selenium for web automation

---

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Pytest Documentation](https://pytest.org/)
- [Selenium Documentation](https://selenium.dev/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

## Notes

- Always activate your virtual environment before working on projects
- Keep your dependencies updated: `pip install --upgrade pip`
- Use version control (Git) to track your changes
- Test your code frequently to catch bugs early

Happy Learning! 🐍

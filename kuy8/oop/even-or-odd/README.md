# [8 kyu] Even or Odd - OOP Solution

![Python](https://img.shields.io/badge/Python-3.x-informational?style=flat&logo=python&logoColor=white)
![Codewars Rank](https://img.shields.io/badge/Rank-8%20kyu-blue?style=flat&logo=codewars&logoColor=white)
![Unit Tests](https://img.shields.io/badge/Unit%20Tests-unittest-success?style=flat&logo=python&logoColor=white)

---

### 🧩 Challenge Description

**[Link to the kata on Codewars](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)**

_Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers._

---

### 🛠 Approach: OOP Programming

This solution is implemented using object-oriented programming principles.
The `NumberClassifier` class encapsulates the logic for validating and classifying integers as either "Even" or "Odd", using properties and methods to ensure clean and reusable code.

---

### ▶ Example Usage

```python
from src.number_classifier import NumberClassifier

classifier = NumberClassifier(7)
print(classifier.classify())  # Output: Odd

classifier.number = 10
print(classifier.classify())  # Output: Even
```

---

### ✔ Running the Tests

Test are written using Python's built-in `unittest` framework.
To run them, navigate to the `kyu8/oop/even_or_odd/` directory and execute:

```bash
python -m unittest discover -s tests
```

---

### 📦 Installing Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt
```

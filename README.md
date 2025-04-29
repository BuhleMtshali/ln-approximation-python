
# 📐 ln(1 + x) Approximation in Python

This Python program approximates the natural logarithm `ln(1 + x)` using a **Taylor series expansion**. It supports either **precision-based** or **term-limit-based** stopping criteria and compares the result to the exact value using Python's `math.log`.

---

## 📊 The Math Behind It

We use the Taylor series expansion:

\[
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots
\]

This works for values of **x where -1 < x < 1**.

---

## 🛠 Features

- Input validation to ensure x is in the correct range.
- User chooses:
  - Precision (e.g. `0.000001`)  
  **OR**
  - Maximum number of terms.
- Prints each term, running total, and change from previous total.
- Final summary includes:
  - Final approximation
  - Exact value using `math.log`
  - Terms used
  - Difference from actual value

---

## 💻 How to Use

1. **Clone the repo**:

```bash
git clone https://github.com/buhleMtshali/ln-approximation-python.git
cd ln-approximation-python

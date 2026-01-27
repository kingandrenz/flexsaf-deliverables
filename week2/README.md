# Student Grade & Award Calculator

A clean, modular Python script that automates student performance tracking by validating inputs, calculating averages, and determining award eligibility.

## 🚀 Features
* **Input Validation**: Prevents crashes by ensuring scores are numeric and fall between 0-100.
* **Arithmetic Processing**: Automatically calculates the total sum and the mean average.
* **Decision Logic**: 
    * **Pass/Fail**: Determines status based on a 50% average.
    * **Award System**: Uses logical `AND` gates to check for high-tier excellence.



## 🛠️ How to Use
1.  **Run the script**:
    ```bash
    python3 grade_calc.py
    ```
2.  **Enter Data**: Input the scores for the Test, Assignment, and Exam when prompted.
3.  **Review Output**: The script will print a formatted summary including:
    * **Total Score**
    * **Mean Average** (rounded to 2 decimal places)
    * **Award Status** (if criteria are met)

## 📋 Logic Specifications
| Metric | Threshold / Formula |
| :--- | :--- |
| **Total** | `Test + Assignment + Exam` |
| **Average** | `Total / 3` |
| **Pass Status** | `Average >= 50` |
| **Award Eligibility** | `Average > 90` AND `Exam > 85` |

## 📁 Requirements
* Python 3.x

---
*Created as a reusable utility for academic data processing.*
*This is part of the weekly flexisaf weekly deliverables

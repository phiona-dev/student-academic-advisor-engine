# Student Academic Advisor Engine

## Project Title
Student Academic Advisor Engine

## Introduction
This project is a simple rule-based reasoning engine for evaluating student academic status. It accepts basic student information such as GPA, attendance, disciplinary history, prerequisite completion, and outstanding fees, then applies predefined rules to generate useful conclusions.

## Problem Statement
Academic advisors often need to make quick decisions based on multiple student conditions. Manually checking every rule for each student can be slow and error-prone. This project solves that problem by using a small knowledge base and a reasoning engine to automatically generate conclusions such as scholarship eligibility, graduation eligibility, probation warning, or registration restrictions.

## Knowledge Base
The system uses the information stored in `knowledge_base.json`, which contains:

- A list of academic facts and conditions
- A list of rules that describe when a conclusion should be produced

This makes the engine easy to extend later by adding more rules without rewriting the main program.

## Rules Implemented
The current version implements these rules:

1. Scholarship Rule
   - If GPA > 3.5
   - AND Attendance > 80%
   - AND No disciplinary cases
   - Then: Eligible for Scholarship

2. Graduation Rule
   - If GPA > 3.0
   - AND Prerequisites are completed
   - AND No outstanding fees
   - Then: Eligible for Graduation

3. Probation Rule
   - If GPA < 3.0
   - Then: Academic Probation

4. Registration Block Rule
   - If outstanding fees exist
   - Then: Registration Blocked

5. Dean's List Rule
   - If GPA > 3.5
   - AND Attendance > 80%
   - Then: Dean's List Candidate

## Reasoning Method Used
The program uses a simple forward-chaining approach:

1. Read the student facts from the program input.
2. Compare those facts against the rules in the knowledge base.
3. If the rule conditions are satisfied, add the conclusion to the result.
4. Print the explanations for each triggered rule.

This is a lightweight example of rule-based reasoning and inference.

## Screenshots
The project includes example outputs and flow visuals in the following folders:

- `screenshots/test_case1.png`
- `screenshots/test_case2.png`
- `screenshots/test_case3.png`
- `diagrams/inference_flow.png`

## How to Run the Program
1. Open a terminal in the project folder.
2. Make sure Python is installed.
3. Run:

   python reasoning_engine.py

4. The program will show example cases and then allow you to enter your own student details.

## Sample Inputs and Outputs
Example input:

- GPA = 3.8
- Attendance = 90%
- No disciplinary cases
- Prerequisites completed
- No outstanding fees

Example output:

- Eligible for Scholarship
- Eligible for Graduation
- Dean's List Candidate

## Group Members (if applicable)
Phiona

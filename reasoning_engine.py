import json;

#load knowledge base
with open("knowledge_base.json", "r") as file:
    kb = json.load(file)
    
def evaluate_student(gpa, attendance, disciplinary, prerequisites, fees):
    """Accepts student info, applies rules,returns conclusions"""
    conclusions = []
    explanations = []
    
    #convert inputs to conditions that can be checked
    gpa_above_3point5 = gpa > 3.5
    gpa_above_3point0 = gpa > 3.0
    gpa_below_3point0 = gpa < 3.0
    attendance_above_80 = attendance > 80
    no_disciplinary = not disciplinary
    has_disciplinary = disciplinary
    completed_prerequisites = prerequisites
    no_fees = not fees
    has_fees = fees
    
    #check each rule from json file
    for rule in kb["rules"]:
        if rule["id"] == "scholarship":
            if gpa_above_3point5 and attendance_above_80 and no_disciplinary:
                conclusions.append("Eligible for Scholarship")
                explanations.append({
                    "conclusion": "Eligible for Scholarship",
                    "rule": "Scholarship Rule",
                    "condition": [
                        "GPA > 3.5",
                        "Attendance > 80%",
                        "No Disciplinary Cases"
                    ]
                })
        
        elif rule["id"] == "graduation":
            if gpa_above_3point0 and completed_prerequisites and no_fees:
                conclusions.append("Eligible for Graduation")
                explanations.append({
                    "conclusion": "Eligible for Graduation",
                    "rule": "Graduation Rule",
                    "condition": [
                        "GPA > 3.0",
                        "Completed Prerequisite Courses",
                        "No Outstanding Fees"
                    ]
                })
        
        elif rule["id"] == "probation":
            if gpa_below_3point0:
                conclusions.append("Academic Probation")
                explanations.append({
                    "conclusion": "Academic Probation",
                    "rule": "Probation Rule",
                    "condition": [
                        "GPA < 3.0"
                    ]
                })
        
        elif rule["id"] == "registration_block":
            if has_fees:
                conclusions.append("Registration Blocked")
                explanations.append({
                    "conclusion": "Registration Blocked",
                    "rule": "Registration Block Rule",
                    "condition": [
                        "Has Outstanding Fees"
                    ]
                })
        
        elif rule["id"] == "deans_list":
            if gpa_above_3point5 and attendance_above_80:
                conclusions.append("Dean's List Candidate")
                explanations.append({
                    "conclusion": "Dean's List Candidate",
                    "rule": "Dean's List Rule",
                    "condition": [
                        "GPA > 3.5",
                        "Attendance > 80%"
                    ]
                })

    return conclusions, explanations

def explain_conclusions(explanations):
    """Prints explanations for each conclusion"""
    if not explanations:
        print("\nNo conclusions to explain.")
        return
    
    explanation_text = "\nEXPLANATIONS:\n" + "="*40 + "\n"
    for exp in explanations:
        explanation_text += f"Conclusion: {exp['conclusion']} because:\n"
        for condition in exp["condition"]:
            explanation_text += f"   - {condition}\n"
        explanation_text += f"   Therefore {exp['rule']} was activated\n"
        explanation_text += "-"*40 + "\n"

    return explanation_text

def forward_chaining():
    """Implements forward chaining inference"""
    print("FORWARD CHAINING INFERENCE")
    print("="*60)
    
    #student 1
    print("\nStudent 1:")
    print("="*30)
    
    print("\n Facts Provided:")
    print("- GPA = 3.8")
    print("- Attendance = 90%")
    print("- No Disciplinary Cases")
    print("- Completed Prerequisites course")
    print("- No Outstanding Fees")
    
    print("\nRules Triggered:")
    print("   • Scholarship Rule: IF GPA > 3.5 AND Attendance > 80% AND No Disciplinary Cases")
    print("   • Graduation Rule: IF GPA > 3.0 AND Completed Prerequisite Courses AND No Outstanding Fees")
    print("   • Dean's List Rule: IF GPA > 3.5 AND Attendance > 80%")
    
    result1, explanations1 = evaluate_student(3.8, 90, False, True, False)
    
    print("\n Final Conclusions:")
    for conclusion in result1:
        print(f"   • {conclusion}")
        
    print(explain_conclusions(explanations1))

#student 2
    print("\n" + "="*60)
    print("\nStudent 2:")
    print("="*30)
    
    
    print("\n Facts Provided:")
    print("- GPA = 2.5")
    print("- Attendance = 70%")
    print("- No Disciplinary Cases")
    print("- Completed Prerequisites course")
    print("- No Outstanding Fees")
    
    
    print("\nRules Triggered:")
    print("   • Probation Rule: IF GPA < 3.0")
    
    result2, explanations2 = evaluate_student(2.5, 70, False, True, False)
    
    print("\n Final Conclusions:")
    for conclusion in result2:
        print(f"   • {conclusion}")
        
    print(explain_conclusions(explanations2))
        
    #student 3
    print("\n" + "="*60)
    print("\nStudent 3:")
    print("="*30)
    
    print("\n Facts Provided:")
    print("- GPA = 3.2")
    print("- Attendance = 85%")
    print("- No Disciplinary Cases")
    print("- Completed Prerequisites course")
    print("- Has Outstanding Fees")
    
    print("\nRules Triggered:")
    print("   • Registration Block Rule: IF Has Outstanding Fees")
    
    result3, explanations3 = evaluate_student(3.2, 85, False, True, True)
    print("\n Final Conclusions:")
    for conclusion in result3:
        print(f"   • {conclusion}")
        
    print(explain_conclusions(explanations3))

def main():
    forward_chaining()
    
     #allow user to input for testing
    print("\n" + "="*40)
    print("\nEnter your own student info for evaluation:")
    print("="*40)
    
    gpa_input = float(input("Enter GPA: "))
    attendance_input = float(input("Enter Attendance %: "))
    disciplinary_input = input("Any disciplinary cases? (yes/no): ").strip().lower() == "yes"
    prerequisites_input = input("Completed prerequisites? (yes/no): ").strip().lower() == "yes"
    fees_input = input("Any outstanding fees? (yes/no): ").strip().lower() == "yes"
    
    result, explanations = evaluate_student(gpa_input, attendance_input, disciplinary_input, prerequisites_input, fees_input)
    print("\nCONCLUSIONS:")
    if result:
        for conclusion in result:
            print(f"{conclusion}")
        print(explain_conclusions(explanations))
    else:
        print("No rules triggered for this student.") 
        print("\nExplanation: None of the rule conditions were satisfied by the provided facts.")

#test the reasoning engine

if __name__ == "__main__":
    main()
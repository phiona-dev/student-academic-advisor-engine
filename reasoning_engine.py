import json;

#load knowledge base
with open("knowledge_base.json", "r") as file:
    kb = json.load(file)
    
def evaluate_student(gpa, attendance, disciplinary, prerequisites, fees):
    """Accepts student info, applies rules,returns conclusions"""
    conclusions = []
    
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
        
        elif rule["id"] == "graduation":
            if gpa_above_3point0 and completed_prerequisites and no_fees:
                conclusions.append("Eligible for Graduation")
        
        elif rule["id"] == "probation":
            if gpa_below_3point0:
                conclusions.append("Academic Probation")
        
        elif rule["id"] == "registration_block":
            if has_fees:
                conclusions.append("Registration blocked") 
        
        
        elif rule["id"] == "deans_list":
            if gpa_above_3point5 and attendance_above_80:
                conclusions.append("Dean's List Candidate")
                
    return conclusions

#test the reasoning engine

if __name__ == "__main__":
    print("REASONING ENGINE TEST")
    
    
    #Test case 1: High performing student
    print("\nTest Student:")
    print("GPA = 3.8, Attendance = 90%, No disciplinary cases")
    print("Completer prerequisites, No outstanding fees")
    
    result = evaluate_student(3.8, 90, False, True, False)
    
    print("\nOutput:")
    for conclusion in result:
        print(f"{conclusion}")
        
    print("\n" + "="*40)
    
    #Test case 2: Probation case
    print("\nTest2: GPA=2.5, Attendance 70%, No disciplinary, Prerequisites done, No fees")
    result2 = evaluate_student(2.5, 70, False, True, False)
    print("Output:")
    for conclusion in result2:
        print(f"{conclusion}")
    
    
    # Test Case 3: Student with fees
    print("\nTest 3: GPA=3.2, Attendance=85%, No disciplinary, Prereqs done, HAS fees")
    result3 = evaluate_student(3.2, 85, False, True, True)
    print("Output:")
    for conclusion in result3:
        print(f"{conclusion}")
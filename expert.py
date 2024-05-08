class ExpertSystem: 
    def __init__(self): 
        self.knowledge_base = { 
"Common Cold": {"Symptoms": ["runny nose", "sneezing", "cough", "sore throat"], 
"Treatment": "Rest and fluids"}, 
"Influenza": {"Symptoms": ["fever", "chills", "muscle aches", "fatigue"], "Treatment": 
"Antiviral medication"}, 
"Food Poisoning": {"Symptoms": ["nausea", "vomiting", "diarrhea", "stomach cramps"], 
"Treatment": "Hydration and rest"} 
} 
        
    def diagnose(self, symptoms): 
        matched_conditions = [] 
        for condition, info in self.knowledge_base.items(): 
            if all(symptom in symptoms for symptom in info["Symptoms"]): 
                matched_conditions.append(condition) 
        return matched_conditions 
    
    def get_treatment(self, condition): 
        if condition in self.knowledge_base: 
            return self.knowledge_base[condition]["Treatment"] 
        else: 
            return "Sorry, I'm not familiar with that condition." 
        
#Example usage:  
expert_system = ExpertSystem() 
print("Welcome to the Hospital Expert System!") 
print("Please describe your symptoms (comma-separated): ") 
user_input = input().lower().split(',') 
matched_conditions = expert_system.diagnose(user_input) 
if matched_conditions: 
    print("Based on your symptoms, you may have:") 
    for condition in matched_conditions: 
        print("- " + condition) 
        print("Recommended treatment:", expert_system.get_treatment(condition)) 
else: 
    print("Sorry, I couldn't identify any matching conditions based on your symptoms.") 
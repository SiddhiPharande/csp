import tkinter as tk
from tkinter import messagebox


class ExpertSystem:
    def __init__(self):
        self.rules = {
            'Fever': ['Flu', 'Common Cold'],
            'Cough': ['Flu', 'Common Cold', 'Pneumonia'],
            'Headache': ['Migraine', 'Tension Headache', 'Sinusitis'],
            # Add more symptoms and associated diseases as needed
        }

    def diagnose(self, symptoms):
        possible_diseases = set()
        for symptom in symptoms:
            if symptom in self.rules:
                possible_diseases.update(self.rules[symptom])
        return possible_diseases

class MedicalExpertApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Expert System")
        self.expert_system = ExpertSystem()

        self.symptoms_label = tk.Label(master, text="Enter your symptoms separated by commas:")
        self.symptoms_label.pack()

        self.symptoms_entry = tk.Entry(master, width=50)
        self.symptoms_entry.pack()

        self.diagnose_button = tk.Button(master, text="Diagnose", command=self.diagnose)
        self.diagnose_button.pack()

    def diagnose(self):
        symptoms = self.symptoms_entry.get().strip().split(',')
        possible_diseases = self.expert_system.diagnose(symptoms)
        if possible_diseases:
            messagebox.showinfo("Diagnosis", "Possible diseases based on your symptoms:\n" + ", ".join(possible_diseases))
        else:
            messagebox.showinfo("Diagnosis", "No diseases found based on the provided symptoms.")

def main():
    root = tk.Tk()
    app = MedicalExpertApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

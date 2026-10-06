from disease_info import disease_data

class CropDiseaseAgent:

    def analyze_disease(self, disease_name, confidence):

        info = disease_data.get(disease_name, {})

        return {
            "Disease": disease_name,
            "Confidence": f"{confidence:.2f}%",
            "Symptoms": info.get("Symptoms", "N/A"),
            "Cause": info.get("Cause", "N/A"),
            "Treatment": info.get("Treatment", "N/A"),
            "Prevention": info.get("Prevention", "N/A"),
            "Pesticides": info.get("Pesticides", "N/A"),
            "Usage": info.get("Usage", "N/A"),
            "Solution": info.get("Solution", "N/A"),
            "Recommendations": info.get("Recommendations", [])
        }
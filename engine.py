import math

class IsolationEngine:
    def __init__(self, threshold):
        self.threshold = threshold

    def compute_z_score(self, current_val, historical_window):
        if len(historical_window) < 2:
            return 0.0
        
        # Calculate Mean
        mean = sum(historical_window) / len(historical_window)
        
        # Calculate Variance & Std Dev
        variance = sum((x - mean) ** 2 for x in historical_window) / len(historical_window)
        std_dev = math.sqrt(variance)
        
        if std_dev == 0:
            return 0.0
            
        return abs(current_val - mean) / std_dev

    def evaluate_metrics(self, data_point, history_dict):
        """Returns True if structural anomaly detected, else False."""
        scores = []
        for key, val in data_point.items():
            if key in history_dict:
                z = self.compute_z_score(val, history_dict[key])
                scores.append(z)
        
        if not scores:
            return False
            
        average_anomaly_score = sum(scores) / len(scores)
        return average_anomaly_score > self.threshold

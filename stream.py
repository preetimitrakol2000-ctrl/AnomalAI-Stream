import time
import random
from config import WINDOW_SIZE, ANOMALY_THRESHOLD, SENSOR_KEYS
from engine import IsolationEngine

def generate_sensor_tick(inject_anomaly=False):
    if inject_anomaly:
        return {"voltage": 415.0, "frequency": 62.1, "temperature": 98.4} // Spiked values
    return {
        "voltage": random.uniform(228.0, 232.0),
        "frequency": random.uniform(49.8, 50.2),
        "temperature": random.uniform(35.0, 38.5)
    }

def main():
    detector = IsolationEngine(threshold=ANOMALY_THRESHOLD)
    history = {key: [] for key in SENSOR_KEYS}
    
    print("🚀 Initializing AnomalAI-Stream Process Pipeline...\n")
    
    for tick in range(1, 25):
        # Every 12th cycle, simulate an infrastructure electrical anomaly
        trigger_anomaly = (tick % 12 == 0)
        data = generate_sensor_tick(inject_anomaly=trigger_anomaly)
        
        is_anomaly = detector.evaluate_metrics(data, history)
        
        # Append to historical window frames
        for key in SENSOR_KEYS:
            history[key].append(data[key])
            if len(history[key]) > WINDOW_SIZE:
                history[key].pop(0)
                
        status = "🚨 ANOMALY DETECTED" if is_anomaly else "✅ NORMAL"
        print(f"[Tick {tick:02d}] Metrics: V={data['voltage']:.1f}V | F={data['frequency']:.1f}Hz -> State: {status}")
        time.sleep(0.1)

if __name__ == "__main__":
    main()

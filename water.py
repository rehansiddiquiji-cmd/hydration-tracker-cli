# Simple Daily Water Consumption Logger
class WaterTracker:
    def __init__(self, target_ml=3000):
        self.target_ml = target_ml
        self.current_ml = 0

    def add_water(self, amount_ml):
        self.current_ml += amount_ml
        print(f"Added {amount_ml}ml. Total today: {self.current_ml}/{self.target_ml}ml.")
        if self.current_ml >= self.target_ml:
            print("🎉 Daily hydration goal reached!")

# Example usage
tracker = WaterTracker()
tracker.add_water(500)
tracker.add_water(1000)
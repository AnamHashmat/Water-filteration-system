class WaterFiltrationSystem:
    def __init__(self):
        self.stages = ["Sedimentation", "Filtration", "Disinfection"]

    def sedimentation(self, water):
        print("Performing sedimentation...")
        return f"{water} with sediments removed"

    def filtration(self, water):
        print("Performing filtration...")
        return f"{water} filtered through fine media"

    def disinfection(self, water):
        print("Performing disinfection...")
        return f"{water} disinfected with chlorine"

    def process_water(self, water):
        print("Starting water filtration process...")
        for stage in self.stages:
            if stage == "Sedimentation":
                water = self.sedimentation(water)
            elif stage == "Filtration":
                water = self.filtration(water)
            elif stage == "Disinfection":
                water = self.disinfection(water)
        print("Water filtration process completed.")
        return water



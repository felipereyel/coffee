from dataclasses import dataclass

@dataclass
class RecipeStep:
    name: str
    description: str
    time: int

@dataclass
class Recipe:
    name: str
    description: str
    steps: list[RecipeStep]

    @property
    def time(self):
        return sum(step.time for step in self.steps)

# Medium
medium = Recipe('Medium', 'A medium cup of coffee (150ml of water, 10g of coffee)', [
    RecipeStep('Boil water', 'Boil 250ml of water', 1),
    RecipeStep('Rinse paper filter', 'Rinse paper filter with hot water', 1),
    RecipeStep('Add coffee', 'Add 10g of coffee', 1),
    RecipeStep('First Pour', 'Pour 60ml of water', 30),
    RecipeStep('Second Pour', 'Pour 90ml of water', 150),
])
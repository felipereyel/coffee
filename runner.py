import abstra.forms as af, recipes, time

def run(recipe: recipes.Recipe):
    af.display_markdown('\n'.join([
        f'# {recipe.name}',
        recipe.description,
        f'### Time: {recipe.time} seconds',
    ]), actions=['Brew'])

    for step in recipe.steps:
        counter = 0
        text = f'{step.name} ({step.time} seconds): {step.description}'

        while counter <= step.time:
            af.display_progress(counter, step.time, text=text)
            time.sleep(1)
            counter += 1

        af.display(text, actions=['Done'])

    af.display_markdown('## Done\n ### Enjoy your coffee!', end_program=True)

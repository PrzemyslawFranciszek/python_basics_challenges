## program will generate poetry
import random

nouns = ["fossil", "horse", "aardvark", "judge",
         "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps",
        "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous",
              "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into",
                "beneath", "upon", "for", "in", "like",
                "over", "within"]
adverbs = ["curiously", "extravagantly",
           "tantalizingly", "furiously", "sensously"]

def drawning(drawed_list, mul_function):
    """Return a random list of strings from list"""
    empty_list = []
    for turn in range(mul_function):
        choice = random.choice(drawed_list)
        empty_list.append(choice)
    return empty_list
drawed_nouns = drawning(nouns, 3)
drawed_verbs = drawning(verbs, 3)
drawed_adjectives = drawning(adjectives, 3)
drawed_prepositions = drawning(prepositions, 2)
drawed_adverbs = drawning(adverbs,1)

print(f"A/An {drawed_adjectives[0]} {drawed_nouns[0]}\n\n"
      f"A/An {drawed_adjectives[0]} {drawed_nouns[0]} {drawed_verbs[0]}"
      f" {drawed_prepositions[0]} the {drawed_adjectives[1]} {drawed_nouns[1]}\n"
      f"{drawed_adverbs[0]}, the {drawed_nouns[0]} {drawed_verbs[1]}\n"
      f"the {drawed_nouns[1]} {drawed_verbs[2]} {drawed_prepositions[1]} "
      f"a {drawed_adjectives[2]} {drawed_nouns[2]}")

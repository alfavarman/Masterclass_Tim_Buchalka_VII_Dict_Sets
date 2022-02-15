text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
# split `text` to list of words
# intersection of the set of words with preposition set
# preps_used

preps_used_l = text.split()
preps_used = set(preps_used_l)
preps_used.intersection_update(prepositions)
print(preps_used)
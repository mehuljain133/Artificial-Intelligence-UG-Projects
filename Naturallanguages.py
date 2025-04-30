# Understanding Natural Languages: Overview of linguistics, Chomsky hierarchy of grammars,parsing techniques.

import nltk
from nltk import CFG
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ChartParser, RecursiveDescentParser

# --- Setup (Download once) ---
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# --- Part 1: Linguistics Overview ---
def linguistics_analysis(sentence):
    print("\n--- LINGUISTICS OVERVIEW ---")
    tokens = word_tokenize(sentence)
    print("Tokens:", tokens)

    pos_tags = pos_tag(tokens)
    print("POS Tags:", pos_tags)

# --- Part 2: Chomsky Type-2 CFG Grammar ---
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'a' | 'the'
    N -> 'man' | 'dog' | 'park' | 'telescope'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
""")

# --- Part 3: Parsing Techniques ---
def parse_sentence(sentence):
    print("\n--- PARSING TECHNIQUES ---")
    tokens = word_tokenize(sentence)
    print("Tokens:", tokens)

    print("\nTop-Down Parsing (Recursive Descent):")
    try:
        top_down = RecursiveDescentParser(grammar)
        for tree in top_down.parse(tokens):
            print(tree)
    except Exception as e:
        print("Top-Down Parser Error:", e)

    print("\nBottom-Up Parsing (Chart Parser):")
    bottom_up = ChartParser(grammar)
    for tree in bottom_up.parse(tokens):
        print(tree)

# --- Unified Main Function ---
def main():
    sentence = "I saw a man with a telescope"
    linguistics_analysis(sentence)
    parse_sentence(sentence)

if __name__ == "__main__":
    main()

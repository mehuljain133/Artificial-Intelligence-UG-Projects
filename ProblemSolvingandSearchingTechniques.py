# Problem Solving and Searching Techniques: Problem characteristics, production systems,control strategies, breadth first search, depth first search, hill climbing and its variations,heuristics search techniques: best first search, A* algorithm, constraint satisfaction problem,means-end analysis.

import math
from collections import defaultdict

# --- 1. Uncertainty Example ---
class Uncertainty:
    def __init__(self, belief):
        self.belief = belief  # Belief between 0 and 1

    def is_confident(self, threshold=0.7):
        return self.belief >= threshold

# --- 2. Non-Monotonic Reasoning Example ---
class NonMonotonicReasoner:
    def __init__(self):
        self.knowledge_base = set()

    def add_fact(self, fact):
        self.knowledge_base.add(fact)

    def retract_fact(self, fact):
        self.knowledge_base.discard(fact)

    def infer(self, query):
        return query in self.knowledge_base

# --- 3. Truth Maintenance System (Simplified) ---
class TruthMaintenanceSystem:
    def __init__(self):
        self.justifications = defaultdict(list)
        self.beliefs = set()

    def add_belief(self, belief, reason):
        self.beliefs.add(belief)
        self.justifications[belief].append(reason)

    def retract_belief(self, belief):
        if belief in self.beliefs:
            self.beliefs.remove(belief)
            del self.justifications[belief]

    def explain(self, belief):
        return self.justifications.get(belief, [])

# --- 4. Default Reasoning with Closed World Assumption ---
class DefaultReasoner:
    def __init__(self, facts):
        self.facts = facts

    def assume(self, query):
        # If it's not in facts, assume false (Closed World Assumption)
        return query in self.facts

# --- 5. Bayesian Probabilistic Inference ---
class BayesianInference:
    def __init__(self):
        self.prior = {}       # P(H)
        self.likelihood = {}  # P(E|H)

    def set_probabilities(self, prior, likelihood):
        self.prior = prior
        self.likelihood = likelihood

    def infer(self, evidence):
        posterior = {}
        for h in self.prior:
            posterior[h] = self.likelihood[evidence][h] * self.prior[h]
        norm = sum(posterior.values())
        for h in posterior:
            posterior[h] /= norm
        return posterior

# --- 6. Fuzzy Sets and Logic ---
class FuzzySet:
    def __init__(self, name, membership_func):
        self.name = name
        self.membership_func = membership_func  # e.g., lambda x: min(1, max(0, (x-10)/10))

    def membership(self, value):
        return self.membership_func(value)

# --- 7. Fuzzy Reasoning ---
class FuzzyReasoning:
    def __init__(self):
        self.rules = []

    def add_rule(self, fuzzy_input, fuzzy_output):
        self.rules.append((fuzzy_input, fuzzy_output))

    def reason(self, input_value):
        output_values = []
        for fuzzy_input, fuzzy_output in self.rules:
            degree = fuzzy_input.membership(input_value)
            output_values.append((fuzzy_output.name, degree))
        return output_values

# --- Main Function to Demonstrate All Concepts ---
def main():
    print("\n1. Uncertainty:")
    belief = Uncertainty(0.8)
    print("Is belief confident?", belief.is_confident())  # True

    print("\n2. Non-Monotonic Reasoning:")
    reasoner = NonMonotonicReasoner()
    reasoner.add_fact("Birds can fly")
    print("Can birds fly?", reasoner.infer("Birds can fly"))  # True
    reasoner.add_fact("Penguins are birds")
    reasoner.retract_fact("Birds can fly")  # Non-monotonic update
    print("Can birds fly (after learning about penguins)?", reasoner.infer("Birds can fly"))  # False

    print("\n3. Truth Maintenance System:")
    tms = TruthMaintenanceSystem()
    tms.add_belief("Earth is round", "Scientific evidence")
    tms.add_belief("Sun rises in east", "Observation")
    print("Explanation for 'Earth is round':", tms.explain("Earth is round"))

    print("\n4. Default Reasoning & Closed World Assumption:")
    facts = {"Sky is blue", "Grass is green"}
    default_reasoner = DefaultReasoner(facts)
    print("Is 'Water is wet' assumed true?", default_reasoner.assume("Water is wet"))  # False
    print("Is 'Sky is blue' assumed true?", default_reasoner.assume("Sky is blue"))  # True

    print("\n5. Bayesian Inference:")
    bayes = BayesianInference()
    bayes.set_probabilities(
        prior={'Rain': 0.3, 'NoRain': 0.7},
        likelihood={'Cloudy': {'Rain': 0.8, 'NoRain': 0.2}}
    )
    result = bayes.infer('Cloudy')
    print("P(Rain | Cloudy):", result['Rain'])  # Should be high

    print("\n6. Fuzzy Sets:")
    cold = FuzzySet("Cold", lambda x: max(0, min(1, (20 - x) / 10)))  # Membership for cold
    print("Cold membership of 15°C:", cold.membership(15))  # 0.5

    print("\n7. Fuzzy Reasoning:")
    fuzzy_reasoner = FuzzyReasoning()
    hot = FuzzySet("Hot", lambda x: max(0, min(1, (x - 20) / 10)))
    fuzzy_reasoner.add_rule(cold, hot)
    print("Fuzzy reasoning for 15°C:", fuzzy_reasoner.reason(15))  # [(‘Hot’, degree)]

if __name__ == "__main__":
    main()

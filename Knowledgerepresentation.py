# Knowledge Representation: Propositional logic, first order predicate logic, resolution principle,unification, semantic nets, conceptual dependencies, frames, scripts, production rules, conceptualgraphs.

# Knowledge Representation: Propositional Logic, Predicate Logic, Semantic Nets, and more

# --- Propositional Logic ---
class PropositionalLogic:
    def __init__(self, symbols, truth_values):
        self.symbols = symbols  # List of symbols (propositions)
        self.truth_values = truth_values  # Dictionary of truth values

    def evaluate(self, expression):
        # Simple evaluation of a propositional expression
        return self.truth_values.get(expression, None)

# --- First-Order Predicate Logic (Simplified) ---
class PredicateLogic:
    def __init__(self, predicates):
        self.predicates = predicates  # Dictionary of predicates and their truth values

    def evaluate(self, predicate, *args):
        # Simple evaluation based on arguments for predicates
        if predicate in self.predicates:
            return self.predicates[predicate](*args)
        return None

# --- Resolution Principle (Simple Example) ---
class Resolution:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def resolve(self, query):
        # Simulating resolution by checking if the fact matches the query
        return query in self.facts

# --- Unification ---
class Unification:
    def unify(self, term1, term2):
        if term1 == term2:
            return True
        return False

# --- Semantic Nets ---
class SemanticNet:
    def __init__(self):
        self.network = {}  # Dictionary for semantic net representation

    def add_relation(self, entity1, relation, entity2):
        if entity1 not in self.network:
            self.network[entity1] = []
        self.network[entity1].append((relation, entity2))

    def get_relations(self, entity):
        return self.network.get(entity, [])

# --- Conceptual Dependencies ---
class ConceptualDependency:
    def __init__(self):
        self.dependencies = {}

    def add_dependency(self, action, subject, object):
        self.dependencies[action] = (subject, object)

    def get_dependency(self, action):
        return self.dependencies.get(action, None)

# --- Frames ---
class Frame:
    def __init__(self, name):
        self.name = name
        self.slots = {}

    def add_slot(self, slot_name, value):
        self.slots[slot_name] = value

    def get_slot(self, slot_name):
        return self.slots.get(slot_name, None)

# --- Scripts ---
class Script:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def get_elements(self):
        return self.elements

# --- Production Rules ---
class ProductionRule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def apply(self, facts):
        if self.condition(facts):
            return self.action(facts)
        return None

# --- Conceptual Graphs ---
class ConceptualGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, attributes):
        self.graph[node] = attributes

    def get_node(self, node):
        return self.graph.get(node, None)

# --- Main Code to Demonstrate All Concepts ---
def main():
    # Propositional Logic
    print("\nPropositional Logic Example:")
    prop_logic = PropositionalLogic(['P', 'Q'], {'P': True, 'Q': False})
    print("P:", prop_logic.evaluate('P'))  # True
    print("Q:", prop_logic.evaluate('Q'))  # False

    # Predicate Logic
    print("\nFirst-Order Predicate Logic Example:")
    pred_logic = PredicateLogic({'father': lambda x: x == 'John'})
    print("father('John'):", pred_logic.evaluate('father', 'John'))  # True
    print("father('Paul'):", pred_logic.evaluate('father', 'Paul'))  # False

    # Resolution Principle
    print("\nResolution Example:")
    res = Resolution()
    res.add_fact('John is a father')
    print("Resolution on 'John is a father':", res.resolve('John is a father'))  # True
    print("Resolution on 'John is a teacher':", res.resolve('John is a teacher'))  # False

    # Unification
    print("\nUnification Example:")
    unify = Unification()
    print("Unification of 'a' and 'a':", unify.unify('a', 'a'))  # True
    print("Unification of 'a' and 'b':", unify.unify('a', 'b'))  # False

    # Semantic Net
    print("\nSemantic Net Example:")
    net = SemanticNet()
    net.add_relation('John', 'is a', 'father')
    net.add_relation('John', 'likes', 'ice cream')
    print("John's relations:", net.get_relations('John'))  # [('is a', 'father'), ('likes', 'ice cream')]

    # Conceptual Dependencies
    print("\nConceptual Dependencies Example:")
    cd = ConceptualDependency()
    cd.add_dependency('eat', 'John', 'apple')
    print("Dependency for 'eat':", cd.get_dependency('eat'))  # ('John', 'apple')

    # Frames
    print("\nFrame Example:")
    frame = Frame('Person')
    frame.add_slot('name', 'John')
    frame.add_slot('age', 30)
    print("Person frame:", frame.slots)  # {'name': 'John', 'age': 30}

    # Scripts
    print("\nScript Example:")
    script = Script('Buying')
    script.add_element('John goes to store')
    script.add_element('John buys an apple')
    print("Buying script elements:", script.get_elements())

    # Production Rules
    print("\nProduction Rule Example:")
    rule = ProductionRule(lambda facts: 'rain' in facts, lambda facts: "Take an umbrella")
    facts = ['rain']
    print("Action after applying rule:", rule.apply(facts))  # "Take an umbrella"

    # Conceptual Graphs
    print("\nConceptual Graph Example:")
    cg = ConceptualGraph()
    cg.add_node('John', {'type': 'Person', 'age': 30})
    print("John's conceptual graph:", cg.get_node('John'))  # {'type': 'Person', 'age': 30}

if __name__ == "__main__":
    main()

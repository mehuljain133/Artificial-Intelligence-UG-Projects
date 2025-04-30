# Introduction: Introduction to artificial intelligence, background and applications, Turing test,rational agents, intelligent agents, structure, behaviour and environment of intelligent agents.

# Full AI Example: Combining Turing Test, Rational Agents, and Intelligent Agents

# --- Turing Test Implementation ---
class ChatBot:
    def __init__(self):
        self.responses = {
            "Hello": "Hi, how can I help you?",
            "How are you?": "I'm good, thank you for asking!",
            "What is AI?": "Artificial Intelligence is the simulation of human intelligence in machines.",
        }
    
    def respond(self, user_input):
        return self.responses.get(user_input, "Sorry, I didn't understand that.")

# --- Rational Agent Implementation ---
class RationalAgent:
    def __init__(self, name):
        self.name = name
        self.knowledge = {}
    
    def perceive(self, environment):
        # Perceiving the environment
        self.knowledge = environment

    def act(self):
        # Act based on the knowledge of the environment
        if 'temperature' in self.knowledge and self.knowledge['temperature'] > 30:
            return "Turn on the AC"
        return "Do nothing"

# --- Intelligent Agent Implementation ---
class IntelligentAgent:
    def __init__(self, name):
        self.name = name
        self.knowledge = {}

    def perceive(self, environment):
        # Sensing the environment
        self.knowledge = environment

    def reason(self):
        # Reasoning based on knowledge
        if self.knowledge.get('goal') == 'maximize profit':
            return "Invest in stocks"
        elif self.knowledge.get('goal') == 'reduce cost':
            return "Cut unnecessary expenses"
        return "Evaluate options"

    def act(self):
        # Acting based on reasoned action
        action = self.reason()
        print(f"{self.name} decides to: {action}")

# --- Structure and Behavior of Intelligent Agents ---
class AgentStructure:
    def __init__(self):
        self.sensors = None
        self.actuators = None
        self.knowledge_base = {}

class IntelligentBehavior:
    def __init__(self, structure):
        self.structure = structure
        
    def update_behavior(self, environment):
        self.structure.sensors = environment
        self.structure.knowledge_base = environment
    
    def perform_action(self):
        # Perform action based on environment
        if self.structure.knowledge_base.get('action') == 'run':
            print("Performing run action...")
        else:
            print("Performing idle action...")

# --- Main Execution of All Concepts ---
def main():
    # Turing Test Example (ChatBot)
    print("Turing Test Example:")
    bot = ChatBot()
    user_input = input("You: ")
    response = bot.respond(user_input)
    print("Bot: " + response)
    
    # Rational Agent Example
    print("\nRational Agent Example:")
    environment = {'temperature': 35}  # Assume it's hot
    agent_rational = RationalAgent("Agent1")
    agent_rational.perceive(environment)
    action = agent_rational.act()
    print(f"Agent {agent_rational.name} decides to: {action}")
    
    # Intelligent Agent Example
    print("\nIntelligent Agent Example:")
    environment = {'goal': 'maximize profit'}  # The agent's goal
    agent_intelligent = IntelligentAgent("SmartAgent")
    agent_intelligent.perceive(environment)
    agent_intelligent.act()
    
    # Structure and Behavior of Intelligent Agent Example
    print("\nStructure and Behavior Example:")
    environment = {'action': 'run'}
    structure = AgentStructure()
    behavior = IntelligentBehavior(structure)
    behavior.update_behavior(environment)
    behavior.perform_action()

# --- Run the Main Program ---
if __name__ == "__main__":
    main()

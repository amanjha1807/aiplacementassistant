class ConversationMemory:

    def __init__(self):

        self.company = None
        self.intent = None
        self.topic = None
        self.history = []

    # ----------------------------------

    def update(self, analysis, query):

        if analysis.get("company"):
            self.company = analysis["company"]

        if analysis.get("intent"):
            self.intent = analysis["intent"]

        if analysis.get("topic"):
            self.topic = analysis["topic"]

        self.history.append(query)

        # Keep only last 10 queries
        self.history = self.history[-10:]

    # ----------------------------------

    def get_context(self):

        return {

            "company": self.company,

            "intent": self.intent,

            "topic": self.topic,

            "history": self.history

        }

    # ----------------------------------

    def clear(self):

        self.company = None
        self.intent = None
        self.topic = None
        self.history = []


memory = ConversationMemory()
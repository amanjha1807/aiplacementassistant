import re

# ==========================================================
# COMPANY LIST
# ==========================================================

COMPANIES = [
    # Product Based
    "Amazon",
    "Google",
    "Microsoft",
    "Meta",
    "Apple",
    "Netflix",
    "Adobe",
    "Uber",
    "Flipkart",
    "Ola",
    "Meesho",
    "Paytm",
    "PhonePe",
    "Razorpay",
    "Salesforce",
    "ServiceNow",
    "Swiggy",
    "Zomato",
    "CRED",
    "Zoho",
    "Atlassian",
    "Freshworks",

    # Service Based
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Capgemini",
    "Cognizant",
    "HCLTech",
    "LTIMindtree",
    "Tech Mahindra"
]

# ==========================================================
# INTENT KEYWORDS
# ==========================================================

INTENTS = {

    "oa": [
        "oa",
        "online assessment",
        "online test",
        "assessment",
        "aptitude"
    ],

    "recruitment": [
        "recruitment",
        "hiring",
        "selection process",
        "recruitment process",
        "hiring process"
    ],

    "interview": [
        "interview",
        "technical interview",
        "hr interview",
        "interview rounds",
        "rounds"
    ],

    "experience": [
        "experience",
        "candidate experience",
        "interview experience"
    ],

    "dsa": [
        "dsa",
        "array",
        "arrays",
        "string",
        "strings",
        "linked list",
        "stack",
        "queue",
        "tree",
        "graph",
        "graphs",
        "heap",
        "trie",
        "dynamic programming",
        "dp",
        "recursion",
        "backtracking",
        "greedy",
        "sliding window"
    ],

    "system_design": [
        "system design",
        "lld",
        "hld",
        "low level design",
        "high level design"
    ],

    "projects": [
        "project",
        "projects",
        "resume project"
    ],

    "hr": [
        "hr",
        "behavioral",
        "managerial",
        "tell me about yourself"
    ],

    "salary": [
        "salary",
        "package",
        "ctc",
        "pay"
    ]
}

# ==========================================================
# SECTION PRIORITY
# ==========================================================

SECTION_MAP = {

    "oa": [
        "Hiring Process",
        "Interview Rounds"
    ],

    "recruitment": [
        "Hiring Process"
    ],

    "interview": [
        "Interview Rounds"
    ],

    "experience": [
        "Sample Candidate Experience"
    ],

    "dsa": [
        "Interview Rounds",
        "Preparation Tips"
    ],

    "system_design": [
        "Interview Rounds",
        "Preparation Tips"
    ],

    "projects": [
        "Preparation Tips"
    ],

    "hr": [
        "Interview Rounds"
    ],

    "salary": [
        "Overview"
    ]
}


# ==========================================================
# DETECT COMPANY
# ==========================================================

def detect_company(query: str):

    query = query.lower()

    for company in COMPANIES:

        pattern = r"\b" + re.escape(company.lower()) + r"\b"

        if re.search(pattern, query):
            return company

    return None


# ==========================================================
# DETECT INTENT
# ==========================================================

def detect_intent(query: str):

    query = query.lower()

    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            if keyword in query:
                return intent

    return None


# ==========================================================
# MAIN ANALYZER
# ==========================================================

def analyze_query(query: str):

    company = detect_company(query)

    intent = detect_intent(query)

    sections = SECTION_MAP.get(intent, [])

    query_type = "company" if company else "global"

    return {

        "original_query": query,

        "company": company,

        "intent": intent,

        "sections": sections,

        "query_type": query_type

    }
    return {

    "original_query": query,

    "company": company,

    "intent": intent,

    "topic": None,

    "sections": sections,

    "query_type": query_type
}


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    while True:

        query = input("\nAsk Question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        result = analyze_query(query)

        print("\nDetected Query")
        print("-" * 40)

        for key, value in result.items():

            print(f"{key:15}: {value}")
            
            


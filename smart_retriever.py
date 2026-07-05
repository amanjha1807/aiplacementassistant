from load_vectorstore import vectorstore

# ----------------------------------------------------
# Supported Companies
# ----------------------------------------------------

COMPANIES = [
    "Adobe",
    "Amazon",
    "Apple",
    "Atlassian",
    "Cred",
    "Flipkart",
    "Freshworks",
    "Google",
    "Meesho",
    "Meta",
    "Microsoft",
    "Netflix",
    "Ola",
    "Paytm",
    "PhonePe",
    "Razorpay",
    "Salesforce",
    "ServiceNow",
    "Swiggy",
    "Uber",
    "Zoho",
    "Zomato",

    "Accenture",
    "Capgemini",
    "Cognizant",
    "HCLTech",
    "Infosys",
    "LTIMindtree",
    "TCS",
    "Tech Mahindra",
    "Wipro"
]


# ----------------------------------------------------
# Company Extraction
# ----------------------------------------------------

def extract_company(query):

    query_lower = query.lower()

    for company in COMPANIES:

        if company.lower() in query_lower:
            return company

    return None


# ----------------------------------------------------
# Smart Retrieval
# ----------------------------------------------------

def smart_retrieve(query, k=5):

    company = extract_company(query)

    print("\nDetected Company :", company)

    if company:

        print("Using Metadata Filtering...\n")

        results = vectorstore.similarity_search(
            query=query,
            k=k,
            filter={
                "company_name": company
            }
        )

    else:

        print("Using Normal Semantic Search...\n")

        results = vectorstore.similarity_search(
            query=query,
            k=k
        )

    return results


# ----------------------------------------------------
# Interactive Testing
# ----------------------------------------------------

if __name__ == "__main__":

    while True:

        query = input("\nAsk Question (type exit to quit): ")

        if query.lower() == "exit":
            break

        docs = smart_retrieve(query)

        print("\nReturned Chunks :", len(docs))

        for i, doc in enumerate(docs):

            print("=" * 100)
            print(f"Result {i+1}\n")

            print("Metadata:")
            print(doc.metadata)

            print("\nContent:")
            print(doc.page_content[:500])
            print()
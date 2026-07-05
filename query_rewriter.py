from conversation_memory import memory
from query_analyzer import analyze_query


def rewrite_query(query):

    analysis = analyze_query(query)

    context = memory.get_context()

    company = analysis["company"]

    if company is None:

        company = context["company"]

    if company:

        if company.lower() not in query.lower():

            query = f"{company} {query}"

    return query
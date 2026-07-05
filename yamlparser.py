import yaml
import re
text = """
     ---
  company: "Amazon"
  type: "Product-based"
  category: "company_experience"
  year: 2026
   ---

# Amazon

## Hiring Process

Amazon has an Online Assessment followed by interviews.
"""




def extract_metadata(text: str):

    match = re.match(
        r"^---\s*\n(.*?)\n---\s*\n?",
        text,
        flags=re.DOTALL
    )

    metadata = {}

    if match:

        try:
            metadata = yaml.safe_load(match.group(1))

            if metadata is None:
                metadata = {}

        except yaml.YAMLError:

            metadata = {}

        content = text[match.end():].strip()

    else:

        content = text.strip()

    return metadata, content



from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# Tool to read a doc
@mcp.tool()
def read_doc(doc_id: str) -> str:
    """Read the contents of a document by its ID."""
    if doc_id in docs:
        return docs[doc_id]
    else:
        return f"Error: Document with ID '{doc_id}' not found."

# Tool to edit a doc
@mcp.tool()
def edit_doc(doc_id: str, new_content: str) -> str:
    """Edit the contents of a document by its ID."""
    if doc_id in docs:
        docs[doc_id] = new_content
        return f"Document '{doc_id}' updated successfully."
    else:
        return f"Error: Document with ID '{doc_id}' not found."

# Resource to return all doc IDs
@mcp.resource("docs://list")
def list_docs() -> list:
    """Return a list of all document IDs."""
    return list(docs.keys())

# Resource to return the contents of a particular doc
@mcp.resource("docs://{doc_id}")
def get_doc_content(doc_id: str) -> str:
    """Return the contents of a particular document."""
    if doc_id in docs:
        return docs[doc_id]
    else:
        return f"Error: Document with ID '{doc_id}' not found."

# Prompt to rewrite a doc in Markdown format
@mcp.prompt()
def rewrite_to_markdown(doc_id: str) -> str:
    """Rewrite a document in Markdown format."""
    if doc_id in docs:
        content = docs[doc_id]
        return f"""Please rewrite the following document content in markdown format:

Document ID: {doc_id}
Content: {content}

Please provide a well-formatted markdown version of this content with appropriate structure, headings, and formatting."""
    else:
        return f"Error: Document with ID '{doc_id}' not found."

# Prompt to summarize a doc
@mcp.prompt()
def summarize_doc(doc_id: str) -> str:
    """Summarize a document."""
    if doc_id in docs:
        content = docs[doc_id]
        return f"""Please provide a concise summary of the following document:

Document ID: {doc_id}
Content: {content}

Please extract the key points and provide a brief summary."""
    else:
        return f"Error: Document with ID '{doc_id}' not found."

if __name__ == "__main__":
    mcp.run(transport="stdio")

import requests 
import time
from datetime import datetime

def fetch_source_documents(source_token):
    all_docs = []
    next_page = None
    while True:
        params = {'withHtmlContent': 'true'}
        if next_page:
            params['pageCursor'] = next_page
        response = requests.get(
            "https://readwise.io/api/v3/list/",
            headers={"Authorization": f"Token {source_token}"},
            params=params
        )
        data = response.json()
        all_docs.extend(data['results'])
        next_page = data.get('nextPageCursor')
        if not next_page:
            break
    return all_docs

def format_date(date_str):
    """Convert date to the required format: YYYY-MM-DDThh:mm:ssZ"""
    if not isinstance(date_str, str) or not date_str.strip():  
        return None  # Skip if not a valid string

    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))  # Ensure UTC format
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")  # Convert to ISO 8601 format
    except ValueError:
        return None  # Ignore invalid date formats

def transfer_documents(source_token, dest_token):
    source_docs = fetch_source_documents(source_token)
    
    for doc in source_docs:
        payload = {
            "url": doc.get('url', ''),
            "html": doc.get('html_content', ''),
            "title": doc.get('title', ''),
            "author": doc.get('author', ''),
            "summary": 'No summary available',  # Ensure summary is not blank
            "published_date": format_date(doc.get('published_date')),  
            "location": doc.get('location', ''),
            "category": doc.get('category', ''),
            "reading_progress": doc.get("reading_progress", 0.05),  # Include reading progress (default 0.05)
            "should_clean_html": False
        }

        # For PDF documents, include the source_url with the raw content endpoint.
        if doc.get('category') == "pdf":
            payload["source_url"] = f"https://readwise.io/reader/document_raw_content/{doc.get('id')}"
        
        # Ensure `notes` is not blank
        notes = doc.get('notes')
        if notes and notes.strip():  
            payload["notes"] = notes

        # Ensure `tags` is a valid list
        tags = doc.get('tags')
        if isinstance(tags, list):  
            payload["tags"] = tags

        # Ensure `image_url` is not empty
        image_url = doc.get('image_url')
        if image_url and image_url.strip():  
            payload["image_url"] = image_url

        # Remove None values to avoid API errors
        payload = {k: v for k, v in payload.items() if v is not None}

        response = requests.post(
            "https://readwise.io/api/v3/save/",
            headers={"Authorization": f"Token {dest_token}"},
            json=payload
        )
        if response.status_code not in [200, 201]:
            print(f"Error transferring {doc.get('id', 'UNKNOWN')}: {response.text}")
        time.sleep(3)  # Stay under rate limit

# Usage
transfer_documents("from_token", "to_token")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from newspaper import Article
import urllib.parse

# ----------------------------
# Google Sheets setup
# ----------------------------
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1anWYzDKOqfbfoLb9mBCaj5KCYyzkaO_pO_vwtFiNP5U/edit#gid=0")
worksheet = sheet.worksheet("Sheet1")

# ----------------------------
# Helper functions
# ----------------------------
def get_real_article_url(google_news_url):
    parsed_url = urllib.parse.urlparse(google_news_url)
    qs = urllib.parse.parse_qs(parsed_url.query)
    real_url = qs.get("url", [google_news_url])[0]
    return real_url


def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text.strip()
        if text == "":
            return "No body extracted, fallback to URL or title..."
        return text
    except:
        return "No body extracted, fallback to URL or title..."


def generate_linkedin_post(article_text):
    # Fallback: just reuse the article text (or first 200 words) if no summarization
    words = article_text.split()
    snippet = " ".join(words[:200]) if len(words) > 200 else article_text
    linkedin_post = f"Sharing insights from this article:\n\n{snippet}\n\n#Business #Startup #India"
    return linkedin_post

# ----------------------------
# Main loop: read URLs from Column 1 and populate Columns 2 and 3
# ----------------------------
urls = worksheet.col_values(1)  # Assuming URLs start from row 1
for i, google_news_url in enumerate(urls, start=2):
    if google_news_url.strip() == "":
        continue

    real_url = get_real_article_url(google_news_url)
    article_text = scrape_article(real_url)
    linkedin_post = generate_linkedin_post(article_text)

    worksheet.update_cell(i, 2, article_text)
    worksheet.update_cell(i, 3, linkedin_post)

print("Sheet updated successfully!")

"""Antigravity完全攻略ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Antigravity完全攻略ガイド"
BLOG_DESCRIPTION = "Google Antigravity AI IDEの使い方・最新機能・料金・活用術を毎日更新。次世代AIコーディング環境を使いこなすための日本語完全ガイド。"
BLOG_URL = "https://musclelove-777.github.io/antigravity-guide"
BLOG_TAGLINE = "Google発の次世代AI IDE Antigravityを完全攻略"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/antigravity-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Antigravity 使い方",
    "Antigravity 料金・プラン",
    "Antigravity vs Cursor",
    "Antigravity 最新ニュース",
    "Antigravity エージェント機能",
    "Antigravity 活用テクニック",
    "AI IDE比較",
    "Antigravity 設定・カスタマイズ",
]

THEME = {
    "primary": "#00FF88",
    "accent": "#4285F4",
    "gradient_start": "#00FF88",
    "gradient_end": "#4285F4",
    "dark_bg": "#0a0a1a",
    "dark_surface": "#1a1a2e",
    "light_bg": "#f0fff4",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Antigravity": [
        {"service": "Antigravity", "url": "https://idx.google.com", "description": "Google Antigravityを試す"},
    ],
    "Google Cloud": [
        {"service": "Google Cloud", "url": "https://cloud.google.com", "description": "Google Cloudに登録する"},
    ],
    "AI IDE": [
        {"service": "Cursor", "url": "https://cursor.sh", "description": "Cursor公式サイト"},
        {"service": "Windsurf", "url": "https://codeium.com/windsurf", "description": "Windsurf公式サイト"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI IDE講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI開発関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI開発関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8090

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}

#!/usr/bin/env python3
"""
Fixed Ghost to Static HTML converter
- Uses relative paths for local testing
- Homepage shows only excerpts, not full content
"""

import os
import re
import urllib.request
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_URL = "https://humansofwelive.org"
OUTPUT_DIR = Path("site")

def download_file(url, output_path):
    """Download a file"""
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloading: {url}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(output_path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def fetch_url(url):
    """Fetch URL"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return None

def strip_html(html):
    """Remove HTML tags and return clean text"""
    clean = re.sub('<.*?>', '', html)
    clean = clean.replace('&nbsp;', ' ').replace('&amp;', '&')
    clean = ' '.join(clean.split())  # Remove extra whitespace
    return clean

def truncate_text(text, max_length=200):
    """Truncate text to max_length"""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + '...'

def parse_rss():
    """Parse RSS feed"""
    print("Fetching posts from RSS...")
    content = fetch_url(f"{BASE_URL}/rss/")
    if not content:
        return []

    root = ET.fromstring(content)
    posts = []

    for item in root.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else ''
        link = item.find('link').text if item.find('link') is not None else ''
        slug = link.rstrip('/').split('/')[-1]

        # Get description (plain text excerpt)
        desc_elem = item.find('description')
        description = desc_elem.text if desc_elem is not None else ''

        # Get full content
        content_elem = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded')
        content = content_elem.text if content_elem is not None else ''

        # Get author
        author_elem = item.find('.//{http://purl.org/dc/elements/1.1/}creator')
        author = author_elem.text if author_elem is not None else 'Unknown'

        # Get date
        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ''

        # Get featured image
        media_elem = item.find('.//{http://search.yahoo.com/mrss/}content')
        image = media_elem.get('url') if media_elem is not None else ''

        # Create clean excerpt from description
        excerpt = strip_html(description)
        excerpt = truncate_text(excerpt, 200)

        posts.append({
            'title': title,
            'slug': slug,
            'description': description,
            'excerpt': excerpt,
            'content': content,
            'author': author,
            'pub_date': pub_date,
            'image': image
        })

    print(f"Found {len(posts)} posts")
    return posts

def download_image(img_url, output_dir):
    """Download image and return relative path"""
    if not img_url or not img_url.startswith('http'):
        return img_url

    # Parse URL and create local path
    path = img_url.replace(BASE_URL, '')
    local_path = output_dir / path.lstrip('/')

    if not local_path.exists():
        download_file(img_url, local_path)

    return path

def process_images_in_content(content, output_dir):
    """Download images and fix paths"""
    def replace_img(match):
        full_tag = match.group(0)
        img_url = match.group(1)
        if img_url.startswith('http'):
            local_path = download_image(img_url, output_dir)
            return full_tag.replace(img_url, local_path)
        return full_tag

    return re.sub(r'<img[^>]+src=["\']([^"\']+)["\']', replace_img, content)

def create_post_html(post, output_dir):
    """Create individual post page"""
    content = process_images_in_content(post['content'], output_dir)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{post['title']} - Humans of WeLive</title>
    <meta name="description" content="{post['excerpt']}">
    <link rel="icon" href="content/images/size/w256h256/2025/06/The-brand-mark-is-a-simplified-version-of-the--1.jpeg" type="image/jpeg">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        :root {{ --accent-color: #f7b37b; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        .header {{
            background: white;
            border-bottom: 1px solid #e6e6e6;
            padding: 20px 0;
        }}
        .header-inner {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }}
        .nav {{
            list-style: none;
            display: flex;
            gap: 20px;
        }}
        .nav a {{
            color: #333;
            text-decoration: none;
        }}
        .nav a:hover {{ color: var(--accent-color); }}
        .main {{
            max-width: 800px;
            margin: 60px auto;
            padding: 0 20px;
        }}
        .article-title {{
            font-size: 3rem;
            line-height: 1.2;
            margin-bottom: 20px;
            font-weight: 700;
        }}
        .article-meta {{
            color: #666;
            font-size: 14px;
            margin-bottom: 40px;
        }}
        .article-content {{
            font-size: 18px;
            line-height: 1.8;
        }}
        .article-content img {{
            max-width: 100%;
            height: auto;
            margin: 30px 0;
            border-radius: 8px;
        }}
        .article-content figure {{
            margin: 30px 0;
        }}
        .article-content p {{
            margin-bottom: 1.5em;
        }}
        .article-content blockquote {{
            border-left: 4px solid var(--accent-color);
            padding-left: 20px;
            margin: 30px 0;
            font-style: italic;
            color: #555;
        }}
        .article-content h2, .article-content h3 {{
            margin-top: 2em;
            margin-bottom: 0.8em;
            font-weight: 700;
        }}
        .article-content ul, .article-content ol {{
            margin-left: 30px;
            margin-bottom: 1.5em;
        }}
        .article-content li {{
            margin-bottom: 0.5em;
        }}
        .article-content a {{
            color: var(--accent-color);
            text-decoration: underline;
        }}
        .footer {{
            background: #f6f6f6;
            padding: 40px 20px;
            text-align: center;
            margin-top: 80px;
            color: #666;
        }}
        @media (max-width: 768px) {{
            .article-title {{ font-size: 2rem; }}
            .article-content {{ font-size: 16px; }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <nav class="header-inner">
            <a href="index.html" class="logo">Humans of WeLive</a>
            <ul class="nav">
                <li><a href="index.html">Home</a></li>
            </ul>
        </nav>
    </header>
    <main class="main">
        <article>
            <h1 class="article-title">{post['title']}</h1>
            <div class="article-meta">
                By {post['author']} • {post['pub_date']}
            </div>
            <div class="article-content">
                {content}
            </div>
        </article>
    </main>
    <footer class="footer">
        <p>© 2025 Humans of WeLive. We are the people of WeLive Foundation!</p>
    </footer>
</body>
</html>'''

    post_path = output_dir / f"{post['slug']}.html"
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {post_path.name}")

def create_homepage(posts, output_dir):
    """Create homepage with post listing"""
    post_cards = ''

    for post in posts:
        # Download featured image
        img_tag = ''
        if post['image']:
            img_path = download_image(post['image'], output_dir)
            img_tag = f'<img class="post-image" src="{img_path}" alt="{post["title"]}">'

        post_cards += f'''
        <article class="post-card">
            {img_tag}
            <div class="post-content">
                <h2 class="post-title">
                    <a href="{post['slug']}.html">{post['title']}</a>
                </h2>
                <p class="post-excerpt">{post['excerpt']}</p>
                <div class="post-meta">
                    By {post['author']} • {post['pub_date']}
                </div>
            </div>
        </article>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Humans of WeLive</title>
    <meta name="description" content="We are the people of WeLive Foundation!">
    <link rel="icon" href="content/images/size/w256h256/2025/06/The-brand-mark-is-a-simplified-version-of-the--1.jpeg" type="image/jpeg">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        :root {{ --accent-color: #f7b37b; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        .header {{
            background: white;
            border-bottom: 1px solid #e6e6e6;
            padding: 20px 0;
        }}
        .header-inner {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }}
        .nav {{
            list-style: none;
            display: flex;
            gap: 20px;
        }}
        .nav a {{
            color: #333;
            text-decoration: none;
        }}
        .nav a:hover {{ color: var(--accent-color); }}
        .main {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        .hero {{
            text-align: center;
            padding: 60px 0;
        }}
        .hero h1 {{
            font-size: 3.5rem;
            margin-bottom: 20px;
            font-weight: 700;
        }}
        .hero p {{
            font-size: 1.5rem;
            color: #666;
        }}
        .post-list {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 40px;
            margin-top: 60px;
        }}
        .post-card {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
        }}
        .post-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        }}
        .post-image {{
            width: 100%;
            height: 240px;
            object-fit: cover;
        }}
        .post-content {{
            padding: 24px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        .post-title {{
            font-size: 1.5rem;
            margin-bottom: 12px;
            font-weight: 700;
            line-height: 1.3;
        }}
        .post-title a {{
            color: #333;
            text-decoration: none;
        }}
        .post-title a:hover {{
            color: var(--accent-color);
        }}
        .post-excerpt {{
            color: #666;
            font-size: 0.95rem;
            margin-bottom: 16px;
            line-height: 1.6;
            flex: 1;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .post-meta {{
            color: #999;
            font-size: 13px;
            margin-top: auto;
        }}
        .footer {{
            background: #f6f6f6;
            padding: 40px 20px;
            text-align: center;
            margin-top: 80px;
            color: #666;
        }}
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2.5rem; }}
            .hero p {{ font-size: 1.2rem; }}
            .post-list {{
                grid-template-columns: 1fr;
                gap: 30px;
            }}
            .post-image {{ height: 200px; }}
        }}
        @media (min-width: 769px) and (max-width: 1024px) {{
            .post-list {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <nav class="header-inner">
            <a href="index.html" class="logo">Humans of WeLive</a>
            <ul class="nav">
                <li><a href="index.html">Home</a></li>
            </ul>
        </nav>
    </header>
    <main class="main">
        <section class="hero">
            <h1>Humans of WeLive</h1>
            <p>We are the people of WeLive Foundation!</p>
        </section>
        <section class="post-list">
            {post_cards}
        </section>
    </main>
    <footer class="footer">
        <p>© 2025 Humans of WeLive. We are the people of WeLive Foundation!</p>
    </footer>
</body>
</html>'''

    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created: index.html")

def main():
    print("Starting conversion...")
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Download favicon
    favicon_url = f"{BASE_URL}/content/images/size/w256h256/2025/06/The-brand-mark-is-a-simplified-version-of-the--1.jpeg"
    download_image(favicon_url, OUTPUT_DIR)

    # Get posts
    posts = parse_rss()
    if not posts:
        print("No posts found!")
        return

    # Create pages
    for post in posts:
        create_post_html(post, OUTPUT_DIR)

    create_homepage(posts, OUTPUT_DIR)

    print(f"\n✓ Done! {len(posts)} posts converted")
    print(f"✓ Open site/index.html in your browser")

if __name__ == "__main__":
    main()

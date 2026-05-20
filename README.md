# Humans of WeLive - Static Website

Static HTML version of the Humans of WeLive Ghost blog, ready for **free GitHub Pages hosting**.

> We are the people of WeLive Foundation!

## 📦 What's Inside

The `/site` folder contains your complete static website:
- **index.html** - Homepage listing all blog posts
- **7 individual blog pages** - Each person's story
- **All images** - Downloaded locally (25 MB)
- **CNAME** - Custom domain configuration
- **No external CSS/JS dependencies** - Everything embedded!

## ✅ Works Everywhere

- ✅ **Double-click index.html** - Opens in browser
- ✅ **VS Code Live Server** - Right-click → Open with Live Server
- ✅ **GitHub Pages** - Push and deploy instantly
- ✅ **Any static host** - Netlify, Vercel, etc.

## 🚀 Deploy to GitHub Pages (3 Steps)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Static site for GitHub Pages"
git remote add origin https://github.com/YOUR_USERNAME/humansofwelive.git
git push -u origin main
```

### Step 2: Enable GitHub Pages
1. Go to repository Settings → Pages
2. Source: Branch `main`, Folder `/site`
3. Click Save

### Step 3: Configure Custom Domain (Optional)
1. In Pages settings, add: `humansofwelive.org`
2. Update DNS at your domain provider:
   ```
   Type: A, Name: @, Value: 185.199.108.153
   Type: A, Name: @, Value: 185.199.109.153
   Type: A, Name: @, Value: 185.199.110.153
   Type: A, Name: @, Value: 185.199.111.153
   ```
3. Wait 1-24 hours for DNS propagation
4. Enable "Enforce HTTPS"

**Done!** Your site will be live at `https://humansofwelive.org`

## 🎯 Key Features

✅ **Pure HTML/CSS** - No build process, no dependencies
✅ **Homepage shows excerpts** - Clean post listing
✅ **Full post pages** - Individual pages for each story
✅ **Responsive design** - Mobile, tablet, desktop
✅ **Fast loading** - All CSS embedded inline
✅ **Relative paths** - Works locally and on GitHub Pages

## 💰 Cost Savings

| Before (Ghost) | After (GitHub Pages) |
|----------------|---------------------|
| $10-30/month | **$0/month** |
| ~$120-360/year | **FREE** ✅ |

## 📁 Project Structure

```
humansofwelive/
├── site/                     # 👈 DEPLOY THIS FOLDER
│   ├── index.html            # Homepage
│   ├── *.html                # Blog post pages
│   ├── CNAME                 # Custom domain
│   ├── content/images/       # All images
│   └── README.md             # Site documentation
├── build_site.py             # Script to rebuild (if needed)
└── README.md                 # This file
```

## 🧪 Test Locally

### Option 1: Just Open It
Double-click `site/index.html` - that's it!

### Option 2: VS Code Live Server
1. Install "Live Server" extension
2. Right-click `site/index.html`
3. Select "Open with Live Server"

### Option 3: Python (if you have it)
```bash
cd site
python3 -m http.server 8000
# Visit http://localhost:8000
```

## 🔄 Updating Content

### If you need to add/edit posts:

**Easy way (no Python):** Edit HTML files directly
- Update `site/index.html` to add/remove posts from homepage
- Create new `.html` files for new posts
- Follow the existing structure

**Automated way (requires Python):**
```bash
python3 build_site.py
```
This will re-fetch all content from the Ghost RSS feed.

## 📝 Blog Posts Included

1. Care Leaver To Change Maker (Nisha Das)
2. Preethi's Story
3. Akhil's Story
4. Divya's Story
5. Vishwajeet's Story
6. Lateeshya's Story
7. Bhavya's Story

## 🌐 Technical Details

- **Original**: Ghost blog at https://humansofwelive.org/
- **Source**: Converted from Ghost RSS feed
- **Format**: Pure HTML5 + inline CSS
- **Images**: All stored locally in `content/images/`
- **Size**: ~25 MB total
- **Browser Support**: All modern browsers
- **Mobile**: Fully responsive

## 🎨 Design

The site preserves the look and feel of the original Ghost blog:
- Clean, minimal design
- Readable typography
- Orange accent color (#f7b37b)
- Card-based post layout
- Professional styling

## ⚡ Performance

- No external CSS files = fewer requests
- No JavaScript required
- Optimized images
- Static HTML = instant loading
- CDN-ready (via GitHub Pages)

## 📱 Responsive

Works perfectly on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktops
- 🖨️ Print media

## 🔒 Security

- No server-side code
- No database
- No user input
- No vulnerabilities
- Always up-to-date

## 📄 License

Content belongs to WeLive Foundation and respective authors.

## 🔗 Links

- **Original Ghost Blog**: https://humansofwelive.org/
- **WeLive Foundation**: https://welivefoundation.org.in/
- **GitHub Pages Docs**: https://docs.github.com/en/pages

---

## ✨ You're All Set!

Your website is ready to deploy. No Python, no build process, no dependencies - just pure HTML/CSS.

**Next step**: Push to GitHub and enable Pages, or just open `site/index.html` in your browser!

💚 **Saving $120-360/year by switching to GitHub Pages** 💚

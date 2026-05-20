# Humans of WeLive - Static Site

This is the deployable static website converted from Ghost blog.

## ✅ Ready for GitHub Pages

This folder contains everything needed for GitHub Pages:
- **index.html** - Homepage with all posts
- **7 blog post pages** - Individual story pages
- **content/images/** - All images (25 MB)
- **CNAME** - Custom domain configuration

## 🚀 Deploy to GitHub Pages

### Method 1: Deploy this folder directly

1. Create a new GitHub repository
2. Push this `site` folder to the repository
3. Go to Settings → Pages
4. Set source to: Branch `main`, Folder `/` (root)
5. Save and wait 5-10 minutes

### Method 2: Deploy as subfolder

1. Push the entire project to GitHub
2. Go to Settings → Pages
3. Set source to: Branch `main`, Folder `/site`
4. Save

## 📝 Important Features

✅ **No external dependencies** - All CSS is embedded in HTML files
✅ **Relative paths** - Works with Live Server, file://, and GitHub Pages
✅ **No Python needed** - Pure HTML/CSS only
✅ **Homepage shows excerpts** - Not full post content
✅ **Mobile responsive** - Works on all devices

## 🧪 Test Locally

### Option 1: Just open the file
Simply double-click `index.html` to open in your browser

### Option 2: Use VS Code Live Server
1. Install "Live Server" extension in VS Code
2. Right-click `index.html`
3. Select "Open with Live Server"

### Option 3: Use Python (optional)
```bash
python3 -m http.server 8000
```
Visit: http://localhost:8000

## 📂 Folder Structure

```
site/
├── index.html                    # Homepage
├── care-leaver-to-chane-maker.html
├── preethi-story.html
├── akhil-story-2.html
├── divya-story.html
├── vishwajeet-story-2.html
├── lateeshyas-story.html
├── bhavyas-story.html
├── CNAME                         # Custom domain
└── content/
    └── images/                   # All images
        ├── 2025/07/              # Blog post images
        └── size/w256h256/2025/06/ # Favicon
```

## 🎨 Features

- Clean, modern design
- Fast loading (static HTML)
- SEO friendly
- Accessible markup
- Print-friendly styles

## 💰 Cost

**$0/month** when hosted on GitHub Pages! 🎉

## 🔄 Updating Content

If you need to add/edit content:

1. **Easy way**: Edit HTML files directly
2. **Automated way**: Use the `build_site.py` script in parent folder

## 📱 Mobile Support

The site is fully responsive and works great on:
- Mobile phones
- Tablets
- Desktops
- Print

## ⚡ Performance

- No external CSS files = fewer HTTP requests
- Optimized images
- Clean HTML
- Fast page load

## 🌐 Browser Support

Works in all modern browsers:
- Chrome, Firefox, Safari, Edge
- iOS Safari, Chrome Mobile
- IE 11+ (basic support)

---

**Enjoy your free, fast, static website!** 🚀

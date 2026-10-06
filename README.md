# Pride Heritage Hotel Website

A luxurious, high-end website for Pride Heritage Hotel restaurant featuring regal design, elegant animations, and a sophisticated user experience.

## 🌟 Features

- **Fully Responsive Design** - Mobile-first approach that works beautifully on all devices
- **4 Complete Pages**:
  - Home page with hero, about, signature dishes, testimonials
  - Full menu page with filters and categories
  - Table booking system with reservation form
  - Photo gallery with lightbox and filters
- **Rich Interactions**:
  - Smooth scroll animations
  - Mobile hamburger menu with full-screen overlay
  - Auto-rotating testimonials carousel
  - Menu and gallery filters
  - Lightbox gallery with keyboard navigation
  - Form validation and success message
- **Luxurious Design**:
  - Deep green and gold color palette inspired by the restaurant images
  - Elegant typography (Cormorant Garamond + Inter)
  - Subtle animations and transitions
  - Heritage-inspired design elements

## 📁 File Structure

```
restaurant/
├── index.html          # Home page
├── menu.html           # Menu page
├── book-table.html     # Reservation page
├── gallery.html        # Photo gallery
├── css/
│   └── style.css       # Main stylesheet
├── js/
│   └── main.js         # JavaScript functionality
└── img/                # All restaurant images (9 images)
    ├── unnamed.webp
    ├── unnamed (1).webp
    ├── unnamed (2).webp
    ├── unnamed (3).webp
    ├── unnamed (4).webp
    ├── unnamed (5).webp
    ├── unnamed (6).webp
    ├── unnamed (7).webp
    └── unnamed (8).webp
```

## 🖼️ Image Usage Map

All 9 provided images are used throughout the website:

1. **unnamed (4).webp** - Signature dishes on marble table
   - Home page: Signature Dishes card
   - Gallery: Featured dish image
   
2. **unnamed (7).webp** - White marble elegant dining hall
   - Home page: About section image
   - Booking page: Header background
   - Gallery: Heritage Dining Hall
   
3. **unnamed (2).webp** - Outdoor terrace with skyline
   - Home page: Experience section background
   - Gallery: Terrace Lounge
   
4. **unnamed (6).webp** - Golden ambient lighting dining room
   - Home page: Signature Dishes card
   - Footer: Background image
   - Gallery: Golden Hour Dining
   
5. **unnamed (8).webp** - Green marble intimate dining space
   - Home page: Signature Dishes card
   - Menu page: Page header background
   - Gallery: Private Dining
   
6. **unnamed (5).webp** - Menu starters page
   - Gallery: Menu showcase
   
7. **unnamed.webp** - Menu soups & starters page
   - Gallery: Menu showcase
   
8. **unnamed (1).webp** - Menu Indian food page
   - Gallery: Menu showcase
   
9. **unnamed (3).webp** - Grand hall with golden lighting
   - Home page: Hero background
   - Gallery page: Header background
   - Gallery: Grand Hall image

## 🚀 How to Open the Website

### Method 1: Direct File Opening (Recommended)
1. Navigate to the `restaurant` folder
2. Double-click `index.html`
3. The website will open in your default browser

### Method 2: Using VS Code Live Server
1. Open the folder in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

### Method 3: Using Python HTTP Server
```bash
cd restaurant
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## 🎨 Design Details

### Color Palette
- **Primary Dark**: Deep forest green (#1a3a2e) - from marble tables
- **Primary Gold**: Antique gold (#d4af37) - luxury accents
- **Primary Light**: Warm ivory (#f8f4ed) - text and backgrounds
- **Accent Burgundy**: Rich burgundy (#5d2e28) - depth and contrast

### Typography
- **Headings**: Cormorant Garamond (elegant serif)
- **Body**: Inter (clean sans-serif)
- Wide letter-spacing on labels for refinement

### Key Interactions
- **Navbar**: Transparent on hero, solid on scroll
- **Mobile Menu**: Full-screen overlay with smooth animations
- **Testimonials**: Auto-rotate every 5 seconds
- **Gallery Lightbox**: Click to expand, arrow keys to navigate
- **Form**: Real-time validation with success confirmation
- **Filters**: Smooth transitions on menu and gallery pages

## 📱 Responsive Breakpoints

- **Desktop**: 1024px and above (full layout)
- **Tablet**: 768px - 1024px (adjusted grid layouts)
- **Mobile**: Below 768px (stacked layouts, hamburger menu)

## ✨ Notable Features

1. **No External Dependencies**: Pure vanilla JavaScript, no jQuery or frameworks
2. **Fast Loading**: Lazy loading for images, optimized CSS
3. **Accessible**: WCAG-compliant color contrast, semantic HTML, keyboard navigation
4. **SEO-Friendly**: Proper meta tags, alt text on all images
5. **Print-Ready**: Clean layouts that work for printing menus

## 🔧 Customization

To customize the content:

1. **Restaurant Name/Info**: Edit the text in each HTML file
2. **Colors**: Modify CSS variables in `style.css` (lines 9-22)
3. **Menu Items**: Edit the menu section in `menu.html`
4. **Images**: Replace images in the `img/` folder (keep same filenames or update paths in HTML)
5. **Contact Details**: Update footer information across all pages

## 📞 Contact Details (Placeholder)

- **Address**: 123 Heritage Lane, MG Road, Bangalore, Karnataka 560001
- **Phone**: +91 80 4567 8900
- **Email**: reservations@prideheritage.com
- **Hours**: 
  - Lunch: 12:00 PM - 3:30 PM
  - Dinner: 7:00 PM - 11:30 PM
  - Open All Days

## 🎯 Browser Compatibility

Tested and works perfectly on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

---

**Built with care for Pride Heritage Hotel** 🏛️✨
A Legacy of Taste

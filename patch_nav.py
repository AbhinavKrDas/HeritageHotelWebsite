import re

files = ["menu.html", "gallery.html", "book-table.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # Desktop Nav
    new_nav = """            <ul class="nav-links" id="navLinks">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="menu.html" class="nav-link{menu_active}">Menu</a></li>
                <li><a href="gallery.html" class="nav-link{gallery_active}">Gallery</a></li>
                <li><a href="index.html#contact" class="nav-link">Contact</a></li>
            </ul>"""
    
    menu_act = ' active' if file == 'menu.html' else ''
    gallery_act = ' active' if file == 'gallery.html' else ''
    
    new_nav_str = new_nav.format(menu_active=menu_act, gallery_active=gallery_act)
    
    pattern_nav = re.compile(r'            <ul class="nav-links" id="navLinks">.*?</ul>', re.DOTALL)
    text = pattern_nav.sub(new_nav_str, text)
    
    # Mobile Nav
    new_mobile = """        <ul class="mobile-nav-links">
            <li><a href="index.html" class="mobile-link">Home</a></li>
            <li><a href="menu.html" class="mobile-link">Menu</a></li>
            <li><a href="gallery.html" class="mobile-link">Gallery</a></li>
            <li><a href="index.html#contact" class="mobile-link">Contact</a></li>
            <li><a href="book-table.html" class="btn-primary mobile-cta">Book a Table</a></li>
        </ul>"""
        
    pattern_mobile = re.compile(r'        <ul class="mobile-nav-links">.*?</ul>', re.DOTALL)
    text = pattern_mobile.sub(new_mobile, text)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)


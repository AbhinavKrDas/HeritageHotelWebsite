import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the heritage and culinary sections with a simplified, luxurious experience section
replacement = """    <!-- The Experience Section -->
    <section class="experience" id="experience" style="padding: 120px 0;">
        <div class="experience-overlay" style="background: linear-gradient(135deg, rgba(13,31,23,0.95), rgba(0,0,0,0.8));"></div>
        <div class="container">
            <div class="experience-content" style="max-width: 800px; margin: 0 auto; text-align: center; position: relative; z-index: 2;">
                <p class="section-label white" data-aos="fade-up">A LEGACY OF ELEGANCE</p>
                <div class="divider center" data-aos="fade-up" data-aos-delay="100"></div>
                <h2 class="section-title white" style="font-size: 3.5rem; letter-spacing: 2px;" data-aos="fade-up" data-aos-delay="200">The Royal Culinary Journey</h2>
                <p class="experience-text" style="font-size: 1.2rem; line-height: 2; margin-top: 30px; margin-bottom: 50px; font-weight: 300; color: #f5f0e8;" data-aos="fade-up" data-aos-delay="300">
                    Step into a sanctuary of regal hospitality. For three decades, Pride Heritage Hotel has stood as a bastion of fine dining, marrying the opulence of Nizami and Mughlai traditions with modern gastronomic artistry. Immerse yourself in an atmosphere of curated luxury, precision, and unparalleled taste.
                </p>
                
                <div class="hero-buttons" data-aos="fade-up" data-aos-delay="400">
                    <a href="menu.html" class="btn-primary btn-glow">Curated Menu</a>
                    <a href="gallery.html" class="btn-secondary">View Elegance</a>
                </div>
            </div>
        </div>
    </section>"""

# Using regex to replace everything from <!-- Our Heritage to the end of culinary-showcase section
pattern = re.compile(r'    <!-- Our Heritage & Story Section -->.*?</section>\n.*<!-- Gastronomic Pillars & Visual Culinary Artistry Showcase -->.*?</section>', re.DOTALL)
text = pattern.sub(replacement, text)

# Also fix the links in footer
text = text.replace('<li><a href="#heritage">Our Heritage Story</a></li>', '<li><a href="menu.html">Curated Menu</a></li>')
text = text.replace('<li><a href="#culinary">Culinary Artistry</a></li>', '')
text = text.replace('<li><a href="menu.html">Full 150+ Menu</a></li>', '')
text = text.replace('<li><a href="gallery.html">Visual Gallery</a></li>', '<li><a href="gallery.html">Gallery</a></li>')
text = text.replace('<a href="#culinary" class="btn-secondary">Explore</a>', '<a href="#experience" class="btn-secondary">Explore</a>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)


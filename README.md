# Quark.py

#### Quark.py is a lightweight Python framework for packaging HTML, CSS, and JS codes into simple desktop apps.

###### Why use Quark.py instead of other frameworks like Electron?
- HTML, CSS and JS packed into desktop apps.
- About 60% lighter than Electron in file size.
- Very light and uses Python.
- Does not packs Chromium inside the apps.
- Faster startup than other frameworks and quite optimized.
- Caching strategies implemented for improved performance.
- Easy distribution of apps.

###### Optimization
1. Caching strategies – App only loads local HTML/CSS/JS without external requests.
2. Lazy loading – The HTML app is loaded only when the window is created and heavy assets can be loaded on demand later on.
3. Reduce memory usage – Minimal dependencies reduce memory usage.
4. Efficient algorithms – Very simple Python app logic was implemented for fast performance.
5. Minimize dependencies – Removed useless libraries which helped to reduce the file size a lot.

###### FAQ
- Can I make apps for Linux and Mac too? Ans: For now it's not possible but I will consider in future.
- Why are icons are not appearing in the app? Ans: Theres some known issue about that, I will try patching it in next version.
- How small is it in file size compared to other frameworks? Ans: Quark.py apps are about 60% more smaller than other framework apps.

###### How to use:
1. Run -> pip install -r requirements.txt
2. Check if everything is installed (If PyInstaller is installed but not in PATH, you can always run it via python -> -m PyInstaller main.py --onedir --windowed --clean --strip --add-data "web;web")
3. Run -> python quark.py
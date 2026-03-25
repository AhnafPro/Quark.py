# Quark.py
[![PyPI version](https://github.com/AhnafPro/Quark.py/blob/main/web/icon.png?raw=true)](https://pypi.org/project/quarkdotpy/) ```

#### Quark.py is a lightweight Python framework for packaging HTML, CSS, and JS codes into simple desktop apps.

###### Why use Quark.py instead of other frameworks like Electron?
- HTML, CSS and JS packed into desktop apps.
- About 65% lighter than Electron in file size.
- Very light and uses Python.
- Does not packs Chromium inside the apps.
- Faster startup than other frameworks and quite optimized.
- Caching strategies implemented for improved performance.
- Easy distribution of apps.

###### Optimization
1. Caching strategies – App only loads local HTML/CSS/JS without external requests.
2. Lazy loading – The HTML codes only load on demand after the window of the app is created.
3. Reduce memory usage – Minimal dependencies reduce memory usage.
4. Efficient algorithms – Very simple Python app logic was implemented for fast performance.
5. Minimize dependencies – Removed useless libraries which helped to reduce the file size a lot.

###### FAQ
- Can I make apps for Linux and Mac too? Ans: For now it's not possible but I will consider in future.
- How small is it in file size compared to other frameworks? Ans: Quark.py apps are about 60% more smaller than other framework apps.
- Will it work across all Windows OS? Ans: You must have a well-updated version of Windows 10/11 with latest Webview2 (comes with Edge).

###### How to use:
1. To initiate the project run -> pip install -r requirements.txt
2. Edit the codes inside the /web directory according to your needs.
3. Run this to build your .exe app -> python -m PyInstaller --onefile --noconsole --name "name of your app" --clean --add-data "web;web" quark.py --icon "icon.ico"

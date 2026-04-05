# Quark.py
[![PyPI version](https://badge.fury.io/py/quarkdotpy.svg)](https://pypi.org/project/quarkdotpy/1.0.4)
[demo.webm](https://github.com/user-attachments/assets/6d182faa-b7d5-4a3c-a692-03128e3a1105)

#### Quark.py is a lightweight Python framework for packaging HTML, CSS, and JS codes into simple desktop apps.

###### Why use Quark.py instead of other frameworks like Electron?
- HTML, CSS and JS packed into desktop apps.
- About 65% lighter than Electron in file size.
- Very light and uses Python.
- Does not packs Chromium inside the apps.
- Faster startup than other frameworks and quite optimized.
- Caching strategies implemented for improved performance.
- Easy distribution of apps.

###### Optimizations
1. Optimize asset sizes: The application bundle was reduced using PyInstaller's binary and size optimization flags.
   - Problem: Normally unoptimized build command looks like this ``` python -m PyInstaller --name "myapp" quark.py ```, which leads to formation of lots of DLLs and tons of dependencies along with the exe.
   - Solution: Using the optimization flags (--clean, --onefile etc.) on the build command fixes it all and slap everything by removing debug symbols, caches, temp files etc. and the finished command looks something like this ``` python -m PyInstaller --onefile --noconsole --name "name of your app" --clean --add-data "web;web" quark.py --icon "icon.ico" ```
   - Proof: Everything turned into a single file and about 45% app size reduction.

   <img width="592" height="400" alt="Untitled design (70)" src="https://github.com/user-attachments/assets/6a233869-e9b5-46c0-bfee-32b700ea47fe" />




###### FAQ
- Can I make apps for Linux and Mac too? Ans: For now it's not possible but I will consider in future.
- How small is it in file size compared to other frameworks? Ans: Quark.py apps are about 60% more smaller than other framework apps.
- Will it work across all Windows OS? Ans: You must have a well-updated version of Windows 10/11 with latest Webview2 (comes with Edge).

###### How to use:
1. [Click here to download directly](https://github.com/AhnafPro/Quark.py/archive/refs/heads/main.zip) or Clone the repo.
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Edit the files inside the `/web` and `quark.py` according to your needs.
4. Build your `.exe` app:
```bash
   python -m PyInstaller --onefile --noconsole --name "name of your app" --clean --add-data "web;web" quark.py --icon "icon.ico"
```

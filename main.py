import webview
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

html_path = resource_path("web/index.html")
icon_path = resource_path("web/assets/icon.ico") 


window = webview.create_window(
    "My Quark.py App",
    html_path,
    width=1000,
    height=700,
    frameless=False
)

try:
    window.gui = 'edgechromium'
    window.set_icon(icon_path)
except Exception:
    print("Icon not supported in this version, skipping.")

webview.start(gui='edgechromium', debug=True)
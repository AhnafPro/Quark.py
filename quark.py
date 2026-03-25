import webview

if __name__ == "__main__":
    window = webview.create_window(
        title="Quark.py",
        url="web/index.html",
        width=800,
        height=620,
        resizable=True,
        min_size=(700, 500),
        background_color="#0d3d55"
    )

    webview.start(
        gui='edgechromium',
        debug=False
    )

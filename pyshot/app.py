import base64

from typing import (
    Any,
    Dict, 
    List,
    Union,
)

from flask import (
    Flask,
    request,
    session,
    url_for,
    redirect,
    render_template,
)

from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles
from pygments.lexers import Python3Lexer
from pygments import highlight

from utils import take_screenshot_from_url

app: Flask = Flask(__name__)
app.secret_key = "AddYourSecretKeyHere" # Secret key used for session management

# Placeholder code to display when no code is provided
PLACEHOLDER_CODE: str = "print('Hello, World!')"
# Default code style
DEFAULT_STYLE: str = "monokai"

# Route to render code input page
@app.route("/", methods=["GET"])
def code() -> str:

    # Initialize session code if not present
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE

    lines: List[str] = session["code"].split("\n")
     
    context: Dict[str, Union[str, List[str], int]] = {
        "message": "Paste Your Code🛠️",
        "code": session["code"],
        "num_lines": len(lines),
        "max_chars": len(max(lines, key=len)),
    }

    return render_template("code_input.html", **context)


# Route to save user provided code
@app.route("/save_code", methods=["POST"])
def save_code() -> Any:
    session["code"] = request.form.get("code")
    return redirect(url_for("code"))


# Route to reset session and revert to placeholder code
@app.route("/reset_session", methods=["POST"])
def reset_session() -> Any:
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    return redirect(url_for("code"))


# Route to render style selection page
@app.route("/style", methods=["GET"])
def style() -> str:
    # Initialize session style if not present
    if session.get("style") is None:
        session["style"] = DEFAULT_STYLE

    formatter: HtmlFormatter = HtmlFormatter(style=session["style"])

    context: Dict[str, Union[str, List[str]]] = {
        "message": "Select Your Style 🎨",
        "all_styles": list(get_all_styles()),
        "style_definitions": formatter.get_style_defs(),
        "style_bg_color": formatter.style.background_color,
        "highlighted_code": highlight(
            session["code"], Python3Lexer(), formatter
        ),
    }
    return render_template("style_selection.html", **context)


# Route to save selected code style
@app.route("/save_style", methods=["POST"])
def save_style() -> Any:
    if request.form.get("style") is not None:
        session["style"] = request.form.get("style")
    if request.form.get("code") is not None:
        session["code"] = request.form.get("code")
    return redirect(url_for("style"))


# Route to generate image from code
@app.route("/image", methods=["GET"])
def image() -> str:
    # Collect session data
    session_data: Dict[str, str] = {
        "name": app.config["SESSION_COOKIE_NAME"],
        "value": request.cookies.get(app.config["SESSION_COOKIE_NAME"]),
        "url": request.host_url,
    }
    # Get target URL and take screenshot
    target_url: str = request.host_url + url_for("style")
    image_bytes: bytes = take_screenshot_from_url(target_url, session_data)

    context: Dict[str, Union[str, bytes]] = {
        "message": "Done! 🎉",
        "image_b64": base64.b64encode(image_bytes).decode("utf-8"),
    }

    return render_template("image.html", **context)

if __name__ == "__main__":
    app.run()

<div align="center">
  <h1 align="center">PyShot</h1>
  <img alt="PyShot Logo" src="https://github.com/chrvstian/pyshot/blob/main/.github/logo.png" width="15%" height="15%">
  <h3>A code-to-image generator written in Python 3.</h3>

</div>

<br/>

<div align="center">
  <a href="https://github.com/chrvstian/pyshot/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/chrvstian/pyshot"></a>
  <a href="https://github.com/chrvstian/pyshot/.github/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-AGPLv3-purple"></a>
</div>

<br/>

PyShot is an open-source code-to-image generator written in Python 3. You can use it to create images of code snippets to share on social media, with your team & any other reason you may want to share an image of a code snippet.

## Features

- **Sessions:** Save sessions so that your code doesn't get deleted when you refresh the page.
- **Saving:** Either copy or save the images of your code snippets.
- **Style:** A wide range of styles to choose from for your images.

## Demo

![Showcase](https://github.com/chrvstian/pyshot/assets/141359845/4e25bc7f-651a-4503-99ea-b1cfdca6b902)

## Tech Stack

- [Pygments](https://pygments.org/) - Syntax Highlighting Library
- HTML & CSS - User Interface
- [Python](https://www.python.org/) – Language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Server

## Getting Started

### Prerequisites

Here's what you need to be able to use PyShot:

- Python 3+
- Flask, Playwright & Pygments modules

### 1. Clone the repository

```shell
git clone https://github.com/chrvstian/pyshot.git
cd pyshot
```

### 2. Install all required modules

```shell
pip3 install -r requirements.txt
```

### 3. Generate your secret key for session management

**Step 1:** Open your terminal & input the following code
```shell
python3
```

**Step 2:** Generate your secret key
```shell
import secrets; secrets.token_hex()
```

**Step 3:** Copy your token & paste it into app.py
- Copy the token that it creates and locate the 27th line in app.py
- Paste the key into the line that says:
```shell
app.secret_key = "AddYourSecretKeyHere" # Secret key used for session management
```

### 4. Run the program

```shell
python3 app.py
```

### 5. Open the app in your browser

- Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Contributing

PyShot is an open-source project and we welcome contributions from the community.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

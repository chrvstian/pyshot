
<div align="center">
  <h1 align="center">PyShot</h1>
  <img alt="PyShot Logo" src="">
  <h3>A code-to-image generator written in Python 3.</h3>

</div>

<br/>

<div align="center">
  <a href="https://github.com/chrvstian/pyshot/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/chrvstian/pyshot"></a>
  <a href="https://github.com/chrvstian/pyshot/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-AGPLv3-purple"></a>
</div>

<br/>

PyShot is an open-source code-to-image generator written in Python 3. You can use it to create images of code snippets to share on social media, with your team & any other reason you may want to share an image of a code snippet.

## Features

- **Sessions:** Save sessions so that your code doesn't get deleted when you refresh the page.
- **Saving:** Either copy or save the images of your code snippets.
- **Style:** A wide range of styles to choose from for your images.

## Demo

![Papermark Welcome GIF](.github/images/papermark-welcome.gif)

## Tech Stack

- [Pygments](https://pygments.org/) - Syntax Highlighting Library
- [Python](https://www.python.org/) – Language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Server
- HTML & CSS - User Interface

## Getting Started

### Prerequisites

Here's what you need to be able to run Papermark:

- Node.js (version >= 18)
- PostgreSQL Database
- Blob storage (currently [AWS S3](https://aws.amazon.com/s3/) or [Vercel Blob](https://vercel.com/storage/blob))
- [Resend](https://resend.com) (for sending emails)

### 1. Clone the repository

```shell
git clone https://github.com/mfts/papermark.git
cd papermark
```

### 2. Install npm dependencies

```shell
npm install
```

### 3. Copy the environment variables to `.env` and change the values

```shell
cp .env.example .env
```

### 4. Initialize the database

```shell
npx prisma generate
npx prisma migrate deploy
```

### 5. Run the dev server

```shell
npm run dev
```

### 6. Open the app in your browser

Visit [http://localhost:3000](http://localhost:3000) in your browser.

## Tinybird instructions

To prepare the Tinybird database, follow these steps:

0. We use `pipenv` to manage my Python dependencies. If you don't have it installed, you can install it using the following command:
   ```sh
   pkgx pipenv
   ```
1. Download the Tinybird CLI from [here](https://www.tinybird.co/docs/cli.html) and install it on your system.
2. After authenticating with the Tinybird CLI, navigate to the `lib/tinybird` directory:
   ```sh
   cd lib/tinybird
   ```
3. Push the necessary datasources using the following command:
   ```sh
   tb push datasources/*
   tb push endpoints/get_*
   ```
4. Don't forget to set the `TINYBIRD_TOKEN` with the appropriate rights in your `.env` file.

#### Updating Tinybird

```sh
pipenv shell
## start: pkgx-specific
cd ..
cd papermark
## end: pkgx-specific
pipenv update tinybird-cli
```

## Contributing

Papermark is an open-source project and we welcome contributions from the community.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

### Our Contributors ✨

<a href="https://github.com/mfts/papermark/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mfts/papermark" />
</a>


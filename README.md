# XKCD API Mirror

**A reliable, up-to-date mirror of the official XKCD API, enhanced with Cross-Origin Resource Sharing (CORS) support.**

This repository provides a seamless way to access XKCD comic data and images, overcoming the CORS limitations of the original API. The mirror is automatically synchronized daily to ensure you always have access to the latest comics.

## Overview

The official XKCD API (xkcd.com/info.0.json) is a fantastic resource but lacks CORS headers. This makes it challenging to use directly in web applications hosted on different domains. This project mirrors the API data and serves it via GitHub's raw content URLs, which inherently support CORS.

## Features

*   **CORS Enabled:** Directly usable in web applications without proxy workarounds.
*   **Always Up-to-Date:** Automatically syncs with the official XKCD API daily.
*   **Reliable Access:** Leverages GitHub's infrastructure for high availability.
*   **Mirrored Images:** Provides direct links to mirrored comic images hosted within this repository.

## Usage

Accessing comic data and images is straightforward using the structured paths within this repository.

### Accessing a Specific Comic

To retrieve the metadata for a specific comic (e.g., comic number `X`), use the following URL pattern:

```
https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/{X}/info.0.json
```

**Example (Comic #190):**

```
https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/info.0.json
```

#### Response Structure

A request will return a JSON object similar to this:

```json
{
  "month": "11",
  "num": 190,
  "link": "",
  "year": "2006",
  "news": "",
  "safe_title": "IPoD",
  "transcript": "[[Character 1 - wearing a black hat - sits at a computer. Character 2 stands behind Character 1]]
Character 1: You see, statisticians communicate using IPoD -- IP over Demographics. For example, the header of the next packet I send will be encoded into the New Jersey death rate.
Character 2: So you're going to hack the census bureau and change the number of reported deaths?
Character 1: Guess again.
Character 1: Hey, have you seen my crossbow?
{{Alt: For smaller numbers he has to SAVE lives.  The birthrate channel is even more of a mixed bag.}}",
  "alt": "For smaller numbers he has to SAVE lives.  The birthrate channel is even more of a mixed bag.",
  "img": "https://imgs.xkcd.com/comics/ipod.png",
  "title": "IPoD",
  "day": "29",
  "mirror_img": "https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/ipod.png"
}

```

#### Using the Mirrored Image

Within the JSON response, use the `mirror_img` field for the CORS-compatible image URL:

*   **Original Image:** `img` (e.g., `https://imgs.xkcd.com/comics/ipod.png`) - May have CORS issues.
*   **Mirrored Image:** `mirror_img` (e.g., `https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/ipod.png`) - **Recommended for use.**

### Accessing the Latest Comic

To find the number of the latest comic, fetch the `syncState.json` file:

```
https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/syncState.json
```

This will return a JSON object indicating the latest comic ID:

```json
{
  "last_update_content": {
    "id": "3083" 
  }
}
```

Use the `id` value (e.g., `3083`) with the method described in "Accessing a Specific Comic" to get the latest comic's data.

## How it Works

A synchronization script (`sync.py`) runs daily, checking for new XKCD comics. If a new comic is found, its metadata and image are downloaded, processed, and committed to this repository. The `syncState.json` file is updated with the latest comic number.

## Contributing

While the core mirroring process is automated, suggestions for improving the README or addressing issues are welcome via GitHub Issues.

## License

This project utilizes data from XKCD, which is licensed under a Creative Commons Attribution-NonCommercial 2.5 License. Please adhere to the XKCD license terms when using the mirrored data and images. The code within this repository is available under the [LICENSE](LICENSE) file.

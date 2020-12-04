# Mirror of xkcd api

> Update-to-date mirror of xkcd api, which Supports CORS.

This repository will automatically update with new content everyday.

## How to use

***to consume json for x/your_value***

```text
https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/{x}/info.0.json
```

***example: make a request to 190***

```text
https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/info.0.json
```

### Making request will give the following response

```json
{
  "month": "11",
  "num": 190,
  "link": "",
  "year": "2006",
  "news": "",
  "safe_title": "IPoD",
  "transcript": "[[Character 1 - wearing a black hat - sits at a computer. Character 2 stands behind Character 1]]\nCharacter 1: You see, statisticians communicate using IPoD -- IP over Demographics. For example, the header of the next packet I send will be encoded into the New Jersey death rate.\nCharacter 2: So you're going to hack the census bureau and change the number of reported deaths?\nCharacter 1: Guess again.\nCharacter 1: Hey, have you seen my crossbow?\n{{Alt: For smaller numbers he has to SAVE lives.  The birthrate channel is even more of a mixed bag.}}",
  "alt": "For smaller numbers he has to SAVE lives.  The birthrate channel is even more of a mixed bag.",
  "img": "https://imgs.xkcd.com/comics/ipod.png",
  "title": "IPoD",
  "day": "29",
  "mirror_img": "https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/ipod.png"
}
```

### Parse the json and use value of "mirror_img" instead of "img"

'img': 'https://imgs.xkcd.com/comics/ipod.png' is the original link, 

You should use, "mirror_img": "https://raw.githubusercontent.com/aghontpi/mirror-xkcd-api/main/api/190/ipod.png"
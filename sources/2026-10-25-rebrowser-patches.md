---
url: https://github.com/rebrowser/rebrowser-patches
captured: 2026-10-25
word_count: 2179
status: raw
---

## Repository

- Public
- Website: https://rebrowser.net
- Stars: 1,441 · Watchers: 27 · Forks: 83
- Default branch: main · Releases: 6 · Tags: 6
- Created: 2024-08-06

# 🪄 Patches for undetectable browser automation

This repo contains patches to enhance popular web automation libraries. Specifically, it targets the [`puppeteer`](https://github.com/puppeteer/puppeteer) and [`playwright`](https://github.com/microsoft/playwright) packages.

Some aspects of automation libraries or browser behavior cannot be adjusted through settings or command-line switches. Therefore, we fix these issues by patching the library's source code. While this approach is fragile and may break as the libraries' source code changes over time, the goal is to maintain this repo with community help to keep the patches up to date.

## Do I really need any patches?

Out of the box Puppeteer and Playwright come with some significant leaks that are easy to detect. It doesn't matter how good your proxies, fingeprints, and behaviour scripts, if you don't have it patched, you're just a big red flag for any major website.

🕵️ You can easily test your automation setup for major modern detections with [rebrowser-bot-detector](https://bot-detector.rebrowser.net/) ([sources and details](https://github.com/rebrowser/rebrowser-bot-detector))

| Before the patches 👎 | After the patches 👍 |
|---|---|
| [![before](https://private-user-images.githubusercontent.com/177686430/368029415-6fc29650-4ea9-4d27-a152-0b7b40cd2b92.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY4MDI5NDE1LTZmYzI5NjUwLTRlYTktNGQyNy1hMTUyLTBiN2I0MGNkMmI5Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZmM5NzhjNTA1YjQ2NWUzNzM1NjY2YTc2NTJlYjYxOGZiMWQ5NzI5NGJhNGM1ZTcwY2Y5ZDVmNzIzZmFhOWFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Rxrj8hP3AGqNi7lHYVPLWUy0RobAx9ta4B0D-tzO-ZQ)](https://private-user-images.githubusercontent.com/177686430/368029415-6fc29650-4ea9-4d27-a152-0b7b40cd2b92.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY4MDI5NDE1LTZmYzI5NjUwLTRlYTktNGQyNy1hMTUyLTBiN2I0MGNkMmI5Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZmM5NzhjNTA1YjQ2NWUzNzM1NjY2YTc2NTJlYjYxOGZiMWQ5NzI5NGJhNGM1ZTcwY2Y5ZDVmNzIzZmFhOWFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Rxrj8hP3AGqNi7lHYVPLWUy0RobAx9ta4B0D-tzO-ZQ) | [![after](https://private-user-images.githubusercontent.com/177686430/368029435-2ba0db25-c0db-4015-9c83-731a355cd2e9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY4MDI5NDM1LTJiYTBkYjI1LWMwZGItNDAxNS05YzgzLTczMWEzNTVjZDJlOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jYTVkNGNjZGU1YTBlMzMzOTc0ZmIwNTAxZDczMWE1MGYyNGQ3ZmNlYWM5ZTcxZTM0NGQxNWJjOTM2NDc4YjIzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.VKn8Tr4idau5lxwLTOd7-zq6wvvFUaZMvjQSFAdiVU8)](https://private-user-images.githubusercontent.com/177686430/368029435-2ba0db25-c0db-4015-9c83-731a355cd2e9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY4MDI5NDM1LTJiYTBkYjI1LWMwZGItNDAxNS05YzgzLTczMWEzNTVjZDJlOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jYTVkNGNjZGU1YTBlMzMzOTc0ZmIwNTAxZDczMWE1MGYyNGQ3ZmNlYWM5ZTcxZTM0NGQxNWJjOTM2NDc4YjIzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.VKn8Tr4idau5lxwLTOd7-zq6wvvFUaZMvjQSFAdiVU8) |

## Is there an easy drop-in replacement?

If you don't want to mess with the patches and all possible errors, there is a drop-in solution for you. These packages have simply applied rebrowser-patches on top of the original code, nothing more.

Puppeteer: [rebrowser-puppeteer](https://www.npmjs.com/package/rebrowser-puppeteer) ([src](https://github.com/rebrowser/rebrowser-puppeteer)) and [rebrowser-puppeteer-core](https://www.npmjs.com/package/rebrowser-puppeteer-core) ([src](https://github.com/rebrowser/rebrowser-puppeteer-core))

Playwright (Node.js): [rebrowser-playwright](https://www.npmjs.com/package/rebrowser-playwright) ([src](https://github.com/rebrowser/rebrowser-playwright)) and [rebrowser-playwright-core](https://www.npmjs.com/package/rebrowser-playwright-core) ([src](https://github.com/rebrowser/rebrowser-playwright-core))

Playwright (Python): [rebrowser-playwright](https://pypi.org/project/rebrowser-playwright/) ([src](https://github.com/rebrowser/rebrowser-playwright-python))

The easiest way to start using it is to fix your `package.json` to use new packages but keep the old name as an alias. This way, you don't need to change any source code of your automation. Here is how to do that:

1. Open `package.json` and replace `"puppeteer": "^23.3.1"` and `"puppeteer-core": "^23.3.1"` with `"puppeteer": "npm:rebrowser-puppeteer@^23.3.1"` and `"puppeteer-core": "npm:rebrowser-puppeteer-core@^23.3.1"`. Note: 23.3.1 is just an example, check the latest version on [npm](https://www.npmjs.com/package/rebrowser-puppeteer-core).
2. Run `npm install` (or `yarn install`)
Another way is to actually use new packages instead of the original one. Here are the steps you need to follow:

1. Open `package.json` and replace `puppeteer` and `puppeteer-core` packages with `rebrowser-puppeteer` and `rebrowser-puppeteer-core`. Don't change versions of the packages, just replace the names.
2. Run `npm install` (or `yarn install`)
3. Find and replace in your scripts any mentions of `puppeteer` and `puppeteer-core` with `rebrowser-puppeteer` and `rebrowser-puppeteer-core`
🚀 That's it! Just visit the [rebrowser-bot-detector](https://bot-detector.rebrowser.net/) page and test your patched browser.

Our goal is to maintain and support these drop-in replacement packages with the latest versions, but we mainly focus on fresh versions, so if you're still using puppeteer 13.3.7 from the early 90s, it might be a good time to upgrade. There's a high chance that it won't really break anything as the API is quite stable over time.

## Available patches

### Fix `Runtime.Enable` leak

Popular automation libraries rely on the CDP command `Runtime.Enable`, which allows receiving events from the `Runtime.` domain. This is crucial for managing execution contexts used to evaluate JavaScript on pages, a key feature for any automation process.

However, there's a technique that detects the usage of this command, revealing that the browser is controlled by automation software like Puppeteer or Playwright. This technique is **used by all major anti-bot software** such as Cloudflare, DataDome, and others.

> We've prepared a full article about our investigation on this leak, which you can read in [our blog](https://rebrowser.net/blog/how-to-fix-runtime-enable-cdp-detection-of-puppeteer-playwright-and-other-automation-libraries-61740).

For more details on this technique, read DataDome's blog post: [How New Headless Chrome & the CDP Signal Are Impacting Bot Detection](https://datadome.co/threat-research/how-new-headless-chrome-the-cdp-signal-are-impacting-bot-detection/). In brief, it's a few lines of JavaScript on the page that are automatically called if `Runtime.Enable` was used.

Our fix disables the automatic `Runtime.Enable` command on every frame. Instead, we manually create contexts with unknown IDs when a frame is created. Then, when code needs to be executed, there are multiple ways to get the context ID.

#### 1. Create a new binding in the main world, call it and save its context ID.

🟢 Pros: The ultimate approach that keeps access to the main world and works with web workers and iframes. You don't need to change any of your existing codebase.

🔴 Cons: None are discovered so far.

#### 2. Create a new isolated context via `Page.createIsolatedWorld` and save its ID.

🟢 Pros: All your code will be executed in a separate isolated world, preventing page scripts from detecting your changes via MutationObserver and other techniques.

🔴 Cons: You won't be able to access main context variables and code. While this is necessary for some use cases, the isolated context generally works fine for most scenarios. Also, web workers don't allow creating new worlds, so you can't execute your code inside a worker. This is a niche use case but may matter in some situations. There is a workaround for this issue, please read [How to Access Main Context Objects from Isolated Context in Puppeteer & Playwright](https://rebrowser.net/blog/how-to-access-main-context-objects-from-isolated-context-in-puppeteer-and-playwright-23741).

#### 3. Call `Runtime.Enable` and then immediately call `Runtime.Disable`.

This triggers `Runtime.executionContextCreated` events, allowing us to catch the proper context ID.

🟢 Pros: You will have full access to the main context.

🔴 Cons: There's a slight chance that during this short timeframe, the page will call code that leads to the leak. The risk is low, as detection code is usually called during specific actions like CAPTCHA pages or login/registration forms, typically right after the page loads. Your business logic is usually called a bit later.

> 🎉 Our tests show that all these approaches are currently undetectable by Cloudflare or DataDome.

Note: you can change settings for this patch on the fly using an environment variable. This allows you to easily switch between patched and non-patched versions based on your business logic.

- `REBROWSER_PATCHES_RUNTIME_FIX_MODE=addBinding` — addBinding technique (default)
- `REBROWSER_PATCHES_RUNTIME_FIX_MODE=alwaysIsolated` — always run all scripts in isolated context
- `REBROWSER_PATCHES_RUNTIME_FIX_MODE=enableDisable` — use Enable/Disable technique
- `REBROWSER_PATCHES_RUNTIME_FIX_MODE=0` — completely disable fix for this leak
- `REBROWSER_PATCHES_DEBUG=1` — enable some debugging messages
Remember, you can set these variables in different ways, for example, in code:

```
process.env.REBROWSER_PATCHES_RUNTIME_FIX_MODE = "alwaysIsolated"
```

or in command line:

```
REBROWSER_PATCHES_RUNTIME_FIX_MODE=alwaysIsolated node app.js
```

### Change sourceURL to generic script name

By default, Puppeteer adds `//# sourceURL=pptr:...` to every script in `page.evaluate()`. A remote website can detect this behavior and raise red flags. This patch changes it to `//# sourceURL=app.js`. You can also adjust it via environment variable:

```
# use any generic filename
REBROWSER_PATCHES_SOURCE_URL=jquery.min.js
# use 0 to completely disable this patch
REBROWSER_PATCHES_SOURCE_URL=0
```

### Method to access browser CDP connection

Sometimes, it could be very useful to access a CDP session at a browser level. For example, when you want to implement some custom CDP command. There is a method `page._client()` that returns CDP session for the current page instance, but there is no such method for browser instance. This patch adds a new method `_connection()` to Browser class, so you can use it like this:

```
browser._connection().on('Rebrowser.addRunEvent', (params) => { ... })
```

*Note: it's not detectable by external website scripts, it's just for your convenience.*

### Change default utility world name

The default utility world name is `'__puppeteer_utility_world__' + packageVersion`. Sometimes you might want to change it to something else. This patch changes it to `util` and allows you to customize it via env variable:

```
REBROWSER_PATCHES_UTILITY_WORLD_NAME=customUtilityWorld
# use 0 to completely disable this patch
REBROWSER_PATCHES_UTILITY_WORLD_NAME=0
```

This env variable cannot be changed on the fly, you have to set it before running your script because it's used at the moment when the module is getting imported.

| Before patch 👎 | After patch 👍 |
|---|---|
| [![before](https://private-user-images.githubusercontent.com/177686430/367928511-3f6719e8-37ab-4451-be19-f854d66184d0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY3OTI4NTExLTNmNjcxOWU4LTM3YWItNDQ1MS1iZTE5LWY4NTRkNjYxODRkMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04N2IzMmU3MGE0MWFhZDFiYzYyZjZkZGM5M2I3MDU5YzAwMDg5Y2YxMDNhZTg2Njk2MDk1NDI2MWI2MWQxZWI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.HlINqN24_M4MBF0YyEAcwJwgdUlr4GWS1QWQ1Y1eSpQ)](https://private-user-images.githubusercontent.com/177686430/367928511-3f6719e8-37ab-4451-be19-f854d66184d0.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY3OTI4NTExLTNmNjcxOWU4LTM3YWItNDQ1MS1iZTE5LWY4NTRkNjYxODRkMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04N2IzMmU3MGE0MWFhZDFiYzYyZjZkZGM5M2I3MDU5YzAwMDg5Y2YxMDNhZTg2Njk2MDk1NDI2MWI2MWQxZWI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.HlINqN24_M4MBF0YyEAcwJwgdUlr4GWS1QWQ1Y1eSpQ) | [![after](https://private-user-images.githubusercontent.com/177686430/367928519-5425ab0e-50bc-4c40-b94f-443011fdb210.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY3OTI4NTE5LTU0MjVhYjBlLTUwYmMtNGM0MC1iOTRmLTQ0MzAxMWZkYjIxMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZDQyYmQ2ZDVmZjRkNmNmYWIzYjJmZTczYzRmMWM3NDIxMjMyNDNkZDYzM2IyOTQ3ZTBkZDljOTA2NmVhYTY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.s3mRUzD-FYh9kj61r_eOJ0GmcL1XBRGLtju_FDJVzhQ)](https://private-user-images.githubusercontent.com/177686430/367928519-5425ab0e-50bc-4c40-b94f-443011fdb210.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY3OTI4NTE5LTU0MjVhYjBlLTUwYmMtNGM0MC1iOTRmLTQ0MzAxMWZkYjIxMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZDQyYmQ2ZDVmZjRkNmNmYWIzYjJmZTczYzRmMWM3NDIxMjMyNDNkZDYzM2IyOTQ3ZTBkZDljOTA2NmVhYTY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.s3mRUzD-FYh9kj61r_eOJ0GmcL1XBRGLtju_FDJVzhQ) |
*Note: it's not detectable by external website scripts, but Google might use this information in their proprietary Chrome; we never know.*

## Usage

This package is designed to be run against an installed library. Install the library, then call the patcher, and it's ready to go.

In the root folder of your project, run:

```
npx rebrowser-patches@latest patch --packageName puppeteer-core
```

You can easily revert all changes with this command:

```
npx rebrowser-patches@latest unpatch --packageName puppeteer-core
```

You can also patch a package by providing the full path to its folder, for example:

```
npx rebrowser-patches@latest patch --packagePath /web/app/node_modules/puppeteer-core-custom
```

You can see all command-line options by running `npx rebrowser-patches@latest --help`, but currently, there's just one patch for one library, so you don't need to configure anything.

⚠️ Be aware that after running `npm install` or `yarn install` in your project folder, it might override all the changes from the patches. You'll need to run the patcher again to keep the patches in place.

## How to update the patches?

If you already have your package patched and want to update to the latest version of rebrowser-patches, the easiest way would be to delete `node_modules/puppeteer-core`, then run `npm install` or `yarn install --check-files`, and then run `npx rebrowser-patches@latest patch`.

## How to patch Java/Python/.NET versions of Playwright?

All these versions are just wrappers around Node.js version of Playwright. You need to find `driver` folder inside your Playwright package and run this patch with `--packagePath=$yourDriverFolder/$yourPlatform/package`.

## Puppeteer support

✅ Latest fully tested version: 24.8.1 (released 2025-05-06)

## Playwright support

Playwright patches include:

- `Runtime.enable` leak: `addBinding` and `alwaysIsolated`modes.
- Ability to change utility world name via `REBROWSER_PATCHES_UTILITY_WORLD_NAME` env variable.
- More patches are coming, star and follow the repo.
Important: `page.pause()` method doesn't work with the enabled fix, it needs more investigation. You can just disable the fix completely while debugging using `REBROWSER_PATCHES_RUNTIME_FIX_MODE=0` env variable.

These patches work only for Chrome for now. If you really want to use it with WebKit or Firefox, please open a new issue.

✅ Latest fully tested version: 1.52.0 (released 2025-04-17)

## How to use `rebrowser-puppeteer` with `puppeteer-extra`?

Use `addExtra` method, here is the example:

```
// before
import puppeteer from 'puppeteer-extra'

// after
import { addExtra } from 'puppeteer-extra'
import rebrowserPuppeteer from 'rebrowser-puppeteer-core'
const puppeteer = addExtra(rebrowserPuppeteer)
```

## Follow the project

We're currently developing more patches to improve web automation transparency, which will be released in this repo soon. Please support the project by clicking ⭐️ star or watch button.

💭 If you have any ideas, thoughts, or questions, feel free to reach out to our team by [email](mailto:info@rebrowser.net) or use the [issues section](https://github.com/rebrowser/rebrowser-patches/issues).

## The fix doesn't help, I'm still getting blocked 🤯

⚠️ It's important to know that this fix alone won't make your browser bulletproof and undetectable. You need to address **many other aspects** such as proxies, proper user-agent and fingerprints (canvas, WebGL), and more.

Always keep in mind: the less you manipulate browser internals via JS injections, the better. There are ways to detect that internal objects such as console, navigator, and others were affected by Proxy objects or Object.defineProperty. It's tricky, but it's always a cat-and-mouse game.

If you've tried everything and still face issues, try asking a question in the issues section or consider using cloud solutions from Rebrowser.

## What is Rebrowser?

This package is sponsored and maintained by [Rebrowser](https://rebrowser.net). We allow you to scale your browser automation and web scraping in the cloud with hundreds of unique fingerprints.

Our cloud browsers have great success rates and come with nice features such as notifications if your library uses `Runtime.Enable` during execution or has other red flags that could be improved. [Create an account](https://rebrowser.net) today to get invited to test our bleeding-edge platform and take your automation business to the next level.

[![Automated warnings](https://private-user-images.githubusercontent.com/177686430/368338539-5bee67ed-2ddd-4d80-9404-f65f19a865ec.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTE4ODU3MDAsIm5iZiI6MTc5MTg4NTQwMCwicGF0aCI6Ii8xNzc2ODY0MzAvMzY4MzM4NTM5LTViZWU2N2VkLTJkZGQtNGQ4MC05NDA0LWY2NWYxOWE4NjVlYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxM1QwOTU2NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mYzE4OTQwZWU2YjkxZGJjZmQ4YjNhNjI2ZjFhNThjNTExMzhmMzMzNDI1NDRmMGE5ZmVjODRkYTYxMDMwZGEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.tpPzrNxc7tEkYdifUFjAJ-OvLcpoOU0X_1ZaWe7Wt5s)](https://rebrowser.net/docs/sensitive-cdp-methods)

## Patch command on Windows

When you try to run this patcher on a Windows machine, you will probably encounter an error because the patch command is not found. To fix this, you need to install [Git](https://git-scm.com/download/win), which includes patch.exe. After you have installed it, you need to add it to your PATH:

```
set PATH=%PATH%;C:\Program Files\Git\usr\bin\
```

You can check that patch.exe is installed correctly by using next command:

```
patch -v
```

### Special thanks

[zfcsoftware/puppeteer-real-browser](https://github.com/zfcsoftware/puppeteer-real-browser) - general ideas and contribution to the automation community

[Kaliiiiiiiiii-Vinyzu/patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright) - set of patches to fix Playwright leaks

[kaliiiiiiiiii/brotector](https://github.com/kaliiiiiiiiii/brotector) - some modern tests, algorithm to distinguish CDP vs devtools

[prescience-data/harden-puppeteer](https://github.com/prescience-data/harden-puppeteer) - one of the pioneers of the execution in an isolated world

[puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth) - where it all started, big props to all the contributors and the community 🙏 berstend and co are the goats

### Disclaimer

 No responsibility is accepted for the use of this software. This software is intended for educational and informational purposes only. Users should use this software at their own risk. The developers of the software cannot be held liable for any damages that may result from the use of this software. This software is not intended to bypass any security measures, including but not limited to CAPTCHAs, anti-bot systems, or other protective mechanisms employed by websites. The software must not be used for malicious purposes. By using this software, you agree to this disclaimer and acknowledge that you are using the software responsibly and in compliance with all applicable laws and regulations.

## Files

patches/, scripts/, .gitignore, README.md, package.json

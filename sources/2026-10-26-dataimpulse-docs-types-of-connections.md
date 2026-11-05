---
url: https://docs.dataimpulse.com/proxies/types-of-connections
captured: 2026-10-26
word_count: 197
status: raw
---

For the complete documentation index, see [llms.txt](https://docs.dataimpulse.com/llms.txt). This page is also available as [Markdown](https://docs.dataimpulse.com/proxies/types-of-connections.md).

### Rotating[Direct link to heading](https://docs.dataimpulse.com/proxies/types-of-connections\#rotating)

The IP address changes automatically with each new request.

You should use:

For HTTP/HTTPS

**823** PORT

For SOCKS5

**824** PORT

![](https://docs.dataimpulse.com/~gitbook/image?url=https%3A%2F%2F2032935727-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2PNbkVMJTPjkWGv2Kbvj%252Fuploads%252FxaFpg37IOci7ozuGfNj5%252FGoogle%2520Chrome%25202024-11-06%2520%25D0%25B2%252009.46.33.png%3Falt%3Dmedia%26token%3D34a3a197-8c87-475c-8452-14e3653cdf61&width=768&dpr=3&quality=100&sign=88fccc0bbc16eae605b0137dc6627faf&sv=3)

* * *

### **Sticky**[Direct link to heading](https://docs.dataimpulse.com/proxies/types-of-connections\#sticky)

Sticky proxies are port-based. IP addresses are bound to a specific port for a period of time.

The rotation interval for sticky proxies can range from 1 to 120 minutes, with the average duration being 30 minutes.

For sticky connections, you can use ports from **10000** to **20000**.

An example of the HTTP sticky proxy:

Copy

```
curl -x "http://login:password@gw.dataimpulse.com:10000" https://api.ipify.org/
```

An example of the SOCKS5 sticky proxy:

Copy

```
curl -x "socks5://login:password@gw.dataimpulse.com:10000" https://api.ipify.org/
```

If no Rotation Interval is specified for a Sticky connection or is set to "0", the default interval will be 30 minutes.

* * *

![](https://docs.dataimpulse.com/~gitbook/image?url=https%3A%2F%2F2032935727-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2PNbkVMJTPjkWGv2Kbvj%252Fuploads%252FmF8SUohvv3OVtohiCfiv%252FGoogle%2520Chrome%25202024-11-06%2520%25D0%25B2%252009.36.29.png%3Falt%3Dmedia%26token%3Dc0d5f2c6-8f79-4634-9e85-79fc17f98e19&width=768&dpr=3&quality=100&sign=6d4c75ecbc432a85bf5bbf9993728f99&sv=3)

Blog article on selecting the best proxy type:

[Rotating or Sticky Proxies: How to Choose the Right Option](https://dataimpulse.com/blog/rotating-or-sticky-proxies-how-to-make-the-right-choice/)

[PreviousProxies](https://docs.dataimpulse.com/proxies) [NextProtocols](https://docs.dataimpulse.com/proxies/protocols)

Last updated 1 year ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://dataimpulse.com/privacy-policy/).

AcceptReject
---
url: https://developers.google.com/gmail/api/overview
captured: 2026-10-27
word_count: 784
status: raw
---

[Skip to main content](https://developers.google.com/workspace/gmail/api/guides#main-content)

[![Google Workspace](https://www.gstatic.com/images/branding/productlogos/googleg_gradient/v1/16px.svg)](https://developers.google.com/workspace)

- [GoogleWorkspace](https://developers.google.com/workspace)

`/`

- English
- Deutsch
- Español
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

Sign in

- [Gmail](https://developers.google.com/workspace/gmail)

- [Home](https://developers.google.com/)
- [Google Workspace](https://developers.google.com/workspace)
- [Gmail](https://developers.google.com/workspace/gmail)
- [Guides](https://developers.google.com/workspace/gmail/api/guides)



 Send feedback



# Gmail API overview    Stay organized with collections      Save and categorize content based on your preferences.

The Gmail API is a RESTful API that lets you access Gmail
mailboxes and send mail. For most web applications, the Gmail API is
the best choice for authorized access to a user's Gmail data and
is suitable for various applications, such as:

- Read-only mail extraction, indexing, and backup
- Automated or programmatic message sending
- Email account migration
- Email organization including filtering and sorting of messages
- Standardization of email signatures across an organization

## Common terms

The following is a list of common terms used in this API:

_Delegator and Delegate_A delegator is a Gmail user who grants mailbox access to
another user within the same Google Workspace organization. The user
receiving this access is the delegate. Delegates can read, send, and delete
messages, as well as view and add contacts on behalf of the delegator's
account. For more information, see [Manage\\
delegates](https://developers.google.com/workspace/gmail/api/guides/delegate_settings)._Draft_An unsent message. You can replace the message contained within the draft.
Sending a draft automatically deletes the draft and creates a message with
the `SENT` system label. The
[`drafts`](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts) resource
represents a draft. For more information, see [Work with\\
drafts](https://developers.google.com/workspace/gmail/api/guides/drafts)._Filters_Advanced rules configured for an account that evaluate incoming messages
against specific matching criteria (like sender, subject, or size). When a
message matches, filters automatically trigger actions such as adding or
removing labels, or forwarding the email to a specified address. For more
information, see [Manage\\
filters](https://developers.google.com/workspace/gmail/api/guides/filter_settings)._Forwarding addresses_Specific, verified email addresses configured to receive auto-forwarded
messages from a user's account. Before you can use an address in a
forwarding rule or filter, you must register and verify it to prove
ownership. For more information, see [Manage\\
forwarding](https://developers.google.com/workspace/gmail/api/guides/forwarding_settings)._Label_

A mechanism for organizing messages and threads. For example, you can create
the label "taxes" and apply it to all messages and threads related to taxes.
For more information, see [Manage\\
labels](https://developers.google.com/workspace/gmail/api/guides/labels).

There are two types of labels:

_System labels_Internally created labels, such as `INBOX`, `TRASH`, or `SPAM`. You can't
delete or modify these labels. However, you can apply or remove some system
labels, such as `INBOX`, to or from messages and threads._User labels_Labels created by a user. A user or an application can delete or modify
these labels. The
[`labels`](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels) resource
represents a user label._Message_

An email message containing the sender, recipients, subject, and body. After
you create a message, you can't change it. The
[`messages`](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages) resource
represents a message.

_Push notifications_

A server-side notification system integrating with Google Cloud Pub/Sub.
Applications can "watch" a mailbox, and the Gmail API sends
automatic webhooks or alerts whenever a change occurs (such as a new email
arriving). This eliminates the need for your app to poll the server for
updates. For more information, see [Push\\
notifications](https://developers.google.com/workspace/gmail/api/guides/push).

_S/MIME certificates_

Digital certificates uploaded to specific send-as aliases. These certificates
let you send encrypted and digitally signed emails, ensuring message
security and sender authenticity. For more information, see [Manage S/MIME\\
certificates](https://developers.google.com/workspace/gmail/api/guides/smime_certs).

_Send-as aliases_

These represent the various email addresses from which an account is
authorized to send mail. Every account has at least one alias representing
the primary email address. Aliases correspond to the "Send mail as" feature
in the Gmail web interface and are also the basis for
configuring per-address email signatures. For more information, see [Manage\\
aliases](https://developers.google.com/workspace/gmail/api/guides/alias_and_signature_settings).

_Thread_

A collection of related messages forming a conversation. In an email client,
a thread forms when one or more recipients respond to a message with their
own message. For more information, see [Manage\\
threads](https://developers.google.com/workspace/gmail/api/guides/threads).

## Related topics

- To learn about developing with Google Workspace APIs, including handling
authentication and authorization, refer to [Develop on\\
Google Workspace](https://developers.google.com/workspace/guides/get-started).

- To learn how to configure and run a Gmail API app, read the
[Quickstarts](https://developers.google.com/workspace/gmail/api/quickstart/js).




 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-09-18 UTC."\],\[\],\[\]\]

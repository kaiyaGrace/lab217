# Grammarly Desktop — Part 2
## JSON Message Structure Analysis

> Generated from observed Grammarly Desktop HTTP traffic.
> Captured JSON values are intentionally not included.

---

## 1. Capture Summary

- HTTP flows analyzed: **27629**
- Unique Grammarly endpoints: **158**
- Endpoints with JSON requests: **22**
- Endpoints with JSON responses: **25**
- Unique request schemas: **131**
- Unique response schemas: **27**

## 2. Observed Endpoint Tree

```text
├── app.grammarly.com
├── assets.grammarly.com
│   ├── emoji
│   │   └── v1
│   │       ├── 1f1fa-1f1f8.svg
│   │       ├── 1f3af.2x.png
│   │       ├── 1f44b.2x.png
│   │       ├── 1f44d.2x.png
│   │       ├── 1f454.2x.png
│   │       ├── 1f455.2x.png
│   │       ├── 1f4a1.2x.png
│   │       ├── 1f4ad.2x.png
│   │       ├── 1f58a.2x.png
│   │       ├── 1f5bc.2x.png
│   │       ├── 1f607.2x.png
│   │       ├── 1f60a.2x.png
│   │       ├── 1f60c.2x.png
│   │       ├── 1f60d.2x.png
│   │       ├── 1f610.2x.png
│   │       ├── 1f642.2x.png
│   │       ├── 1f913.2x.png
│   │       ├── 1f914.2x.png
│   │       ├── 1f917.2x.png
│   │       ├── 1f91d.2x.png
│   │       ├── 1f929.2x.png
│   │       ├── 1f92d.2x.png
│   │       └── 261d.2x.png
│   ├── icons
│   │   └── v1
│   │       ├── gds-icon-ggo-action-generate-ideas-category.2x.png
│   │       ├── gds-icon-ggo-action-improve.2x.png
│   │       ├── gds-icon-ggo-action-make-it-personal.2x.png
│   │       ├── gds-icon-ggo-action-make-it-professional.2x.png
│   │       ├── gds-icon-ggo-action-shorten.2x.png
│   │       └── gds-icon-ggo-action-simplify.2x.png
│   └── sdui
│       └── v1
│           ├── magic-document.2x.png
│           ├── star.2x.png
│           └── success-impression.2x.png
├── assistant.femetrics.grammarly.io
│   └── batch
│       └── import
├── auth.grammarly.com
│   ├── auth
│   │   ├── v3
│   │   │   └── user
│   │   │       ├── bridge
│   │   │       │   └── check-eligibility
│   │   │       │       └── coda
│   │   │       └── oranonymous
│   │   └── v5
│   │       └── api
│   │           └── userinfo
│   └── tokens
│       └── v4
│           └── api
│               └── oauth2
│                   └── token
├── capi.grammarly.com
│   ├── api
│   │   └── configuration
│   │       ├── cheetah
│   │       │   └── v1
│   │       │       └── settings
│   │       └── suggestion-bundles
│   │           └── v1
│   │               └── settings
│   ├── fpws
│   └── freews
├── coda.grammarly.com
│   └── internalAppApi
│       └── doclist
│           └── recent
├── denali-static.grammarly.com
│   └── js
│       └── {token}
│           ├── default-mp.js
│           ├── runtime.js
│           └── vendor-e~ae~ci~cb~as~mp.js
├── dox.grammarly.com
│   └── documents
├── editor.femetrics.grammarly.io
│   └── batch
│       └── import
├── f-log-assistant.grammarly.io
│   └── log
├── f-log-editor-debug.grammarly.io
│   └── logv2
├── f-log-editor.grammarly.io
│   └── logv2
├── f-log-inkwell.grammarly.io
│   └── batch
│       └── log
├── f-log-win-extension.grammarly.io
│   └── logv2
├── gateway.grammarly.com
│   ├── authorship
│   │   └── v1
│   │       └── user
│   │           └── {id}
│   │               └── settings
│   ├── experimentation
│   │   ├── gates
│   │   │   └── get
│   │   ├── properties
│   │   │   └── showDesktopIntegrationExtensionToggle
│   │   └── treatment
│   │       ├── get
│   │       └── log
│   ├── health
│   ├── mise
│   │   └── api
│   │       └── v1
│   │           └── iterable
│   │               └── access
│   │                   └── token
│   ├── passport
│   │   └── api
│   │       └── v1
│   │           └── passport
│   ├── privacy
│   │   └── v1
│   │       └── api
│   │           └── data-sharing
│   │               └── user
│   ├── subscription
│   │   └── api
│   │       ├── v1
│   │       │   └── subscription
│   │       └── v2
│   │           └── support-portal
│   │               └── userInfo
│   ├── uhub
│   │   ├── configuration
│   │   └── events
│   └── vito
│       ├── plans
│       └── special-offers
├── gnar.grammarly.com
│   ├── events
│   └── lite
├── go.grammarly.com
│   └── analytics
├── goldengate.grammarly.com
│   ├── institution
│   │   └── api
│   │       └── institution
│   │           └── admin
│   │               └── institution_info
│   └── skills
│       └── users
│           └── {id}
│               └── skills
├── in.grammarly.com
│   └── v1
│       └── events
│           └── ingestion_front_end
├── inkwell.femetrics.grammarly.io
│   └── batch
│       └── import
├── static-web.grammarly.com
│   ├── 1e6ajr2k4140
│   │   ├── 16iyP4HxLGn8HRUVz73yxf
│   │   │   └── {token}
│   │   │       └── Frame_2055245639.svg
│   │   ├── 4p0YxlEhKBkGTE3g1oX6Fh
│   │   │   └── {token}
│   │   │       └── square_image__1_.png
│   │   ├── 5423x1zYeb1zyldyyUdYPI
│   │   │   └── {token}
│   │   │       └── ICONS__30_.svg
│   │   ├── 5J6bEVGOrnZvAXNVfEwi2Q
│   │   │   └── {token}
│   │   │       └── ICONS__29_.svg
│   │   ├── 67Dl0aecY6JEAJ61q42Iwh
│   │   │   └── {token}
│   │   │       └── Frame_2055245682.svg
│   │   ├── 77xEyv3tvgGYDQjdo3vljv
│   │   │   └── {token}
│   │   │       └── ICONS__28_.svg
│   │   └── ltlKbGWebGgQGEVfOIszz
│   │       └── {token}
│   │           └── Frame_2055245684__1_.svg
│   ├── cms
│   │   └── master
│   │       └── _next
│   │           └── static
│   │               ├── 8aa1SwZmUdTTBQ_xRC1J4
│   │               │   ├── _buildManifest.js
│   │               │   └── _ssgManifest.js
│   │               ├── chunks
│   │               │   ├── 1a192442-332914e99bef1049.js
│   │               │   ├── 2581.0d6df08d5ee7c339.js
│   │               │   ├── 2810.2a82a60015e534cd.js
│   │               │   ├── 3234.be94bafbca8e422c.js
│   │               │   ├── 3446.2f43a1ffbde3f5c1.js
│   │               │   ├── 4902.96a5571238a2af78.js
│   │               │   ├── 4956.62e09d77974d2c0e.js
│   │               │   ├── 4957.262428f454a2402a.js
│   │               │   ├── 5082-f108c72735a88874.js
│   │               │   ├── 6497-0a8c419515b66d21.js
│   │               │   ├── 6e5e196e-66b1a94fba27f601.js
│   │               │   ├── 7248.435b716bf1f28dcf.js
│   │               │   ├── 7564.a57ed589727aa0c0.js
│   │               │   ├── framework-9188fd1d264b3ab9.js
│   │               │   ├── main-056f5034ee75ac0f.js
│   │               │   ├── pages
│   │               │   │   ├── _app-20531691b7ff54d1.js
│   │               │   │   └── render-1df5ea362bf639f5.js
│   │               │   └── webpack-7717e9e0ed3d9bc6.js
│   │               └── css
│   │                   ├── 11cd3a9b870d8cea.css
│   │                   ├── 26ad7c2b7243e22c.css
│   │                   ├── 27203ff1a31c1d3e.css
│   │                   ├── 5182367ecb17ba61.css
│   │                   ├── 66378a4254fb9db8.css
│   │                   ├── 8f5d1d401fc71ea3.css
│   │                   └── afeb416bd6ea3894.css
│   ├── shared
│   │   └── fonts
│   │       ├── glyph-bold.woff2
│   │       ├── glyph-regular.woff2
│   │       ├── matter-medium.woff2
│   │       └── matter-semi-bold.woff2
│   └── web-heartbeat
│       └── latest
│           └── index.js
├── static.institution.grammarly.com
│   └── logo
│       └── ec8c59d1a4c7b0698cda682c3ee2f69ed3d7279d.png
├── subscription.grammarly.com
│   └── api
│       ├── v1
│       │   ├── referrals
│       │   │   └── info
│       │   ├── sku-type
│       │   └── subscription
│       └── v2
│           └── support-portal
│               └── chatbot
│                   └── token
├── support.grammarly.com
│   ├── api
│   │   └── v2
│   │       ├── help_center
│   │       │   └── en-us
│   │       │       └── articles
│   │       │           └── {id}
│   │       │               └── stats
│   │       │                   └── view.json
│   │       └── requests.json
│   └── hc
│       ├── activity
│       ├── en-us
│       │   └── articles
│       │       └── 4403227220237-Is-Grammarly-HIPAA-compliant
│       └── theming_assets
│           ├── 01HZAXT1YPZJP3VQJVC6HGA4M1
│           ├── 01HZAXT2FM04Y7K940XV55PJG6
│           ├── 01HZAXT2WSVN7PZTM4S8NXZHCZ
│           ├── 01HZAXT3GMDNWVQRD5AD6NPM0C
│           ├── 01HZAXT3R76SQ3MWB33MVEHJ51
│           ├── 01HZAXT3VKRH22X382D0MXNXSQ
│           ├── 01HZAXT43MV98QKSSQ85Y9M3AQ
│           ├── 01HZAXT4TV234GMK6HGHFMAXM8
│           ├── 01HZAXT67W142QH6S0VKSTREYR
│           ├── 01HZAXT684AW9802Y6VJF5J3EY
│           ├── 01HZAXT69TK9XZ8J984DXQZTG3
│           ├── 01JYHF5RR5AS8XV9SKQP7FS6J1
│           ├── 01JYHF5S113PH9BW1TC1ZM25RP
│           ├── 01JYHF5S1JGTEZYXMBJ3CKBPHX
│           ├── 01JYHF5S85C2BQZK6X4ZVMCAV4
│           ├── 01JYHF5SEFXEG1EKJCJZ42AZQ4
│           ├── 01JYHF5SSANKF3GB4AFRB1XEGV
│           ├── 01JYHF5SZKJNZ5P7QT6FJPF69J
│           ├── 01JYHF5T6BS1EEED7WPY7JX62V
│           ├── 01JYHF5T7D5ETZCN3WSSRGETHY
│           ├── 01KB0826J1HQ60ESX1SHSSZ6DK
│           ├── 01KQZ04BZH071BEY5A1AYQ2HF0
│           └── {id}
│               └── {id}
│                   ├── script.js
│                   └── style.css
├── treatment.grammarly.com
│   └── treatment
│       └── get
├── update-windows.grammarly.com
│   └── update
│       └── llamaWindows
├── website.femetrics.grammarly.io
│   └── batch
│       └── import
├── win-extension.femetrics.grammarly.io
│   └── batch
│       └── import
└── www.grammarly.com
    ├── api
    │   └── tracking
    │       └── load
    ├── css
    │   └── transcend-airgap.css
    └── privacy
```

## 3. Endpoint Frequency

| Method | Host | Endpoint | Requests | JSON Requests | JSON Responses |
|---|---|---|---:|---:|---:|
| POST | `win-extension.femetrics.grammarly.io` | `/batch/import` | 1134 | 0 | 0 |
| OPTIONS, POST | `gateway.grammarly.com` | `/experimentation/treatment/get` | 677 | 377 | 95 |
| POST | `gnar.grammarly.com` | `/lite` | 642 | 642 | 0 |
| POST | `inkwell.femetrics.grammarly.io` | `/batch/import` | 616 | 616 | 0 |
| OPTIONS, POST | `gnar.grammarly.com` | `/events` | 532 | 525 | 0 |
| POST | `in.grammarly.com` | `/v1/events` | 403 | 403 | 0 |
| POST, OPTIONS | `gateway.grammarly.com` | `/experimentation/gates/get` | 131 | 113 | 95 |
| OPTIONS, POST | `f-log-inkwell.grammarly.io` | `/batch/log` | 110 | 48 | 0 |
| GET | `capi.grammarly.com` | `/fpws` | 109 | 0 | 0 |
| POST | `in.grammarly.com` | `/v1/events/ingestion_front_end` | 80 | 80 | 0 |
| GET, OPTIONS | `auth.grammarly.com` | `/auth/v5/api/userinfo` | 50 | 0 | 4 |
| OPTIONS, GET | `capi.grammarly.com` | `/api/configuration/cheetah/v1/settings` | 50 | 0 | 17 |
| POST | `f-log-assistant.grammarly.io` | `/log` | 50 | 50 | 0 |
| POST | `assistant.femetrics.grammarly.io` | `/batch/import` | 42 | 42 | 0 |
| GET | `capi.grammarly.com` | `/freews` | 26 | 0 | 0 |
| POST | `auth.grammarly.com` | `/tokens/v4/api/oauth2/token` | 24 | 24 | 24 |
| OPTIONS, POST | `f-log-editor.grammarly.io` | `/logv2` | 18 | 9 | 0 |
| POST | `f-log-win-extension.grammarly.io` | `/logv2` | 14 | 14 | 0 |
| OPTIONS, GET | `gateway.grammarly.com` | `/passport/api/v1/passport` | 13 | 0 | 11 |
| GET | `goldengate.grammarly.com` | `/skills/users/{id}/skills` | 12 | 0 | 0 |
| OPTIONS, GET | `gateway.grammarly.com` | `/uhub/configuration` | 11 | 0 | 10 |
| POST | `treatment.grammarly.com` | `/treatment/get` | 9 | 9 | 9 |
| POST | `update-windows.grammarly.com` | `/update/llamaWindows` | 9 | 9 | 9 |
| OPTIONS, GET, POST | `gateway.grammarly.com` | `/experimentation/properties` | 6 | 2 | 2 |
| OPTIONS, GET | `subscription.grammarly.com` | `/api/v1/subscription` | 4 | 0 | 3 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f3af.2x.png` | 2 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f455.2x.png` | 2 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f914.2x.png` | 2 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f917.2x.png` | 2 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f91d.2x.png` | 2 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/261d.2x.png` | 2 | 0 | 0 |
| OPTIONS, GET | `auth.grammarly.com` | `/auth/v3/user` | 2 | 0 | 0 |
| OPTIONS, GET | `auth.grammarly.com` | `/auth/v3/user/bridge/check-eligibility/coda` | 2 | 0 | 1 |
| OPTIONS, GET | `auth.grammarly.com` | `/auth/v3/user/oranonymous` | 2 | 0 | 0 |
| GET | `capi.grammarly.com` | `/api/configuration/suggestion-bundles/v1/settings` | 2 | 0 | 2 |
| OPTIONS, GET | `dox.grammarly.com` | `/documents` | 2 | 0 | 0 |
| OPTIONS, POST | `f-log-editor-debug.grammarly.io` | `/logv2` | 2 | 1 | 0 |
| GET | `gateway.grammarly.com` | `/authorship/v1/user/{id}/settings` | 2 | 0 | 0 |
| GET | `gateway.grammarly.com` | `/experimentation/properties/showDesktopIntegrationExtensionToggle` | 2 | 0 | 2 |
| GET | `gateway.grammarly.com` | `/health` | 2 | 0 | 2 |
| GET | `gateway.grammarly.com` | `/mise/api/v1/iterable/access/token` | 2 | 0 | 2 |
| GET | `gateway.grammarly.com` | `/privacy/v1/api/data-sharing/user` | 2 | 0 | 2 |
| OPTIONS, GET | `gateway.grammarly.com` | `/subscription/api/v1/subscription` | 2 | 0 | 1 |
| OPTIONS, GET | `gateway.grammarly.com` | `/subscription/api/v2/support-portal/userInfo` | 2 | 0 | 1 |
| OPTIONS, POST | `gateway.grammarly.com` | `/uhub/events` | 2 | 1 | 0 |
| OPTIONS, GET | `gateway.grammarly.com` | `/vito/plans` | 2 | 0 | 1 |
| OPTIONS, GET | `gateway.grammarly.com` | `/vito/special-offers` | 2 | 0 | 1 |
| GET | `go.grammarly.com` | `/analytics` | 2 | 0 | 0 |
| OPTIONS, GET | `goldengate.grammarly.com` | `/institution/api/institution/admin/institution_info` | 2 | 0 | 1 |
| OPTIONS, POST | `subscription.grammarly.com` | `/api/v1/referrals/info` | 2 | 0 | 1 |
| OPTIONS, GET | `subscription.grammarly.com` | `/api/v1/sku-type` | 2 | 0 | 1 |
| OPTIONS, GET | `subscription.grammarly.com` | `/api/v2/support-portal/chatbot/token` | 2 | 0 | 1 |
| POST | `website.femetrics.grammarly.io` | `/batch/import` | 2 | 2 | 0 |
| GET | `app.grammarly.com` | `/` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f1fa-1f1f8.svg` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f44b.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f44d.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f454.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f4a1.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f4ad.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f58a.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f5bc.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f607.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f60a.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f60c.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f60d.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f610.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f642.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f913.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f929.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/emoji/v1/1f92d.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-generate-ideas-category.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-improve.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-make-it-personal.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-make-it-professional.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-shorten.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/icons/v1/gds-icon-ggo-action-simplify.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/sdui/v1/magic-document.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/sdui/v1/star.2x.png` | 1 | 0 | 0 |
| GET | `assets.grammarly.com` | `/sdui/v1/success-impression.2x.png` | 1 | 0 | 0 |
| OPTIONS | `coda.grammarly.com` | `/internalAppApi/doclist/recent` | 1 | 0 | 0 |
| GET | `denali-static.grammarly.com` | `/js/{token}/default-mp.js` | 1 | 0 | 0 |
| GET | `denali-static.grammarly.com` | `/js/{token}/runtime.js` | 1 | 0 | 0 |
| GET | `denali-static.grammarly.com` | `/js/{token}/vendor-e~ae~ci~cb~as~mp.js` | 1 | 0 | 0 |
| POST | `editor.femetrics.grammarly.io` | `/batch/import` | 1 | 1 | 0 |
| POST | `gateway.grammarly.com` | `/experimentation/treatment/log` | 1 | 1 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/16iyP4HxLGn8HRUVz73yxf/{token}/Frame_2055245639.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/4p0YxlEhKBkGTE3g1oX6Fh/{token}/square_image__1_.png` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/5423x1zYeb1zyldyyUdYPI/{token}/ICONS__30_.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/5J6bEVGOrnZvAXNVfEwi2Q/{token}/ICONS__29_.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/67Dl0aecY6JEAJ61q42Iwh/{token}/Frame_2055245682.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/77xEyv3tvgGYDQjdo3vljv/{token}/ICONS__28_.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/1e6ajr2k4140/ltlKbGWebGgQGEVfOIszz/{token}/Frame_2055245684__1_.svg` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/8aa1SwZmUdTTBQ_xRC1J4/_buildManifest.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/8aa1SwZmUdTTBQ_xRC1J4/_ssgManifest.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/1a192442-332914e99bef1049.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/2581.0d6df08d5ee7c339.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/2810.2a82a60015e534cd.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/3234.be94bafbca8e422c.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/3446.2f43a1ffbde3f5c1.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/4902.96a5571238a2af78.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/4956.62e09d77974d2c0e.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/4957.262428f454a2402a.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/5082-f108c72735a88874.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/6497-0a8c419515b66d21.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/6e5e196e-66b1a94fba27f601.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/7248.435b716bf1f28dcf.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/7564.a57ed589727aa0c0.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/framework-9188fd1d264b3ab9.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/main-056f5034ee75ac0f.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/pages/_app-20531691b7ff54d1.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/pages/render-1df5ea362bf639f5.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/chunks/webpack-7717e9e0ed3d9bc6.js` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/11cd3a9b870d8cea.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/26ad7c2b7243e22c.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/27203ff1a31c1d3e.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/5182367ecb17ba61.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/66378a4254fb9db8.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/8f5d1d401fc71ea3.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/cms/master/_next/static/css/afeb416bd6ea3894.css` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/shared/fonts/glyph-bold.woff2` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/shared/fonts/glyph-regular.woff2` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/shared/fonts/matter-medium.woff2` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/shared/fonts/matter-semi-bold.woff2` | 1 | 0 | 0 |
| GET | `static-web.grammarly.com` | `/web-heartbeat/latest/index.js` | 1 | 0 | 0 |
| GET | `static.institution.grammarly.com` | `/logo/ec8c59d1a4c7b0698cda682c3ee2f69ed3d7279d.png` | 1 | 0 | 0 |
| POST | `support.grammarly.com` | `/api/v2/help_center/en-us/articles/{id}/stats/view.json` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/api/v2/requests.json` | 1 | 0 | 0 |
| POST | `support.grammarly.com` | `/hc/activity` | 1 | 1 | 0 |
| GET | `support.grammarly.com` | `/hc/en-us/articles/4403227220237-Is-Grammarly-HIPAA-compliant` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT1YPZJP3VQJVC6HGA4M1` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT2FM04Y7K940XV55PJG6` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT2WSVN7PZTM4S8NXZHCZ` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT3GMDNWVQRD5AD6NPM0C` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT3R76SQ3MWB33MVEHJ51` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT3VKRH22X382D0MXNXSQ` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT43MV98QKSSQ85Y9M3AQ` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT4TV234GMK6HGHFMAXM8` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT67W142QH6S0VKSTREYR` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT684AW9802Y6VJF5J3EY` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01HZAXT69TK9XZ8J984DXQZTG3` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5RR5AS8XV9SKQP7FS6J1` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5S113PH9BW1TC1ZM25RP` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5S1JGTEZYXMBJ3CKBPHX` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5S85C2BQZK6X4ZVMCAV4` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5SEFXEG1EKJCJZ42AZQ4` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5SSANKF3GB4AFRB1XEGV` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5SZKJNZ5P7QT6FJPF69J` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5T6BS1EEED7WPY7JX62V` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01JYHF5T7D5ETZCN3WSSRGETHY` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01KB0826J1HQ60ESX1SHSSZ6DK` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/01KQZ04BZH071BEY5A1AYQ2HF0` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/{id}/{id}/script.js` | 1 | 0 | 0 |
| GET | `support.grammarly.com` | `/hc/theming_assets/{id}/{id}/style.css` | 1 | 0 | 0 |
| GET | `www.grammarly.com` | `/` | 1 | 0 | 0 |
| GET | `www.grammarly.com` | `/api/tracking/load` | 1 | 0 | 0 |
| GET | `www.grammarly.com` | `/css/transcend-airgap.css` | 1 | 0 | 0 |
| GET | `www.grammarly.com` | `/privacy` | 1 | 0 | 0 |

## 4. JSON Message Structures by Endpoint

---

### `win-extension.femetrics.grammarly.io/batch/import`

**Observed methods:** `POST`
**Observed requests:** 1134
**Response statuses:** 200: 1100

#### Request

**No JSON request body was observed.**

#### Response

Content types: `text/plain` (1100)

**No response body was observed.**

---

### `gateway.grammarly.com/experimentation/treatment/get`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 677
**Response statuses:** 200: 659

#### Request

Content types: `application/json` (377)

JSON requests: **377**

**Request field frequency**


**Request schema variants**

**Schema 1** `76efce69de` — 377 requests

```json
[
    string
]
```

#### Response

Content types: `text/plain` (282), `application/json` (377)

JSON responses: **95**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].containerId` | 100% | string |
| `[].dynamicConfiguration` | 100% | string |
| `[].experimentId` | 100% | string |
| `[].experimentName` | 100% | string |
| `[].groupName` | 100% | string |
| `[].isTest` | 100% | boolean |
| `[].needLog` | 100% | boolean |
| `[].overrideType` | 100% | null |
| `[].qualifiedName` | 100% | null |
| `[].sender` | 100% | null |
| `[].source` | 100% | string |
| `[].type` | 100% | string |
| `[].userId` | 100% | integer |

**Response schema variants**

**Schema 1** `7ca95307b7` — 95 responses

```json
[
    {
        "containerId": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": null,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
    {
        "containerId": string,
        "dynamicConfiguration": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": null,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
]
```

---

### `gnar.grammarly.com/lite`

**Observed methods:** `POST`
**Observed requests:** 642
**Response statuses:** 200: 642

#### Request

Content types: `application/json` (642)

JSON requests: **642**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `events` | 100% | array |
| `events[].action` | 98.1% | string |
| `events[].actionId` | 97.4% | string |
| `events[].actionName` | 97.4% | string |
| `events[].client` | 100% | string |
| `events[].clientVersion` | 100% | string |
| `events[].containerHeight` | 100% | integer |
| `events[].containerId` | 100% | string |
| `events[].containerWidth` | 100% | integer |
| `events[].devicePixelRatio` | 100% | integer |
| `events[].eventName` | 100% | string |
| `events[].feed` | 0.3% | string |
| `events[].isTest` | 100% | boolean |
| `events[].lens` | 0.5% | string |
| `events[].object` | 98.1% | string |
| `events[].objectId` | 98.1% | string |
| `events[].options` | 1.9% | object |
| `events[].options.error` | 1.9% | string |
| `events[].options.message` | 1.9% | string |
| `events[].placement` | 97.4% | string |
| `events[].position` | 97.4% | integer |
| `events[].promptNumber` | 97.4% | integer |
| `events[].referrer` | 100% | string |
| `events[].screenHeight` | 100% | integer |
| `events[].screenWidth` | 100% | integer |
| `events[].sessionUuid` | 98.1% | string |
| `events[].successStateType` | 0.3% | string |
| `events[].url` | 100% | string |
| `events[].userAgent` | 100% | string |
| `events[].userId` | 100% | string |

**Request schema variants**

**Schema 1** `f48224ca56` — 625 requests

```json
{
    "events": [
            {
                "action": string,
                "actionId": string,
                "actionName": string,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "isTest": boolean,
                "object": string,
                "objectId": string,
                "placement": string,
                "position": integer,
                "promptNumber": integer,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "sessionUuid": string,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 2** `79ccafa058` — 12 requests

```json
{
    "events": [
            {
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "isTest": boolean,
                "options": {
                                "error": string,
                                "message": string
                            },
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 3** `637c6eff18` — 3 requests

```json
{
    "events": [
            {
                "action": string,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "isTest": boolean,
                "lens": string,
                "object": string,
                "objectId": string,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "sessionUuid": string,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 4** `b83b1fce39` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "feed": string,
                "isTest": boolean,
                "object": string,
                "objectId": string,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "sessionUuid": string,
                "successStateType": string,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

#### Response

**No response body was observed.**

---

### `inkwell.femetrics.grammarly.io/batch/import`

**Observed methods:** `POST`
**Observed requests:** 616
**Response statuses:** 200: 604

#### Request

Content types: `application/json` (299), `text/plain` (317)

JSON requests: **616**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].labels` | 100% | array |
| `[].labels[].key` | 100% | string |
| `[].labels[].value` | 100% | string |
| `[].name` | 100% | string |
| `[].report_interval` | 100% | string |
| `[].type` | 100% | string |
| `[].value` | 100% | integer, number |

**Request schema variants**

**Schema 1** `65f5461f02` — 299 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": number
    }
]
```

**Schema 2** `ff5759dd77` — 198 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": integer
    }
]
```

**Schema 3** `b4707be24e` — 104 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": integer
    }
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": number
    }
]
```

**Schema 4** `ca0e2883a6` — 15 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": number
    }
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": integer
    }
]
```

#### Response

Content types: `text/plain` (604)

**No response body was observed.**

---

### `gnar.grammarly.com/events`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 532
**Response statuses:** 200: 532

#### Request

Content types: `application/json` (525)

JSON requests: **525**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `events` | 100% | array |
| `events[].Accessible2LongKeyboardSimulationSelectionCount` | 28.0% | number |
| `events[].acc2SelectCount` | 28.0% | number |
| `events[].acc2SelectUIAutoAndKbSimFallbackCount` | 28.0% | number |
| `events[].acc2SelectUIAutoAndKbSimFallbackFailedCount` | 28.0% | number |
| `events[].acc2SelectUIAutoFallbackCount` | 28.0% | number |
| `events[].acc2SelectUIAutoFallbackFailedCount` | 28.0% | number |
| `events[].accessible2KeyboardSimulationSelectionCount` | 28.0% | number |
| `events[].action` | 100% | string |
| `events[].alertAcceptedLongRewriteCount` | 28.0% | number |
| `events[].alertAcceptedRewrite101_200CharsCount` | 28.0% | number |
| `events[].alertAcceptedRewrite31_100CharsCount` | 28.0% | number |
| `events[].alertAcceptedRewriteBeyond200CharsCount` | 28.0% | number |
| `events[].alertAcceptedRewriteUnder30CharsCount` | 28.0% | number |
| `events[].alertAcceptedShortRewriteCount` | 28.0% | number |
| `events[].alertsAcceptedClassicCount` | 28.0% | number |
| `events[].alertsAcceptedClassicInlineCount` | 28.0% | number |
| `events[].alertsAcceptedClassicLongFormCount` | 28.0% | number |
| `events[].alertsAcceptedClassicShortFormCount` | 28.0% | number |
| `events[].alertsAcceptedCount` | 28.0% | number |
| `events[].alertsAcceptedGenerationInsertsCount` | 28.0% | number |
| `events[].alertsAcceptedInline` | 28.0% | number |
| `events[].alertsAcceptedRevision` | 28.0% | number |
| `events[].alertsAcceptedSnippetsCount` | 28.0% | number |
| `events[].alertsAcceptedVBarCount` | 28.0% | number |
| `events[].alertsIgnoredInline` | 28.0% | number |
| `events[].alertsIgnoredRevision` | 28.0% | number |
| `events[].alertsShownInline` | 28.0% | number |
| `events[].anchorHeightUsed` | 1.3% | string |
| `events[].anchorLocationUsed` | 1.3% | string |
| `events[].anchorSideUsed` | 1.3% | string |
| `events[].appPlatformType` | 29.3% | string |
| `events[].applySource` | 4.8% | string |
| `events[].applyStatusCorruptedCount` | 28.0% | number |
| `events[].applyStatusFailCount` | 28.0% | number |
| `events[].applyStatusUnknownCount` | 28.0% | number |
| `events[].areSame` | 4.6% | boolean |
| `events[].articleTitle` | 0.2% | string |
| `events[].assistantAvailable` | 43.0% | boolean |
| `events[].bannerType` | 0.2% | string |
| `events[].batchId` | 100% | integer |
| `events[].brandToneShown` | 31.4% | boolean |
| `events[].browserType` | 14.9% | string |
| `events[].capiAuthAttempts` | 28.0% | number |
| `events[].capiAuthFails` | 28.0% | number |
| `events[].capiAuthTime` | 28.0% | number |
| `events[].capiSessionType` | 29.7% | string |
| `events[].clarity` | 5.1% | number |
| `events[].client` | 100% | string |
| `events[].clientName` | 0.6% | string |
| `events[].clientVersion` | 100% | string |
| `events[].containerHeight` | 1.3% | integer |
| `events[].containerId` | 100% | string |
| `events[].containerWidth` | 1.3% | integer |
| `events[].correctness` | 5.1% | number |
| `events[].cpuArchitecture` | 28.4% | string |
| `events[].currentLanguage` | 0.2% | string |
| `events[].delivery` | 5.1% | number |
| `events[].detectionTs` | 43.4% | number |
| `events[].devicePixelRatio` | 1.3% | integer |
| `events[].deviceSystemVersion` | 100% | string |
| `events[].deviceType` | 0.2% | string |
| `events[].domainName` | 0.6% | string |
| `events[].duration` | 8.0% | number |
| `events[].emogenieShown` | 51.8% | boolean, number |
| `events[].emogenieVisible` | 1.7% | boolean |
| `events[].emotion` | 2.5% | string |
| `events[].endpoint` | 5.0% | string |
| `events[].engagement` | 5.1% | number |
| `events[].eventName` | 100% | string |
| `events[].eventSchemaVersion` | 43.4% | number |
| `events[].extendedUpdateInterval` | 0.4% | boolean |
| `events[].feature` | 1.7% | string |
| `events[].fieldHeight` | 29.3% | number |
| `events[].fieldWidth` | 29.3% | number |
| `events[].finalTextLength` | 28.0% | number |
| `events[].firstMessageReceivedWithRevisionIdTs` | 43.4% | number |
| `events[].firstMessageSentWithRevisionIdTextLength` | 43.4% | number |
| `events[].firstMessageSentWithRevisionIdTs` | 43.4% | number |
| `events[].freePremiumSuggestionsAvailable` | 28.0% | boolean |
| `events[].gButtonInitializedStatus` | 23.8% | string |
| `events[].gButtonInitializedTs` | 23.8% | number |
| `events[].gButtonShownStatus` | 41.3% | string |
| `events[].gButtonShownTs` | 41.3% | number |
| `events[].gaClientId` | 0.2% | string |
| `events[].initialTextLength` | 23.8% | number |
| `events[].instanceId` | 100% | string |
| `events[].integrationUuid` | 77.3% | string |
| `events[].intentTs` | 43.4% | number |
| `events[].isAnonymous` | 4.6% | boolean |
| `events[].isBrandTone` | 2.5% | boolean |
| `events[].isCppRedistAvailable` | 0.4% | boolean |
| `events[].isFirstLaunch` | 0.4% | boolean |
| `events[].isMobile` | 0.2% | boolean |
| `events[].isSduiFeed` | 31.6% | boolean |
| `events[].isStaticFallback` | 0.2% | boolean |
| `events[].isTest` | 100% | boolean |
| `events[].isTouchDevice` | 0.4% | boolean |
| `events[].isUnload` | 0.6% | boolean |
| `events[].lastStage` | 43.4% | string |
| `events[].launchAtStartupState` | 0.4% | string |
| `events[].lockedUISuggestionsAvailable` | 28.0% | boolean |
| `events[].microsoftCampaign` | 100% | boolean |
| `events[].object` | 100% | string |
| `events[].objectId` | 100% | string |
| `events[].onboardingInProgress` | 1.3% | boolean |
| `events[].os` | 0.2% | string |
| `events[].outOfSyncCount` | 28.0% | number |
| `events[].pageHeartbeatSeconds` | 0.6% | integer, number |
| `events[].pageId` | 0.6% | string |
| `events[].pageSlug` | 0.8% | string |
| `events[].pageUrl` | 0.6% | string |
| `events[].pageViewId` | 0.6% | string |
| `events[].pagedModeEnabled` | 29.7% | boolean |
| `events[].perMachineInstallation` | 100% | boolean |
| `events[].pluginActivation` | 81.3% | string |
| `events[].primaryUIType` | 28.0% | string |
| `events[].programmableStart` | 100% | boolean |
| `events[].referrer` | 1.7% | string |
| `events[].responseStatus` | 5.0% | string |
| `events[].rti` | 4.6% | string |
| `events[].savedEmpty` | 4.6% | boolean |
| `events[].savingEmpty` | 4.6% | boolean |
| `events[].screenHeight` | 1.3% | integer |
| `events[].screenWidth` | 1.3% | integer |
| `events[].secondsSinceOpened` | 0.8% | number |
| `events[].sessionDuration` | 28.0% | number |
| `events[].sessionUuid` | 72.0% | string |
| `events[].source` | 8.8% | string |
| `events[].startSessionReceivedTs` | 43.4% | number |
| `events[].startSessionSentTs` | 43.4% | number |
| `events[].status` | 1.7% | string |
| `events[].styleGuide` | 5.1% | number |
| `events[].success` | 1.7% | boolean |
| `events[].suggestionCount` | 29.0% | number |
| `events[].superhumanMode` | 100% | boolean |
| `events[].textCorruptionClassicCount` | 28.0% | number |
| `events[].textCorruptionClassicInlineCount` | 28.0% | number |
| `events[].textCorruptionClassicLongFormCount` | 28.0% | number |
| `events[].textCorruptionClassicShortFormCount` | 28.0% | number |
| `events[].textCorruptionCount` | 28.0% | number |
| `events[].textCorruptionGenerationInsertsCount` | 28.0% | number |
| `events[].textCorruptionLongRewriteCount` | 28.0% | number |
| `events[].textCorruptionRewrite101_200CharsCount` | 28.0% | number |
| `events[].textCorruptionRewrite31_100CharsCount` | 28.0% | number |
| `events[].textCorruptionRewriteBeyond200CharsCount` | 28.0% | number |
| `events[].textCorruptionRewriteUnder30CharsCount` | 28.0% | number |
| `events[].textCorruptionShortRewriteCount` | 28.0% | number |
| `events[].textCorruptionSnippetsCount` | 28.0% | number |
| `events[].textCorruptionVBarCount` | 28.0% | number |
| `events[].textHash` | 17.7% | null, string |
| `events[].textLength` | 17.7% | number |
| `events[].timeSpentInCheetah` | 28.0% | number |
| `events[].timeSpentInInline` | 28.0% | number |
| `events[].timeSpentInLongForm` | 28.0% | number |
| `events[].timeSpentInShortForm` | 28.0% | number |
| `events[].timestamp` | 0.6% | integer |
| `events[].totalCpuCores` | 0.4% | number |
| `events[].totalPhysicalMemory` | 0.4% | number |
| `events[].trigger` | 4.2% | string |
| `events[].triggerReason` | 43.4% | string |
| `events[].triggerTs` | 43.4% | number |
| `events[].typedCharsCount` | 28.0% | number |
| `events[].uiType` | 7.4% | string |
| `events[].url` | 1.1% | string |
| `events[].userAgent` | 1.3% | string |
| `events[].userId` | 100% | string |
| `events[].vBarId` | 17.7% | string |
| `events[].vBarTextLength` | 17.7% | number |
| `events[].vBarType` | 17.7% | string |
| `events[].webSessionId` | 0.6% | string |
| `events[].websiteSessionId` | 0.4% | string |
| `events[].windowsStoreInstallation` | 100% | boolean |

**Request schema variants**

**Schema 1** `2b30ebc7e1` — 106 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 2** `da3cb60dd8` — 76 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 3** `544ab86f27` — 38 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 4** `de242a34a1` — 29 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 5** `a2912b1fb5` — 25 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 6** `b50a6a611d` — 23 requests

```json
{
    "events": [
            {
                "action": string,
                "applySource": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 7** `24e37fcc0d` — 18 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 8** `19873b4fd3` — 18 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 9** `9e598bd0fc` — 17 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "endpoint": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "responseStatus": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "areSame": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isAnonymous": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "rti": string,
                "savedEmpty": boolean,
                "savingEmpty": boolean,
                "source": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 10** `4ac78cec35` — 17 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 11** `14fce36bb4` — 15 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "trigger": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 12** `acb9bb6372` — 13 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 13** `3a6f64749e` — 8 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 14** `01cc4f6ccc` — 7 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 15** `116eb2e3d2` — 7 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "emogenieVisible": boolean,
                "engagement": number,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "status": string,
                "styleGuide": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "brandToneShown": boolean,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "engagement": number,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "source": string,
                "styleGuide": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "brandToneShown": boolean,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "duration": number,
                "engagement": number,
                "eventName": string,
                "feature": string,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "source": string,
                "styleGuide": number,
                "success": boolean,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 16** `884ffd3785` — 7 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 17** `461770b56e` — 7 requests

```json
{
    "events": [
            {
                "action": string,
                "anchorHeightUsed": string,
                "anchorLocationUsed": string,
                "anchorSideUsed": string,
                "appPlatformType": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "onboardingInProgress": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 18** `125163f5ac` — 6 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 19** `dcf9aed7a1` — 6 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 20** `1384e6d927` — 5 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "endpoint": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "responseStatus": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "areSame": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isAnonymous": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "rti": string,
                "savedEmpty": boolean,
                "savingEmpty": boolean,
                "source": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 21** `037cae7698` — 4 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 22** `a95a494cf2` — 4 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 23** `b7ecc2eece` — 4 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 24** `7cdb8d5551` — 4 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "trigger": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 25** `ed8daf57ea` — 4 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 26** `e6468f0ef2` — 3 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 27** `ba1696d8a9` — 3 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "secondsSinceOpened": number,
                "source": string,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 28** `54da35d171` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 29** `fbb27d93f2` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 30** `1e20b633bf` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 31** `4ed57fa4ad` — 2 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 32** `22ad33eca7` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "trigger": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 33** `91d52965e5` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "emogenieVisible": boolean,
                "engagement": number,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "status": string,
                "styleGuide": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "brandToneShown": boolean,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "engagement": number,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "source": string,
                "styleGuide": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 34** `97bfe46a68` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "brandToneShown": boolean,
                "clarity": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "correctness": number,
                "delivery": number,
                "deviceSystemVersion": string,
                "duration": number,
                "engagement": number,
                "eventName": string,
                "feature": string,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "source": string,
                "styleGuide": number,
                "success": boolean,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 35** `724a3f398b` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "endpoint": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "responseStatus": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 36** `855aa05a78` — 2 requests

```json
{
    "events": [
            {
                "action": string,
                "areSame": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isAnonymous": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "rti": string,
                "savedEmpty": boolean,
                "savingEmpty": boolean,
                "source": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 37** `4e9b0b3744` — 2 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "clientName": string,
                "containerId": string,
                "domainName": string,
                "eventName": string,
                "instanceId": string,
                "isUnload": boolean,
                "pageHeartbeatSeconds": number,
                "pageSlug": string,
                "pageUrl": string,
                "pageViewId": string,
                "referrer": string,
                "timestamp": integer,
                "webSessionId": string
            }
        ]
}
```

**Schema 38** `d8b687491f` — 1 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "gaClientId": string,
                "instanceId": string,
                "isTest": boolean,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 39** `d881c6f059` — 1 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "isTouchDevice": boolean,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 40** `e1ed3495cf` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "bannerType": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "object": string,
                "objectId": string,
                "pageId": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 41** `92e9b32be4` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "endpoint": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "responseStatus": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "extendedUpdateInterval": boolean,
                "instanceId": string,
                "isCppRedistAvailable": boolean,
                "isFirstLaunch": boolean,
                "isTest": boolean,
                "launchAtStartupState": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "totalCpuCores": number,
                "totalPhysicalMemory": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 42** `6d6eefe165` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 43** `4dc5aed4b9` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 44** `28aedd2e02` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 45** `b7d337e75a` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 46** `1b2d63531a` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 47** `9bd3102aac` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "applySource": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": null,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 48** `a021c66751` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "applySource": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "duration": number,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 49** `e850d3b8a1` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 50** `7dbfde59d3` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 51** `8d6dbe9478` — 1 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 52** `ca28bcd555` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 53** `10552af7d7` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "browserType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 54** `9c729cfbb8` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textHash": string,
                "textLength": number,
                "userId": string,
                "vBarId": string,
                "vBarTextLength": number,
                "vBarType": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 55** `beae897c5b` — 1 requests

```json
{
    "events": [
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 56** `b7078f96fa` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 57** `4b6d0d3995` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "integrationUuid": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "secondsSinceOpened": number,
                "source": string,
                "superhumanMode": boolean,
                "uiType": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 58** `9dc42e6dad` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "trigger": string,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 59** `1d840bffd6` — 1 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "clientName": string,
                "containerId": string,
                "domainName": string,
                "eventName": string,
                "instanceId": string,
                "isUnload": boolean,
                "pageHeartbeatSeconds": integer,
                "pageSlug": string,
                "pageUrl": string,
                "pageViewId": string,
                "referrer": string,
                "timestamp": integer,
                "webSessionId": string
            }
        ]
}
```

**Schema 60** `366418f413` — 1 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string,
                "websiteSessionId": string
            }
        ]
}
```

**Schema 61** `e64ca43c18` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "currentLanguage": string,
                "devicePixelRatio": integer,
                "deviceType": string,
                "eventName": string,
                "instanceId": string,
                "isMobile": boolean,
                "isStaticFallback": boolean,
                "isTest": boolean,
                "isTouchDevice": boolean,
                "object": string,
                "os": string,
                "pageId": string,
                "pageSlug": string,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string,
                "websiteSessionId": string
            }
        ]
}
```

**Schema 62** `52c178bdf4` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 63** `e1c5d136b8` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 64** `7c81b74f18` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "assistantAvailable": boolean,
                "batchId": integer,
                "capiSessionType": string,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "detectionTs": number,
                "deviceSystemVersion": string,
                "emogenieShown": boolean,
                "eventName": string,
                "eventSchemaVersion": number,
                "firstMessageReceivedWithRevisionIdTs": number,
                "firstMessageSentWithRevisionIdTextLength": number,
                "firstMessageSentWithRevisionIdTs": number,
                "gButtonInitializedStatus": string,
                "gButtonInitializedTs": number,
                "gButtonShownStatus": string,
                "gButtonShownTs": number,
                "initialTextLength": number,
                "instanceId": string,
                "integrationUuid": string,
                "intentTs": number,
                "isTest": boolean,
                "lastStage": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "sessionUuid": string,
                "startSessionReceivedTs": number,
                "startSessionSentTs": number,
                "suggestionCount": number,
                "superhumanMode": boolean,
                "triggerReason": string,
                "triggerTs": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "emotion": string,
                "eventName": string,
                "instanceId": string,
                "isBrandTone": boolean,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "Accessible2LongKeyboardSimulationSelectionCount": number,
                "acc2SelectCount": number,
                "acc2SelectUIAutoAndKbSimFallbackCount": number,
                "acc2SelectUIAutoAndKbSimFallbackFailedCount": number,
                "acc2SelectUIAutoFallbackCount": number,
                "acc2SelectUIAutoFallbackFailedCount": number,
                "accessible2KeyboardSimulationSelectionCount": number,
                "action": string,
                "alertAcceptedLongRewriteCount": number,
                "alertAcceptedRewrite101_200CharsCount": number,
                "alertAcceptedRewrite31_100CharsCount": number,
                "alertAcceptedRewriteBeyond200CharsCount": number,
                "alertAcceptedRewriteUnder30CharsCount": number,
                "alertAcceptedShortRewriteCount": number,
                "alertsAcceptedClassicCount": number,
                "alertsAcceptedClassicInlineCount": number,
                "alertsAcceptedClassicLongFormCount": number,
                "alertsAcceptedClassicShortFormCount": number,
                "alertsAcceptedCount": number,
                "alertsAcceptedGenerationInsertsCount": number,
                "alertsAcceptedInline": number,
                "alertsAcceptedRevision": number,
                "alertsAcceptedSnippetsCount": number,
                "alertsAcceptedVBarCount": number,
                "alertsIgnoredInline": number,
                "alertsIgnoredRevision": number,
                "alertsShownInline": number,
                "appPlatformType": string,
                "applyStatusCorruptedCount": number,
                "applyStatusFailCount": number,
                "applyStatusUnknownCount": number,
                "batchId": integer,
                "brandToneShown": boolean,
                "capiAuthAttempts": number,
                "capiAuthFails": number,
                "capiAuthTime": number,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "emogenieShown": number,
                "eventName": string,
                "fieldHeight": number,
                "fieldWidth": number,
                "finalTextLength": number,
                "freePremiumSuggestionsAvailable": boolean,
                "instanceId": string,
                "integrationUuid": string,
                "isSduiFeed": boolean,
                "isTest": boolean,
                "lockedUISuggestionsAvailable": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "outOfSyncCount": number,
                "pagedModeEnabled": boolean,
                "perMachineInstallation": boolean,
                "pluginActivation": string,
                "primaryUIType": string,
                "programmableStart": boolean,
                "sessionDuration": number,
                "sessionUuid": string,
                "superhumanMode": boolean,
                "textCorruptionClassicCount": number,
                "textCorruptionClassicInlineCount": number,
                "textCorruptionClassicLongFormCount": number,
                "textCorruptionClassicShortFormCount": number,
                "textCorruptionCount": number,
                "textCorruptionGenerationInsertsCount": number,
                "textCorruptionLongRewriteCount": number,
                "textCorruptionRewrite101_200CharsCount": number,
                "textCorruptionRewrite31_100CharsCount": number,
                "textCorruptionRewriteBeyond200CharsCount": number,
                "textCorruptionRewriteUnder30CharsCount": number,
                "textCorruptionShortRewriteCount": number,
                "textCorruptionSnippetsCount": number,
                "textCorruptionVBarCount": number,
                "timeSpentInCheetah": number,
                "timeSpentInInline": number,
                "timeSpentInLongForm": number,
                "timeSpentInShortForm": number,
                "typedCharsCount": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 65** `56c0dd671b` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "articleTitle": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "object": string,
                "objectId": string,
                "pageId": string,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 66** `b2199fe902` — 1 requests

```json
{
    "events": [
            {
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerHeight": integer,
                "containerId": string,
                "containerWidth": integer,
                "devicePixelRatio": integer,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "referrer": string,
                "screenHeight": integer,
                "screenWidth": integer,
                "url": string,
                "userAgent": string,
                "userId": string
            }
        ]
}
```

**Schema 67** `e94c56cabe` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "endpoint": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "responseStatus": string,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "instanceId": string,
                "isTest": boolean,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

**Schema 68** `da2ad51523` — 1 requests

```json
{
    "events": [
            {
                "action": string,
                "batchId": integer,
                "client": string,
                "clientVersion": string,
                "containerId": string,
                "cpuArchitecture": string,
                "deviceSystemVersion": string,
                "eventName": string,
                "extendedUpdateInterval": boolean,
                "instanceId": string,
                "isCppRedistAvailable": boolean,
                "isFirstLaunch": boolean,
                "isTest": boolean,
                "launchAtStartupState": string,
                "microsoftCampaign": boolean,
                "object": string,
                "objectId": string,
                "perMachineInstallation": boolean,
                "programmableStart": boolean,
                "superhumanMode": boolean,
                "totalCpuCores": number,
                "totalPhysicalMemory": number,
                "userId": string,
                "windowsStoreInstallation": boolean
            }
        ]
}
```

#### Response

**No response body was observed.**

---

### `in.grammarly.com/v1/events`

**Observed methods:** `POST`
**Observed requests:** 403
**Response statuses:** 200: 403

#### Request

Content types: `application/json` (403)

JSON requests: **403**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `action` | 0.5% | string |
| `action_id` | 0.5% | null |
| `alert_text_corruption_count` | 36.5% | null |
| `alerts` | 36.5% | object |
| `alerts.accepted_autocomplete_count` | 36.5% | null |
| `alerts.accepted_autocorrect_count` | 36.5% | null |
| `alerts.accepted_classic_count` | 36.5% | integer |
| `alerts.accepted_classic_inline_count` | 36.5% | integer |
| `alerts.accepted_classic_long_form_count` | 36.5% | integer |
| `alerts.accepted_classic_short_form_count` | 36.5% | integer |
| `alerts.accepted_count` | 36.5% | integer |
| `alerts.accepted_generation_inserts_count` | 36.5% | integer |
| `alerts.accepted_inline` | 36.5% | integer |
| `alerts.accepted_proofit_count` | 36.5% | null |
| `alerts.accepted_revision` | 36.5% | integer |
| `alerts.accepted_snippets_count` | 36.5% | integer |
| `alerts.accepted_synonyms_count` | 36.5% | null |
| `alerts.accepted_touch_typist_count` | 36.5% | null |
| `alerts.accepted_touch_typist_individual_count` | 36.5% | null |
| `alerts.accepted_touch_typist_revert_count` | 36.5% | null |
| `alerts.accepted_vbar_count` | 36.5% | integer |
| `alerts.ignored_inline` | 36.5% | integer |
| `alerts.ignored_revision` | 36.5% | integer |
| `alerts.long_rewrite_count` | 36.5% | integer |
| `alerts.nonce` | 36.5% | integer |
| `alerts.rewrite_101_200_chars` | 36.5% | integer |
| `alerts.rewrite_31_100_chars` | 36.5% | integer |
| `alerts.rewrite_beyond_200_chars` | 36.5% | integer |
| `alerts.rewrite_under_30_chars` | 36.5% | integer |
| `alerts.short_rewrite_count` | 36.5% | integer |
| `alerts.shown_inline` | 36.5% | integer |
| `app` | 99.5% | null, string |
| `app_platform_type` | 36.5% | string |
| `app_version` | 36.5% | string |
| `apply_status` | 36.5% | object |
| `apply_status.corrupted_count` | 36.5% | integer |
| `apply_status.fail_count` | 36.5% | integer |
| `apply_status.nonce` | 36.5% | integer |
| `apply_status.unknown_count` | 36.5% | integer |
| `assistant_available` | 56.6% | boolean, null |
| `assistant_fail_replacement_count` | 36.5% | null |
| `assistant_replacement_count` | 36.5% | null |
| `authorship` | 0.5% | object |
| `authorship.doc_id` | 0.5% | string |
| `authorship.is_resume` | 0.5% | null |
| `authorship.surface` | 0.5% | null |
| `authorship.untracked_text_len` | 0.5% | null |
| `autocomplete_fail_replacement_count` | 36.5% | null |
| `autocomplete_replacement_count` | 36.5% | null |
| `autocorrect_fail_replacement_count` | 36.5% | null |
| `autocorrect_popups_shown` | 36.5% | null |
| `autocorrect_replacement_count` | 36.5% | null |
| `autocorrect_reverted` | 36.5% | null |
| `autocorrect_triggered` | 36.5% | null |
| `brand_tone_shown` | 36.5% | integer |
| `capi_session_type` | 56.6% | null, string |
| `cheetah_fail_replacement_count` | 36.5% | null |
| `cheetah_replacement_count` | 36.5% | null |
| `client` | 100% | object, string |
| `client.category` | 0.5% | null |
| `client.host_app` | 0.5% | null |
| `client.host_app_bit` | 0.5% | null |
| `client.install_source` | 0.5% | null |
| `client.is_per_machine_install` | 0.5% | null |
| `client.name` | 0.5% | string |
| `client.sub_type` | 0.5% | null |
| `client.type` | 0.5% | null |
| `client.version` | 0.5% | string |
| `client_event_epoch` | 99.5% | integer |
| `client_session_id` | 36.5% | null |
| `client_version` | 99.5% | string |
| `container_id` | 99.5% | string |
| `content_text_corruption_count` | 36.5% | null |
| `detection_ts` | 56.6% | integer |
| `device` | 99.5% | object |
| `device.browser_name` | 99.5% | null |
| `device.browser_version` | 99.5% | null |
| `device.nonce` | 99.5% | integer |
| `device.platform` | 99.5% | string |
| `device.system_name` | 99.5% | string |
| `device.system_version` | 99.5% | string |
| `device.user_agent` | 99.5% | null |
| `emogenie_shown` | 93.1% | boolean, integer, null |
| `event_name` | 100% | string |
| `extra` | 99.5% | object |
| `extra.acc2SelectCount` | 36.5% | string |
| `extra.acc2SelectUIAutoAndKbSimFallbackCount` | 36.5% | string |
| `extra.acc2SelectUIAutoAndKbSimFallbackFailedCount` | 36.5% | string |
| `extra.acc2SelectUIAutoFallbackCount` | 36.5% | string |
| `extra.acc2SelectUIAutoFallbackFailedCount` | 36.5% | string |
| `extra.accessible2KeyboardSimulationSelectionCount` | 36.5% | string |
| `extra.accessible2LongKeyboardSimulationSelectionCount` | 36.5% | string |
| `extra.affected_text_length` | 6.2% | string |
| `extra.alert_category` | 6.2% | string |
| `extra.alert_group` | 6.2% | string |
| `extra.alert_pname` | 6.2% | string |
| `extra.fieldHeight` | 36.5% | string |
| `extra.fieldWidth` | 36.5% | string |
| `extra.integration_kind` | 6.2% | string |
| `extra.isSduiFeed` | 36.5% | string |
| `extra.lockedUISuggestionsAvailable` | 36.5% | string |
| `extra.pagedModeEnabled` | 36.5% | string |
| `extra.per_machine_installation` | 99.5% | string |
| `extra.pluginActivation` | 36.5% | string |
| `extra.replacement_length` | 6.2% | string |
| `extra.running_target_framework` | 99.5% | string |
| `extra.source` | 6.2% | string |
| `extra.status` | 6.2% | string |
| `extra.windows_store_installation` | 99.5% | string |
| `fail_replacement_count` | 36.5% | null |
| `final_text_length` | 36.5% | integer |
| `first_message_received_with_revision_id_ts` | 56.6% | integer |
| `first_message_sent_with_revision_id_text_length` | 56.6% | integer |
| `first_message_sent_with_revision_id_ts` | 56.6% | integer |
| `free_premium_suggestions_available` | 36.5% | boolean |
| `g_button_initialized_status` | 56.6% | null, string |
| `g_button_initialized_ts` | 56.6% | integer, null |
| `g_button_shown_status` | 56.6% | null, string |
| `g_button_shown_ts` | 56.6% | integer, null |
| `hostname` | 99.5% | null, string |
| `initial_text_length` | 56.6% | integer, null |
| `inline_card_fail_replacement_count` | 36.5% | null |
| `inline_card_replacement_count` | 36.5% | null |
| `institution_id` | 99.5% | null |
| `integration_id` | 99.5% | string |
| `intent_ts` | 56.6% | integer |
| `is_decoration_shown_applicable` | 56.6% | null |
| `last_stage` | 56.6% | string |
| `latency` | 6.5% | integer |
| `memory_average_commit_size_mb` | 6.5% | null, number |
| `memory_average_managed_memory_mb` | 6.5% | null, number |
| `memory_average_working_set_mb` | 6.5% | null, number |
| `metadata` | 0.5% | object |
| `metadata.database_size_bytes` | 0.5% | string |
| `metadata.entry_count` | 0.5% | string |
| `metadata.per_machine_installation` | 0.5% | string |
| `metadata.running_target_framework` | 0.5% | string |
| `metadata.windows_store_installation` | 0.5% | string |
| `nonce` | 100% | integer |
| `object` | 0.5% | string |
| `object_id` | 0.5% | string |
| `out_of_sync_count` | 36.5% | integer |
| `plugin_activation` | 56.6% | string |
| `plugin_instance_id` | 56.6% | null |
| `primary_ui_type` | 36.5% | string |
| `proofit_fail_replacement_count` | 36.5% | null |
| `proofit_replacement_count` | 36.5% | null |
| `referral_container_id` | 99.5% | null |
| `replacement_corrupted_count` | 36.5% | null |
| `replacement_count` | 36.5% | null |
| `replacement_execution_fail_count` | 36.5% | null |
| `replacement_validation_fail_count` | 36.5% | null |
| `session_category` | 36.5% | null |
| `session_duration` | 36.5% | integer |
| `session_id` | 99.5% | null, string |
| `sidebar_fail_replacement_count` | 36.5% | null |
| `sidebar_replacement_count` | 36.5% | null |
| `snippet_text_corruption_count` | 36.5% | null |
| `snippets_fail_replacement_count` | 36.5% | null |
| `snippets_replacement_count` | 36.5% | null |
| `start_session_received_ts` | 56.6% | integer |
| `start_session_sent_ts` | 56.6% | integer |
| `suggestion_count` | 56.6% | integer, null |
| `superhuman_mode` | 99.5% | string |
| `synonyms_fail_replacement_count` | 36.5% | null |
| `synonyms_replacement_count` | 36.5% | null |
| `text_corruption` | 36.5% | object |
| `text_corruption.autocomplete_count` | 36.5% | null |
| `text_corruption.autocorrect_count` | 36.5% | null |
| `text_corruption.classic_count` | 36.5% | integer |
| `text_corruption.classic_inline_count` | 36.5% | integer |
| `text_corruption.classic_long_form_count` | 36.5% | integer |
| `text_corruption.classic_short_form_count` | 36.5% | integer |
| `text_corruption.count` | 36.5% | integer |
| `text_corruption.generation_inserts_count` | 36.5% | integer |
| `text_corruption.long_rewrite_count` | 36.5% | integer |
| `text_corruption.nonce` | 36.5% | integer |
| `text_corruption.proofit_count` | 36.5% | null |
| `text_corruption.rewrite_101_200_chars` | 36.5% | integer |
| `text_corruption.rewrite_31_100_chars` | 36.5% | integer |
| `text_corruption.rewrite_beyond_200_chars` | 36.5% | integer |
| `text_corruption.rewrite_under_30_chars` | 36.5% | integer |
| `text_corruption.short_rewrite_count` | 36.5% | integer |
| `text_corruption.snippets_count` | 36.5% | integer |
| `text_corruption.synonyms_count` | 36.5% | null |
| `text_corruption.touch_typist_count` | 36.5% | null |
| `text_corruption.touch_typist_individual_count` | 36.5% | null |
| `text_corruption.touch_typist_revert_count` | 36.5% | null |
| `text_corruption.vbar_count` | 36.5% | integer |
| `text_length` | 6.5% | integer |
| `time_spent_in` | 36.5% | object |
| `time_spent_in.cheetah` | 36.5% | integer |
| `time_spent_in.cheetah_web_view` | 36.5% | null |
| `time_spent_in.inline` | 36.5% | integer |
| `time_spent_in.long_form` | 36.5% | integer |
| `time_spent_in.nonce` | 36.5% | integer |
| `time_spent_in.oggy` | 36.5% | null |
| `time_spent_in.print_document_view` | 36.5% | null |
| `time_spent_in.short_form` | 36.5% | integer |
| `time_spent_in.web_document_view` | 36.5% | null |
| `trigger_reason` | 56.6% | string |
| `trigger_ts` | 56.6% | integer |
| `typed_chars_count` | 36.5% | integer |
| `user` | 0.5% | object |
| `user.container_id` | 0.5% | string |
| `user.id` | 0.5% | string |
| `user.institution_id` | 0.5% | null |
| `user.pid` | 0.5% | null |
| `user.referral_container_id` | 0.5% | null |
| `user.type` | 0.5% | null |
| `user_id` | 100% | string |
| `vbar_available` | 36.5% | null |
| `vbar_card_apply_count` | 36.5% | null |
| `vbar_card_show_count` | 36.5% | null |
| `windows_version` | 0.5% | string |
| `workspace_id` | 36.5% | null |

**Request schema variants**

**Schema 1** `60a3acc723` — 147 requests

```json
{
    "alert_text_corruption_count": null,
    "alerts": {
            "accepted_autocomplete_count": null,
            "accepted_autocorrect_count": null,
            "accepted_classic_count": integer,
            "accepted_classic_inline_count": integer,
            "accepted_classic_long_form_count": integer,
            "accepted_classic_short_form_count": integer,
            "accepted_count": integer,
            "accepted_generation_inserts_count": integer,
            "accepted_inline": integer,
            "accepted_proofit_count": null,
            "accepted_revision": integer,
            "accepted_snippets_count": integer,
            "accepted_synonyms_count": null,
            "accepted_touch_typist_count": null,
            "accepted_touch_typist_individual_count": null,
            "accepted_touch_typist_revert_count": null,
            "accepted_vbar_count": integer,
            "ignored_inline": integer,
            "ignored_revision": integer,
            "long_rewrite_count": integer,
            "nonce": integer,
            "rewrite_101_200_chars": integer,
            "rewrite_31_100_chars": integer,
            "rewrite_beyond_200_chars": integer,
            "rewrite_under_30_chars": integer,
            "short_rewrite_count": integer,
            "shown_inline": integer
        },
    "app": string,
    "app_platform_type": string,
    "app_version": string,
    "apply_status": {
            "corrupted_count": integer,
            "fail_count": integer,
            "nonce": integer,
            "unknown_count": integer
        },
    "assistant_fail_replacement_count": null,
    "assistant_replacement_count": null,
    "autocomplete_fail_replacement_count": null,
    "autocomplete_replacement_count": null,
    "autocorrect_fail_replacement_count": null,
    "autocorrect_popups_shown": null,
    "autocorrect_replacement_count": null,
    "autocorrect_reverted": null,
    "autocorrect_triggered": null,
    "brand_tone_shown": integer,
    "cheetah_fail_replacement_count": null,
    "cheetah_replacement_count": null,
    "client": string,
    "client_event_epoch": integer,
    "client_session_id": null,
    "client_version": string,
    "container_id": string,
    "content_text_corruption_count": null,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": integer,
    "event_name": string,
    "extra": {
            "acc2SelectCount": string,
            "acc2SelectUIAutoAndKbSimFallbackCount": string,
            "acc2SelectUIAutoAndKbSimFallbackFailedCount": string,
            "acc2SelectUIAutoFallbackCount": string,
            "acc2SelectUIAutoFallbackFailedCount": string,
            "accessible2KeyboardSimulationSelectionCount": string,
            "accessible2LongKeyboardSimulationSelectionCount": string,
            "fieldHeight": string,
            "fieldWidth": string,
            "isSduiFeed": string,
            "lockedUISuggestionsAvailable": string,
            "pagedModeEnabled": string,
            "per_machine_installation": string,
            "pluginActivation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "fail_replacement_count": null,
    "final_text_length": integer,
    "free_premium_suggestions_available": boolean,
    "hostname": string,
    "inline_card_fail_replacement_count": null,
    "inline_card_replacement_count": null,
    "institution_id": null,
    "integration_id": string,
    "nonce": integer,
    "out_of_sync_count": integer,
    "primary_ui_type": string,
    "proofit_fail_replacement_count": null,
    "proofit_replacement_count": null,
    "referral_container_id": null,
    "replacement_corrupted_count": null,
    "replacement_count": null,
    "replacement_execution_fail_count": null,
    "replacement_validation_fail_count": null,
    "session_category": null,
    "session_duration": integer,
    "session_id": string,
    "sidebar_fail_replacement_count": null,
    "sidebar_replacement_count": null,
    "snippet_text_corruption_count": null,
    "snippets_fail_replacement_count": null,
    "snippets_replacement_count": null,
    "superhuman_mode": string,
    "synonyms_fail_replacement_count": null,
    "synonyms_replacement_count": null,
    "text_corruption": {
            "autocomplete_count": null,
            "autocorrect_count": null,
            "classic_count": integer,
            "classic_inline_count": integer,
            "classic_long_form_count": integer,
            "classic_short_form_count": integer,
            "count": integer,
            "generation_inserts_count": integer,
            "long_rewrite_count": integer,
            "nonce": integer,
            "proofit_count": null,
            "rewrite_101_200_chars": integer,
            "rewrite_31_100_chars": integer,
            "rewrite_beyond_200_chars": integer,
            "rewrite_under_30_chars": integer,
            "short_rewrite_count": integer,
            "snippets_count": integer,
            "synonyms_count": null,
            "touch_typist_count": null,
            "touch_typist_individual_count": null,
            "touch_typist_revert_count": null,
            "vbar_count": integer
        },
    "time_spent_in": {
            "cheetah": integer,
            "cheetah_web_view": null,
            "inline": integer,
            "long_form": integer,
            "nonce": integer,
            "oggy": null,
            "print_document_view": null,
            "short_form": integer,
            "web_document_view": null
        },
    "typed_chars_count": integer,
    "user_id": string,
    "vbar_available": null,
    "vbar_card_apply_count": null,
    "vbar_card_show_count": null,
    "workspace_id": null
}
```

**Schema 2** `6296f341fd` — 89 requests

```json
{
    "app": string,
    "assistant_available": boolean,
    "capi_session_type": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": boolean,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": string,
    "g_button_initialized_ts": integer,
    "g_button_shown_status": string,
    "g_button_shown_ts": integer,
    "hostname": string,
    "initial_text_length": integer,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": string,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": integer,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 3** `217d389263` — 70 requests

```json
{
    "app": string,
    "assistant_available": boolean,
    "capi_session_type": null,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": null,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": null,
    "g_button_initialized_ts": null,
    "g_button_shown_status": string,
    "g_button_shown_ts": integer,
    "hostname": string,
    "initial_text_length": null,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": null,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 4** `3e412a781a` — 36 requests

```json
{
    "app": string,
    "assistant_available": boolean,
    "capi_session_type": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": boolean,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": string,
    "g_button_initialized_ts": integer,
    "g_button_shown_status": string,
    "g_button_shown_ts": integer,
    "hostname": string,
    "initial_text_length": integer,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": integer,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 5** `33e3b6d359` — 25 requests

```json
{
    "app": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "event_name": string,
    "extra": {
            "affected_text_length": string,
            "alert_category": string,
            "alert_group": string,
            "alert_pname": string,
            "integration_kind": string,
            "per_machine_installation": string,
            "replacement_length": string,
            "running_target_framework": string,
            "source": string,
            "status": string,
            "windows_store_installation": string
        },
    "hostname": string,
    "institution_id": null,
    "integration_id": string,
    "latency": integer,
    "memory_average_commit_size_mb": null,
    "memory_average_managed_memory_mb": null,
    "memory_average_working_set_mb": null,
    "nonce": integer,
    "referral_container_id": null,
    "session_id": string,
    "superhuman_mode": string,
    "text_length": integer,
    "user_id": string
}
```

**Schema 6** `0f333e64ce` — 22 requests

```json
{
    "app": string,
    "assistant_available": boolean,
    "capi_session_type": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": null,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": null,
    "g_button_initialized_ts": null,
    "g_button_shown_status": string,
    "g_button_shown_ts": integer,
    "hostname": string,
    "initial_text_length": null,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": null,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 7** `8bf6b599ea` — 9 requests

```json
{
    "app": string,
    "assistant_available": null,
    "capi_session_type": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": null,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": null,
    "g_button_initialized_ts": null,
    "g_button_shown_status": null,
    "g_button_shown_ts": null,
    "hostname": string,
    "initial_text_length": null,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": null,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 8** `b70be6b4ba` — 2 requests

```json
{
    "action": string,
    "action_id": null,
    "authorship": {
            "doc_id": string,
            "is_resume": null,
            "surface": null,
            "untracked_text_len": null
        },
    "client": {
            "category": null,
            "host_app": null,
            "host_app_bit": null,
            "install_source": null,
            "is_per_machine_install": null,
            "name": string,
            "sub_type": null,
            "type": null,
            "version": string
        },
    "event_name": string,
    "metadata": {
            "database_size_bytes": string,
            "entry_count": string,
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "nonce": integer,
    "object": string,
    "object_id": string,
    "user": {
            "container_id": string,
            "id": string,
            "institution_id": null,
            "pid": null,
            "referral_container_id": null,
            "type": null
        },
    "user_id": string,
    "windows_version": string
}
```

**Schema 9** `6905dadbd1` — 2 requests

```json
{
    "app": null,
    "assistant_available": null,
    "capi_session_type": null,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "detection_ts": integer,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "emogenie_shown": null,
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "first_message_received_with_revision_id_ts": integer,
    "first_message_sent_with_revision_id_text_length": integer,
    "first_message_sent_with_revision_id_ts": integer,
    "g_button_initialized_status": null,
    "g_button_initialized_ts": null,
    "g_button_shown_status": null,
    "g_button_shown_ts": null,
    "hostname": null,
    "initial_text_length": null,
    "institution_id": null,
    "integration_id": string,
    "intent_ts": integer,
    "is_decoration_shown_applicable": null,
    "last_stage": string,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "start_session_received_ts": integer,
    "start_session_sent_ts": integer,
    "suggestion_count": null,
    "superhuman_mode": string,
    "trigger_reason": string,
    "trigger_ts": integer,
    "user_id": string
}
```

**Schema 10** `d83b33bff5` — 1 requests

```json
{
    "app": string,
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "hostname": string,
    "institution_id": null,
    "integration_id": string,
    "latency": integer,
    "memory_average_commit_size_mb": number,
    "memory_average_managed_memory_mb": number,
    "memory_average_working_set_mb": number,
    "nonce": integer,
    "referral_container_id": null,
    "session_id": string,
    "superhuman_mode": string,
    "text_length": integer,
    "user_id": string
}
```

#### Response

Content types: `text/plain` (403)

**No JSON response body was observed.**

---

### `gateway.grammarly.com/experimentation/gates/get`

**Observed methods:** `POST, OPTIONS`
**Observed requests:** 131
**Response statuses:** 200: 113

#### Request

Content types: `application/json` (113)

JSON requests: **113**

**Request field frequency**


**Request schema variants**

**Schema 1** `76efce69de` — 113 requests

```json
[
    string
]
```

#### Response

Content types: `application/json` (95), `text/plain` (18)

JSON responses: **95**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].containerId` | 100% | string |
| `[].experimentId` | 100% | string |
| `[].experimentName` | 100% | string |
| `[].groupName` | 100% | string |
| `[].isTest` | 100% | boolean |
| `[].needLog` | 100% | boolean |
| `[].overrideType` | 100% | null |
| `[].qualifiedName` | 100% | null, string |
| `[].sender` | 100% | null |
| `[].source` | 100% | string |
| `[].type` | 100% | string |
| `[].userId` | 100% | integer |

**Response schema variants**

**Schema 1** `94b9dfff31` — 95 responses

```json
[
    {
        "containerId": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": null,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
    {
        "containerId": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": string,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
]
```

---

### `f-log-inkwell.grammarly.io/batch/log`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 110
**Response statuses:** 200: 47, 204: 48

#### Request

Content types: `application/json` (48)

JSON requests: **48**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].application` | 100% | string |
| `[].attrs` | 100% | object |
| `[].attrs.error` | 47.9% | object, string |
| `[].attrs.input` | 100% | string |
| `[].attrs.traceId` | 100% | string |
| `[].client` | 100% | string |
| `[].context` | 100% | null, string |
| `[].env` | 100% | string |
| `[].exception` | 100% | object |
| `[].exception.cause` | 14.6% | object |
| `[].exception.cause.message` | 14.6% | string |
| `[].exception.cause.name` | 14.6% | string |
| `[].exception.cause.stack` | 14.6% | string |
| `[].exception.errors` | 8.3% | array |
| `[].exception.errors[].deltas` | 8.3% | array |
| `[].exception.errors[].deltas[].ops` | 12.5% | array |
| `[].exception.errors[].deltas[].ops[].attributes` | 25.0% | object |
| `[].exception.errors[].deltas[].ops[].attributes.KnowledgeHubTerm` | 25.0% | boolean |
| `[].exception.errors[].deltas[].ops[].attributes.Type` | 25.0% | integer |
| `[].exception.errors[].deltas[].ops[].delete` | 8.3% | integer |
| `[].exception.errors[].deltas[].ops[].insert` | 8.3% | string |
| `[].exception.errors[].deltas[].ops[].retain` | 8.3% | integer |
| `[].exception.errors[].fromRevision` | 8.3% | integer |
| `[].exception.errors[].message` | 8.3% | string |
| `[].exception.errors[].name` | 8.3% | string |
| `[].exception.errors[].range` | 8.3% | object |
| `[].exception.errors[].range.end` | 8.3% | integer |
| `[].exception.errors[].range.start` | 8.3% | integer |
| `[].exception.errors[].rebasedRange` | 8.3% | object |
| `[].exception.errors[].rebasedRange.end` | 8.3% | integer |
| `[].exception.errors[].rebasedRange.start` | 8.3% | integer |
| `[].exception.errors[].stack` | 8.3% | string |
| `[].exception.errors[].toRevision` | 8.3% | integer |
| `[].exception.message` | 100% | string |
| `[].exception.name` | 100% | string |
| `[].exception.stack` | 100% | string |
| `[].extra` | 100% | array |
| `[].level` | 100% | string |
| `[].logger` | 100% | string |
| `[].message` | 100% | string |
| `[].platformType` | 100% | string |
| `[].platformVersion` | 100% | string |
| `[].session` | 100% | string |
| `[].timestamp` | 100% | integer |
| `[].version` | 100% | string |

**Request schema variants**

**Schema 1** `05907afe7b` — 17 requests

```json
[
    {
        "application": string,
        "attrs": {
                    "input": string,
                    "traceId": string
                },
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 2** `fee07c5a9f` — 9 requests

```json
[
    {
        "application": string,
        "attrs": {
                    "input": string,
                    "traceId": string
                },
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "client": string,
        "context": null,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "attrs": {
                    "error": {
                                }
                },
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 3** `3de7b9b1c1` — 8 requests

```json
[
    {
        "application": string,
        "attrs": {
                    "error": string
                },
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 4** `829e7779fb` — 2 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "attrs": {
                    "error": string
                },
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 5** `8610c67ee4` — 2 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": string,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 6** `8c34a45423` — 2 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": string,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 7** `2d67411138` — 2 requests

```json
[
    {
        "application": string,
        "attrs": {
                    "error": string
                },
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "attrs": {
                    "input": string,
                    "traceId": string
                },
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 8** `017e506cac` — 2 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "cause": {
                                    "message": string,
                                    "name": string,
                                    "stack": string
                                },
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 9** `cbfc0c8807` — 2 requests

```json
[
    {
        "application": string,
        "attrs": {
                    "input": string,
                    "traceId": string
                },
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "attrs": {
                    "error": {
                                }
                },
        "client": string,
        "context": null,
        "env": string,
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
    {
        "application": string,
        "client": string,
        "context": null,
        "env": string,
        "exception": {
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 10** `ca2c92ffe5` — 1 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "errors": [
                                    {
                                        "deltas": [
                                                                {
                                                                    "ops": [
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "retain": integer
                                                                                                    }
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "delete": integer
                                                                                                    }
                                                                                                ]
                                                                }
                                                            ],
                                        "fromRevision": integer,
                                        "message": string,
                                        "name": string,
                                        "range": {
                                                                "end": integer,
                                                                "start": integer
                                                            },
                                        "rebasedRange": {
                                                                "end": integer,
                                                                "start": integer
                                                            },
                                        "stack": string,
                                        "toRevision": integer
                                    }
                                ],
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

**Schema 11** `46e37f3804` — 1 requests

```json
[
    {
        "application": string,
        "client": string,
        "context": string,
        "env": string,
        "exception": {
                    "errors": [
                                    {
                                        "deltas": [
                                                                {
                                                                    "ops": [
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "retain": integer
                                                                                                    }
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "insert": string
                                                                                                    }
                                                                                                ]
                                                                }
                                                                {
                                                                    "ops": [
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "delete": integer
                                                                                                    }
                                                                                                    {
                                                                                                        "attributes": {
                                                                                                                                                "KnowledgeHubTerm": boolean,
                                                                                                                                                "Type": integer
                                                                                                                                            },
                                                                                                        "insert": string
                                                                                                    }
                                                                                                ]
                                                                }
                                                            ],
                                        "fromRevision": integer,
                                        "message": string,
                                        "name": string,
                                        "range": {
                                                                "end": integer,
                                                                "start": integer
                                                            },
                                        "rebasedRange": {
                                                                "end": integer,
                                                                "start": integer
                                                            },
                                        "stack": string,
                                        "toRevision": integer
                                    }
                                ],
                    "message": string,
                    "name": string,
                    "stack": string
                },
        "extra": [],
        "level": string,
        "logger": string,
        "message": string,
        "platformType": string,
        "platformVersion": string,
        "session": string,
        "timestamp": integer,
        "version": string
    }
]
```

#### Response

**No response body was observed.**

---

### `capi.grammarly.com/fpws`

**Observed methods:** `GET`
**Observed requests:** 109
**Response statuses:** 101: 107

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `in.grammarly.com/v1/events/ingestion_front_end`

**Observed methods:** `POST`
**Observed requests:** 80
**Response statuses:** 200: 80

#### Request

Content types: `application/json` (80)

JSON requests: **80**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `alert_id` | 97.5% | string |
| `application` | 97.5% | string |
| `capi_session_type` | 97.5% | string |
| `client` | 100% | string |
| `client_event_dt` | 97.5% | integer |
| `client_event_epoch` | 100% | integer |
| `client_event_ts` | 97.5% | integer |
| `client_version` | 100% | string |
| `container_id` | 100% | string |
| `device` | 100% | object |
| `device.browser_name` | 100% | null |
| `device.browser_version` | 100% | null |
| `device.nonce` | 100% | integer |
| `device.platform` | 100% | string |
| `device.system_name` | 100% | string |
| `device.system_version` | 100% | string |
| `device.user_agent` | 100% | null |
| `duration_ms` | 2.5% | integer |
| `event_name` | 100% | string |
| `extra` | 100% | object |
| `extra.failed_count` | 2.5% | string |
| `extra.failed_tests` | 2.5% | string |
| `extra.per_machine_installation` | 100% | string |
| `extra.running_target_framework` | 100% | string |
| `extra.windows_store_installation` | 100% | string |
| `hostname` | 97.5% | string |
| `institution_id` | 100% | null |
| `integration_id` | 97.5% | string |
| `is_first_decoration` | 97.5% | boolean |
| `nonce` | 100% | integer |
| `outcome` | 2.5% | string |
| `placement_context` | 2.5% | string |
| `plugin_activation` | 97.5% | string |
| `plugin_instance_id` | 97.5% | null |
| `referral_container_id` | 100% | null |
| `session_id` | 97.5% | null, string |
| `session_uuid` | 2.5% | null |
| `shown_ts` | 97.5% | integer |
| `subtype` | 97.5% | string |
| `superhuman_mode` | 100% | string |
| `text_length` | 97.5% | integer |
| `user_id` | 100% | string |

**Request schema variants**

**Schema 1** `0cb227abc0` — 43 requests

```json
{
    "alert_id": string,
    "application": string,
    "capi_session_type": string,
    "client": string,
    "client_event_dt": integer,
    "client_event_epoch": integer,
    "client_event_ts": integer,
    "client_version": string,
    "container_id": string,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "hostname": string,
    "institution_id": null,
    "integration_id": string,
    "is_first_decoration": boolean,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": null,
    "shown_ts": integer,
    "subtype": string,
    "superhuman_mode": string,
    "text_length": integer,
    "user_id": string
}
```

**Schema 2** `ecbae03459` — 35 requests

```json
{
    "alert_id": string,
    "application": string,
    "capi_session_type": string,
    "client": string,
    "client_event_dt": integer,
    "client_event_epoch": integer,
    "client_event_ts": integer,
    "client_version": string,
    "container_id": string,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "event_name": string,
    "extra": {
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "hostname": string,
    "institution_id": null,
    "integration_id": string,
    "is_first_decoration": boolean,
    "nonce": integer,
    "plugin_activation": string,
    "plugin_instance_id": null,
    "referral_container_id": null,
    "session_id": string,
    "shown_ts": integer,
    "subtype": string,
    "superhuman_mode": string,
    "text_length": integer,
    "user_id": string
}
```

**Schema 3** `aff4ea58ca` — 2 requests

```json
{
    "client": string,
    "client_event_epoch": integer,
    "client_version": string,
    "container_id": string,
    "device": {
            "browser_name": null,
            "browser_version": null,
            "nonce": integer,
            "platform": string,
            "system_name": string,
            "system_version": string,
            "user_agent": null
        },
    "duration_ms": integer,
    "event_name": string,
    "extra": {
            "failed_count": string,
            "failed_tests": string,
            "per_machine_installation": string,
            "running_target_framework": string,
            "windows_store_installation": string
        },
    "institution_id": null,
    "nonce": integer,
    "outcome": string,
    "placement_context": string,
    "referral_container_id": null,
    "session_uuid": null,
    "superhuman_mode": string,
    "user_id": string
}
```

#### Response

Content types: `text/plain` (80)

**No JSON response body was observed.**

---

### `auth.grammarly.com/auth/v5/api/userinfo`

**Observed methods:** `GET, OPTIONS`
**Observed requests:** 50
**Response statuses:** 200: 40

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (18), `text/plain` (22)

JSON responses: **4**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `anonymous` | 100% | boolean |
| `confirmed` | 100% | boolean |
| `customFields` | 100% | object |
| `customFields.data-regulation` | 100% | string |
| `customFields.frontend_primaryLanguage` | 100% | string |
| `customFields.frontend_role` | 100% | string |
| `customFields.frontend_soundFluent` | 100% | string |
| `disabled` | 100% | boolean |
| `editorFeatures` | 100% | object |
| `editorFeatures.docsDisabled` | 100% | boolean |
| `editorFeatures.fullCards` | 100% | boolean |
| `editorFeatures.msOutlookEnabled` | 100% | boolean |
| `editorFeatures.msWordEnabled` | 100% | boolean |
| `editorFeatures.plagiarismDisabled` | 100% | boolean |
| `editorFeatures.proofit` | 100% | boolean |
| `editorFeatures.quickReplacement` | 100% | boolean |
| `editorFeatures.scoreDisabled` | 100% | boolean |
| `email` | 100% | string |
| `extensionInstallDate` | 100% | string |
| `firstName` | 100% | string |
| `free` | 100% | boolean |
| `freemium` | 100% | boolean |
| `freemiumRegDate` | 100% | string |
| `grammarlyEdu` | 100% | boolean |
| `groups` | 100% | array |
| `id` | 100% | string |
| `institutionAdmin` | 100% | boolean |
| `institutionFullCards` | 100% | boolean |
| `institutionPlagiarismDisabled` | 100% | boolean |
| `institutionProofit` | 100% | boolean |
| `institutionQuickReplacement` | 100% | boolean |
| `institutionScoreDisabled` | 100% | boolean |
| `isTest` | 100% | boolean |
| `lastName` | 100% | string |
| `loginProviders` | 100% | array |
| `loginType` | 100% | string |
| `name` | 100% | string |
| `origin` | 100% | string |
| `passwordlessUser` | 100% | boolean |
| `permissions` | 100% | array |
| `plagiarismOn` | 100% | boolean |
| `registrationDate` | 100% | string |
| `roles` | 100% | array |
| `settings` | 100% | object |
| `subscriptionFree` | 100% | boolean |
| `trusted` | 100% | boolean |
| `type` | 100% | string |

**Response schema variants**

**Schema 1** `a8b133f77a` — 4 responses

```json
{
    "anonymous": boolean,
    "confirmed": boolean,
    "customFields": {
            "data-regulation": string,
            "frontend_primaryLanguage": string,
            "frontend_role": string,
            "frontend_soundFluent": string
        },
    "disabled": boolean,
    "editorFeatures": {
            "docsDisabled": boolean,
            "fullCards": boolean,
            "msOutlookEnabled": boolean,
            "msWordEnabled": boolean,
            "plagiarismDisabled": boolean,
            "proofit": boolean,
            "quickReplacement": boolean,
            "scoreDisabled": boolean
        },
    "email": string,
    "extensionInstallDate": string,
    "firstName": string,
    "free": boolean,
    "freemium": boolean,
    "freemiumRegDate": string,
    "grammarlyEdu": boolean,
    "groups": [
            string
        ],
    "id": string,
    "institutionAdmin": boolean,
    "institutionFullCards": boolean,
    "institutionPlagiarismDisabled": boolean,
    "institutionProofit": boolean,
    "institutionQuickReplacement": boolean,
    "institutionScoreDisabled": boolean,
    "isTest": boolean,
    "lastName": string,
    "loginProviders": [
            string
        ],
    "loginType": string,
    "name": string,
    "origin": string,
    "passwordlessUser": boolean,
    "permissions": [],
    "plagiarismOn": boolean,
    "registrationDate": string,
    "roles": [],
    "settings": {
        },
    "subscriptionFree": boolean,
    "trusted": boolean,
    "type": string
}
```

---

### `capi.grammarly.com/api/configuration/cheetah/v1/settings`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 50
**Response statuses:** 200: 40

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (17)

JSON responses: **17**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `cheetahEnabled` | 100% | boolean |
| `entryPointsConfig` | 100% | object |
| `entryPointsConfig.inlineQuickReplyEnabled` | 100% | boolean |
| `entryPointsConfig.inlineRewriteEnabled` | 100% | boolean |
| `featuresConfig` | 100% | object |
| `featuresConfig.promptStorageEnabled` | 100% | boolean |
| `status` | 100% | string |

**Response schema variants**

**Schema 1** `87f058b371` — 17 responses

```json
{
    "cheetahEnabled": boolean,
    "entryPointsConfig": {
            "inlineQuickReplyEnabled": boolean,
            "inlineRewriteEnabled": boolean
        },
    "featuresConfig": {
            "promptStorageEnabled": boolean
        },
    "status": string
}
```

---

### `f-log-assistant.grammarly.io/log`

**Observed methods:** `POST`
**Observed requests:** 50
**Response statuses:** 200: 45

#### Request

Content types: `text/plain` (50)

JSON requests: **50**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `cheetahClientProtocolVersion` | 100% | string |
| `clientType` | 100% | string |
| `clientVersion` | 100% | string |
| `data` | 86.0% | object |
| `data.actionId` | 38.0% | string |
| `data.reason` | 48.0% | string |
| `data.taskName` | 24.0% | string |
| `environment` | 100% | string |
| `experience` | 100% | string |
| `logLevel` | 100% | string |
| `message` | 100% | string |
| `source` | 100% | string |
| `userId` | 100% | string |
| `version` | 100% | string |

**Request schema variants**

**Schema 1** `987f4ebb23` — 19 requests

```json
{
    "cheetahClientProtocolVersion": string,
    "clientType": string,
    "clientVersion": string,
    "data": {
            "actionId": string
        },
    "environment": string,
    "experience": string,
    "logLevel": string,
    "message": string,
    "source": string,
    "userId": string,
    "version": string
}
```

**Schema 2** `9552777a35` — 12 requests

```json
{
    "cheetahClientProtocolVersion": string,
    "clientType": string,
    "clientVersion": string,
    "data": {
            "reason": string,
            "taskName": string
        },
    "environment": string,
    "experience": string,
    "logLevel": string,
    "message": string,
    "source": string,
    "userId": string,
    "version": string
}
```

**Schema 3** `f8f3253f30` — 12 requests

```json
{
    "cheetahClientProtocolVersion": string,
    "clientType": string,
    "clientVersion": string,
    "data": {
            "reason": string
        },
    "environment": string,
    "experience": string,
    "logLevel": string,
    "message": string,
    "source": string,
    "userId": string,
    "version": string
}
```

**Schema 4** `9dcd419084` — 7 requests

```json
{
    "cheetahClientProtocolVersion": string,
    "clientType": string,
    "clientVersion": string,
    "environment": string,
    "experience": string,
    "logLevel": string,
    "message": string,
    "source": string,
    "userId": string,
    "version": string
}
```

#### Response

**No response body was observed.**

---

### `assistant.femetrics.grammarly.io/batch/import`

**Observed methods:** `POST`
**Observed requests:** 42
**Response statuses:** 200: 34

#### Request

Content types: `text/plain` (42)

JSON requests: **42**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].labels` | 100% | array |
| `[].labels[].key` | 100% | string |
| `[].labels[].value` | 100% | string |
| `[].name` | 100% | string |
| `[].type` | 100% | string |
| `[].value` | 100% | integer, number |

**Request schema variants**

**Schema 1** `0f79d7ca09` — 41 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "type": string,
        "value": integer
    }
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "type": string,
        "value": number
    }
]
```

**Schema 2** `0df7b068da` — 1 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "type": string,
        "value": integer
    }
]
```

#### Response

Content types: `text/plain` (34)

**No response body was observed.**

---

### `capi.grammarly.com/freews`

**Observed methods:** `GET`
**Observed requests:** 26
**Response statuses:** 101: 26

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `auth.grammarly.com/tokens/v4/api/oauth2/token`

**Observed methods:** `POST`
**Observed requests:** 24
**Response statuses:** 200: 24

#### Request

Content types: `application/json` (24)

JSON requests: **24**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `client_id` | 100% | string |
| `grant_type` | 100% | string |
| `refresh_token` | 100% | string |

**Request schema variants**

**Schema 1** `f9f6667576` — 24 requests

```json
{
    "client_id": string,
    "grant_type": string,
    "refresh_token": string
}
```

#### Response

Content types: `application/json` (24)

JSON responses: **24**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `access_token` | 100% | string |
| `expires_in` | 100% | integer |
| `refresh_token` | 100% | string |
| `refresh_token_expires_in` | 100% | integer |
| `rti` | 100% | string |
| `token_type` | 100% | string |

**Response schema variants**

**Schema 1** `440623cc1a` — 24 responses

```json
{
    "access_token": string,
    "expires_in": integer,
    "refresh_token": string,
    "refresh_token_expires_in": integer,
    "rti": string,
    "token_type": string
}
```

---

### `f-log-editor.grammarly.io/logv2`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 18
**Response statuses:** 200: 9, 204: 9

#### Request

Content types: `application/json` (9)

JSON requests: **9**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `application` | 100% | string |
| `context` | 100% | object |
| `context.containerId` | 88.9% | string |
| `context.manakinExperiments` | 77.8% | object |
| `context.manakinExperiments.ai_editor_gate` | 55.6% | string |
| `context.manakinExperiments.ai_editor_individual_users_gate` | 77.8% | string |
| `context.manakinExperiments.ai_editor_pdf_upload_h1_2026` | 11.1% | string |
| `context.manakinExperiments.ai_editor_rollout_primary_existing` | 66.7% | string |
| `context.manakinExperiments.cpra` | 55.6% | string |
| `context.manakinExperiments.editor_my_grammarly_forethought_chat` | 11.1% | string |
| `context.manakinExperiments.gdpr_inverted` | 55.6% | string |
| `context.manakinExperiments.persistent_client_entry_point_my_grammarly` | 11.1% | string |
| `context.sessionId` | 100% | string |
| `context.user` | 88.9% | object |
| `context.user.id` | 88.9% | string |
| `context.user.type` | 88.9% | string |
| `context.userAgent` | 100% | object |
| `context.userAgent.browser` | 100% | string |
| `context.userAgent.os` | 100% | string |
| `context.userAgent.raw` | 100% | string |
| `context.userAgent.type` | 100% | string |
| `context.userAgent.version` | 100% | string |
| `context.visibilityState` | 88.9% | string |
| `env` | 100% | string |
| `extra` | 22.2% | object |
| `extra.hash` | 11.1% | string |
| `extra.pathname` | 11.1% | string |
| `extra.search` | 11.1% | string |
| `level` | 100% | string |
| `logger` | 100% | string |
| `message` | 100% | string |
| `version` | 100% | string |

**Request schema variants**

**Schema 1** `283811d49b` — 4 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "manakinExperiments": {
                        "ai_editor_gate": string,
                        "ai_editor_individual_users_gate": string,
                        "ai_editor_rollout_primary_existing": string,
                        "cpra": string,
                        "gdpr_inverted": string
                    },
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

**Schema 2** `415503290e` — 1 requests

```json
{
    "application": string,
    "context": {
            "sessionId": string,
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    }
        },
    "env": string,
    "extra": {
            "hash": string,
            "pathname": string,
            "search": string
        },
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

**Schema 3** `57c3f45b4d` — 1 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "extra": {
        },
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

**Schema 4** `d1e21e66a8` — 1 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "manakinExperiments": {
                        "ai_editor_individual_users_gate": string
                    },
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

**Schema 5** `d2e0f98068` — 1 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "manakinExperiments": {
                        "ai_editor_individual_users_gate": string,
                        "ai_editor_rollout_primary_existing": string
                    },
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

**Schema 6** `90ac015bae` — 1 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "manakinExperiments": {
                        "ai_editor_gate": string,
                        "ai_editor_individual_users_gate": string,
                        "ai_editor_pdf_upload_h1_2026": string,
                        "ai_editor_rollout_primary_existing": string,
                        "cpra": string,
                        "editor_my_grammarly_forethought_chat": string,
                        "gdpr_inverted": string,
                        "persistent_client_entry_point_my_grammarly": string
                    },
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

#### Response

**No response body was observed.**

---

### `f-log-win-extension.grammarly.io/logv2`

**Observed methods:** `POST`
**Observed requests:** 14
**Response statuses:** 200: 14

#### Request

Content types: `application/json` (14)

JSON requests: **14**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `Application` | 100% | string |
| `ApplicationInstanceId` | 14.3% | string |
| `ContainerId` | 100% | string |
| `Environment` | 100% | string |
| `Exception` | 100% | null, string |
| `Extra` | 100% | null, object |
| `Extra.Average memory: ` | 28.6% | number |
| `Extra.Culture` | 14.3% | string |
| `Extra.ExtraInfo` | 14.3% | object |
| `Extra.Initial memory: ` | 28.6% | number |
| `Extra.Is64BitOperatingSystem` | 35.7% | string |
| `Extra.Maximum memory: ` | 28.6% | number |
| `Extra.Memory usage increase: ` | 28.6% | number |
| `Extra.NetVersion` | 50.0% | string |
| `Extra.OSVersion` | 35.7% | string |
| `Extra.OsVersion` | 14.3% | string |
| `Extra.ProcessorCount` | 35.7% | string |
| `Extra.RunningTargetFramework` | 35.7% | string |
| `Extra.ScreenCount` | 35.7% | string |
| `Extra.ScreenScales` | 35.7% | string |
| `Extra.ScreensInfo` | 35.7% | string |
| `Extra.Source` | 35.7% | string |
| `Extra.TextScaleFactor` | 35.7% | string |
| `InstallerContainerId` | 14.3% | string |
| `IsPerMachine` | 14.3% | string |
| `Level` | 100% | string |
| `LogContainerId` | 85.7% | null |
| `Logger` | 100% | string |
| `Message` | 100% | string |
| `RunningTargetFramework` | 85.7% | string |
| `UserId` | 85.7% | null, string |
| `Version` | 100% | string |

**Request schema variants**

**Schema 1** `86c762e8c9` — 4 requests

```json
{
    "Application": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": null,
    "Extra": {
            "Average memory: ": number,
            "Initial memory: ": number,
            "Maximum memory: ": number,
            "Memory usage increase: ": number
        },
    "Level": string,
    "LogContainerId": null,
    "Logger": string,
    "Message": string,
    "RunningTargetFramework": string,
    "UserId": string,
    "Version": string
}
```

**Schema 2** `aba6b714d7` — 3 requests

```json
{
    "Application": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": null,
    "Extra": {
            "Is64BitOperatingSystem": string,
            "NetVersion": string,
            "OSVersion": string,
            "ProcessorCount": string,
            "RunningTargetFramework": string,
            "ScreenCount": string,
            "ScreenScales": string,
            "ScreensInfo": string,
            "Source": string,
            "TextScaleFactor": string
        },
    "Level": string,
    "LogContainerId": null,
    "Logger": string,
    "Message": string,
    "RunningTargetFramework": string,
    "UserId": null,
    "Version": string
}
```

**Schema 3** `4c55b1c476` — 2 requests

```json
{
    "Application": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": null,
    "Extra": null,
    "Level": string,
    "LogContainerId": null,
    "Logger": string,
    "Message": string,
    "RunningTargetFramework": string,
    "UserId": null,
    "Version": string
}
```

**Schema 4** `29e5d769cd` — 2 requests

```json
{
    "Application": string,
    "ApplicationInstanceId": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": null,
    "Extra": {
            "Culture": string,
            "ExtraInfo": {
                    },
            "NetVersion": string,
            "OsVersion": string
        },
    "InstallerContainerId": string,
    "IsPerMachine": string,
    "Level": string,
    "Logger": string,
    "Message": string,
    "Version": string
}
```

**Schema 5** `7276bf73d6` — 2 requests

```json
{
    "Application": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": null,
    "Extra": {
            "Is64BitOperatingSystem": string,
            "NetVersion": string,
            "OSVersion": string,
            "ProcessorCount": string,
            "RunningTargetFramework": string,
            "ScreenCount": string,
            "ScreenScales": string,
            "ScreensInfo": string,
            "Source": string,
            "TextScaleFactor": string
        },
    "Level": string,
    "LogContainerId": null,
    "Logger": string,
    "Message": string,
    "RunningTargetFramework": string,
    "UserId": string,
    "Version": string
}
```

**Schema 6** `e9354e3cf7` — 1 requests

```json
{
    "Application": string,
    "ContainerId": string,
    "Environment": string,
    "Exception": string,
    "Extra": null,
    "Level": string,
    "LogContainerId": null,
    "Logger": string,
    "Message": string,
    "RunningTargetFramework": string,
    "UserId": string,
    "Version": string
}
```

#### Response

**No response body was observed.**

---

### `gateway.grammarly.com/passport/api/v1/passport`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 13
**Response statuses:** 200: 13

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (12)

JSON responses: **11**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `passport` | 100% | object |
| `passport.featureVisa` | 100% | array |
| `passport.featureVisa[].entitlement` | 100% | object |
| `passport.featureVisa[].entitlement.boolValue` | 100% | boolean |
| `passport.featureVisa[].entitlement.stringValue` | 100% | string |
| `passport.featureVisa[].featureReference` | 100% | string |
| `passport.institutionDetails` | 100% | object |
| `passport.passportStatus` | 100% | object |
| `passport.passportStatus.passportStatusCode` | 100% | string |
| `passport.privacyDetails` | 100% | object |
| `passport.privacyDetails.settings` | 100% | string |
| `passport.userDetails` | 100% | object |
| `passport.userDetails.userId` | 100% | string |

**Response schema variants**

**Schema 1** `b8939e0ce3` — 6 responses

```json
{
    "passport": {
            "featureVisa": [
                        {
                            "entitlement": {
                                                "stringValue": string
                                            },
                            "featureReference": string
                        }
                        {
                            "entitlement": {
                                                "boolValue": boolean
                                            },
                            "featureReference": string
                        }
                    ],
            "institutionDetails": {
                    },
            "passportStatus": {
                        "passportStatusCode": string
                    },
            "privacyDetails": {
                        "settings": string
                    },
            "userDetails": {
                        "userId": string
                    }
        }
}
```

**Schema 2** `e8abfdccf2` — 5 responses

```json
{
    "passport": {
            "featureVisa": [
                        {
                            "entitlement": {
                                                "boolValue": boolean
                                            },
                            "featureReference": string
                        }
                        {
                            "entitlement": {
                                                "stringValue": string
                                            },
                            "featureReference": string
                        }
                    ],
            "institutionDetails": {
                    },
            "passportStatus": {
                        "passportStatusCode": string
                    },
            "privacyDetails": {
                        "settings": string
                    },
            "userDetails": {
                        "userId": string
                    }
        }
}
```

---

### `goldengate.grammarly.com/skills/users/{id}/skills`

**Observed methods:** `GET`
**Observed requests:** 12
**Response statuses:** 403: 12

#### Request

**No request body was observed.**

#### Response

Content types: `text/html` (12)

**No JSON response body was observed.**

---

### `gateway.grammarly.com/uhub/configuration`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 11
**Response statuses:** 200: 11

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (10)

JSON responses: **10**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `emogenieReport` | 90.0% | object |
| `emogenieReport.content` | 90.0% | object |
| `emogenieReport.content.ctaCopy` | 90.0% | string |
| `emogenieReport.content.ctaUrl` | 90.0% | string |
| `emogenieReport.tags` | 90.0% | array |
| `emogenieReport.upgradeHookName` | 90.0% | string |
| `emogenieReport.upgradeHookSlot` | 90.0% | string |
| `emogenieReport.upgradeHookSubVariant` | 90.0% | string |
| `emogenieReport.upgradeHookVariant` | 90.0% | string |
| `fallback` | 100% | object |
| `fallback.content` | 100% | object |
| `fallback.content.ctaCopy` | 100% | string |
| `fallback.content.ctaUrl` | 100% | string |
| `fallback.content.dismissCopy` | 100% | string |
| `fallback.content.title` | 100% | string |
| `fallback.upgradeHookName` | 100% | string |
| `fallback.upgradeHookSlot` | 100% | string |
| `fallback.upgradeHookSubVariant` | 100% | string |
| `fallback.upgradeHookVariant` | 100% | string |
| `plagiarismView` | 90.0% | object |
| `plagiarismView.content` | 90.0% | object |
| `plagiarismView.content.ctaCopy` | 90.0% | string |
| `plagiarismView.content.ctaUrl` | 90.0% | string |
| `plagiarismView.content.dismissCopy` | 90.0% | string |
| `plagiarismView.content.subtitle` | 90.0% | string |
| `plagiarismView.content.title` | 90.0% | string |
| `plagiarismView.tags` | 90.0% | array |
| `plagiarismView.upgradeHookName` | 90.0% | string |
| `plagiarismView.upgradeHookSlot` | 90.0% | string |
| `plagiarismView.upgradeHookSubVariant` | 90.0% | string |
| `plagiarismView.upgradeHookVariant` | 90.0% | string |
| `titleBar` | 10.0% | object |
| `titleBar.content` | 10.0% | object |
| `titleBar.content.advancedSuggestionsCtaCopy` | 10.0% | string |
| `titleBar.content.ctaCopy` | 10.0% | string |
| `titleBar.content.ctaUrl` | 10.0% | string |
| `titleBar.content.title` | 10.0% | string |
| `titleBar.tags` | 10.0% | array |
| `titleBar.upgradeHookName` | 10.0% | string |
| `titleBar.upgradeHookSlot` | 10.0% | string |
| `titleBar.upgradeHookSubVariant` | 10.0% | string |
| `titleBar.upgradeHookVariant` | 10.0% | string |

**Response schema variants**

**Schema 1** `29c30933fb` — 9 responses

```json
{
    "emogenieReport": {
            "content": {
                        "ctaCopy": string,
                        "ctaUrl": string
                    },
            "tags": [
                        string
                    ],
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        },
    "fallback": {
            "content": {
                        "ctaCopy": string,
                        "ctaUrl": string,
                        "dismissCopy": string,
                        "title": string
                    },
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        },
    "plagiarismView": {
            "content": {
                        "ctaCopy": string,
                        "ctaUrl": string,
                        "dismissCopy": string,
                        "subtitle": string,
                        "title": string
                    },
            "tags": [
                        string
                    ],
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        }
}
```

**Schema 2** `c086eec686` — 1 responses

```json
{
    "fallback": {
            "content": {
                        "ctaCopy": string,
                        "ctaUrl": string,
                        "dismissCopy": string,
                        "title": string
                    },
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        },
    "titleBar": {
            "content": {
                        "advancedSuggestionsCtaCopy": string,
                        "ctaCopy": string,
                        "ctaUrl": string,
                        "title": string
                    },
            "tags": [
                        string
                    ],
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        }
}
```

---

### `treatment.grammarly.com/treatment/get`

**Observed methods:** `POST`
**Observed requests:** 9
**Response statuses:** 200: 9

#### Request

Content types: `application/json` (9)

JSON requests: **9**

**Request field frequency**


**Request schema variants**

**Schema 1** `76efce69de` — 9 requests

```json
[
    string
]
```

#### Response

Content types: `application/json` (9)

JSON responses: **9**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].containerId` | 100% | string |
| `[].experimentId` | 100% | string |
| `[].experimentName` | 100% | string |
| `[].groupName` | 100% | string |
| `[].isTest` | 100% | boolean |
| `[].needLog` | 100% | boolean |
| `[].overrideType` | 100% | null |
| `[].qualifiedName` | 100% | null, string |
| `[].sender` | 100% | null |
| `[].source` | 100% | string |
| `[].type` | 100% | string |
| `[].userId` | 100% | integer |

**Response schema variants**

**Schema 1** `94b9dfff31` — 9 responses

```json
[
    {
        "containerId": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": null,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
    {
        "containerId": string,
        "experimentId": string,
        "experimentName": string,
        "groupName": string,
        "isTest": boolean,
        "needLog": boolean,
        "overrideType": null,
        "qualifiedName": string,
        "sender": null,
        "source": string,
        "type": string,
        "userId": integer
    }
]
```

---

### `update-windows.grammarly.com/update/llamaWindows`

**Observed methods:** `POST`
**Observed requests:** 9
**Response statuses:** 200: 9

#### Request

Content types: `text/plain` (9)

JSON requests: **9**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `currentVersion` | 100% | string |
| `experiments` | 100% | array |
| `isPremium` | 100% | boolean |
| `isPro` | 100% | boolean |
| `osArchitecture` | 100% | string |
| `userId` | 100% | string |

**Request schema variants**

**Schema 1** `00c9e0d787` — 9 requests

```json
{
    "currentVersion": string,
    "experiments": [
            string
        ],
    "isPremium": boolean,
    "isPro": boolean,
    "osArchitecture": string,
    "userId": string
}
```

#### Response

Content types: `application/json` (9)

JSON responses: **9**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `download` | 100% | string |
| `hash` | 100% | string |
| `isForceUpdate` | 100% | boolean |
| `releaseDate` | 100% | string |
| `targetFramework` | 100% | string |
| `version` | 100% | string |

**Response schema variants**

**Schema 1** `cff8d57e78` — 9 responses

```json
{
    "download": string,
    "hash": string,
    "isForceUpdate": boolean,
    "releaseDate": string,
    "targetFramework": string,
    "version": string
}
```

---

### `gateway.grammarly.com/experimentation/properties`

**Observed methods:** `OPTIONS, GET, POST`
**Observed requests:** 6
**Response statuses:** 200: 6

#### Request

Content types: `application/json` (2)

JSON requests: **2**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `DN:modals` | 50.0% | string |
| `banners` | 50.0% | string |

**Request schema variants**

**Schema 1** `d6a28da59a` — 1 requests

```json
{
    "banners": string
}
```

**Schema 2** `d35f7dfad4` — 1 requests

```json
{
    "DN:modals": string
}
```

#### Response

Content types: `text/plain` (1), `application/json` (3)

JSON responses: **2**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `DN:featuresOnboardingSeen` | 100% | string |
| `DN:modals` | 100% | string |
| `DN:news` | 100% | string |
| `DN:seenDenaliWelcome` | 100% | string |
| `DN:survey` | 100% | string |
| `banners` | 100% | string |
| `cheetah:onboardingState` | 100% | string |
| `cheetah:onboardingState:llamaWin` | 100% | string |
| `dialectWeak` | 100% | string |
| `emogenieEmojiState` | 100% | string |
| `firstCall` | 100% | string |
| `firstSeenTrashBin` | 100% | string |
| `kaza:bookmarks:onboarding:disabled` | 100% | string |
| `onboardingPassed` | 100% | string |
| `personalizedInsightsConsent:onboardingState:extension` | 100% | string |
| `showDesktopIntegrationExtensionToggle` | 100% | string |

**Response schema variants**

**Schema 1** `c6f0be0b0a` — 2 responses

```json
{
    "DN:featuresOnboardingSeen": string,
    "DN:modals": string,
    "DN:news": string,
    "DN:seenDenaliWelcome": string,
    "DN:survey": string,
    "banners": string,
    "cheetah:onboardingState": string,
    "cheetah:onboardingState:llamaWin": string,
    "dialectWeak": string,
    "emogenieEmojiState": string,
    "firstCall": string,
    "firstSeenTrashBin": string,
    "kaza:bookmarks:onboarding:disabled": string,
    "onboardingPassed": string,
    "personalizedInsightsConsent:onboardingState:extension": string,
    "showDesktopIntegrationExtensionToggle": string
}
```

---

### `subscription.grammarly.com/api/v1/subscription`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 4
**Response statuses:** 200: 4

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (3)

JSON responses: **3**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `bundleBasicProPlans` | 100% | array |
| `bundleBasicProPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleBasicProPlans[].description` | 100% | string |
| `bundleBasicProPlans[].hasTrial` | 100% | boolean |
| `bundleBasicProPlans[].id` | 100% | integer |
| `bundleBasicProPlans[].periodMonths` | 100% | integer |
| `bundleBasicProPlans[].price` | 100% | number |
| `bundleBasicProPlans[].priceMoney` | 100% | object |
| `bundleBasicProPlans[].priceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].priceMoney.value` | 100% | number |
| `bundleBasicProPlans[].regularPlanId` | 100% | integer |
| `bundleBasicProPlans[].regularPrice` | 100% | number |
| `bundleBasicProPlans[].regularPriceMoney` | 100% | object |
| `bundleBasicProPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].regularPriceMoney.value` | 100% | number |
| `bundleBasicProPlans[].renewalPlanId` | 100% | integer |
| `bundleBasicProPlans[].renewalPrice` | 100% | number |
| `bundleBasicProPlans[].renewalPriceMoney` | 100% | object |
| `bundleBasicProPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleBasicProPlans[].title` | 100% | string |
| `bundleBasicProPlans[].trialDays` | 100% | integer |
| `bundleBasicProPricingOptions` | 100% | object |
| `bundleBasicProPricingOptions.discountSuppressed` | 100% | boolean |
| `bundleBusinessPlans` | 100% | array |
| `bundleBusinessPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleBusinessPlans[].description` | 100% | string |
| `bundleBusinessPlans[].hasTrial` | 100% | boolean |
| `bundleBusinessPlans[].id` | 100% | integer |
| `bundleBusinessPlans[].periodMonths` | 100% | integer |
| `bundleBusinessPlans[].price` | 100% | number |
| `bundleBusinessPlans[].priceMoney` | 100% | object |
| `bundleBusinessPlans[].priceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].priceMoney.value` | 100% | number |
| `bundleBusinessPlans[].priceTiers` | 100% | array |
| `bundleBusinessPlans[].priceTiers[].fromSeats` | 100% | integer |
| `bundleBusinessPlans[].priceTiers[].price` | 100% | number |
| `bundleBusinessPlans[].priceTiers[].priceMoney` | 100% | object |
| `bundleBusinessPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `bundleBusinessPlans[].priceTiers[].toSeats` | 100% | integer |
| `bundleBusinessPlans[].regularPlanId` | 100% | integer |
| `bundleBusinessPlans[].regularPrice` | 100% | number |
| `bundleBusinessPlans[].regularPriceMoney` | 100% | object |
| `bundleBusinessPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].regularPriceMoney.value` | 100% | number |
| `bundleBusinessPlans[].renewalPlanId` | 100% | integer |
| `bundleBusinessPlans[].renewalPrice` | 100% | number |
| `bundleBusinessPlans[].renewalPriceMoney` | 100% | object |
| `bundleBusinessPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleBusinessPlans[].title` | 100% | string |
| `bundleBusinessPlans[].trialDays` | 100% | integer |
| `bundleBusinessPricingOptions` | 100% | object |
| `bundleBusinessPricingOptions.discountSuppressed` | 100% | boolean |
| `bundleProPlans` | 100% | array |
| `bundleProPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleProPlans[].description` | 100% | string |
| `bundleProPlans[].hasTrial` | 100% | boolean |
| `bundleProPlans[].id` | 100% | integer |
| `bundleProPlans[].periodMonths` | 100% | integer |
| `bundleProPlans[].price` | 100% | number |
| `bundleProPlans[].priceMoney` | 100% | object |
| `bundleProPlans[].priceMoney.currency` | 100% | string |
| `bundleProPlans[].priceMoney.value` | 100% | number |
| `bundleProPlans[].priceTiers` | 100% | array |
| `bundleProPlans[].priceTiers[].fromSeats` | 100% | integer |
| `bundleProPlans[].priceTiers[].price` | 100% | number |
| `bundleProPlans[].priceTiers[].priceMoney` | 100% | object |
| `bundleProPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `bundleProPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `bundleProPlans[].priceTiers[].toSeats` | 100% | integer |
| `bundleProPlans[].regularPlanId` | 100% | integer |
| `bundleProPlans[].regularPrice` | 100% | number |
| `bundleProPlans[].regularPriceMoney` | 100% | object |
| `bundleProPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleProPlans[].regularPriceMoney.value` | 100% | number |
| `bundleProPlans[].renewalPlanId` | 100% | integer |
| `bundleProPlans[].renewalPrice` | 100% | number |
| `bundleProPlans[].renewalPriceMoney` | 100% | object |
| `bundleProPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleProPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleProPlans[].title` | 100% | string |
| `bundleProPlans[].trialDays` | 100% | integer |
| `bundleProPricingOptions` | 100% | object |
| `bundleProPricingOptions.discountSuppressed` | 100% | boolean |
| `countryCode` | 100% | string |
| `institutionDynamicPlans` | 100% | array |
| `institutionDynamicPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionDynamicPlans[].description` | 100% | string |
| `institutionDynamicPlans[].hasTrial` | 100% | boolean |
| `institutionDynamicPlans[].id` | 100% | integer |
| `institutionDynamicPlans[].periodMonths` | 100% | integer |
| `institutionDynamicPlans[].price` | 100% | number |
| `institutionDynamicPlans[].priceMoney` | 100% | object |
| `institutionDynamicPlans[].priceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].priceMoney.value` | 100% | number |
| `institutionDynamicPlans[].priceTiers` | 100% | array |
| `institutionDynamicPlans[].priceTiers[].fromSeats` | 100% | integer |
| `institutionDynamicPlans[].priceTiers[].price` | 100% | number |
| `institutionDynamicPlans[].priceTiers[].priceMoney` | 100% | object |
| `institutionDynamicPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `institutionDynamicPlans[].priceTiers[].toSeats` | 100% | integer |
| `institutionDynamicPlans[].regularPlanId` | 100% | integer |
| `institutionDynamicPlans[].regularPrice` | 100% | number |
| `institutionDynamicPlans[].regularPriceMoney` | 100% | object |
| `institutionDynamicPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].regularPriceMoney.value` | 100% | number |
| `institutionDynamicPlans[].title` | 100% | string |
| `institutionDynamicPlans[].trialDays` | 100% | integer |
| `institutionEduPlans` | 100% | array |
| `institutionEduPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionEduPlans[].description` | 100% | string |
| `institutionEduPlans[].hasTrial` | 100% | boolean |
| `institutionEduPlans[].id` | 100% | integer |
| `institutionEduPlans[].periodMonths` | 100% | integer |
| `institutionEduPlans[].price` | 100% | number |
| `institutionEduPlans[].priceMoney` | 100% | object |
| `institutionEduPlans[].priceMoney.currency` | 100% | string |
| `institutionEduPlans[].priceMoney.value` | 100% | number |
| `institutionEduPlans[].regularPlanId` | 100% | integer |
| `institutionEduPlans[].regularPrice` | 100% | number |
| `institutionEduPlans[].regularPriceMoney` | 100% | object |
| `institutionEduPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionEduPlans[].regularPriceMoney.value` | 100% | number |
| `institutionEduPlans[].title` | 100% | string |
| `institutionEduPlans[].trialDays` | 100% | integer |
| `institutionPlans` | 100% | array |
| `institutionPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionPlans[].description` | 100% | string |
| `institutionPlans[].hasTrial` | 100% | boolean |
| `institutionPlans[].id` | 100% | integer |
| `institutionPlans[].periodMonths` | 100% | integer |
| `institutionPlans[].price` | 100% | number |
| `institutionPlans[].priceMoney` | 100% | object |
| `institutionPlans[].priceMoney.currency` | 100% | string |
| `institutionPlans[].priceMoney.value` | 100% | number |
| `institutionPlans[].regularPlanId` | 100% | integer |
| `institutionPlans[].regularPrice` | 100% | number |
| `institutionPlans[].regularPriceMoney` | 100% | object |
| `institutionPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionPlans[].regularPriceMoney.value` | 100% | number |
| `institutionPlans[].title` | 100% | string |
| `institutionPlans[].trialDays` | 100% | integer |
| `isAppleSubscription` | 100% | boolean |
| `isGooglePlaySubscription` | 100% | boolean |
| `isPremium` | 100% | boolean |
| `paymentMethodOptions` | 100% | object |
| `paymentMethodOptions.americanExpressDisabled` | 100% | boolean |
| `paymentMethodOptions.disabledCardTypes` | 100% | array |
| `paymentMethodOptions.payPalDisabled` | 100% | boolean |
| `plans` | 100% | array |
| `plans[].baseInstitutionCampaign` | 100% | boolean |
| `plans[].description` | 100% | string |
| `plans[].hasTrial` | 100% | boolean |
| `plans[].id` | 100% | integer |
| `plans[].periodMonths` | 100% | integer |
| `plans[].price` | 100% | number |
| `plans[].priceMoney` | 100% | object |
| `plans[].priceMoney.currency` | 100% | string |
| `plans[].priceMoney.value` | 100% | number |
| `plans[].regularPlanId` | 100% | integer |
| `plans[].regularPrice` | 100% | number |
| `plans[].regularPriceMoney` | 100% | object |
| `plans[].regularPriceMoney.currency` | 100% | string |
| `plans[].regularPriceMoney.value` | 100% | number |
| `plans[].title` | 100% | string |
| `plans[].trialDays` | 100% | integer |
| `pricingOptions` | 100% | object |
| `pricingOptions.discountSuppressed` | 100% | boolean |
| `proPlans` | 100% | array |
| `proPlans[].baseInstitutionCampaign` | 100% | boolean |
| `proPlans[].description` | 100% | string |
| `proPlans[].hasTrial` | 100% | boolean |
| `proPlans[].id` | 100% | integer |
| `proPlans[].periodMonths` | 100% | integer |
| `proPlans[].price` | 100% | number |
| `proPlans[].priceMoney` | 100% | object |
| `proPlans[].priceMoney.currency` | 100% | string |
| `proPlans[].priceMoney.value` | 100% | number |
| `proPlans[].priceTiers` | 100% | array |
| `proPlans[].priceTiers[].fromSeats` | 100% | integer |
| `proPlans[].priceTiers[].price` | 100% | number |
| `proPlans[].priceTiers[].priceMoney` | 100% | object |
| `proPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `proPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `proPlans[].priceTiers[].toSeats` | 100% | integer |
| `proPlans[].regularPlanId` | 100% | integer |
| `proPlans[].regularPrice` | 100% | number |
| `proPlans[].regularPriceMoney` | 100% | object |
| `proPlans[].regularPriceMoney.currency` | 100% | string |
| `proPlans[].regularPriceMoney.value` | 100% | number |
| `proPlans[].renewalPlanId` | 100% | integer |
| `proPlans[].renewalPrice` | 100% | number |
| `proPlans[].renewalPriceMoney` | 100% | object |
| `proPlans[].renewalPriceMoney.currency` | 100% | string |
| `proPlans[].renewalPriceMoney.value` | 100% | number |
| `proPlans[].title` | 100% | string |
| `proPlans[].trialDays` | 100% | integer |
| `proPricingOptions` | 100% | object |
| `proPricingOptions.discountSuppressed` | 100% | boolean |

**Response schema variants**

**Schema 1** `48d18ea436` — 3 responses

```json
{
    "bundleBasicProPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleBasicProPricingOptions": {
            "discountSuppressed": boolean
        },
    "bundleBusinessPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleBusinessPricingOptions": {
            "discountSuppressed": boolean
        },
    "bundleProPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleProPricingOptions": {
            "discountSuppressed": boolean
        },
    "countryCode": string,
    "institutionDynamicPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "institutionEduPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "institutionPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "isAppleSubscription": boolean,
    "isGooglePlaySubscription": boolean,
    "isPremium": boolean,
    "paymentMethodOptions": {
            "americanExpressDisabled": boolean,
            "disabledCardTypes": [],
            "payPalDisabled": boolean
        },
    "plans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "pricingOptions": {
            "discountSuppressed": boolean
        },
    "proPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "proPricingOptions": {
            "discountSuppressed": boolean
        }
}
```

---

### `assets.grammarly.com/emoji/v1/1f3af.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1, 304: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f455.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1, 304: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f914.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f917.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1, 304: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f91d.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1, 304: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/261d.2x.png`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (2)

**No JSON response body was observed.**

---

### `auth.grammarly.com/auth/v3/user`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

**No JSON response body was observed.**

---

### `auth.grammarly.com/auth/v3/user/bridge/check-eligibility/coda`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `isEligible` | 100% | boolean |

**Response schema variants**

**Schema 1** `01a34c673e` — 1 responses

```json
{
    "isEligible": boolean
}
```

---

### `auth.grammarly.com/auth/v3/user/oranonymous`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

**No JSON response body was observed.**

---

### `capi.grammarly.com/api/configuration/suggestion-bundles/v1/settings`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (2)

JSON responses: **2**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `correctnessFullSentenceRewrites` | 100% | string |

**Response schema variants**

**Schema 1** `8f808a6b5f` — 2 responses

```json
{
    "correctnessFullSentenceRewrites": string
}
```

---

### `dox.grammarly.com/documents`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (1)

**No JSON response body was observed.**

---

### `f-log-editor-debug.grammarly.io/logv2`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 2
**Response statuses:** 200: 1, 204: 1

#### Request

Content types: `application/json` (1)

JSON requests: **1**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `application` | 100% | string |
| `context` | 100% | object |
| `context.containerId` | 100% | string |
| `context.manakinExperiments` | 100% | object |
| `context.manakinExperiments.ai_editor_gate` | 100% | string |
| `context.manakinExperiments.ai_editor_individual_users_gate` | 100% | string |
| `context.manakinExperiments.ai_editor_pdf_upload_h1_2026` | 100% | string |
| `context.manakinExperiments.ai_editor_rollout_primary_existing` | 100% | string |
| `context.manakinExperiments.cpra` | 100% | string |
| `context.manakinExperiments.editor_my_grammarly_forethought_chat` | 100% | string |
| `context.manakinExperiments.gdpr_inverted` | 100% | string |
| `context.manakinExperiments.persistent_client_entry_point_my_grammarly` | 100% | string |
| `context.sessionId` | 100% | string |
| `context.user` | 100% | object |
| `context.user.id` | 100% | string |
| `context.user.type` | 100% | string |
| `context.userAgent` | 100% | object |
| `context.userAgent.browser` | 100% | string |
| `context.userAgent.os` | 100% | string |
| `context.userAgent.raw` | 100% | string |
| `context.userAgent.type` | 100% | string |
| `context.userAgent.version` | 100% | string |
| `context.visibilityState` | 100% | string |
| `env` | 100% | string |
| `extra` | 100% | object |
| `extra.action` | 100% | string |
| `extra.bannerType` | 100% | string |
| `extra.object` | 100% | string |
| `extra.objectId` | 100% | string |
| `extra.pageId` | 100% | string |
| `level` | 100% | string |
| `logger` | 100% | string |
| `message` | 100% | string |
| `version` | 100% | string |

**Request schema variants**

**Schema 1** `8650ee17c5` — 1 requests

```json
{
    "application": string,
    "context": {
            "containerId": string,
            "manakinExperiments": {
                        "ai_editor_gate": string,
                        "ai_editor_individual_users_gate": string,
                        "ai_editor_pdf_upload_h1_2026": string,
                        "ai_editor_rollout_primary_existing": string,
                        "cpra": string,
                        "editor_my_grammarly_forethought_chat": string,
                        "gdpr_inverted": string,
                        "persistent_client_entry_point_my_grammarly": string
                    },
            "sessionId": string,
            "user": {
                        "id": string,
                        "type": string
                    },
            "userAgent": {
                        "browser": string,
                        "os": string,
                        "raw": string,
                        "type": string,
                        "version": string
                    },
            "visibilityState": string
        },
    "env": string,
    "extra": {
            "action": string,
            "bannerType": string,
            "object": string,
            "objectId": string,
            "pageId": string
        },
    "level": string,
    "logger": string,
    "message": string,
    "version": string
}
```

#### Response

**No response body was observed.**

---

### `gateway.grammarly.com/authorship/v1/user/{id}/settings`

**Observed methods:** `GET`
**Observed requests:** 2

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `gateway.grammarly.com/experimentation/properties/showDesktopIntegrationExtensionToggle`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (2)

JSON responses: **2**

**Response field frequency**


**Response schema variants**

**Schema 1** `a5b031ab62` — 2 responses

```json
boolean
```

---

### `gateway.grammarly.com/health`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (2)

JSON responses: **2**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `status` | 100% | string |

**Response schema variants**

**Schema 1** `057dbc6d9b` — 2 responses

```json
{
    "status": string
}
```

---

### `gateway.grammarly.com/mise/api/v1/iterable/access/token`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (2)

JSON responses: **2**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `apiKey` | 100% | string |
| `jwtToken` | 100% | string |

**Response schema variants**

**Schema 1** `8df505cf2b` — 2 responses

```json
{
    "apiKey": string,
    "jwtToken": string
}
```

---

### `gateway.grammarly.com/privacy/v1/api/data-sharing/user`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (2)

JSON responses: **2**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `consentRequired` | 100% | boolean |
| `dataSharing` | 100% | boolean |
| `features` | 100% | object |
| `features.personalizedInsights` | 100% | object |
| `features.personalizedInsights.dataSharing` | 100% | boolean |

**Response schema variants**

**Schema 1** `9c53bc262d` — 2 responses

```json
{
    "consentRequired": boolean,
    "dataSharing": boolean,
    "features": {
            "personalizedInsights": {
                        "dataSharing": boolean
                    }
        }
}
```

---

### `gateway.grammarly.com/subscription/api/v1/subscription`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `bundleBasicProPlans` | 100% | array |
| `bundleBasicProPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleBasicProPlans[].description` | 100% | string |
| `bundleBasicProPlans[].hasTrial` | 100% | boolean |
| `bundleBasicProPlans[].id` | 100% | integer |
| `bundleBasicProPlans[].periodMonths` | 100% | integer |
| `bundleBasicProPlans[].price` | 100% | number |
| `bundleBasicProPlans[].priceMoney` | 100% | object |
| `bundleBasicProPlans[].priceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].priceMoney.value` | 100% | number |
| `bundleBasicProPlans[].regularPlanId` | 100% | integer |
| `bundleBasicProPlans[].regularPrice` | 100% | number |
| `bundleBasicProPlans[].regularPriceMoney` | 100% | object |
| `bundleBasicProPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].regularPriceMoney.value` | 100% | number |
| `bundleBasicProPlans[].renewalPlanId` | 100% | integer |
| `bundleBasicProPlans[].renewalPrice` | 100% | number |
| `bundleBasicProPlans[].renewalPriceMoney` | 100% | object |
| `bundleBasicProPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleBasicProPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleBasicProPlans[].title` | 100% | string |
| `bundleBasicProPlans[].trialDays` | 100% | integer |
| `bundleBasicProPricingOptions` | 100% | object |
| `bundleBasicProPricingOptions.discountSuppressed` | 100% | boolean |
| `bundleBusinessPlans` | 100% | array |
| `bundleBusinessPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleBusinessPlans[].description` | 100% | string |
| `bundleBusinessPlans[].hasTrial` | 100% | boolean |
| `bundleBusinessPlans[].id` | 100% | integer |
| `bundleBusinessPlans[].periodMonths` | 100% | integer |
| `bundleBusinessPlans[].price` | 100% | number |
| `bundleBusinessPlans[].priceMoney` | 100% | object |
| `bundleBusinessPlans[].priceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].priceMoney.value` | 100% | number |
| `bundleBusinessPlans[].priceTiers` | 100% | array |
| `bundleBusinessPlans[].priceTiers[].fromSeats` | 100% | integer |
| `bundleBusinessPlans[].priceTiers[].price` | 100% | number |
| `bundleBusinessPlans[].priceTiers[].priceMoney` | 100% | object |
| `bundleBusinessPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `bundleBusinessPlans[].priceTiers[].toSeats` | 100% | integer |
| `bundleBusinessPlans[].regularPlanId` | 100% | integer |
| `bundleBusinessPlans[].regularPrice` | 100% | number |
| `bundleBusinessPlans[].regularPriceMoney` | 100% | object |
| `bundleBusinessPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].regularPriceMoney.value` | 100% | number |
| `bundleBusinessPlans[].renewalPlanId` | 100% | integer |
| `bundleBusinessPlans[].renewalPrice` | 100% | number |
| `bundleBusinessPlans[].renewalPriceMoney` | 100% | object |
| `bundleBusinessPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleBusinessPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleBusinessPlans[].title` | 100% | string |
| `bundleBusinessPlans[].trialDays` | 100% | integer |
| `bundleBusinessPricingOptions` | 100% | object |
| `bundleBusinessPricingOptions.discountSuppressed` | 100% | boolean |
| `bundleProPlans` | 100% | array |
| `bundleProPlans[].baseInstitutionCampaign` | 100% | boolean |
| `bundleProPlans[].description` | 100% | string |
| `bundleProPlans[].hasTrial` | 100% | boolean |
| `bundleProPlans[].id` | 100% | integer |
| `bundleProPlans[].periodMonths` | 100% | integer |
| `bundleProPlans[].price` | 100% | number |
| `bundleProPlans[].priceMoney` | 100% | object |
| `bundleProPlans[].priceMoney.currency` | 100% | string |
| `bundleProPlans[].priceMoney.value` | 100% | number |
| `bundleProPlans[].priceTiers` | 100% | array |
| `bundleProPlans[].priceTiers[].fromSeats` | 100% | integer |
| `bundleProPlans[].priceTiers[].price` | 100% | number |
| `bundleProPlans[].priceTiers[].priceMoney` | 100% | object |
| `bundleProPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `bundleProPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `bundleProPlans[].priceTiers[].toSeats` | 100% | integer |
| `bundleProPlans[].regularPlanId` | 100% | integer |
| `bundleProPlans[].regularPrice` | 100% | number |
| `bundleProPlans[].regularPriceMoney` | 100% | object |
| `bundleProPlans[].regularPriceMoney.currency` | 100% | string |
| `bundleProPlans[].regularPriceMoney.value` | 100% | number |
| `bundleProPlans[].renewalPlanId` | 100% | integer |
| `bundleProPlans[].renewalPrice` | 100% | number |
| `bundleProPlans[].renewalPriceMoney` | 100% | object |
| `bundleProPlans[].renewalPriceMoney.currency` | 100% | string |
| `bundleProPlans[].renewalPriceMoney.value` | 100% | number |
| `bundleProPlans[].title` | 100% | string |
| `bundleProPlans[].trialDays` | 100% | integer |
| `bundleProPricingOptions` | 100% | object |
| `bundleProPricingOptions.discountSuppressed` | 100% | boolean |
| `countryCode` | 100% | string |
| `institutionDynamicPlans` | 100% | array |
| `institutionDynamicPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionDynamicPlans[].description` | 100% | string |
| `institutionDynamicPlans[].hasTrial` | 100% | boolean |
| `institutionDynamicPlans[].id` | 100% | integer |
| `institutionDynamicPlans[].periodMonths` | 100% | integer |
| `institutionDynamicPlans[].price` | 100% | number |
| `institutionDynamicPlans[].priceMoney` | 100% | object |
| `institutionDynamicPlans[].priceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].priceMoney.value` | 100% | number |
| `institutionDynamicPlans[].priceTiers` | 100% | array |
| `institutionDynamicPlans[].priceTiers[].fromSeats` | 100% | integer |
| `institutionDynamicPlans[].priceTiers[].price` | 100% | number |
| `institutionDynamicPlans[].priceTiers[].priceMoney` | 100% | object |
| `institutionDynamicPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `institutionDynamicPlans[].priceTiers[].toSeats` | 100% | integer |
| `institutionDynamicPlans[].regularPlanId` | 100% | integer |
| `institutionDynamicPlans[].regularPrice` | 100% | number |
| `institutionDynamicPlans[].regularPriceMoney` | 100% | object |
| `institutionDynamicPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionDynamicPlans[].regularPriceMoney.value` | 100% | number |
| `institutionDynamicPlans[].title` | 100% | string |
| `institutionDynamicPlans[].trialDays` | 100% | integer |
| `institutionEduPlans` | 100% | array |
| `institutionEduPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionEduPlans[].description` | 100% | string |
| `institutionEduPlans[].hasTrial` | 100% | boolean |
| `institutionEduPlans[].id` | 100% | integer |
| `institutionEduPlans[].periodMonths` | 100% | integer |
| `institutionEduPlans[].price` | 100% | number |
| `institutionEduPlans[].priceMoney` | 100% | object |
| `institutionEduPlans[].priceMoney.currency` | 100% | string |
| `institutionEduPlans[].priceMoney.value` | 100% | number |
| `institutionEduPlans[].regularPlanId` | 100% | integer |
| `institutionEduPlans[].regularPrice` | 100% | number |
| `institutionEduPlans[].regularPriceMoney` | 100% | object |
| `institutionEduPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionEduPlans[].regularPriceMoney.value` | 100% | number |
| `institutionEduPlans[].title` | 100% | string |
| `institutionEduPlans[].trialDays` | 100% | integer |
| `institutionPlans` | 100% | array |
| `institutionPlans[].baseInstitutionCampaign` | 100% | boolean |
| `institutionPlans[].description` | 100% | string |
| `institutionPlans[].hasTrial` | 100% | boolean |
| `institutionPlans[].id` | 100% | integer |
| `institutionPlans[].periodMonths` | 100% | integer |
| `institutionPlans[].price` | 100% | number |
| `institutionPlans[].priceMoney` | 100% | object |
| `institutionPlans[].priceMoney.currency` | 100% | string |
| `institutionPlans[].priceMoney.value` | 100% | number |
| `institutionPlans[].regularPlanId` | 100% | integer |
| `institutionPlans[].regularPrice` | 100% | number |
| `institutionPlans[].regularPriceMoney` | 100% | object |
| `institutionPlans[].regularPriceMoney.currency` | 100% | string |
| `institutionPlans[].regularPriceMoney.value` | 100% | number |
| `institutionPlans[].title` | 100% | string |
| `institutionPlans[].trialDays` | 100% | integer |
| `isAppleSubscription` | 100% | boolean |
| `isGooglePlaySubscription` | 100% | boolean |
| `isPremium` | 100% | boolean |
| `paymentMethodOptions` | 100% | object |
| `paymentMethodOptions.americanExpressDisabled` | 100% | boolean |
| `paymentMethodOptions.disabledCardTypes` | 100% | array |
| `paymentMethodOptions.payPalDisabled` | 100% | boolean |
| `plans` | 100% | array |
| `plans[].baseInstitutionCampaign` | 100% | boolean |
| `plans[].description` | 100% | string |
| `plans[].hasTrial` | 100% | boolean |
| `plans[].id` | 100% | integer |
| `plans[].periodMonths` | 100% | integer |
| `plans[].price` | 100% | number |
| `plans[].priceMoney` | 100% | object |
| `plans[].priceMoney.currency` | 100% | string |
| `plans[].priceMoney.value` | 100% | number |
| `plans[].regularPlanId` | 100% | integer |
| `plans[].regularPrice` | 100% | number |
| `plans[].regularPriceMoney` | 100% | object |
| `plans[].regularPriceMoney.currency` | 100% | string |
| `plans[].regularPriceMoney.value` | 100% | number |
| `plans[].title` | 100% | string |
| `plans[].trialDays` | 100% | integer |
| `pricingOptions` | 100% | object |
| `pricingOptions.discountSuppressed` | 100% | boolean |
| `proPlans` | 100% | array |
| `proPlans[].baseInstitutionCampaign` | 100% | boolean |
| `proPlans[].description` | 100% | string |
| `proPlans[].hasTrial` | 100% | boolean |
| `proPlans[].id` | 100% | integer |
| `proPlans[].periodMonths` | 100% | integer |
| `proPlans[].price` | 100% | number |
| `proPlans[].priceMoney` | 100% | object |
| `proPlans[].priceMoney.currency` | 100% | string |
| `proPlans[].priceMoney.value` | 100% | number |
| `proPlans[].priceTiers` | 100% | array |
| `proPlans[].priceTiers[].fromSeats` | 100% | integer |
| `proPlans[].priceTiers[].price` | 100% | number |
| `proPlans[].priceTiers[].priceMoney` | 100% | object |
| `proPlans[].priceTiers[].priceMoney.currency` | 100% | string |
| `proPlans[].priceTiers[].priceMoney.value` | 100% | number |
| `proPlans[].priceTiers[].toSeats` | 100% | integer |
| `proPlans[].regularPlanId` | 100% | integer |
| `proPlans[].regularPrice` | 100% | number |
| `proPlans[].regularPriceMoney` | 100% | object |
| `proPlans[].regularPriceMoney.currency` | 100% | string |
| `proPlans[].regularPriceMoney.value` | 100% | number |
| `proPlans[].renewalPlanId` | 100% | integer |
| `proPlans[].renewalPrice` | 100% | number |
| `proPlans[].renewalPriceMoney` | 100% | object |
| `proPlans[].renewalPriceMoney.currency` | 100% | string |
| `proPlans[].renewalPriceMoney.value` | 100% | number |
| `proPlans[].title` | 100% | string |
| `proPlans[].trialDays` | 100% | integer |
| `proPricingOptions` | 100% | object |
| `proPricingOptions.discountSuppressed` | 100% | boolean |

**Response schema variants**

**Schema 1** `48d18ea436` — 1 responses

```json
{
    "bundleBasicProPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleBasicProPricingOptions": {
            "discountSuppressed": boolean
        },
    "bundleBusinessPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleBusinessPricingOptions": {
            "discountSuppressed": boolean
        },
    "bundleProPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "bundleProPricingOptions": {
            "discountSuppressed": boolean
        },
    "countryCode": string,
    "institutionDynamicPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "institutionEduPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "institutionPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "isAppleSubscription": boolean,
    "isGooglePlaySubscription": boolean,
    "isPremium": boolean,
    "paymentMethodOptions": {
            "americanExpressDisabled": boolean,
            "disabledCardTypes": [],
            "payPalDisabled": boolean
        },
    "plans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "pricingOptions": {
            "discountSuppressed": boolean
        },
    "proPlans": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": number,
                "priceMoney": {
                                "currency": string,
                                "value": number
                            },
                "priceTiers": [
                                {
                                    "fromSeats": integer,
                                    "price": number,
                                    "priceMoney": {
                                                            "currency": string,
                                                            "value": number
                                                        },
                                    "toSeats": integer
                                }
                            ],
                "regularPlanId": integer,
                "regularPrice": number,
                "regularPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "renewalPlanId": integer,
                "renewalPrice": number,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": number
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "proPricingOptions": {
            "discountSuppressed": boolean
        }
}
```

---

### `gateway.grammarly.com/subscription/api/v2/support-portal/userInfo`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (2)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `userType` | 100% | string |

**Response schema variants**

**Schema 1** `7bc6231a4a` — 1 responses

```json
{
    "userType": string
}
```

---

### `gateway.grammarly.com/uhub/events`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 2
**Response statuses:** 200: 1, 201: 1

#### Request

Content types: `application/json` (1)

JSON requests: **1**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `kind` | 100% | string |
| `uphook` | 100% | object |
| `uphook.content` | 100% | object |
| `uphook.content.advancedSuggestionsCtaCopy` | 100% | string |
| `uphook.content.ctaCopy` | 100% | string |
| `uphook.content.ctaUrl` | 100% | string |
| `uphook.content.title` | 100% | string |
| `uphook.tags` | 100% | array |
| `uphook.upgradeHookName` | 100% | string |
| `uphook.upgradeHookSlot` | 100% | string |
| `uphook.upgradeHookSubVariant` | 100% | string |
| `uphook.upgradeHookVariant` | 100% | string |

**Request schema variants**

**Schema 1** `ef60aa06d8` — 1 requests

```json
{
    "kind": string,
    "uphook": {
            "content": {
                        "advancedSuggestionsCtaCopy": string,
                        "ctaCopy": string,
                        "ctaUrl": string,
                        "title": string
                    },
            "tags": [
                        string
                    ],
            "upgradeHookName": string,
            "upgradeHookSlot": string,
            "upgradeHookSubVariant": string,
            "upgradeHookVariant": string
        }
}
```

#### Response

Content types: `text/plain` (1)

**No response body was observed.**

---

### `gateway.grammarly.com/vito/plans`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `fallback` | 100% | array |
| `fallback[].baseInstitutionCampaign` | 100% | boolean |
| `fallback[].description` | 100% | string |
| `fallback[].hasTrial` | 100% | boolean |
| `fallback[].id` | 100% | integer |
| `fallback[].periodMonths` | 100% | integer |
| `fallback[].price` | 100% | integer |
| `fallback[].priceMoney` | 100% | object |
| `fallback[].priceMoney.currency` | 100% | string |
| `fallback[].priceMoney.value` | 100% | integer |
| `fallback[].regularPlanId` | 100% | integer |
| `fallback[].regularPrice` | 100% | integer |
| `fallback[].regularPriceMoney` | 100% | object |
| `fallback[].regularPriceMoney.currency` | 100% | string |
| `fallback[].regularPriceMoney.value` | 100% | integer |
| `fallback[].renewalPlanId` | 100% | integer |
| `fallback[].renewalPrice` | 100% | integer |
| `fallback[].renewalPriceMoney` | 100% | object |
| `fallback[].renewalPriceMoney.currency` | 100% | string |
| `fallback[].renewalPriceMoney.value` | 100% | integer |
| `fallback[].title` | 100% | string |
| `fallback[].trialDays` | 100% | integer |
| `plansBySpecialOffer` | 100% | object |
| `plansBySpecialOffer.pro_free_trial` | 100% | array |
| `plansBySpecialOffer.pro_free_trial[].baseInstitutionCampaign` | 100% | boolean |
| `plansBySpecialOffer.pro_free_trial[].description` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].hasTrial` | 100% | boolean |
| `plansBySpecialOffer.pro_free_trial[].id` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].periodMonths` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].price` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].priceMoney` | 100% | object |
| `plansBySpecialOffer.pro_free_trial[].priceMoney.currency` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].priceMoney.value` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].priceTiers` | 100% | array |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].fromSeats` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].price` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].priceMoney` | 100% | object |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].priceMoney.currency` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].priceMoney.value` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].priceTiers[].toSeats` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].regularPlanId` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].regularPrice` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].regularPriceMoney` | 100% | object |
| `plansBySpecialOffer.pro_free_trial[].regularPriceMoney.currency` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].regularPriceMoney.value` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].renewalPlanId` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].renewalPrice` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].renewalPriceMoney` | 100% | object |
| `plansBySpecialOffer.pro_free_trial[].renewalPriceMoney.currency` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].renewalPriceMoney.value` | 100% | integer |
| `plansBySpecialOffer.pro_free_trial[].title` | 100% | string |
| `plansBySpecialOffer.pro_free_trial[].trialDays` | 100% | integer |

**Response schema variants**

**Schema 1** `feefb4edf1` — 1 responses

```json
{
    "fallback": [
            {
                "baseInstitutionCampaign": boolean,
                "description": string,
                "hasTrial": boolean,
                "id": integer,
                "periodMonths": integer,
                "price": integer,
                "priceMoney": {
                                "currency": string,
                                "value": integer
                            },
                "regularPlanId": integer,
                "regularPrice": integer,
                "regularPriceMoney": {
                                "currency": string,
                                "value": integer
                            },
                "renewalPlanId": integer,
                "renewalPrice": integer,
                "renewalPriceMoney": {
                                "currency": string,
                                "value": integer
                            },
                "title": string,
                "trialDays": integer
            }
        ],
    "plansBySpecialOffer": {
            "pro_free_trial": [
                        {
                            "baseInstitutionCampaign": boolean,
                            "description": string,
                            "hasTrial": boolean,
                            "id": integer,
                            "periodMonths": integer,
                            "price": integer,
                            "priceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "regularPlanId": integer,
                            "regularPrice": integer,
                            "regularPriceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "renewalPlanId": integer,
                            "renewalPrice": integer,
                            "renewalPriceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "title": string,
                            "trialDays": integer
                        }
                        {
                            "baseInstitutionCampaign": boolean,
                            "description": string,
                            "hasTrial": boolean,
                            "id": integer,
                            "periodMonths": integer,
                            "price": integer,
                            "priceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "priceTiers": [
                                                {
                                                    "fromSeats": integer,
                                                    "price": integer,
                                                    "priceMoney": {
                                                                                "currency": string,
                                                                                "value": integer
                                                                            },
                                                    "toSeats": integer
                                                }
                                            ],
                            "regularPlanId": integer,
                            "regularPrice": integer,
                            "regularPriceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "renewalPlanId": integer,
                            "renewalPrice": integer,
                            "renewalPriceMoney": {
                                                "currency": string,
                                                "value": integer
                                            },
                            "title": string,
                            "trialDays": integer
                        }
                    ]
        }
}
```

---

### `gateway.grammarly.com/vito/special-offers`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `in_product_discount_pro` | 100% | object |
| `in_product_discount_pro.eligibility` | 100% | boolean |
| `pro_free_trial` | 100% | object |
| `pro_free_trial.eligibility` | 100% | boolean |

**Response schema variants**

**Schema 1** `14ea2f7167` — 1 responses

```json
{
    "in_product_discount_pro": {
            "eligibility": boolean
        },
    "pro_free_trial": {
            "eligibility": boolean
        }
}
```

---

### `go.grammarly.com/analytics`

**Observed methods:** `GET`
**Observed requests:** 2
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `goldengate.grammarly.com/institution/api/institution/admin/institution_info`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 1, 401: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (2)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `reason` | 100% | string |

**Response schema variants**

**Schema 1** `ef7c5c7658` — 1 responses

```json
{
    "reason": string
}
```

---

### `subscription.grammarly.com/api/v1/referrals/info`

**Observed methods:** `OPTIONS, POST`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `canReferUsersStatus` | 100% | string |
| `referralLink` | 100% | object |
| `referralLink.notEligibleReason` | 100% | string |

**Response schema variants**

**Schema 1** `ebfa8f4d87` — 1 responses

```json
{
    "canReferUsersStatus": string,
    "referralLink": {
            "notEligibleReason": string
        }
}
```

---

### `subscription.grammarly.com/api/v1/sku-type`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `skuType` | 100% | string |

**Response schema variants**

**Schema 1** `bc973d977e` — 1 responses

```json
{
    "skuType": string
}
```

---

### `subscription.grammarly.com/api/v2/support-portal/chatbot/token`

**Observed methods:** `OPTIONS, GET`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

**No request body was observed.**

#### Response

Content types: `text/plain` (1), `application/json` (1)

JSON responses: **1**

**Response field frequency**

| Field | Present | Type |
|---|---:|---|
| `token` | 100% | string |

**Response schema variants**

**Schema 1** `c14e4be8e3` — 1 responses

```json
{
    "token": string
}
```

---

### `website.femetrics.grammarly.io/batch/import`

**Observed methods:** `POST`
**Observed requests:** 2
**Response statuses:** 200: 2

#### Request

Content types: `text/plain` (2)

JSON requests: **2**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].labels` | 100% | array |
| `[].labels[].key` | 100% | string |
| `[].labels[].value` | 100% | string |
| `[].name` | 100% | string |
| `[].report_interval` | 100% | string |
| `[].type` | 100% | string |
| `[].value` | 100% | integer |

**Request schema variants**

**Schema 1** `ff5759dd77` — 2 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": integer
    }
]
```

#### Response

Content types: `text/plain` (2)

**No response body was observed.**

---

### `app.grammarly.com/`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/html` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f1fa-1f1f8.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f44b.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f44d.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f454.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f4a1.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f4ad.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f58a.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f5bc.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f607.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f60a.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f60c.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f60d.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f610.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f642.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f913.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f929.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/emoji/v1/1f92d.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-generate-ideas-category.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-improve.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 304: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-make-it-personal.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-make-it-professional.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-shorten.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/icons/v1/gds-icon-ggo-action-simplify.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/sdui/v1/magic-document.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/sdui/v1/star.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `assets.grammarly.com/sdui/v1/success-impression.2x.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `coda.grammarly.com/internalAppApi/doclist/recent`

**Observed methods:** `OPTIONS`
**Observed requests:** 1
**Response statuses:** 204: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `denali-static.grammarly.com/js/{token}/default-mp.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `denali-static.grammarly.com/js/{token}/runtime.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `denali-static.grammarly.com/js/{token}/vendor-e~ae~ci~cb~as~mp.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `editor.femetrics.grammarly.io/batch/import`

**Observed methods:** `POST`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

Content types: `text/plain` (1)

JSON requests: **1**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `[].labels` | 100% | array |
| `[].labels[].key` | 100% | string |
| `[].labels[].value` | 100% | string |
| `[].name` | 100% | string |
| `[].report_interval` | 100% | string |
| `[].type` | 100% | string |
| `[].value` | 100% | integer |

**Request schema variants**

**Schema 1** `ff5759dd77` — 1 requests

```json
[
    {
        "labels": [
                    {
                        "key": string,
                        "value": string
                    }
                ],
        "name": string,
        "report_interval": string,
        "type": string,
        "value": integer
    }
]
```

#### Response

Content types: `text/plain` (1)

**No response body was observed.**

---

### `gateway.grammarly.com/experimentation/treatment/log`

**Observed methods:** `POST`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

Content types: `application/json` (1)

JSON requests: **1**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `containerId` | 100% | string |
| `experimentId` | 100% | string |
| `experimentName` | 100% | string |
| `groupName` | 100% | string |
| `isTest` | 100% | boolean |
| `needLog` | 100% | boolean |
| `type` | 100% | string |
| `userId` | 100% | integer |

**Request schema variants**

**Schema 1** `ab9a6410fa` — 1 requests

```json
{
    "containerId": string,
    "experimentId": string,
    "experimentName": string,
    "groupName": string,
    "isTest": boolean,
    "needLog": boolean,
    "type": string,
    "userId": integer
}
```

#### Response

**No response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/16iyP4HxLGn8HRUVz73yxf/{token}/Frame_2055245639.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/4p0YxlEhKBkGTE3g1oX6Fh/{token}/square_image__1_.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/webp` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/5423x1zYeb1zyldyyUdYPI/{token}/ICONS__30_.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/5J6bEVGOrnZvAXNVfEwi2Q/{token}/ICONS__29_.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/67Dl0aecY6JEAJ61q42Iwh/{token}/Frame_2055245682.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/77xEyv3tvgGYDQjdo3vljv/{token}/ICONS__28_.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/1e6ajr2k4140/ltlKbGWebGgQGEVfOIszz/{token}/Frame_2055245684__1_.svg`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/8aa1SwZmUdTTBQ_xRC1J4/_buildManifest.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/8aa1SwZmUdTTBQ_xRC1J4/_ssgManifest.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/1a192442-332914e99bef1049.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/2581.0d6df08d5ee7c339.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/2810.2a82a60015e534cd.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/3234.be94bafbca8e422c.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/3446.2f43a1ffbde3f5c1.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/4902.96a5571238a2af78.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/4956.62e09d77974d2c0e.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/4957.262428f454a2402a.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/5082-f108c72735a88874.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/6497-0a8c419515b66d21.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/6e5e196e-66b1a94fba27f601.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/7248.435b716bf1f28dcf.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/7564.a57ed589727aa0c0.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/framework-9188fd1d264b3ab9.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/main-056f5034ee75ac0f.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/pages/_app-20531691b7ff54d1.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/pages/render-1df5ea362bf639f5.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/chunks/webpack-7717e9e0ed3d9bc6.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/11cd3a9b870d8cea.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/26ad7c2b7243e22c.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/27203ff1a31c1d3e.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/5182367ecb17ba61.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/66378a4254fb9db8.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/8f5d1d401fc71ea3.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/cms/master/_next/static/css/afeb416bd6ea3894.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/shared/fonts/glyph-bold.woff2`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `binary/octet-stream` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/shared/fonts/glyph-regular.woff2`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `binary/octet-stream` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/shared/fonts/matter-medium.woff2`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `binary/octet-stream` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/shared/fonts/matter-semi-bold.woff2`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `binary/octet-stream` (1)

**No JSON response body was observed.**

---

### `static-web.grammarly.com/web-heartbeat/latest/index.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `static.institution.grammarly.com/logo/ec8c59d1a4c7b0698cda682c3ee2f69ed3d7279d.png`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/api/v2/help_center/en-us/articles/{id}/stats/view.json`

**Observed methods:** `POST`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (1)

**No response body was observed.**

---

### `support.grammarly.com/api/v2/requests.json`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 401: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/json` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/activity`

**Observed methods:** `POST`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

Content types: `application/json` (1)

JSON requests: **1**

**Request field frequency**

| Field | Present | Type |
|---|---:|---|
| `data` | 100% | string |
| `event` | 100% | string |
| `referrer` | 100% | string |

**Request schema variants**

**Schema 1** `7765fff763` — 1 requests

```json
{
    "data": string,
    "event": string,
    "referrer": string
}
```

#### Response

Content types: `text/html` (1)

**No response body was observed.**

---

### `support.grammarly.com/hc/en-us/articles/4403227220237-Is-Grammarly-HIPAA-compliant`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/html` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT1YPZJP3VQJVC6HGA4M1`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `font/woff2` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT2FM04Y7K940XV55PJG6`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `font/woff2` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT2WSVN7PZTM4S8NXZHCZ`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/png` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT3GMDNWVQRD5AD6NPM0C`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT3R76SQ3MWB33MVEHJ51`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT3VKRH22X382D0MXNXSQ`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT43MV98QKSSQ85Y9M3AQ`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT4TV234GMK6HGHFMAXM8`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT67W142QH6S0VKSTREYR`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/vnd.microsoft.icon` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT684AW9802Y6VJF5J3EY`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `font/woff` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01HZAXT69TK9XZ8J984DXQZTG3`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `font/woff` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5RR5AS8XV9SKQP7FS6J1`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5S113PH9BW1TC1ZM25RP`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5S1JGTEZYXMBJ3CKBPHX`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5S85C2BQZK6X4ZVMCAV4`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5SEFXEG1EKJCJZ42AZQ4`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5SSANKF3GB4AFRB1XEGV`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5SZKJNZ5P7QT6FJPF69J`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5T6BS1EEED7WPY7JX62V`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01JYHF5T7D5ETZCN3WSSRGETHY`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `image/svg+xml` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01KB0826J1HQ60ESX1SHSSZ6DK`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/01KQZ04BZH071BEY5A1AYQ2HF0`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `application/javascript` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/{id}/{id}/script.js`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/javascript` (1)

**No JSON response body was observed.**

---

### `support.grammarly.com/hc/theming_assets/{id}/{id}/style.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `www.grammarly.com/`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 302: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `www.grammarly.com/api/tracking/load`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

**No response body was observed.**

---

### `www.grammarly.com/css/transcend-airgap.css`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/css` (1)

**No JSON response body was observed.**

---

### `www.grammarly.com/privacy`

**Observed methods:** `GET`
**Observed requests:** 1
**Response statuses:** 200: 1

#### Request

**No request body was observed.**

#### Response

Content types: `text/html` (1)

**No JSON response body was observed.**

---

## 5. Schema Index

| Endpoint | Direction | Schema | Occurrences |
|---|---|---|---:|
| `gateway.grammarly.com/experimentation/treatment/get` | Request | `76efce69de` | 377 |
| `gateway.grammarly.com/experimentation/treatment/get` | Response | `7ca95307b7` | 95 |
| `gnar.grammarly.com/lite` | Request | `f48224ca56` | 625 |
| `gnar.grammarly.com/lite` | Request | `79ccafa058` | 12 |
| `gnar.grammarly.com/lite` | Request | `637c6eff18` | 3 |
| `gnar.grammarly.com/lite` | Request | `b83b1fce39` | 2 |
| `inkwell.femetrics.grammarly.io/batch/import` | Request | `65f5461f02` | 299 |
| `inkwell.femetrics.grammarly.io/batch/import` | Request | `ff5759dd77` | 198 |
| `inkwell.femetrics.grammarly.io/batch/import` | Request | `b4707be24e` | 104 |
| `inkwell.femetrics.grammarly.io/batch/import` | Request | `ca0e2883a6` | 15 |
| `gnar.grammarly.com/events` | Request | `2b30ebc7e1` | 106 |
| `gnar.grammarly.com/events` | Request | `da3cb60dd8` | 76 |
| `gnar.grammarly.com/events` | Request | `544ab86f27` | 38 |
| `gnar.grammarly.com/events` | Request | `de242a34a1` | 29 |
| `gnar.grammarly.com/events` | Request | `a2912b1fb5` | 25 |
| `gnar.grammarly.com/events` | Request | `b50a6a611d` | 23 |
| `gnar.grammarly.com/events` | Request | `24e37fcc0d` | 18 |
| `gnar.grammarly.com/events` | Request | `19873b4fd3` | 18 |
| `gnar.grammarly.com/events` | Request | `9e598bd0fc` | 17 |
| `gnar.grammarly.com/events` | Request | `4ac78cec35` | 17 |
| `gnar.grammarly.com/events` | Request | `14fce36bb4` | 15 |
| `gnar.grammarly.com/events` | Request | `acb9bb6372` | 13 |
| `gnar.grammarly.com/events` | Request | `3a6f64749e` | 8 |
| `gnar.grammarly.com/events` | Request | `01cc4f6ccc` | 7 |
| `gnar.grammarly.com/events` | Request | `116eb2e3d2` | 7 |
| `gnar.grammarly.com/events` | Request | `884ffd3785` | 7 |
| `gnar.grammarly.com/events` | Request | `461770b56e` | 7 |
| `gnar.grammarly.com/events` | Request | `125163f5ac` | 6 |
| `gnar.grammarly.com/events` | Request | `dcf9aed7a1` | 6 |
| `gnar.grammarly.com/events` | Request | `1384e6d927` | 5 |
| `gnar.grammarly.com/events` | Request | `037cae7698` | 4 |
| `gnar.grammarly.com/events` | Request | `a95a494cf2` | 4 |
| `gnar.grammarly.com/events` | Request | `b7ecc2eece` | 4 |
| `gnar.grammarly.com/events` | Request | `7cdb8d5551` | 4 |
| `gnar.grammarly.com/events` | Request | `ed8daf57ea` | 4 |
| `gnar.grammarly.com/events` | Request | `e6468f0ef2` | 3 |
| `gnar.grammarly.com/events` | Request | `ba1696d8a9` | 3 |
| `gnar.grammarly.com/events` | Request | `54da35d171` | 2 |
| `gnar.grammarly.com/events` | Request | `fbb27d93f2` | 2 |
| `gnar.grammarly.com/events` | Request | `1e20b633bf` | 2 |
| `gnar.grammarly.com/events` | Request | `4ed57fa4ad` | 2 |
| `gnar.grammarly.com/events` | Request | `22ad33eca7` | 2 |
| `gnar.grammarly.com/events` | Request | `91d52965e5` | 2 |
| `gnar.grammarly.com/events` | Request | `97bfe46a68` | 2 |
| `gnar.grammarly.com/events` | Request | `724a3f398b` | 2 |
| `gnar.grammarly.com/events` | Request | `855aa05a78` | 2 |
| `gnar.grammarly.com/events` | Request | `4e9b0b3744` | 2 |
| `gnar.grammarly.com/events` | Request | `d8b687491f` | 1 |
| `gnar.grammarly.com/events` | Request | `d881c6f059` | 1 |
| `gnar.grammarly.com/events` | Request | `e1ed3495cf` | 1 |
| `gnar.grammarly.com/events` | Request | `92e9b32be4` | 1 |
| `gnar.grammarly.com/events` | Request | `6d6eefe165` | 1 |
| `gnar.grammarly.com/events` | Request | `4dc5aed4b9` | 1 |
| `gnar.grammarly.com/events` | Request | `28aedd2e02` | 1 |
| `gnar.grammarly.com/events` | Request | `b7d337e75a` | 1 |
| `gnar.grammarly.com/events` | Request | `1b2d63531a` | 1 |
| `gnar.grammarly.com/events` | Request | `9bd3102aac` | 1 |
| `gnar.grammarly.com/events` | Request | `a021c66751` | 1 |
| `gnar.grammarly.com/events` | Request | `e850d3b8a1` | 1 |
| `gnar.grammarly.com/events` | Request | `7dbfde59d3` | 1 |
| `gnar.grammarly.com/events` | Request | `8d6dbe9478` | 1 |
| `gnar.grammarly.com/events` | Request | `ca28bcd555` | 1 |
| `gnar.grammarly.com/events` | Request | `10552af7d7` | 1 |
| `gnar.grammarly.com/events` | Request | `9c729cfbb8` | 1 |
| `gnar.grammarly.com/events` | Request | `beae897c5b` | 1 |
| `gnar.grammarly.com/events` | Request | `b7078f96fa` | 1 |
| `gnar.grammarly.com/events` | Request | `4b6d0d3995` | 1 |
| `gnar.grammarly.com/events` | Request | `9dc42e6dad` | 1 |
| `gnar.grammarly.com/events` | Request | `1d840bffd6` | 1 |
| `gnar.grammarly.com/events` | Request | `366418f413` | 1 |
| `gnar.grammarly.com/events` | Request | `e64ca43c18` | 1 |
| `gnar.grammarly.com/events` | Request | `52c178bdf4` | 1 |
| `gnar.grammarly.com/events` | Request | `e1c5d136b8` | 1 |
| `gnar.grammarly.com/events` | Request | `7c81b74f18` | 1 |
| `gnar.grammarly.com/events` | Request | `56c0dd671b` | 1 |
| `gnar.grammarly.com/events` | Request | `b2199fe902` | 1 |
| `gnar.grammarly.com/events` | Request | `e94c56cabe` | 1 |
| `gnar.grammarly.com/events` | Request | `da2ad51523` | 1 |
| `in.grammarly.com/v1/events` | Request | `60a3acc723` | 147 |
| `in.grammarly.com/v1/events` | Request | `6296f341fd` | 89 |
| `in.grammarly.com/v1/events` | Request | `217d389263` | 70 |
| `in.grammarly.com/v1/events` | Request | `3e412a781a` | 36 |
| `in.grammarly.com/v1/events` | Request | `33e3b6d359` | 25 |
| `in.grammarly.com/v1/events` | Request | `0f333e64ce` | 22 |
| `in.grammarly.com/v1/events` | Request | `8bf6b599ea` | 9 |
| `in.grammarly.com/v1/events` | Request | `b70be6b4ba` | 2 |
| `in.grammarly.com/v1/events` | Request | `6905dadbd1` | 2 |
| `in.grammarly.com/v1/events` | Request | `d83b33bff5` | 1 |
| `gateway.grammarly.com/experimentation/gates/get` | Request | `76efce69de` | 113 |
| `gateway.grammarly.com/experimentation/gates/get` | Response | `94b9dfff31` | 95 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `05907afe7b` | 17 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `fee07c5a9f` | 9 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `3de7b9b1c1` | 8 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `829e7779fb` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `8610c67ee4` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `8c34a45423` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `2d67411138` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `017e506cac` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `cbfc0c8807` | 2 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `ca2c92ffe5` | 1 |
| `f-log-inkwell.grammarly.io/batch/log` | Request | `46e37f3804` | 1 |
| `in.grammarly.com/v1/events/ingestion_front_end` | Request | `0cb227abc0` | 43 |
| `in.grammarly.com/v1/events/ingestion_front_end` | Request | `ecbae03459` | 35 |
| `in.grammarly.com/v1/events/ingestion_front_end` | Request | `aff4ea58ca` | 2 |
| `auth.grammarly.com/auth/v5/api/userinfo` | Response | `a8b133f77a` | 4 |
| `capi.grammarly.com/api/configuration/cheetah/v1/settings` | Response | `87f058b371` | 17 |
| `f-log-assistant.grammarly.io/log` | Request | `987f4ebb23` | 19 |
| `f-log-assistant.grammarly.io/log` | Request | `9552777a35` | 12 |
| `f-log-assistant.grammarly.io/log` | Request | `f8f3253f30` | 12 |
| `f-log-assistant.grammarly.io/log` | Request | `9dcd419084` | 7 |
| `assistant.femetrics.grammarly.io/batch/import` | Request | `0f79d7ca09` | 41 |
| `assistant.femetrics.grammarly.io/batch/import` | Request | `0df7b068da` | 1 |
| `auth.grammarly.com/tokens/v4/api/oauth2/token` | Request | `f9f6667576` | 24 |
| `auth.grammarly.com/tokens/v4/api/oauth2/token` | Response | `440623cc1a` | 24 |
| `f-log-editor.grammarly.io/logv2` | Request | `283811d49b` | 4 |
| `f-log-editor.grammarly.io/logv2` | Request | `415503290e` | 1 |
| `f-log-editor.grammarly.io/logv2` | Request | `57c3f45b4d` | 1 |
| `f-log-editor.grammarly.io/logv2` | Request | `d1e21e66a8` | 1 |
| `f-log-editor.grammarly.io/logv2` | Request | `d2e0f98068` | 1 |
| `f-log-editor.grammarly.io/logv2` | Request | `90ac015bae` | 1 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `86c762e8c9` | 4 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `aba6b714d7` | 3 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `4c55b1c476` | 2 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `29e5d769cd` | 2 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `7276bf73d6` | 2 |
| `f-log-win-extension.grammarly.io/logv2` | Request | `e9354e3cf7` | 1 |
| `gateway.grammarly.com/passport/api/v1/passport` | Response | `b8939e0ce3` | 6 |
| `gateway.grammarly.com/passport/api/v1/passport` | Response | `e8abfdccf2` | 5 |
| `gateway.grammarly.com/uhub/configuration` | Response | `29c30933fb` | 9 |
| `gateway.grammarly.com/uhub/configuration` | Response | `c086eec686` | 1 |
| `treatment.grammarly.com/treatment/get` | Request | `76efce69de` | 9 |
| `treatment.grammarly.com/treatment/get` | Response | `94b9dfff31` | 9 |
| `update-windows.grammarly.com/update/llamaWindows` | Request | `00c9e0d787` | 9 |
| `update-windows.grammarly.com/update/llamaWindows` | Response | `cff8d57e78` | 9 |
| `gateway.grammarly.com/experimentation/properties` | Request | `d6a28da59a` | 1 |
| `gateway.grammarly.com/experimentation/properties` | Request | `d35f7dfad4` | 1 |
| `gateway.grammarly.com/experimentation/properties` | Response | `c6f0be0b0a` | 2 |
| `subscription.grammarly.com/api/v1/subscription` | Response | `48d18ea436` | 3 |
| `auth.grammarly.com/auth/v3/user/bridge/check-eligibility/coda` | Response | `01a34c673e` | 1 |
| `capi.grammarly.com/api/configuration/suggestion-bundles/v1/settings` | Response | `8f808a6b5f` | 2 |
| `f-log-editor-debug.grammarly.io/logv2` | Request | `8650ee17c5` | 1 |
| `gateway.grammarly.com/experimentation/properties/showDesktopIntegrationExtensionToggle` | Response | `a5b031ab62` | 2 |
| `gateway.grammarly.com/health` | Response | `057dbc6d9b` | 2 |
| `gateway.grammarly.com/mise/api/v1/iterable/access/token` | Response | `8df505cf2b` | 2 |
| `gateway.grammarly.com/privacy/v1/api/data-sharing/user` | Response | `9c53bc262d` | 2 |
| `gateway.grammarly.com/subscription/api/v1/subscription` | Response | `48d18ea436` | 1 |
| `gateway.grammarly.com/subscription/api/v2/support-portal/userInfo` | Response | `7bc6231a4a` | 1 |
| `gateway.grammarly.com/uhub/events` | Request | `ef60aa06d8` | 1 |
| `gateway.grammarly.com/vito/plans` | Response | `feefb4edf1` | 1 |
| `gateway.grammarly.com/vito/special-offers` | Response | `14ea2f7167` | 1 |
| `goldengate.grammarly.com/institution/api/institution/admin/institution_info` | Response | `ef7c5c7658` | 1 |
| `subscription.grammarly.com/api/v1/referrals/info` | Response | `ebfa8f4d87` | 1 |
| `subscription.grammarly.com/api/v1/sku-type` | Response | `bc973d977e` | 1 |
| `subscription.grammarly.com/api/v2/support-portal/chatbot/token` | Response | `c14e4be8e3` | 1 |
| `website.femetrics.grammarly.io/batch/import` | Request | `ff5759dd77` | 2 |
| `editor.femetrics.grammarly.io/batch/import` | Request | `ff5759dd77` | 1 |
| `gateway.grammarly.com/experimentation/treatment/log` | Request | `ab9a6410fa` | 1 |
| `support.grammarly.com/hc/activity` | Request | `7765fff763` | 1 |

---

## 6. Interpretation Notes

- Field percentages represent how often a field was observed among JSON messages for that endpoint.
- A field observed in approximately 100% of messages is treated as consistently present in the capture.
- Multiple schema fingerprints indicate structurally different JSON messages were observed for the same endpoint.
- Dynamic URL path components such as numeric IDs and UUIDs are normalized when constructing endpoint identities.
- JSON values are not included; only their observed structure and primitive types are reported.

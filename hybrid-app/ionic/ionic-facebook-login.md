# IonicでFacebook Login
## API
- [Permissions Reference](https://developers.facebook.com/docs/facebook-login/permissions#reference-user_about_me)

## 【フロント】ngCordova 使い方

### login
``` $cordovaFacebook.login(["public_profile","email"])
{"status":"connected",
"authResponse":
	{"secret":"...",
	"session_key":true,
	"sig":"...",
	"accessToken":"CAAXzPsDdIacBAByA0vaZA07hkozJEhAhIGVFxCh875A7htxyNZBvdwZB8HQHWu63nS2cXY4vviNSHZAQ9TQOoIuyDnuVbaMlCoVNZCSdKhawNXHuaUPZAWdnKIgGndw5MyCielSHk6wZCVSRC5ta4s6ue61zvUZCupnfLO00qZBZAFurm5CyJ8TPq1XMxQXF9W0XQxkQDjyTm2bHFwa3X6ZCv4PZCx4GN3DAb2tTkuP1XAWDcUQc4EUKZCGsqhDzm8oZBaZAKmxdNZA96yRWXwZDZD",
	"userID":"943100449105995",
	"expiresIn":"5183199"}
}

```
- logout状態⇒errorCB

### api

``` $cordovaFacebook.api("me")
{"name":"Tomokatsu Iguchi","id":"943100449105995"}
```
- logout状態⇒errorCB The operation couldn’t be completed. (com.facebook.sdk error 5.)

### getLoginStatus

``` $cordovaFacebook.getLoginStatus()
{"status":"connected",
"authResponse":
	{"secret":"...",
	"session_key":true,
	"sig":"...",
	"accessToken":"CAAXzPsDdIacBAByA0vaZA07hkozJEhAhIGVFxCh875A7htxyNZBvdwZB8HQHWu63nS2cXY4vviNSHZAQ9TQOoIuyDnuVbaMlCoVNZCSdKhawNXHuaUPZAWdnKIgGndw5MyCielSHk6wZCVSRC5ta4s6ue61zvUZCupnfLO00qZBZAFurm5CyJ8TPq1XMxQXF9W0XQxkQDjyTm2bHFwa3X6ZCv4PZCx4GN3DAb2tTkuP1XAWDcUQc4EUKZCGsqhDzm8oZBaZAKmxdNZA96yRWXwZDZD",
	"userID":"943100449105995",
	"expiresIn":"5183199"}
}

```
- logout状態⇒successCB
{"status":"unknown"}

### getAccessToken

``` $cordovaFacebook.getAccessToken()
"CAAXzPsDdIacBAByA0vaZA07hkozJEhAhIGVFxCh875A7htxyNZBvdwZB8HQHWu63nS2cXY4vviNSHZAQ9TQOoIuyDnuVbaMlCoVNZCSdKhawNXHuaUPZAWdnKIgGndw5MyCielSHk6wZCVSRC5ta4s6ue61zvUZCupnfLO00qZBZAFurm5CyJ8TPq1XMxQXF9W0XQxkQDjyTm2bHFwa3X6ZCv4PZCx4GN3DAb2tTkuP1XAWDcUQc4EUKZCGsqhDzm8oZBaZAKmxdNZA96yRWXwZDZD"
```
- errorCB⇒Session not open.
### logout

``` $cordovaFacebook.logout()
null
```
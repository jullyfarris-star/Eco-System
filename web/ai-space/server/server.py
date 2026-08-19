@@
-    url = f"{base}/web/ai-space/index.html?session={new_session}&token={new_token}"
-    return {"session": new_session, "token": new_token, "url": url}
+    # Return URL WITHOUT token embedded for safer sharing; token is returned in response but should be kept private.
+    url_no_token = f"{base}/web/ai-space/index.html?session={new_session}"
+    return {"session": new_session, "token": new_token, "url": url_no_token, "note": "Do not share token publicly; provide it via private channel."}

const express = require("express"),
      bodyParser = require("body-parser"),
      path = require("path"),
      webpush = require("web-push");

const vapidKeys = webpush.generateVAPIDKeys(),
      port = 1234,
      mail = "test",
      publicKey = "BOyJlSgMcj43C3go0n-BX3IyUkofL0IxwXVyWiThfOAEwFPdcRKBXz0-BxYpCMagRoaPzuOemscJMYsrqObQz-g",
      privateKey = "i3uwXy6jyoAKl4IegtUTABokDzqDiiPE1dJKE1lKIi8";

webpush.setVapidDetails("mailto:" + mail, publicKey, privateKey);
const app = express();
app.use(express.static(__dirname));
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "/index.html"));
});

app.post("/sendpush", (req, res) => {
  res.status(201).json({});
  webpush.sendNotification(req.body, JSON.stringify({
    title: "Notification",
    body: "Text"
  }))
  .catch((err) => { console.log(err); });
});

app.listen(port, () => {
  console.log(`Listening on ${port}`)
});
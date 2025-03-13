from flask import Flask, request, send_file, render_template, redirect, url_for
from threading import Thread
import time, requests, io
import resend

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
# Example code

app = Flask(__name__, template_folder="templates")

@app.route('/about/')
def about():
    return f'About'

@app.route("/")
def secret_():
    response = requests.get("https://uploads.scratch.mit.edu/get_image/project/1016006035_480x360.png")
    file = io.BytesIO(response.content)
    resp = send_file(
        file,
        mimetype='image/gif'
    )
    resp.headers["Origin"] = "https://scratch.mit.edu/projects/1016006035"
    resp.set_cookie("been_there", "1")
    return resp

@app.route("/super_secret_url/")
def secret_again():
    response = requests.get("https://uploads.scratch.mit.edu/get_image/project/1016006035_480x360.png")
    file = io.BytesIO(response.content)
    resp = send_file(
        file,
        mimetype='image/gif'
    )
    resp.headers["Origin"] = "Not Origin, look elsewhere"
    resp.set_cookie("elsewhere", "Wow! You are good. Comment \"What the origin???\" on @TheCommCraft on Scratch to find the next clue.")
    return resp

@app.route("/elsewhere/")
def secret_again_again():
    response = requests.get("https://uploads.scratch.mit.edu/get_image/project/1016006035_480x360.png")
    file = io.BytesIO(response.content)
    resp = send_file(
        file,
        mimetype='image/gif'
    )
    resp.headers["Origin"] = "Nah."
    resp.set_cookie("too_clever", "1")
    return resp

@app.route("/keep_alive/")
def keep_alive():
    response = requests.get(request.args.get("url") or 'https://abrupt-imaginary-text.glitch.me/hello', headers=headers)
    return "probably alive"

@app.errorhandler(404)
def page_not_found(e):
    response = requests.get("https://uploads.scratch.mit.edu/get_image/project/1016006035_480x360.png")
    file = io.BytesIO(response.content)
    resp = send_file(
        file,
        mimetype='image/gif'
    )
    resp.headers["Origin"] = "Wrong page."
    return resp

@app.get("/hehe/")
def hehe():
    return ""

@app.route("/send_email/", methods=["GET", "POST"])
def email():
    if request.args.get("apikey"):
        response = redirect(url_for(email))
        response.set_cookie("apikey", request.args.get("apikey"))
        return response
    if request.method == "POST":
        resend.api_key = request.cookies.get("apikey", "")
        html = request.form.get("htmlcontent", "")
        subject = request.form.get("subject", "")
        sender = request.form.get("sender", "")
        receiver = request.form.get("receiver", "")
        params: resend.Emails.SendParams = {
           "from": sender,
           "to": [i.strip() for i in receiver.split(",")],
           "subject": subject,
           "html": html,
        }

        email = resend.Emails.send(params)
    return render_template("send_email.html")
#

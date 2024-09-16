from flask import Flask, request, abort

app = Flask(__name__)

# BANK side like SBI,HDFC bank (it act like server side, which will return response to webhook.py)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        print('123loki')
        abort(400)

if __name__ == '__main__':
    app.run()

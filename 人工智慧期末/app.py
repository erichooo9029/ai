from flask import Flask, request, abort
import os
from service.Clawer import ticketInfo,imageInfo,exchangeRate,fruitPrice,getHtmlImgUrl,getSebUrl,getCk101Url,getCk101Photo,takeDigCurrency,takeUsdtPremium

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('tUOMzUCySGCu/oltCkP1RQxrgdrleT3rwV8XfXhJu2IzdthwsY440T8EMTXelG1b1NX2SH2OsamNOv+DzmDv2Iov7/uWUGpkxIJyg++EN7e5mJY25rhGAQ4z+w1gherHeOELjOYDihZ2/Tfrsr1GngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a05fbef12228323c5168e8f965e7c49d')



# 監聽所有來自 /callback 的 Post Request
@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print('on Call' + event.message.text)

    if 'https://www.instagram.com' in event.message.text:
        # 返回含圖片Message
        imageUrl = ''
        imageUrl += imageInfo(event.message.text)

        if imageUrl != '':
            message = ImageSendMessage(
                original_content_url=imageUrl,
                preview_image_url=imageUrl
            )
            line_bot_api.reply_message(
                event.reply_token,
                message)
    if '!妹子' in event.message.text:
        imageBase = getCk101Url('https://ck101.com/beauty/')
        imageUrl = getCk101Photo(imageBase)
        print('imageUrl' + imageUrl)
        if imageUrl != '':
            message = ImageSendMessage(
                original_content_url=imageUrl,
                preview_image_url=imageUrl
            )
            textMessage = TextSendMessage(text=imageBase)
            listMessage = [message,textMessage]

            line_bot_api.reply_message(
                event.reply_token,
                listMessage)

    else:
        
        # 返回純文字Message
        outInfo = ''
        if '!新聞' in event.message.text:
            outInfo += googlesearchnews()
        if '!機票' in event.message.text:
            outInfo += ticketInfo()

        if '！機票' in event.message.text:
            outInfo += ticketInfo()

        if '!日幣' in event.message.text:
            outInfo += exchangeRate("JPY")

        if '！日幣' in event.message.text:
            outInfo += exchangeRate("JPY")

        if '!美金' in event.message.text:
            outInfo += exchangeRate("USD")

        if '！美金' in event.message.text:
            outInfo += exchangeRate("USD")

        if '!人民幣' in event.message.text:
            outInfo += exchangeRate("CNY")

        if '！人民幣' in event.message.text:
            outInfo += exchangeRate("CNY")

        if '!歐元' in event.message.text:
            outInfo += exchangeRate("EUR")

        if '！歐元' in event.message.text:
            outInfo += exchangeRate("EUR")

        if '!英鎊' in event.message.text:
            outInfo += exchangeRate("GBP")

        if '！英鎊' in event.message.text:
            outInfo += exchangeRate("GBP")

        if '!USDT' in event.message.text:
            outInfo += takeDigCurrency('usdttwd')

        if '！USDT' in event.message.text:
            outInfo += takeDigCurrency('usdttwd')

        # if '!妹子' in event.message.text:
        #     outInfo += getHtmlImgUrl(getSebUrl('https://www.mzitu.com/'))

        if '!奶子' in event.message.text:
            outInfo += getHtmlImgUrl(getSebUrl('https://www.mzitu.com/tag/baoru/'))

        if '！奶子' in event.message.text:
            outInfo += getHtmlImgUrl(getSebUrl('https://www.mzitu.com/tag/baoru/'))

        if '!火龍果' in event.message.text:
            outInfo += fruitPrice("812/%E7%81%AB%E9%BE%8D%E6%9E%9C-%E7%B4%85%E8%82%89(%E7%B4%85%E9%BE%8D%E6%9E%9C")

        if '！火龍果' in event.message.text:
            outInfo += fruitPrice("812/%E7%81%AB%E9%BE%8D%E6%9E%9C-%E7%B4%85%E8%82%89(%E7%B4%85%E9%BE%8D%E6%9E%9C")

        if '!芒果' in event.message.text:
            outInfo += fruitPrice("R6/芒果-金煌")

        if '！芒果' in event.message.text:
            outInfo += fruitPrice("R6/芒果-金煌")

        if '!U溢價' in event.message.text:
            outInfo += takeUsdtPremium(event.message.text)

        print('outInfo:' + outInfo)

        if outInfo != '':
            message = TextSendMessage(text=outInfo)
            line_bot_api.reply_message(
                event.reply_token,
                message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

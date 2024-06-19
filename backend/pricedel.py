# 가격정보 리스트 삭제

from telegram import Update
from telegram.ext import ContextTypes
import asyncio

async def pricedel(update: Update, context: ContextTypes.DEFAULT_TYPE, price_list: list):
    args = context.args
    if args:
        coin = args[0]
        if coin in price_list:
            price_list.remove(coin)
            await update.message.reply_text(f'{coin} 코인을 리스트에서 삭제하였습니다.')
        else:
            await update.message.reply_text(f'{coin} 코인은 리스트에 없습니다.')

        if price_list:
            await asyncio.sleep(2)
            await update.message.reply_text(f'현재 코인 확인 리스트:\n- ' + '\n- '.join(price_list))
    else:
        await update.message.reply_text('삭제할 코인의 코드를 입력하세요.')

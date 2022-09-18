import os
import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from requests.adapters import HTTPAdapter, Retry

from core.models import Stock, StockInfo

logger = get_task_logger(__name__)

API_KEY = os.getenv('API_KEY', None)

@shared_task
def get_stock_info():

    if not API_KEY:
        logger.info("Error: API Key not provided")
        return None

    session = requests.Session()
    retries = Retry(total=3,
                    backoff_factor=1,
                    allowed_methods=["GET"])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    stocks = Stock.objects.all()
    for stock in stocks:
        # endpoint = f'http://api.marketstack.com/v1/eod?access_key={API_KEY}&symbol={stock.symbol}&limit=1'
        endpoint = 'http://api.marketstack.com/v1/eod?access_key=fe3fe42d89f1d5e93ecab6f8794cb2a6&symbols=AAPL&limit=1'
        response = session.get(endpoint).json()
        data_list =  response.get('data', None)
        if data_list:
            data = data_list[0]
            StockInfo.objects.create(stock=stock,
                                     open_value=data.get('open'),
                                     close_value=data.get('close'),
                                     high_value=data.get('high'),
                                     low_value=data.get('low'),
                                     dividend=data.get('dividend'),
                                     adjust_open_value=data.get('adj_open'),
                                     adjust_close_value=data.get('adj_close'),
                                     adjust_high_value=data.get('adj_high'),
                                     adjust_low_value=data.get('adj_low')
                                     )
    logger.info("Task concluded successfuly!")

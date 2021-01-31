import requests
import singer

LOGGER = singer.get_logger()

class EstocaClient():

    def __init__(self, config):
        self.config = config
        # define URL for this endpoint
        url = "/".join([self.config['api_url']])
        # define request parameters
        params = {'storeID':storeID,'startDate': startDate,'endDate': endDate,'columns':columns,'api_key':api_key}

    def get_orders(self,start_date,end_date):
        api_data = []           
        LOGGER.info("Start Date: {0}, Finish Date: {1}".format(start_date,end_date))
        response = [1]
        # iterate through VNDA pages
        while response:
            params['page'] = page
            # TODO : Handle errors
            req = requests.get(url=url, params=params, headers=self.headers)
            response = req.json()
            LOGGER.info("Page requested: {}".format(page))
            api_data.extend(req.json())
            page = page + 1

        return api_data


import requests
import singer

LOGGER = singer.get_logger()

class EstocaClient():

    def __init__(self, config):
        self.config = config
       
    def get_orders(self,startDate,endDate):
        
        columns = {
            "id",
            "created_at",
            "customer_full_address",
            "customer_name",
            "delivery_full_address",
            "delivery_name",
            "erp_marketplace_id",
            "external_id",
            "handoff_finished_at",
            "handoff_idle_time",
            "has_extra_packaging",
            "holded_at",
            "human_id",
            "invoice_access_key",
            "invoice_number",
            "invoice_serie",
            "is_manual_order",
            "is_quarantine",
            "is_same_day_delivery",
            "marketplace_name",
            "operator_name",
            "order_price",
            "packing_finished_at",
            "packing_idle_time",
            "packing_packer_name",
            "packing_started_at",
            "packing_total_time",
            "picking_finished_at",
            "picking_idle_time",
            "picking_picker_name",
            "picking_started_at",
            "picking_total_time",
            "quarantine_comment",
            "service_name",
            "status",
            "store_id",
            "store_name",
            "total_items",
            "total_skus",
            "transporter",
            "updated_at",
            "warehouse_name"
        }

        apiurl = "https://plataforma.estoca.com.br/devtools/data_connector/get_data"
         # define URL for this endpoint
        LOGGER.info(apiurl)
        url = apiurl
        LOGGER.info(url)
       
        # define request parameters
        params = dict()
        params ["storeID"] = "2c25c5a9-f5a4-4e8a-9e49-9bad1359bfc0"
        params ["columns"] = columns
        params ["startDate"] = "20200203"
        params ["endDate"] = "20200204"
        params ["api_key"] = "0af09adc-139c-11eb-9921-38f9d361ecb6"
        
                
        startDate = "20200203"
        endDate = "20200204"
        api_data = []           
        LOGGER.info("Start Date: {0}, Finish Date: {1}".format(startDate,endDate))
        req = requests.get(url=url, params=params)
        response = req.json()
        LOGGER.info(response)
        api_data.extend(req.json())
       
        return api_data
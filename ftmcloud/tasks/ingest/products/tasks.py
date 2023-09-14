from ftmcloud.core.crosscutting.models.tasks.tasks import BaseTask


class ProductImportTask(BaseTask):
    """
    Ingests many products into MongoDB.
    """

    def __init__(self):
        super().__init__(name="product_import", exchange_name="", queue="", routing_key="")

    def handle_message(self, body, message):
        print("Hello world!")
        pass

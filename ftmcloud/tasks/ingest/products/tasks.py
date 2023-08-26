from ftmcloud.core.crosscutting.models.tasks import BaseTask


class ProductImportTask(BaseTask):
    """
    Ingests many products into MongoDB.
    """

    def __init__(self):
        super().__init__()

from ma import ma

from models.item import ItemModel
from models.store import StoreModel
from schemas.item import ItemSchema


class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = StoreModel
        dump_only = ("id",)
        load_instance = True
        include_fk = True

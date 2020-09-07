from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta:
        dump_only = ("id",)
        load_only = ("password",)

    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)

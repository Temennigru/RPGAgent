from .entity import CampaignEntity

class Item(CampaignEntity):
    def __init__(self, name, description, effects, value, history, ownership, related_entities=None, tags=None):
        super().__init__(name, description, related_entities, tags)
        self.effects = effects
        self.value = value
        self.history = history
        self.ownership = ownership

    def __str__(self):
        return f"{super().__str__()} [Value: {self.value}, Owned by: {self.ownership}]"

    def to_schema(self):
        schema = super().to_schema()
        schema.update({
            "effects": self.effects,
            "value": self.value,
            "history": self.history,
            "ownership": self.ownership
        })
        return schema

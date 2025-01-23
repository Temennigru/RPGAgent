from .entity import CampaignEntity

class Location(CampaignEntity):
    def __init__(self, name, description, features, climate, history, significance, related_entities=None, tags=None):
        super().__init__(name, description, related_entities, tags)
        self.features = features
        self.climate = climate
        self.history = history
        self.significance = significance

    def __str__(self):
        return f"{super().__str__()} [Coordinates: {self.coordinates}, Significance: {self.significance}]"

    def to_schema(self):
        schema = super().to_schema()
        schema.update({
            "features": self.features,
            "climate": self.climate,
            "history": self.history,
            "significance": self.significance
        })
        return schema
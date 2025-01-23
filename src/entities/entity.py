class CampaignEntity:
    def __init__(self, name, description, related_entities=None, tags=None):
        """
        Initialize a generic entity for an RPG campaign.
        
        Args:
        name (str): The name of the entity.
        description (str): A brief description of the entity.
        tags (list of str, optional): Tags to categorize the entity. Defaults to None.
        """
        self.name = name
        self.description = description
        self.related_entities = related_entities if related_entities else []
        self.tags = tags if tags else []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_tag(self, tag):
        """
        Add a tag to the entity to help categorize it.

        Args:
        tag (str): The tag to add.
        """
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        """
        Remove a tag from the entity.

        Args:
        tag (str): The tag to remove.
        """
        if tag in self.tags:
            self.tags.remove(tag)

    def to_schema(self):
        """
        Returns a dictionary that represents the schema of the entity for an LLM.

        Returns:
        dict: A dictionary with structured key-value pairs representing the entity.
        """
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags
        }

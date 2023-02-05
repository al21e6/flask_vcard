from typing import Optional
from flask import Flask


class VCard:
    """A flask VCard extension.

    Attributes:
        app: The flask application.
    """

    def __init__(self, app: Optional[Flask] = None):
        self.app = app        
        self.first_name = ""
        self.last_name = ""
        self.description = ""
        self.website = ""
        self.street = ""
        self.city = ""
        self.state = ""
        self.postcode = ""
        self.country = ""
        self.telephone = ""
        self.email = ""
        if app is not None:
            self.init_app(app)

    def __repr__(self) -> str:
        v_card = f"""
            BEGIN:VCARD
            N:{self.last_name};{self.first_name};
            ORG:{self.description};
            URL:{self.website};
            ADR:{self.street};{self.city};{self.state};{self.postcode};{self.country};
            TEL:{self.telephone}
            EMAIL:{self.email}
            END:VCARD
        """
        v_card = v_card.strip().replace(" ", "")
        return v_card

    def init_app(self, app: Flask):
        self.first_name = app.config.get("VCARD_FIRST_NAME", "")
        self.last_name = app.config.get("VCARD_LAST_NAME", "")
        self.description = app.config.get("VCARD_DESCRIPTION", "")
        self.website = app.config.get("VCARD_WEBSITE", "")
        self.street = app.config.get("VCARD_STREET", "")
        self.city = app.config.get("VCARD_CITY", "")
        self.state = app.config.get("VCARD_STATE", "")
        self.postcode = app.config.get("VCARD_POSTCODE", "")
        self.country = app.config.get("VCARD_COUNTRY", "")
        self.telephone = app.config.get("VCARD_TELEPHONE", "")
        self.email = app.config.get("VCARD_EMAIL", "")

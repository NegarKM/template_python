import os
from typing import Any, Dict

import api_service

SWAGGER_CONFIG: Dict[str, Any] = {
    "title": "Sample API",
    "uiversion": 3,
    "doc_dir": f"{os.path.dirname(api_service.__file__)}/swagger/",
    "specs_route": "/api/swagger/",
    "specs": [{"endpoint": "specifications", "route": "/api/specifications.json"}],
    "static_url_path": "/api/flasgger_static",
    "description": "---",
}

SWAGGER_TEMPLATE: Dict[str, Any] = {
    "securityDefinitions": {
        # "basic": {"type": "basic", "in": "header", "name": "Authorization"},
        "bearer": {
            "type": "API Key",
            "in": "header",
            "name": "Authentication",
            "description": "---",
        },
    }
}

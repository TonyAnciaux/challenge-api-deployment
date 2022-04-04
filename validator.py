schema = {
        "area": {"type": "integer", "min": 10, "required": True},
        "property-type": {"type": "string", "allowed": ['apartment', 'bungalow', 'chalet', 'duplex', 'ground-floor',
                                                        'loft', 'mansion', 'master-house', 'mixed-building',
                                                        'penthouse', 'residence', 'studio', 'triplex', 'villa'],
                          "required": True},
        "bedrooms-number": {"type": "integer", "required": True},
        "zip-code": {"type": "integer", "min": 1000, "max": 9999, "required": True},
        "garden-area": {"type": "integer"},
        "kitchen": {"type": "string", "allowed": ["Not equipped", "Partially equipped", "Fully equipped",
                                                  "Super equipped"]},
        "balcony": {"type": "boolean"},
        "terrace-area": {"type": "integer"},
        "facades-number": {"type": "integer"},
        "building-state": {"type": "string", "allowed": ['To be renovated', 'Normal', 'Excellent', 'Fully renovated',
                                                         'New']},
        "garage": {"type": "boolean"}
        }

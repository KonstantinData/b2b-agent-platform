def run(company_name, company_url, region, mapping_table):
    # TODO: implement real research (public sources) + English translation
    return {
        "company": {
            "name": company_name,
            "url": company_url,
            "legal_form": None,
            "address": None,
            "vat_id": None,
            "founded": None
        },
        "contacts": [
            # {"name":"Jane Doe","role":"CEO","linkedin":"...","email":null}
        ],
        "business_units": [
            # {"name":"Drives","wz2008":"27.11","nace":"27.11","oenace":"27.11","desc":"Electric motors"}
        ],
        "classifications": [
            # {"wz2008":"27.11","nace":"27.11","oenace":"27.11","desc":"Electric motors"}
        ],
        "reports": [
            # {"title":"Annual Report 2024","url":"...","year":2024}
        ],
        "economics": [
            # {"bu":"Drives","trend":"stable","challenges":"supply chain","opportunities":"aftermarket"}
        ],
        "language": "EN"
    }

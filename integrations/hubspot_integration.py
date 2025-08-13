import os
from hubspot import HubSpot

def _client():
    token = os.getenv("HUBSPOT_API_KEY")
    if not token:
        raise RuntimeError("HUBSPOT_API_KEY not set")
    return HubSpot(access_token=token)

def _build_company_props(company):
    # Adjust mapping to your HubSpot properties (create custom fields as needed)
    return {
        "name": company.get("name"),
        "domain": company.get("url"),
    }

def upsert_company_pack(company_pack):
    api = _client()
    company = company_pack.get("company", {})
    props = _build_company_props(company)
    # Minimal create (replace with proper search + update if exists)
    api.crm.companies.basic_api.create({"properties": props})

def upsert_contacts_pack(company_pack):
    # Iterate contacts, create/update similarly; placeholder
    return

import argparse, json, os, pathlib
from datetime import datetime

from agents.agent1_company_research import run as run_agent1
from agents.agent2_competitor_search import run as run_agent2
from agents.agent3_buyer_identification import run as run_agent3
from agents.mapping_update import run as run_mapping_update
from integrations.hubspot_integration import upsert_company_pack, upsert_contacts_pack
from integrations.pdf_report import build_pdf

OUTDIR = pathlib.Path("data/outputs"); OUTDIR.mkdir(parents=True, exist_ok=True)
MASTER = pathlib.Path("data/master_list.json"); MASTER.touch(exist_ok=True)
MAPTAB = pathlib.Path("data/mapping_table.json"); MAPTAB.touch(exist_ok=True)

def load_json(p):
    try:
        return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
    except Exception:
        return {}

def save_json(p, obj):
    pathlib.Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company-name", required=True)
    ap.add_argument("--company-url", required=True)
    ap.add_argument("--industries", required=True)
    ap.add_argument("--region", default="DACH")
    ap.add_argument("--mode", default="full_auto")
    args = ap.parse_args()

    master = load_json(MASTER)
    maptab = load_json(MAPTAB)

    company_pack = run_agent1(args.company_name, args.company_url, args.region, maptab)
    competitors_pack = run_agent2(company_pack, args.region, maptab)
    buyers_pack = run_agent3(company_pack, competitors_pack, args.region, maptab)

    maptab = run_mapping_update([company_pack, competitors_pack, buyers_pack], maptab)
    save_json(MAPTAB, maptab)

    try:
        upsert_company_pack(company_pack)
        upsert_contacts_pack(company_pack)
    except Exception as e:
        print("HubSpot integration skipped or failed:", e)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_json = OUTDIR / f"{args.company_name.replace(' ','_')}_{timestamp}.json"
    save_json(out_json, {"company": company_pack, "competitors": competitors_pack, "buyers": buyers_pack})

    pdf_path = OUTDIR / f"{args.company_name.replace(' ','_')}_{timestamp}.pdf"
    build_pdf(company_pack, competitors_pack, buyers_pack, pdf_path, branding_path="config/branding_liquisto.json")

    master.setdefault("companies", [])
    master["companies"].append({
        "name": args.company_name,
        "url": args.company_url,
        "classifications": company_pack.get("classifications", []),
        "ts": timestamp
    })
    save_json(MASTER, master)

if __name__ == "__main__":
    main()

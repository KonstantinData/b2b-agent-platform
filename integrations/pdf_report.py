from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import json

def build_pdf(company_pack, competitors_pack, buyers_pack, out_path, branding_path):
    branding = json.load(open(branding_path, "r", encoding="utf-8"))
    c = canvas.Canvas(str(out_path), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(20*mm, (h-20*mm), f"Company Research – {company_pack['company']['name']}")
    c.setFont("Helvetica", 10)
    c.drawString(20*mm, (h-27*mm), f"Website: {company_pack['company'].get('url','n/a')}")

    y = h - 40*mm
    def line(txt, step=6):
        nonlocal y
        if y < 20*mm:
            c.showPage(); y = h - 20*mm
            c.setFont("Helvetica", 10)
        c.drawString(20*mm, y, (txt or '')[:110])
        y -= step*mm

    line("Company Profile")
    for k,v in (company_pack.get("company") or {}).items():
        line(f"- {k}: {v}")

    line("Contacts"); 
    for m in (company_pack.get("contacts") or [])[:15]:
        line(f"- {m.get('name')} – {m.get('role')} – {m.get('linkedin','')}")

    line("Business Units")
    for bu in (company_pack.get("business_units") or [])[:15]:
        line(f"- {bu.get('name')}: WZ {bu.get('wz2008')} / NACE {bu.get('nace')} / ÖNACE {bu.get('oenace')} – {bu.get('desc','')}")

    line("Reports (last 5y)")
    for r in (company_pack.get("reports") or [])[:10]:
        line(f"- {r.get('year')}: {r.get('title')} – {r.get('url','')}")

    line("Economics (per BU)")
    for e in (company_pack.get('economics') or [])[:10]:
        line(f"- {e.get('bu')}: trend={e.get('trend')} | challenges={e.get('challenges')} | opportunities={e.get('opportunities')}")

    line("Competitors (match by code)")
    for m in (competitors_pack.get("matches_by_code") or [])[:15]:
        line(f"- {m.get('company')} ({','.join(m.get('codes',[]))}) – {m.get('url','')} [{m.get('country','')}]")

    line("Potential Buyers")
    for b in (buyers_pack.get("potential_buyers") or [])[:15]:
        line(f"- {b.get('company')} – {b.get('rationale','')} – {b.get('url','')}")

    line("Executive Summary")
    line("- Key opportunities & risks summarized here. (placeholder)")

    c.showPage()
    c.save()

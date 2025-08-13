def run(packs, mapping_table):
    seen = set(mapping_table.keys())
    for p in packs:
        for item in p.get("classifications", []):
            code = item.get("wz2008")
            if code and code not in mapping_table:
                mapping_table[code] = {"nace": None, "oenace": None, "desc": None}
    return mapping_table

def sanitize(s: str) -> str:
    return s.replace("\x00", "").strip()

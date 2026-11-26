#!/usr/bin/env python3
"""Embed offline PDF license notices and gzipped html2pdf bundle into testing-guide.html."""

from __future__ import annotations

import base64
import html
import re
import sys
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
LICENSE_PATH = ASSETS_DIR / "pdf-license.txt"
LIBRARY_PATH = ASSETS_DIR / "pdf-library.js.gz"

LICENSE_RE = re.compile(
    r'(<template\s+id="pdf-license">)([\s\S]*?)(</template>)',
    re.IGNORECASE,
)
LIBRARY_RE = re.compile(
    r'(<script\s+type="application/octet-stream"\s+id="pdf-library">)([\s\S]*?)(</script>)',
    re.IGNORECASE,
)


def embed_pdf(html_path: Path) -> None:
    """Populate #pdf-license and #pdf-library in html_path from bundled assets."""
    if not html_path.is_file():
        raise FileNotFoundError(f"HTML file not found: {html_path}")
    if not LICENSE_PATH.is_file() or not LIBRARY_PATH.is_file():
        raise FileNotFoundError(f"Missing PDF assets in {ASSETS_DIR}")

    license_escaped = html.escape(LICENSE_PATH.read_text(encoding="utf-8"), quote=True)
    library_b64 = base64.b64encode(LIBRARY_PATH.read_bytes()).decode("ascii")
    if not library_b64:
        raise ValueError("Encoded PDF library is empty")

    content = html_path.read_text(encoding="utf-8")
    content, lic_count = LICENSE_RE.subn(
        lambda m: f"{m.group(1)}{license_escaped}{m.group(3)}",
        content,
        count=1,
    )
    if lic_count != 1:
        raise ValueError("Missing <template id=\"pdf-license\"></template> tag")

    content, lib_count = LIBRARY_RE.subn(
        lambda m: f"{m.group(1)}{library_b64}{m.group(3)}",
        content,
        count=1,
    )
    if lib_count != 1:
        raise ValueError(
            "Missing <script type=\"application/octet-stream\" id=\"pdf-library\"></script> tag"
        )

    html_path.write_text(content, encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: embed_pdf.py <html_path>", file=sys.stderr)
        return 2
    try:
        embed_pdf(Path(argv[1]))
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

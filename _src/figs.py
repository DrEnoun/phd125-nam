"""Structure figures for PHD125 slides and activities, drawn with RDKit from SMILES.
Every figure is an SVG data URI, so pages work offline and never depend on a CDN.
mol(smiles, ...)      one structure
grid([(smiles, label), ...], per_row)   several structures with labels
3D coordinates for the floating molecule library: coords3d(smiles)."""
import base64
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D

# Highlight colours for functional groups (soft, readable on white)
HL = {
    'ring':  (0.55, 0.72, 1.00),
    'acid':  (1.00, 0.60, 0.48),
    'ester': (1.00, 0.80, 0.25),
    'amide': (0.55, 0.85, 0.55),
    'oh':    (0.75, 0.60, 1.00),
    'amine': (0.40, 0.85, 0.92),
}


def _uri(svg):
    svg = svg.replace("<?xml version='1.0' encoding='iso-8859-1'?>", '').strip()
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def _opts(d, font=0.75):
    o = d.drawOptions()
    o.bondLineWidth = 2
    o.minFontSize = 14
    o.legendFontSize = 18
    o.padding = 0.08
    o.additionalAtomLabelPadding = 0.08
    o.setBackgroundColour((1, 1, 1, 1))
    return o


def mol(smiles, w=420, h=260, hs=False, highlight=None, legend=''):
    """highlight: list of (smarts, colour-key) pairs; matched atoms and bonds are shaded."""
    m = Chem.MolFromSmiles(smiles)
    if hs:
        m = Chem.AddHs(m)
    AllChem.Compute2DCoords(m)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    _opts(d)
    atoms, bonds, acol, bcol = [], [], {}, {}
    for smarts, key in (highlight or []):
        patt = Chem.MolFromSmarts(smarts)
        for match in m.GetSubstructMatches(patt):
            for a in match:
                atoms.append(a); acol[a] = HL[key]
            for b in m.GetBonds():
                if b.GetBeginAtomIdx() in match and b.GetEndAtomIdx() in match:
                    bonds.append(b.GetIdx()); bcol[b.GetIdx()] = HL[key]
    if atoms:
        d.drawOptions().highlightRadius = 0.45
        d.drawOptions().fillHighlights = True
        rdMolDraw2D.PrepareAndDrawMolecule(d, m, legend=legend, highlightAtoms=list(set(atoms)),
                                           highlightAtomColors=acol, highlightBonds=list(set(bonds)),
                                           highlightBondColors=bcol)
    else:
        rdMolDraw2D.PrepareAndDrawMolecule(d, m, legend=legend)
    d.FinishDrawing()
    return _uri(d.GetDrawingText())


def grid(items, per_row=3, w=240, h=190, hs=False):
    ms = []
    for smi, _ in items:
        m = Chem.MolFromSmiles(smi)
        if hs:
            m = Chem.AddHs(m)
        AllChem.Compute2DCoords(m)
        ms.append(m)
    o = rdMolDraw2D.MolDrawOptions()
    o.bondLineWidth = 2
    o.minFontSize = 14
    o.legendFontSize = 17
    o.setBackgroundColour((1, 1, 1, 1))
    svg = Draw.MolsToGridImage(ms, molsPerRow=per_row, subImgSize=(w, h), legends=[l for _, l in items],
                               useSVG=True, drawOptions=o)
    return _uri(svg)


def coords3d(smiles, seed=7):
    """Approximate 3D geometry (Å) for the floating ball-and-stick molecules."""
    m = Chem.AddHs(Chem.MolFromSmiles(smiles))
    AllChem.EmbedMolecule(m, randomSeed=seed)
    AllChem.MMFFOptimizeMolecule(m)
    conf = m.GetConformer()
    c = [conf.GetAtomPosition(i) for i in range(m.GetNumAtoms())]
    cx = sum(p.x for p in c) / len(c); cy = sum(p.y for p in c) / len(c); cz = sum(p.z for p in c) / len(c)
    atoms = [[a.GetSymbol(), round(c[i].x - cx, 2), round(c[i].y - cy, 2), round(c[i].z - cz, 2)] for i, a in enumerate(m.GetAtoms())]
    bonds = []
    for b in m.GetBonds():
        order = 2 if b.GetBondType() == Chem.BondType.DOUBLE else (3 if b.GetBondType() == Chem.BondType.TRIPLE else 1)
        if b.GetIsAromatic():
            order = 1
        bonds.append([b.GetBeginAtomIdx(), b.GetEndAtomIdx(), order] if order > 1 else [b.GetBeginAtomIdx(), b.GetEndAtomIdx()])
    return {'atoms': atoms, 'bonds': bonds}


def row(panels, w=280, h=210, label_h=30):
    """Side-by-side panels, each (data_uri, label). Lets each panel have its own highlights or hydrogens."""
    W = w * len(panels); H = h + label_h
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for i, (uri, label) in enumerate(panels):
        parts.append(f'<image x="{i*w}" y="0" width="{w}" height="{h}" href="{uri}" xlink:href="{uri}"/>')
        parts.append(f'<text x="{i*w + w/2}" y="{h + label_h*0.7}" text-anchor="middle" font-family="sans-serif" font-size="17" fill="#222">{label}</text>')
    parts.append('</svg>')
    return _uri(''.join(parts))

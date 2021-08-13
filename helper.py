from cicada.cicada import LiberPrimus, gematria
from cicada.cicada.gematria import Latin, Runes

LP = LiberPrimus()


def runes2latin(runes):
    return Runes(runes).to_latin()


def runes2index(runes):
    return Runes(runes).to_index()


def latin2runes(latin):
    return Latin(latin).to_runes()


def latin2index(latin):
    return Latin(latin).to_index()


def index2latin(index):
    return Latin('').alpha.index(index)


def index2runes(index):
    return Latin('').alpha.index(index)


def get_page(page_num):
    return LP.pages[page_num] if (page_num < len(LP.pages)) else False


def get_segment(seg_num):
    return LP.segments[seg_num] if (seg_num < len(LP.segments)) else False


def get_paragraph(p_num):
    return LP.paragraphs[p_num] if (p_num < len(LP.paragraphs)) else False

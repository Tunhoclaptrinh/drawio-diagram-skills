"""Forward example: interlibrary loan (synthetic; not an exam or bundled pattern).

Usage: python3 -B build_diagram.py SKILL_DIR OUTPUT_DIR
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SKILL, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
sys.path.insert(0, str(SKILL / 'scripts'))
from bpmn_builder import Diagram, document  # noqa: E402
from colorize_drawio import colorize_tree  # noqa: E402

W = 2120


def fx(x):
    """Pool-relative exit/entry fraction for an absolute x on a full-width pool."""
    return round((x - 40) / W, 4)


def restyle(d, key, extra):
    cell = d.objects[key].find('mxCell')
    cell.set('style', cell.get('style') + extra)


def build():
    d = Diagram('lien-thu-vien', 'Mượn sách liên thư viện', 2200, 1010)
    d.pool('BD', 'Bạn đọc', 40, 90, W, 70, black=True)
    d.pool('TV', 'Thư viện trường', 40, 200, W, 660)
    d.lane('QUAY', 'QUẦY LƯU THÔNG', (88, 200, W - 48, 300), 'TV')
    d.lane('LTV', 'BỘ PHẬN LIÊN THƯ VIỆN', (88, 500, W - 48, 360), 'TV')
    d.pool('DT', 'Thư viện đối tác', 40, 900, W, 70, black=True)

    # Front desk: eligibility, rejection, handover and reminder.
    d.event('S', 'Nhận phiếu đề nghị mượn', 170, 281, 'QUAY', symbol='message')
    restyle(d, 'S', 'labelWidth=110;')
    d.task('T1', 'Kiểm tra thẻ, hạn mức mượn và tài liệu yêu cầu', 245, 258, 'QUAY', marker='user', w=200, h=84)
    d.vertex('DB', 'CSDL bạn đọc', (310, 395, 70, 60), 'dataStore', 'QUAY',
             'shape=datastore;html=0;whiteSpace=wrap;fontFamily=Arial;fontSize=12;fontColor=#172b42;strokeColor=#334155;fillColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;labelWidth=120;spacingTop=4;')
    d.gateway('G1', 'Đủ điều kiện mượn liên thư viện?', 490, 273, 'QUAY')
    restyle(d, 'G1', 'labelWidth=130;')
    d.task('T_REJ', 'Thông báo từ chối kèm lý do', 600, 258, 'QUAY', marker='send', w=190, h=84)
    d.event('E_REJ', 'Đề nghị bị từ chối', 850, 281, 'QUAY', outline='end')
    d.task('T4', 'Báo bạn đọc đến quầy nhận sách', 1310, 258, 'QUAY', marker='send', w=200, h=84)
    d.task('T5', 'Giao sách và ghi mượn cho bạn đọc', 1560, 258, 'QUAY', marker='user', w=200, h=84)
    d.event('E_OK', 'Đã giao sách', 2030, 281, 'QUAY', outline='end')
    d.event('LC', 'A · Báo không mượn được', 890, 416, 'QUAY', outline='catching', symbol='link')
    restyle(d, 'LC', 'labelPosition=left;verticalLabelPosition=middle;align=right;verticalAlign=middle;spacingTop=0;spacingRight=6;labelWidth=125;')
    d.task('T8', 'Báo bạn đọc không mượn được', 960, 398, 'QUAY', marker='send', w=190, h=74)
    d.event('E_NO', 'Không mượn được', 1190, 416, 'QUAY', outline='end')
    restyle(d, 'E_NO', 'labelWidth=110;')
    d.task('T6', 'Nhắc bạn đọc đến nhận sách', 1800, 400, 'QUAY', marker='send', w=170, h=70)
    d.event('E_REM', 'Đã nhắc', 2040, 416, 'QUAY', outline='end')
    restyle(d, 'E_REM', 'labelWidth=110;')
    d.boundary('B2', '7 ngày chưa nhận', 'T5', symbol='timer', interrupt=True)
    d.boundary('B1', '3 ngày chưa nhận', 'T5', symbol='timer', interrupt=False)
    for key, offset, side in (('B2', 30, 'left;align=right;spacingRight=6;'), ('B1', 150, 'right;align=left;spacingLeft=6;')):
        d.objects[key].find('mxCell/mxGeometry').set('x', str(offset))
        d.boxes[key] = (1560 + offset, 325, 34, 34)
        restyle(d, key, 'verticalLabelPosition=bottom;verticalAlign=top;spacingTop=2;labelPosition=' + side)

    # Interlibrary unit: request, event race, receipt, cancellation and return.
    d.task('T2', 'Gửi yêu cầu mượn tới thư viện đối tác', 570, 558, 'LTV', marker='send', w=200, h=84)
    d.gateway('EG', '', 830, 573, 'LTV', kind='eventBasedGateway')
    d.event('C1', 'Nhận xác nhận đã gửi sách', 960, 581, 'LTV', outline='catching', symbol='message')
    d.event('C2', 'Nhận thông báo không cho mượn', 960, 681, 'LTV', outline='catching', symbol='message')
    d.event('C3', 'Quá 10 ngày làm việc chưa phản hồi', 960, 771, 'LTV', outline='catching', symbol='timer')
    for key in ('C1', 'C2'):
        restyle(d, key, 'verticalLabelPosition=top;verticalAlign=bottom;spacingTop=0;spacingBottom=6;labelWidth=130;')
    restyle(d, 'C3', 'labelWidth=130;')
    d.task('T3', 'Nhận sách và dán nhãn liên thư viện', 1060, 558, 'LTV', marker='manual', w=190, h=84)
    d.task('T9', 'Gửi hủy yêu cầu tới thư viện đối tác', 1060, 748, 'LTV', marker='send', w=190, h=84)
    d.gateway('GM', '', 1300, 673, 'LTV')
    d.event('LT', 'A · Báo không mượn được', 1420, 681, 'LTV', outline='throwing', symbol='link')
    restyle(d, 'LT', 'labelWidth=120;')
    d.task('T7', 'Gửi trả sách cho thư viện đối tác', 1680, 558, 'LTV', marker='manual', w=190, h=84)
    d.event('E_RET', 'Đã trả sách do quá hạn nhận', 1950, 581, 'LTV', outline='end')
    restyle(d, 'E_RET', 'labelWidth=110;')

    seq = [('F1', 'S', 'T1', '', {}), ('F2', 'T1', 'G1', '', {}),
           ('F3', 'G1', 'T_REJ', 'Không', {'default': True}), ('F4', 'T_REJ', 'E_REJ', '', {}),
           ('F5', 'G1', 'T2', 'Có', {'condition': 'eligible', 'exit': (.5, 1), 'points': ((517, 600),)}),
           ('F6', 'T2', 'EG', '', {}), ('F7', 'EG', 'C1', '', {}),
           ('F8', 'EG', 'C2', '', {'exit': (.5, 1), 'points': ((857, 700),)}),
           ('F9', 'EG', 'C3', '', {'exit': (.5, 1), 'points': ((857, 790),)}),
           ('F10', 'C1', 'T3', '', {}),
           ('F11', 'T3', 'T4', '', {'points': ((1280, 600), (1280, 300))}),
           ('F12', 'T4', 'T5', '', {}), ('F13', 'T5', 'E_OK', '', {}),
           ('F14', 'C2', 'GM', '', {}), ('F15', 'C3', 'T9', '', {}),
           ('F16', 'T9', 'GM', '', {'points': ((1327, 790),), 'entry': (.5, 1)}),
           ('F17', 'GM', 'LT', '', {}), ('F18', 'LC', 'T8', '', {}), ('F19', 'T8', 'E_NO', '', {}),
           ('F20', 'B1', 'T6', '', {'exit': (.5, 1), 'points': ((1727, 435),)}), ('F21', 'T6', 'E_REM', '', {}),
           ('F22', 'B2', 'T7', '', {'exit': (.5, 1), 'points': ((1607, 600),)}), ('F23', 'T7', 'E_RET', '', {})]
    for key, a, b, label, opts in seq:
        d.edge(key, a, b, label, **opts)
    d.edge('D1', 'DB', 'T1', kind='dataAssociation', exit=(.5, 0), entry=(.45, 1), offset=(0, 0))
    msgs = [('M1', 'BD', 'S', 'Phiếu đề nghị mượn', (fx(189), 1), (.5, 0), ()),
            ('M2', 'T_REJ', 'BD', 'Từ chối', (.5, 0), (fx(695), 1), ()),
            ('M3', 'T2', 'DT', 'Yêu cầu mượn', (.5, 1), (fx(670), 0), ()),
            ('M4', 'DT', 'C1', 'Xác nhận gửi sách', (fx(905), 0), (.5, 1), ((905, 632), (979, 632))),
            ('M5', 'DT', 'C2', 'Không cho mượn', (fx(1050), 0), (.5, 1), ((1050, 742), (979, 742))),
            ('M6', 'T9', 'DT', 'Hủy yêu cầu', (.5, 1), (fx(1155), 0), ()),
            ('M7', 'T4', 'BD', 'Mời đến nhận sách', (.5, 0), (fx(1410), 1), ()),
            ('M8', 'T6', 'BD', 'Nhắc nhận sách', (.5, 0), (fx(1885), 1), ()),
            ('M9', 'T8', 'BD', 'Không mượn được', (.5, 0), (fx(1055), 1), ())]
    for key, a, b, label, exit, entry, points in msgs:
        d.edge(key, a, b, label, kind='messageFlow', exit=exit, entry=entry, points=points, offset=(0, 0))
    # Keep partner-message labels in the gap above the partner pool, clear of catches/tasks.
    for key in ('M4', 'M5'):
        d.objects[key].find('mxCell/mxGeometry').set('x', '-0.88')
    return document([d])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    root = build()
    for name, theme in (('interlibrary-loan.drawio', 'monochrome'), ('interlibrary-loan-color.drawio', 'bizagi-inspired')):
        tree = colorize_tree(root, theme)
        ET.indent(tree, space='  ')
        ET.ElementTree(tree).write(OUT / name, encoding='utf-8', xml_declaration=True)
    print('created', OUT)


if __name__ == '__main__':
    main()
